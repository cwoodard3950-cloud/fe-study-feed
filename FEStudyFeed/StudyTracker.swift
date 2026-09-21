//
//  StudyTracker.swift
//  FEStudyFeed
//
//  Tracks streaks, per-topic accuracy, and which cards have been seen.
//  Persisted to UserDefaults so progress survives app relaunches.
//

import Foundation
import Combine

struct TopicStat: Codable {
    var seen: Int = 0
    var correct: Int = 0

    var accuracy: Double {
        seen == 0 ? 0 : Double(correct) / Double(seen)
    }
}

private struct PersistedState: Codable {
    var topicStats: [String: TopicStat] = [:]
    var seenCardIDs: Set<String> = []
    var missedCardIDs: Set<String> = []
    var totalCardsStudied: Int = 0
    var currentStreak: Int = 0
    var bestStreak: Int = 0
    var lastStudyDay: Date? = nil
}

final class StudyTracker: ObservableObject {
    static let defaultsKey = "com.festudyfeed.state.v1"

    @Published private(set) var topicStats: [Topic: TopicStat] = [:]
    @Published private(set) var totalCardsStudied: Int = 0
    @Published private(set) var currentStreak: Int = 0
    @Published private(set) var bestStreak: Int = 0

    private(set) var seenCardIDs: Set<String> = []
    private(set) var missedCardIDs: Set<String> = []
    private var lastStudyDay: Date?

    private let calendar = Calendar.current

    init() {
        load()
        refreshStreakForToday()
    }

    // MARK: - Recording

    func recordAnswer(card: StudyCard, correct: Bool) {
        var stat = topicStats[card.topic] ?? TopicStat()
        stat.seen += 1
        if correct { stat.correct += 1 }
        topicStats[card.topic] = stat

        seenCardIDs.insert(card.id)
        if correct {
            missedCardIDs.remove(card.id)
        } else {
            missedCardIDs.insert(card.id)
        }

        totalCardsStudied += 1
        bumpStreakForActivityToday()
        save()
    }

    /// For flashcards/formulas, which have no right/wrong answer, just mark as seen.
    func recordViewed(card: StudyCard) {
        var stat = topicStats[card.topic] ?? TopicStat()
        stat.seen += 1
        topicStats[card.topic] = stat
        seenCardIDs.insert(card.id)
        totalCardsStudied += 1
        bumpStreakForActivityToday()
        save()
    }

    // MARK: - Derived data

    /// Topics with at least 4 attempts and under 70% accuracy, worst first.
    func weakTopics() -> [Topic] {
        topicStats
            .filter { $0.value.seen >= 4 && $0.value.accuracy < 0.7 }
            .sorted { $0.value.accuracy < $1.value.accuracy }
            .map { $0.key }
    }

    func stat(for topic: Topic) -> TopicStat {
        topicStats[topic] ?? TopicStat()
    }

    func overallAccuracy() -> Double {
        let all = topicStats.values
        let seen = all.reduce(0) { $0 + $1.seen }
        let correct = all.reduce(0) { $0 + $1.correct }
        return seen == 0 ? 0 : Double(correct) / Double(seen)
    }

    func resetProgress() {
        topicStats = [:]
        seenCardIDs = []
        missedCardIDs = []
        totalCardsStudied = 0
        currentStreak = 0
        bestStreak = 0
        lastStudyDay = nil
        save()
    }

    // MARK: - Streak bookkeeping

    private func bumpStreakForActivityToday() {
        let today = calendar.startOfDay(for: Date())
        if let last = lastStudyDay {
            let lastDay = calendar.startOfDay(for: last)
            if lastDay == today {
                // already counted today
                return
            } else if let daysBetween = calendar.dateComponents([.day], from: lastDay, to: today).day, daysBetween == 1 {
                currentStreak += 1
            } else {
                currentStreak = 1
            }
        } else {
            currentStreak = 1
        }
        lastStudyDay = today
        bestStreak = max(bestStreak, currentStreak)
    }

    /// Called on launch: if the last study day was before yesterday, the
    /// streak has lapsed even though no new card has been answered yet.
    private func refreshStreakForToday() {
        guard let last = lastStudyDay else { return }
        let today = calendar.startOfDay(for: Date())
        let lastDay = calendar.startOfDay(for: last)
        if let daysBetween = calendar.dateComponents([.day], from: lastDay, to: today).day, daysBetween > 1 {
            currentStreak = 0
        }
    }

    // MARK: - Persistence

    private func save() {
        let state = PersistedState(
            topicStats: Dictionary(uniqueKeysWithValues: topicStats.map { ($0.key.rawValue, $0.value) }),
            seenCardIDs: seenCardIDs,
            missedCardIDs: missedCardIDs,
            totalCardsStudied: totalCardsStudied,
            currentStreak: currentStreak,
            bestStreak: bestStreak,
            lastStudyDay: lastStudyDay
        )
        if let data = try? JSONEncoder().encode(state) {
            UserDefaults.standard.set(data, forKey: Self.defaultsKey)
        }
    }

    private func load() {
        guard let data = UserDefaults.standard.data(forKey: Self.defaultsKey),
              let state = try? JSONDecoder().decode(PersistedState.self, from: data) else {
            return
        }
        topicStats = Dictionary(uniqueKeysWithValues: state.topicStats.compactMap { key, value in
            Topic(rawValue: key).map { ($0, value) }
        })
        seenCardIDs = state.seenCardIDs
        missedCardIDs = state.missedCardIDs
        totalCardsStudied = state.totalCardsStudied
        currentStreak = state.currentStreak
        bestStreak = state.bestStreak
        lastStudyDay = state.lastStudyDay
    }
}

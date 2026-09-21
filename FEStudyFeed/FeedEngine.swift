//
//  FeedEngine.swift
//  FEStudyFeed
//
//  Builds the endless, shuffled feed of cards. Weighted so that weak
//  topics and previously-missed cards show up more often, and refills
//  itself as the person scrolls so the feed never runs dry.
//

import Foundation
import Combine

/// Wraps a StudyCard with a unique per-appearance identity, so the same
/// card can safely show up more than once in the feed (weighted sampling
/// duplicates weak-topic cards on purpose) without confusing SwiftUI's
/// diffing or reusing another appearance's answered/revealed state.
struct FeedItem: Identifiable {
    let id = UUID()
    let card: StudyCard
}

final class FeedEngine: ObservableObject {
    @Published private(set) var queue: [FeedItem] = []

    /// nil means "All topics"
    @Published var topicFilter: Topic? {
        didSet { reshuffle() }
    }

    private let allCards: [StudyCard]
    private unowned let tracker: StudyTracker
    private let refillThreshold = 6
    private let batchSize = 20

    init(cards: [StudyCard] = CardBank.all, tracker: StudyTracker) {
        self.allCards = cards
        self.tracker = tracker
        reshuffle()
    }

    private var pool: [StudyCard] {
        guard let filter = topicFilter else { return allCards }
        return allCards.filter { $0.topic == filter }
    }

    func reshuffle() {
        queue = []
        appendBatch()
    }

    /// Call as the user approaches the end of the visible feed.
    func ensureCards(currentIndex: Int) {
        if queue.count - currentIndex <= refillThreshold {
            appendBatch()
        }
    }

    /// Bump a missed quiz card back into the feed a little further down,
    /// so it resurfaces this session instead of only tomorrow.
    func requeueMissed(_ card: StudyCard) {
        let insertAt = min(queue.count, 8)
        queue.insert(FeedItem(card: card), at: insertAt)
    }

    private func appendBatch() {
        let candidates = pool
        guard !candidates.isEmpty else { return }

        let weakSet = Set(tracker.weakTopics())
        let missedSet = tracker.missedCardIDs
        let seenSet = tracker.seenCardIDs

        // Weight: weak-topic cards and previously-missed cards are duplicated
        // in the sampling bag so they're proportionally more likely to be
        // picked, without ever fully excluding the rest of the deck.
        var bag: [StudyCard] = []
        for card in candidates {
            var weight = 1
            if weakSet.contains(card.topic) { weight += 2 }
            if missedSet.contains(card.id) { weight += 3 }
            if !seenSet.contains(card.id) { weight += 1 } // gentle bias toward fresh material
            bag.append(contentsOf: Array(repeating: card, count: weight))
        }

        var next: [StudyCard] = []
        var lastTopic: Topic? = queue.last?.card.topic
        var shuffled = bag.shuffled()

        while next.count < batchSize && !shuffled.isEmpty {
            // Avoid two cards from the same topic back-to-back when possible.
            if let idx = shuffled.firstIndex(where: { $0.topic != lastTopic }) {
                let card = shuffled.remove(at: idx)
                next.append(card)
                lastTopic = card.topic
            } else {
                let card = shuffled.removeFirst()
                next.append(card)
                lastTopic = card.topic
            }
        }

        queue.append(contentsOf: next.map { FeedItem(card: $0) })
    }
}

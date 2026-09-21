//
//  CardView.swift
//  FEStudyFeed
//
//  One full-screen page of the feed. Layout depends on the card's kind:
//  quiz cards get tappable choices, flashcards/formulas flip to reveal
//  an answer, and handbook-lookup cards reveal where to find something
//  in the FE Reference Handbook.
//

import SwiftUI

struct CardPageView: View {
    let card: StudyCard
    @EnvironmentObject private var tracker: StudyTracker
    @EnvironmentObject private var engine: FeedEngine

    @State private var selectedChoice: Int?
    @State private var revealed = false
    @State private var hasRecorded = false

    var body: some View {
        ZStack {
            backgroundGradient

            VStack(alignment: .leading, spacing: 20) {
                header

                Spacer(minLength: 8)

                promptSection

                Spacer(minLength: 12)

                switch card.kind {
                case .quiz:
                    quizChoices
                case .flashcard, .formula:
                    flipSection
                case .handbookLookup:
                    lookupSection
                }

                if isResolved {
                    explanationPanel
                }

                Spacer(minLength: 24)

                swipeHint
            }
            .padding(.horizontal, 22)
            .padding(.top, 20)
            .padding(.bottom, 24)
        }
    }

    private var isResolved: Bool {
        switch card.kind {
        case .quiz: return selectedChoice != nil
        case .flashcard, .formula, .handbookLookup: return revealed
        }
    }

    // MARK: - Sections

    private var backgroundGradient: some View {
        LinearGradient(
            colors: [card.topic.color.opacity(0.35), Color.black],
            startPoint: .top,
            endPoint: .bottom
        )
        .ignoresSafeArea()
    }

    private var header: some View {
        HStack(spacing: 8) {
            Text(card.topic.displayName)
                .font(.caption.weight(.bold))
                .padding(.horizontal, 10)
                .padding(.vertical, 5)
                .background(card.topic.color.opacity(0.9), in: Capsule())
                .foregroundStyle(.black)

            Text(kindLabel)
                .font(.caption.weight(.semibold))
                .foregroundStyle(.white.opacity(0.7))
                .padding(.horizontal, 10)
                .padding(.vertical, 5)
                .background(.white.opacity(0.12), in: Capsule())
        }
    }

    private var kindLabel: String {
        switch card.kind {
        case .quiz: return "Quiz"
        case .flashcard: return "Flashcard"
        case .formula: return "Formula"
        case .handbookLookup: return "Handbook Lookup"
        }
    }

    private var promptSection: some View {
        Text(card.prompt)
            .font(.title2.weight(.semibold))
            .foregroundStyle(.white)
            .fixedSize(horizontal: false, vertical: true)
    }

    // MARK: - Quiz

    private var quizChoices: some View {
        VStack(spacing: 12) {
            if let choices = card.choices {
                ForEach(choices.indices, id: \.self) { idx in
                    choiceButton(index: idx, text: choices[idx])
                }
            }
        }
    }

    private func choiceButton(index: Int, text: String) -> some View {
        let isCorrect = index == card.correctIndex
        let isSelected = selectedChoice == index
        let showResult = selectedChoice != nil

        return Button {
            guard selectedChoice == nil else { return }
            selectedChoice = index
            recordQuizResult(correct: isCorrect)
        } label: {
            HStack {
                Text(text)
                    .font(.body.weight(.medium))
                    .multilineTextAlignment(.leading)
                Spacer()
                if showResult && isCorrect {
                    Image(systemName: "checkmark.circle.fill")
                } else if showResult && isSelected && !isCorrect {
                    Image(systemName: "xmark.circle.fill")
                }
            }
            .padding()
            .foregroundStyle(.white)
            .background(choiceBackground(showResult: showResult, isCorrect: isCorrect, isSelected: isSelected))
            .clipShape(RoundedRectangle(cornerRadius: 14, style: .continuous))
            .overlay(
                RoundedRectangle(cornerRadius: 14, style: .continuous)
                    .stroke(.white.opacity(0.15), lineWidth: 1)
            )
        }
        .disabled(selectedChoice != nil)
    }

    private func choiceBackground(showResult: Bool, isCorrect: Bool, isSelected: Bool) -> Color {
        guard showResult else { return .white.opacity(0.08) }
        if isCorrect { return .green.opacity(0.35) }
        if isSelected && !isCorrect { return .red.opacity(0.35) }
        return .white.opacity(0.05)
    }

    private func recordQuizResult(correct: Bool) {
        guard !hasRecorded else { return }
        hasRecorded = true
        tracker.recordAnswer(card: card, correct: correct)
        if !correct {
            engine.requeueMissed(card)
        }
    }

    // MARK: - Flashcard / Formula

    private var flipSection: some View {
        VStack(alignment: .leading, spacing: 14) {
            if revealed, let answer = card.answer {
                Text(answer)
                    .font(.title3.weight(.semibold))
                    .foregroundStyle(card.topic.color)
                    .padding()
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .background(.white.opacity(0.08), in: RoundedRectangle(cornerRadius: 16, style: .continuous))
            } else {
                Button {
                    reveal()
                } label: {
                    HStack {
                        Spacer()
                        Label("Show Answer", systemImage: "eye.fill")
                            .font(.body.weight(.semibold))
                        Spacer()
                    }
                    .padding()
                    .foregroundStyle(.black)
                    .background(card.topic.color, in: RoundedRectangle(cornerRadius: 16, style: .continuous))
                }
            }
        }
    }

    // MARK: - Handbook lookup

    private var lookupSection: some View {
        VStack(alignment: .leading, spacing: 14) {
            if revealed {
                Text(card.handbookRef)
                    .font(.title3.weight(.semibold))
                    .foregroundStyle(card.topic.color)
                    .padding()
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .background(.white.opacity(0.08), in: RoundedRectangle(cornerRadius: 16, style: .continuous))
            } else {
                Button {
                    reveal()
                } label: {
                    HStack {
                        Spacer()
                        Label("Reveal Location", systemImage: "book.fill")
                            .font(.body.weight(.semibold))
                        Spacer()
                    }
                    .padding()
                    .foregroundStyle(.black)
                    .background(card.topic.color, in: RoundedRectangle(cornerRadius: 16, style: .continuous))
                }
            }
        }
    }

    private func reveal() {
        guard !revealed else { return }
        revealed = true
        guard !hasRecorded else { return }
        hasRecorded = true
        tracker.recordViewed(card: card)
    }

    // MARK: - Explanation + footer

    private var explanationPanel: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text(card.explanation)
                .font(.subheadline)
                .foregroundStyle(.white.opacity(0.9))

            if card.kind != .handbookLookup {
                Label(card.handbookRef, systemImage: "book.closed.fill")
                    .font(.caption.weight(.medium))
                    .foregroundStyle(.white.opacity(0.6))
            }
        }
        .padding()
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(.white.opacity(0.06), in: RoundedRectangle(cornerRadius: 14, style: .continuous))
        .transition(.opacity.combined(with: .move(edge: .top)))
        .animation(.easeOut(duration: 0.2), value: isResolved)
    }

    private var swipeHint: some View {
        HStack {
            Spacer()
            Image(systemName: "chevron.up")
                .font(.caption)
            Text(isResolved ? "Swipe up for next" : "Swipe up to skip")
                .font(.caption.weight(.medium))
            Spacer()
        }
        .foregroundStyle(.white.opacity(0.35))
    }
}

#Preview {
    let tracker = StudyTracker()
    return CardPageView(card: CardBank.all.first { $0.kind == .quiz }!)
        .environmentObject(tracker)
        .environmentObject(FeedEngine(tracker: tracker))
}

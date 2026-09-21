//
//  StatsView.swift
//  FEStudyFeed
//
//  Progress sheet: streak, overall accuracy, and a per-topic breakdown
//  so it's obvious at a glance which topics need more study time.
//

import SwiftUI

struct StatsView: View {
    @EnvironmentObject private var tracker: StudyTracker
    @Environment(\.dismiss) private var dismiss
    @State private var confirmingReset = false

    var body: some View {
        NavigationStack {
            List {
                Section {
                    HStack {
                        statTile(title: "Current Streak", value: "\(tracker.currentStreak)", systemImage: "flame.fill", tint: .orange)
                        statTile(title: "Best Streak", value: "\(tracker.bestStreak)", systemImage: "trophy.fill", tint: .yellow)
                    }
                    HStack {
                        statTile(title: "Cards Studied", value: "\(tracker.totalCardsStudied)", systemImage: "square.stack.fill", tint: .blue)
                        statTile(title: "Accuracy", value: percent(tracker.overallAccuracy()), systemImage: "target", tint: .green)
                    }
                }
                .listRowBackground(Color.clear)
                .listRowSeparator(.hidden)

                Section("By Topic") {
                    ForEach(Topic.allCases) { topic in
                        topicRow(topic)
                    }
                }

                Section {
                    Button(role: .destructive) {
                        confirmingReset = true
                    } label: {
                        Label("Reset Progress", systemImage: "arrow.counterclockwise")
                    }
                }
            }
            .navigationTitle("Your Progress")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .confirmationAction) {
                    Button("Done") { dismiss() }
                }
            }
            .confirmationDialog(
                "Reset all progress?",
                isPresented: $confirmingReset,
                titleVisibility: .visible
            ) {
                Button("Reset Everything", role: .destructive) {
                    tracker.resetProgress()
                }
                Button("Cancel", role: .cancel) {}
            } message: {
                Text("This clears your streak, accuracy, and history for every topic. It can't be undone.")
            }
        }
    }

    private func statTile(title: String, value: String, systemImage: String, tint: Color) -> some View {
        VStack(alignment: .leading, spacing: 6) {
            Image(systemName: systemImage)
                .foregroundStyle(tint)
            Text(value)
                .font(.title2.weight(.bold))
            Text(title)
                .font(.caption)
                .foregroundStyle(.secondary)
        }
        .frame(maxWidth: .infinity, alignment: .leading)
        .padding()
        .background(.thinMaterial, in: RoundedRectangle(cornerRadius: 14, style: .continuous))
    }

    private func topicRow(_ topic: Topic) -> some View {
        let stat = tracker.stat(for: topic)
        return VStack(alignment: .leading, spacing: 6) {
            HStack {
                Circle()
                    .fill(topic.color)
                    .frame(width: 10, height: 10)
                Text(topic.displayName)
                    .font(.subheadline.weight(.medium))
                Spacer()
                if stat.seen == 0 {
                    Text("Not studied yet")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                } else {
                    Text("\(percent(stat.accuracy)) · \(stat.seen) seen")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
            }
            ProgressView(value: stat.seen == 0 ? 0 : stat.accuracy)
                .tint(stat.seen >= 4 && stat.accuracy < 0.7 ? .red : topic.color)
        }
        .padding(.vertical, 4)
    }

    private func percent(_ value: Double) -> String {
        "\(Int((value * 100).rounded()))%"
    }
}

#Preview {
    StatsView()
        .environmentObject(StudyTracker())
}

//
//  TopicFilterView.swift
//  FEStudyFeed
//
//  Lets the person narrow the feed to one topic, or go back to
//  everything mixed together.
//

import SwiftUI

struct TopicFilterView: View {
    @Binding var selection: Topic?
    @EnvironmentObject private var tracker: StudyTracker
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            List {
                Button {
                    selection = nil
                    dismiss()
                } label: {
                    HStack {
                        Text("All Topics")
                            .foregroundStyle(.primary)
                        Spacer()
                        if selection == nil {
                            Image(systemName: "checkmark")
                                .foregroundStyle(.blue)
                        }
                    }
                }

                ForEach(Topic.allCases) { topic in
                    let stat = tracker.stat(for: topic)
                    Button {
                        selection = topic
                        dismiss()
                    } label: {
                        HStack {
                            Circle()
                                .fill(topic.color)
                                .frame(width: 10, height: 10)
                            Text(topic.displayName)
                                .foregroundStyle(.primary)
                            Spacer()
                            if stat.seen >= 4 && stat.accuracy < 0.7 {
                                Text("Needs work")
                                    .font(.caption2.weight(.semibold))
                                    .padding(.horizontal, 6)
                                    .padding(.vertical, 2)
                                    .background(.red.opacity(0.15), in: Capsule())
                                    .foregroundStyle(.red)
                            }
                            if selection == topic {
                                Image(systemName: "checkmark")
                                    .foregroundStyle(.blue)
                            }
                        }
                    }
                }
            }
            .navigationTitle("Study Topic")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .confirmationAction) {
                    Button("Done") { dismiss() }
                }
            }
        }
    }
}

#Preview {
    TopicFilterView(selection: .constant(nil))
        .environmentObject(StudyTracker())
}

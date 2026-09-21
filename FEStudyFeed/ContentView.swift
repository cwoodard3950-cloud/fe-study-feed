//
//  ContentView.swift
//  FEStudyFeed
//
//  The main feed: a full-screen vertical pager, one study card per page,
//  with a thin overlay bar for streak, topic filter, and stats.
//

import SwiftUI

struct ContentView: View {
    @EnvironmentObject private var tracker: StudyTracker
    @EnvironmentObject private var engine: FeedEngine
    @State private var scrollPosition: UUID?
    @State private var showingStats = false
    @State private var showingTopicPicker = false

    var body: some View {
        ZStack(alignment: .top) {
            Color.black.ignoresSafeArea()

            ScrollView(.vertical, showsIndicators: false) {
                LazyVStack(spacing: 0) {
                    ForEach(Array(engine.queue.enumerated()), id: \.element.id) { index, item in
                        CardPageView(card: item.card)
                            .containerRelativeFrame([.horizontal, .vertical])
                            .id(item.id)
                            .onAppear { engine.ensureCards(currentIndex: index) }
                    }
                }
                .scrollTargetLayout()
            }
            .scrollTargetBehavior(.paging)
            .scrollPosition(id: $scrollPosition)
            .ignoresSafeArea()

            topBar
        }
        .sheet(isPresented: $showingStats) {
            StatsView()
                .environmentObject(tracker)
        }
        .sheet(isPresented: $showingTopicPicker) {
            TopicFilterView(selection: $engine.topicFilter)
                .environmentObject(tracker)
        }
    }

    private var topBar: some View {
        HStack {
            Button {
                showingTopicPicker = true
            } label: {
                HStack(spacing: 6) {
                    Image(systemName: "line.3.horizontal.decrease.circle.fill")
                    Text(engine.topicFilter?.shortName ?? "All Topics")
                        .lineLimit(1)
                }
                .font(.subheadline.weight(.semibold))
                .foregroundStyle(.white)
                .padding(.horizontal, 12)
                .padding(.vertical, 8)
                .background(.ultraThinMaterial, in: Capsule())
            }

            Spacer()

            HStack(spacing: 4) {
                Image(systemName: "flame.fill")
                    .foregroundStyle(.orange)
                Text("\(tracker.currentStreak)")
                    .foregroundStyle(.white)
                    .fontWeight(.semibold)
            }
            .padding(.horizontal, 12)
            .padding(.vertical, 8)
            .background(.ultraThinMaterial, in: Capsule())

            Button {
                showingStats = true
            } label: {
                Image(systemName: "chart.bar.fill")
                    .foregroundStyle(.white)
                    .padding(10)
                    .background(.ultraThinMaterial, in: Circle())
            }
        }
        .padding(.horizontal)
        .padding(.top, 8)
    }
}

#Preview {
    let tracker = StudyTracker()
    return ContentView()
        .environmentObject(tracker)
        .environmentObject(FeedEngine(tracker: tracker))
}

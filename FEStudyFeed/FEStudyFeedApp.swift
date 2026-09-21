//
//  FEStudyFeedApp.swift
//  FEStudyFeed
//
//  An endless swipe-to-study feed for the FE Mechanical exam, built to
//  fill the same phone habit as scrolling a social feed.
//

import SwiftUI

@main
struct FEStudyFeedApp: App {
    @StateObject private var tracker: StudyTracker
    @StateObject private var engine: FeedEngine

    init() {
        let tracker = StudyTracker()
        _tracker = StateObject(wrappedValue: tracker)
        _engine = StateObject(wrappedValue: FeedEngine(tracker: tracker))
    }

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(tracker)
                .environmentObject(engine)
                .preferredColorScheme(.dark)
        }
    }
}

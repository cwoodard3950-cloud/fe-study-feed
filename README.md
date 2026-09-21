# FE Study Feed

An endless, swipe-to-study feed for the FE Mechanical exam — built to fill
the same phone habit as scrolling Instagram/TikTok, except every card is a
quiz question, flashcard, formula, or "where is this in the handbook"
drill.

It ships with **138 original cards** across the 14 major NCEES FE
Mechanical topic areas (Math, Probability & Stats, Ethics & Engineering
Economics, E&M, Statics, Dynamics, Mechanics of Materials, Material
Properties, Fluid Mechanics, Thermodynamics, Heat Transfer, Measurements &
Controls, Mechanical Design, and General ME fundamentals). All of the
question/answer content is written from general engineering knowledge —
none of it is copied from the NCEES FE Reference Handbook, since that's
copyrighted — but every card points to the handbook section where the real
reference material lives, so you also learn to navigate the handbook fast.

## What it does

- **Endless vertical feed**, one card per screen, swipe up for the next —
  same motion as Reels/TikTok.
- **Mixed card types**: multiple-choice quiz, flip flashcards, formula
  cards, and handbook-location drills.
- **Adaptive weighting**: topics you're missing (under 70% accuracy, after
  a few attempts) and previously-missed questions show up more often,
  without ever fully excluding the rest of the deck.
- **Streaks and per-topic accuracy**, saved locally on-device
  (`UserDefaults`, no account or network needed).
- **Topic filter**, so you can drill one subject (say, Statics before a
  midterm) instead of the full mix.

## Opening it in Xcode

1. Copy the `FEStudyFeed` folder to your Mac.
2. Double-click `FEStudyFeed.xcodeproj` to open it in Xcode (built for
   Xcode 15/16, targeting **iOS 17.0+**).
3. Select your Apple ID under **Signing & Capabilities** for the
   `FEStudyFeed` target (Xcode → target → Signing & Capabilities →
   Team). You may also want to change `PRODUCT_BUNDLE_IDENTIFIER` (currently
   `com.carsonwoodard.festudyfeed`) if that reverse-DNS string is already
   taken under your account.
4. Plug in your iPhone, select it as the run destination, hit **Run**.
   The first time, you'll need to trust the developer certificate on your
   phone under Settings → General → VPN & Device Management.

No CocoaPods, Swift Package dependencies, or backend — it's a single
self-contained SwiftUI app.

## Project layout

```
FEStudyFeed/
  FEStudyFeed.xcodeproj/        Xcode project
  FEStudyFeed/
    FEStudyFeedApp.swift        App entry point
    ContentView.swift           The paging feed + top bar
    Models.swift                Topic, CardKind, StudyCard
    StudyTracker.swift          Streak/accuracy tracking, persisted locally
    FeedEngine.swift            Builds & weights the endless card queue
    CardBank.swift              AUTO-GENERATED — the 138 cards (see below)
    Views/
      CardView.swift            Renders one card (quiz/flashcard/formula/lookup)
      StatsView.swift           Progress sheet
      TopicFilterView.swift     Topic picker sheet
    Assets.xcassets             App icon slot + accent color
```

## Continuous integration + screenshots (no Mac needed)

`.github/workflows/ios-build.yml` builds the app on a real Xcode toolchain
via GitHub Actions' macOS runners, then actually **boots it in the iOS
Simulator, launches it, and saves a screenshot** — so you can see the real
rendered app without owning a Mac or an iPhone. Code signing stays off
throughout; the Simulator needs none.

To use it: push this project to a GitHub repo (the `FEStudyFeed` folder
itself as the repo root):

```
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<you>/<your-repo>.git
git push -u origin main
```

Then on GitHub: **Actions tab → the run → Artifacts (bottom of the run
page) → `fe-study-feed-simulator-run`**. That zip has:

- `fe-study-feed-screenshot.png` — what the app actually looks like on
  first launch
- `simulator-console.log` — the app's console output during that run,
  useful for debugging if the "app is still running" check fails (which
  means it crashed on launch)

It re-runs automatically on every push, so each change gets a fresh
screenshot. This only proves the app boots and renders one screen though
— it's not a substitute for actually swiping through it, which needs a
real Simulator session (a borrowed/rented Mac) or a real device.

## Editing or adding cards

`CardBank.swift` is generated, not hand-written, so the content and its
validation never drift apart. The source lives outside the Xcode project:

- `card_data.py` — every card as a plain Python dict (id, topic, kind,
  prompt, choices/correctIndex or answer, explanation, handbookRef).
- `build_cardbank.py` — validates the data (unique ids, quiz answer
  indexes in range, no topic left empty, required fields present) and
  regenerates `FEStudyFeed/CardBank.swift` from it.

To add or edit cards: edit `card_data.py`, then run:

```
python3 build_cardbank.py
```

It'll refuse to write the Swift file (and tell you exactly which card and
field) if anything doesn't check out — a quiz card with a `correctIndex`
outside its `choices`, a duplicate id, an empty topic, and so on.

## Notes on scope

- The topic list mirrors the general shape of the NCEES FE Mechanical exam
  specification, but that specification is revised from time to time —
  treat these as study buckets, and double-check current exam weighting on
  ncees.org before your test date.
- The app defaults to iPhone-only, portrait, dark mode. All of that is a
  couple of build-setting or `.preferredColorScheme` tweaks away if you
  want it different.
- There's no real app icon image yet (`Assets.xcassets/AppIcon.appiconset`
  has an empty slot) — drop in a 1024×1024 PNG there whenever you want a
  real icon instead of the blank default.

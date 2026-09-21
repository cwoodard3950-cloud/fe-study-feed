//
//  Models.swift
//  FEStudyFeed
//
//  Core data types: exam topics and study cards.
//

import Foundation
import SwiftUI

/// Major topic areas on the NCEES FE Mechanical exam specification.
/// (Section weights on the real exam shift between handbook editions —
/// treat these as study buckets, not a guarantee of exam percentages.)
enum Topic: String, CaseIterable, Codable, Identifiable, Hashable {
    case mathematics
    case probabilityStatistics
    case ethicsEconomics
    case electricityMagnetism
    case statics
    case dynamics
    case mechanicsOfMaterials
    case materialProperties
    case fluidMechanics
    case thermodynamics
    case heatTransfer
    case measurementsControls
    case mechanicalDesign
    case generalME

    var id: String { rawValue }

    var displayName: String {
        switch self {
        case .mathematics: return "Mathematics"
        case .probabilityStatistics: return "Probability & Statistics"
        case .ethicsEconomics: return "Ethics & Engineering Economics"
        case .electricityMagnetism: return "Electricity & Magnetism"
        case .statics: return "Statics"
        case .dynamics: return "Dynamics, Kinematics & Vibrations"
        case .mechanicsOfMaterials: return "Mechanics of Materials"
        case .materialProperties: return "Material Properties & Processing"
        case .fluidMechanics: return "Fluid Mechanics"
        case .thermodynamics: return "Thermodynamics"
        case .heatTransfer: return "Heat Transfer"
        case .measurementsControls: return "Measurements, Instrumentation & Controls"
        case .mechanicalDesign: return "Mechanical Design & Analysis"
        case .generalME: return "General ME Fundamentals"
        }
    }

    var shortName: String {
        switch self {
        case .probabilityStatistics: return "Prob & Stats"
        case .ethicsEconomics: return "Ethics & Econ"
        case .electricityMagnetism: return "E&M"
        case .mechanicsOfMaterials: return "Mech of Materials"
        case .materialProperties: return "Materials"
        case .measurementsControls: return "Measurements"
        case .mechanicalDesign: return "Design"
        case .generalME: return "General ME"
        default: return displayName
        }
    }

    /// Accent color per topic, used as a quick visual anchor while swiping.
    /// Generated from evenly spaced hues rather than named asset colors, so
    /// the app needs no extra asset-catalog entries per topic.
    var color: Color {
        let index = Double(Topic.allCases.firstIndex(of: self) ?? 0)
        let hue = (index / Double(Topic.allCases.count)).truncatingRemainder(dividingBy: 1.0)
        return Color(hue: hue, saturation: 0.55, brightness: 0.95)
    }
}

enum CardKind: String, Codable, Hashable {
    case quiz
    case flashcard
    case formula
    case handbookLookup
}

/// A single card in the swipe feed.
struct StudyCard: Identifiable, Codable, Hashable {
    let id: String
    let topic: Topic
    let kind: CardKind

    /// The question, term, or prompt shown on the front of the card.
    let prompt: String

    /// Multiple choice options. Present only for `.quiz` cards.
    let choices: [String]?

    /// Index into `choices` of the correct answer. Present only for `.quiz` cards.
    let correctIndex: Int?

    /// The back-of-card answer for `.flashcard` and `.formula` cards.
    let answer: String?

    /// One or two sentences explaining the reasoning or the formula's terms.
    let explanation: String

    /// A pointer to where this concept lives in the NCEES FE Reference Handbook,
    /// e.g. "FE Handbook: Statics — Centroids of Common Shapes". Written from
    /// general engineering knowledge, not copied from the handbook itself.
    let handbookRef: String

    var isQuiz: Bool { kind == .quiz }
}

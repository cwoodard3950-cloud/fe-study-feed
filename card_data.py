# -*- coding: utf-8 -*-
"""
Source data for the FE Mechanical study card bank.
Each card: id, topic, kind, prompt, choices (or None), correctIndex (or None),
answer (or None), explanation, handbookRef.

kind in {"quiz", "flashcard", "formula", "handbookLookup"}
topic must match a Topic enum rawValue in Models.swift
"""

CARDS = []

def add(id, topic, kind, prompt, explanation, handbookRef,
        choices=None, correctIndex=None, answer=None):
    CARDS.append(dict(
        id=id, topic=topic, kind=kind, prompt=prompt,
        choices=choices, correctIndex=correctIndex, answer=answer,
        explanation=explanation, handbookRef=handbookRef,
    ))

# ---------------------------------------------------------------- MATH
add("math_01", "mathematics", "quiz",
    "d/dx [sin(x)] = ?",
    "The derivative of sine is cosine; the derivative of cosine is negative sine.",
    "FE Handbook: Mathematics — Differential Calculus, derivatives table.",
    choices=["-sin(x)", "cos(x)", "-cos(x)", "sec²(x)"], correctIndex=1)

add("math_02", "mathematics", "quiz",
    "For a 2×2 matrix [[a, b], [c, d]], the determinant is:",
    "det = ad − bc. A zero determinant means the matrix is singular (non-invertible).",
    "FE Handbook: Mathematics — Linear Algebra, matrix operations.",
    choices=["a+d - b-c", "ad - bc", "ab - cd", "ad + bc"], correctIndex=1)

add("math_03", "mathematics", "flashcard",
    "Vector dot product formula",
    "The dot product measures how much two vectors point in the same direction; it's zero when they're perpendicular.",
    "FE Handbook: Mathematics — Vectors.",
    answer="A·B = |A||B|cosθ = AxBx + AyBy + AzBz")

add("math_04", "mathematics", "formula",
    "Quadratic formula for ax²+bx+c=0",
    "Works for any quadratic; the discriminant b²-4ac tells you if the roots are real and distinct, real and repeated, or complex.",
    "FE Handbook: Mathematics — Algebra.",
    answer="x = (−b ± √(b²−4ac)) / (2a)")

add("math_05", "mathematics", "quiz",
    "∫ eˣ dx = ?",
    "eˣ is its own derivative and its own antiderivative (plus a constant).",
    "FE Handbook: Mathematics — Integral Calculus.",
    choices=["eˣ + C", "x·eˣ + C", "eˣ/x + C", "ln(x) + C"], correctIndex=0)

add("math_06", "mathematics", "quiz",
    "L'Hôpital's rule is used to evaluate limits of which form?",
    "When direct substitution gives 0/0 or ∞/∞, differentiate numerator and denominator separately and try the limit again.",
    "FE Handbook: Mathematics — Differential Calculus, limits.",
    choices=["Any limit at infinity", "Indeterminate forms like 0/0 or ∞/∞",
             "Limits of trigonometric functions only", "Only limits equal to zero"], correctIndex=1)

add("math_07", "mathematics", "formula",
    "Taylor series expansion of f(x) about x = a",
    "A polynomial approximation built from a function's derivatives at a single point; more terms means better local accuracy.",
    "FE Handbook: Mathematics — Series.",
    answer="f(x) = f(a) + f'(a)(x−a) + f''(a)(x−a)²/2! + ...")

add("math_08", "mathematics", "handbookLookup",
    "You need a table of standard derivatives and integrals during the exam. Which handbook section has it?",
    "The Mathematics section up front covers algebra, trig identities, vectors, and calculus tables — worth flipping to once before test day so you know the layout.",
    "FE Handbook: Mathematics section (Differential and Integral Calculus subsections).")

add("math_09", "mathematics", "quiz",
    "The cross product A × B of two vectors points:",
    "Use the right-hand rule: curl fingers from A to B, thumb gives the direction, which is perpendicular to the plane containing both vectors.",
    "FE Handbook: Mathematics — Vectors.",
    choices=["Along A", "Along B", "Perpendicular to both A and B", "Parallel to A+B"], correctIndex=2)

add("math_10", "mathematics", "flashcard",
    "Euler's formula",
    "It links exponential and trigonometric functions and is the basis for phasor math in AC circuits and vibrations.",
    "FE Handbook: Mathematics — Complex Numbers.",
    answer="e^(iθ) = cosθ + i·sinθ")

# ---------------------------------------------------------------- PROB/STATS
add("stat_01", "probabilityStatistics", "quiz",
    "The arithmetic mean of a data set is:",
    "Sum every value and divide by the count — the most common measure of central tendency, but it's sensitive to outliers.",
    "FE Handbook: Probability and Statistics — Dispersion, Mean, Median, Mode.",
    choices=["The middle value when sorted", "The most frequent value",
             "The sum of values divided by the count", "The range divided by two"], correctIndex=2)

add("stat_02", "probabilityStatistics", "flashcard",
    "What does standard deviation measure?",
    "A small standard deviation means data clusters near the mean; a large one means it's spread out.",
    "FE Handbook: Probability and Statistics — Dispersion.",
    answer="How spread out data values are from the mean (the square root of the variance).")

add("stat_03", "probabilityStatistics", "quiz",
    "A normal (Gaussian) distribution is fully described by which two parameters?",
    "Once you know the mean and standard deviation, you know the entire shape of the bell curve.",
    "FE Handbook: Probability and Statistics — Normal Distribution.",
    choices=["Mean and mode", "Mean and standard deviation",
             "Median and range", "Variance and skewness"], correctIndex=1)

add("stat_04", "probabilityStatistics", "formula",
    "Sample standard deviation, s",
    "Dividing by n−1 (Bessel's correction) instead of n gives an unbiased estimate of the population standard deviation from a sample.",
    "FE Handbook: Probability and Statistics — Dispersion.",
    answer="s = √[ Σ(xᵢ − x̄)² / (n−1) ]")

add("stat_05", "probabilityStatistics", "quiz",
    "If events A and B are independent, P(A and B) = ?",
    "Independence means one event's outcome doesn't affect the other's probability, so their joint probability is the product.",
    "FE Handbook: Probability and Statistics — Probability rules.",
    choices=["P(A) + P(B)", "P(A) − P(B)", "P(A) × P(B)", "P(A) / P(B)"], correctIndex=2)

add("stat_06", "probabilityStatistics", "quiz",
    "A Type I error in hypothesis testing means:",
    "Type I = false positive (rejecting a true null). Type II = false negative (failing to reject a false null).",
    "FE Handbook: Probability and Statistics — Hypothesis Testing.",
    choices=["Failing to reject a false null hypothesis", "Rejecting a true null hypothesis",
             "Accepting the alternative hypothesis correctly", "Using too small a sample size"], correctIndex=1)

add("stat_07", "probabilityStatistics", "formula",
    "Binomial probability of exactly k successes in n trials",
    "Used whenever you have a fixed number of independent yes/no trials with the same success probability p each time.",
    "FE Handbook: Probability and Statistics — Binomial Distribution.",
    answer="P(k) = C(n,k)·pᵏ·(1−p)ⁿ⁻ᵏ")

add("stat_08", "probabilityStatistics", "handbookLookup",
    "You need standard normal (z) table values during the exam. Where do you look?",
    "The Probability and Statistics section includes the cumulative standard normal distribution table — know how to read it both ways (z-to-probability and back).",
    "FE Handbook: Probability and Statistics — Standard Normal Distribution table.")

add("stat_09", "probabilityStatistics", "quiz",
    "In a distribution skewed heavily to the right (a long tail of high values), the mean is usually:",
    "Outliers on the high end pull the mean up more than the median, which is more robust to extreme values.",
    "FE Handbook: Probability and Statistics — Measures of Central Tendency.",
    choices=["Greater than the median", "Less than the median",
             "Equal to the median", "Equal to the mode"], correctIndex=0)

add("stat_10", "probabilityStatistics", "flashcard",
    "Linear regression (least squares)",
    "It's called 'least squares' because it finds the line minimizing the sum of squared vertical errors from each data point.",
    "FE Handbook: Probability and Statistics — Linear Regression.",
    answer="Fits a straight line y = mx + b that minimizes the sum of squared residuals between data and line.")

# ---------------------------------------------------------------- ETHICS & ECON
add("econ_01", "ethicsEconomics", "quiz",
    "Under most engineering codes of ethics, an engineer's paramount obligation is to:",
    "Every major code of ethics (NSPE and similar) puts public safety, health, and welfare above the client's, employer's, or engineer's own interests.",
    "FE Handbook: Ethics — Fundamental Canons.",
    choices=["Their employer's profitability", "Their own professional reputation",
             "The health, safety, and welfare of the public", "Completing projects on schedule"], correctIndex=2)

add("econ_02", "ethicsEconomics", "formula",
    "Present worth P of a single future amount F",
    "This is the reverse of compounding — it tells you what a future payment is worth today at interest rate i.",
    "FE Handbook: Engineering Economics — Factors: single payment present worth.",
    answer="P = F / (1+i)ⁿ")

add("econ_03", "ethicsEconomics", "formula",
    "Future worth F of a present amount P",
    "The basic compound interest formula — everything else in engineering economics builds from this and its present-worth inverse.",
    "FE Handbook: Engineering Economics — Factors: single payment compound amount.",
    answer="F = P(1+i)ⁿ")

add("econ_04", "ethicsEconomics", "quiz",
    "Straight-line depreciation assumes an asset loses value:",
    "Book value drops by the same dollar amount each period: (cost − salvage value) / useful life.",
    "FE Handbook: Engineering Economics — Depreciation.",
    choices=["By the same fixed amount every period", "By a fixed percentage of remaining value each period",
             "Only in the final year", "Randomly based on usage"], correctIndex=0)

add("econ_05", "ethicsEconomics", "flashcard",
    "What is a code of ethics for engineers?",
    "Bodies like NSPE publish these; state licensing boards can discipline a PE for violating similar standards.",
    "FE Handbook: Ethics section.",
    answer="A formal set of professional obligations — covering public safety, honesty, competence, and conflicts of interest — that licensed engineers are expected to follow.")

add("econ_06", "ethicsEconomics", "quiz",
    "In a benefit-cost analysis, a project is generally considered economically justified when B/C is:",
    "A ratio above 1 means the present worth of benefits exceeds the present worth of costs.",
    "FE Handbook: Engineering Economics — Benefit-Cost Analysis.",
    choices=["Less than 1", "Equal to 0", "Greater than 1", "Equal to the interest rate"], correctIndex=2)

add("econ_07", "ethicsEconomics", "formula",
    "Capital recovery / uniform annual worth factor, A given P",
    "Converts a present lump sum into an equivalent series of equal payments over n periods at interest rate i.",
    "FE Handbook: Engineering Economics — Factors: capital recovery.",
    answer="A = P · [ i(1+i)ⁿ / ((1+i)ⁿ−1) ]")

add("econ_08", "ethicsEconomics", "handbookLookup",
    "You need discrete compound interest factor tables (P/F, F/P, A/P, etc.) during the exam. Where are they?",
    "The Engineering Economics section has both the formulas and pre-computed factor tables for common interest rates — much faster than calculating by hand under time pressure.",
    "FE Handbook: Engineering Economics — Interest Factor Tables.")

add("econ_09", "ethicsEconomics", "quiz",
    "The internal rate of return (IRR) on a project is the interest rate at which:",
    "IRR is the break-even interest rate for the investment — compare it to your minimum acceptable rate of return (MARR) to judge the project.",
    "FE Handbook: Engineering Economics — Rate of Return.",
    choices=["Net present worth equals zero", "Net present worth is maximized",
             "Annual costs equal annual revenue exactly each year", "Depreciation equals salvage value"], correctIndex=0)

add("econ_10", "ethicsEconomics", "quiz",
    "An engineer discovers a safety defect in a completed design that could endanger the public. The ethical first step is to:",
    "Codes of ethics call for raising the issue through proper channels — supervisor, client, or, if unresolved and public safety is at risk, appropriate authorities — rather than staying silent or acting alone outside those channels.",
    "FE Handbook: Ethics — Fundamental Canons and Rules of Practice.",
    choices=["Say nothing since the project is already complete", "Report it through appropriate professional and organizational channels",
             "Fix it personally without telling anyone", "Wait to see if anyone notices"], correctIndex=1)

# ---------------------------------------------------------------- E&M
add("em_01", "electricityMagnetism", "quiz",
    "Ohm's law relates voltage, current, and resistance as:",
    "V = IR is the foundation of DC circuit analysis — memorize it cold.",
    "FE Handbook: Electricity and Magnetism — DC Circuits.",
    choices=["V = IR", "V = I/R", "V = I²R", "V = R/I"], correctIndex=0)

add("em_02", "electricityMagnetism", "formula",
    "Electrical power dissipated in a resistor (three equivalent forms)",
    "All three come from combining P=IV with Ohm's law; use whichever form matches the two quantities you already know.",
    "FE Handbook: Electricity and Magnetism — Power.",
    answer="P = IV = I²R = V²/R")

add("em_03", "electricityMagnetism", "quiz",
    "Capacitors in series combine like:",
    "Series capacitance is like parallel resistance — reciprocals add. Series capacitors always have less total capacitance than the smallest one.",
    "FE Handbook: Electricity and Magnetism — Capacitance.",
    choices=["Resistors in series (values add directly)", "Resistors in parallel (reciprocals add)",
             "They always cancel to zero", "Their capacitances multiply"], correctIndex=1)

add("em_04", "electricityMagnetism", "quiz",
    "Capacitors in parallel combine like:",
    "Parallel capacitance simply adds — opposite of the series case, and opposite of how resistors behave in parallel.",
    "FE Handbook: Electricity and Magnetism — Capacitance.",
    choices=["Values add directly", "Reciprocals add", "Values multiply", "Only the largest one matters"], correctIndex=0)

add("em_05", "electricityMagnetism", "flashcard",
    "Kirchhoff's Current Law (KCL)",
    "This is just conservation of charge applied to a circuit node.",
    "FE Handbook: Electricity and Magnetism — Circuit Laws.",
    answer="The sum of currents entering a node equals the sum of currents leaving it.")

add("em_06", "electricityMagnetism", "flashcard",
    "Kirchhoff's Voltage Law (KVL)",
    "This is conservation of energy applied around a closed circuit path.",
    "FE Handbook: Electricity and Magnetism — Circuit Laws.",
    answer="The sum of voltage rises and drops around any closed loop equals zero.")

add("em_07", "electricityMagnetism", "formula",
    "Voltage across an inductor",
    "Inductor voltage depends on how fast current is changing, not on the current itself — the opposite of a resistor.",
    "FE Handbook: Electricity and Magnetism — Inductance.",
    answer="V = L · (di/dt)")

add("em_08", "electricityMagnetism", "quiz",
    "For a sinusoidal voltage with peak amplitude Vp, the RMS value is:",
    "RMS (root-mean-square) is the DC-equivalent value for delivering the same average power; for a sine wave it's the peak divided by √2.",
    "FE Handbook: Electricity and Magnetism — AC Circuits.",
    choices=["Vp", "Vp / √2", "Vp × √2", "Vp / 2"], correctIndex=1)

add("em_09", "electricityMagnetism", "handbookLookup",
    "You need AC circuit impedance and phasor formulas during the exam. Where are they?",
    "The Electricity and Magnetism section covers both DC and AC circuit relationships, including impedance of R, L, and C elements.",
    "FE Handbook: Electricity and Magnetism section — AC Circuits.")

add("em_10", "electricityMagnetism", "quiz",
    "The SI unit of magnetic flux density is the:",
    "Tesla (T) is the unit for magnetic flux density B; magnetic flux itself (Φ) is measured in webers.",
    "FE Handbook: Electricity and Magnetism — Units.",
    choices=["Weber", "Tesla", "Henry", "Farad"], correctIndex=1)

# ---------------------------------------------------------------- STATICS
add("stat2_01", "statics", "quiz",
    "For a rigid body in static equilibrium, the sum of all forces and the sum of all moments about any point must equal:",
    "This is the entire basis of statics: ΣF = 0 and ΣM = 0 in every direction, or the body would accelerate or rotate.",
    "FE Handbook: Statics — Equilibrium of Rigid Bodies.",
    choices=["Zero", "The applied load", "The reaction force", "One"], correctIndex=0)

add("stat2_02", "statics", "formula",
    "Moment of a force F about a point, using the position vector r",
    "The magnitude is F·d, where d is the perpendicular distance from the point to the force's line of action.",
    "FE Handbook: Statics — Moments and Couples.",
    answer="M = r × F")

add("stat2_03", "statics", "quiz",
    "For a right triangle of height h with its right angle at the base, the centroid's height above the base is:",
    "The centroid of a triangle sits at 1/3 the height from its base, regardless of which side you call the base.",
    "FE Handbook: Statics — Centroids of Common Shapes.",
    choices=["h/2", "h/3", "2h/3", "h/4"], correctIndex=1)

add("stat2_04", "statics", "flashcard",
    "What is a free body diagram (FBD)?",
    "It's the first step of virtually every statics and dynamics problem — isolate the body, then apply equilibrium or Newton's second law.",
    "FE Handbook: Statics — Problem-Solving Approach.",
    answer="A sketch of an isolated body showing every external force and moment acting on it, with internal forces removed.")

add("stat2_05", "statics", "quiz",
    "The method of joints for truss analysis works by applying equilibrium to:",
    "Method of joints uses ΣFx=0 and ΣFy=0 at each pin; method of sections instead cuts through the truss and sums forces/moments on one half, which is faster when you only need a few specific member forces.",
    "FE Handbook: Statics — Trusses.",
    choices=["One pin (joint) at a time", "A cut section through several members at once",
             "The entire truss as a single rigid body only", "The support reactions only"], correctIndex=0)

add("stat2_06", "statics", "formula",
    "Friction force at the point of impending slip",
    "μ is the coefficient of static (or kinetic) friction and N is the normal force; this gives the maximum friction force available before slipping.",
    "FE Handbook: Statics — Friction.",
    answer="f = μ·N")

add("stat2_07", "statics", "quiz",
    "A two-force member (loaded only at two points, no moments applied) must have its internal force directed:",
    "This is why truss members can be analyzed as simple axial members — equilibrium of a two-force member forces the resultant at each end to lie along the line connecting the two points.",
    "FE Handbook: Statics — Two-Force Members.",
    choices=["Perpendicular to the line between the two points", "Along the line connecting the two points",
             "In the direction of gravity", "It can be in any direction"], correctIndex=1)

add("stat2_08", "statics", "handbookLookup",
    "You need the centroid location and moment of inertia of a semicircular area. Where do you look?",
    "The Statics section has a table of centroids and area moments of inertia for common shapes — circles, triangles, rectangles, semicircles, and composite combinations.",
    "FE Handbook: Statics — Centroids and Moments of Inertia of Common Shapes.")

add("stat2_09", "statics", "formula",
    "Parallel axis theorem for area moment of inertia",
    "Ī is the moment of inertia about the shape's own centroidal axis; A is the area and d is the distance to the new parallel axis.",
    "FE Handbook: Statics — Moments of Inertia.",
    answer="I = Ī + A·d²")

add("stat2_10", "statics", "quiz",
    "A planar truss is statically determinate (and stable) when its members m, reactions r, and joints j satisfy:",
    "If m + r < 2j the truss is unstable (a mechanism); if m + r > 2j it's statically indeterminate.",
    "FE Handbook: Statics — Trusses, Determinacy.",
    choices=["m + r = 2j", "m + r = j", "m = 2j + r", "m + j = 2r"], correctIndex=0)

# ---------------------------------------------------------------- DYNAMICS
add("dyn_01", "dynamics", "formula",
    "Newton's second law",
    "The foundation of dynamics: net force equals mass times acceleration, in the same direction as the net force.",
    "FE Handbook: Dynamics — Kinetics of Particles.",
    answer="ΣF = m·a")

add("dyn_02", "dynamics", "quiz",
    "For constant acceleration, which kinematics equation gives final velocity?",
    "This is one of the standard constant-acceleration kinematics equations, alongside s = s₀ + v₀t + ½at² and v² = v₀² + 2a(s−s₀).",
    "FE Handbook: Dynamics — Kinematics of a Particle.",
    choices=["v = v₀ + at", "v = v₀ − at²", "v = at²", "v = v₀ × at"], correctIndex=0)

add("dyn_03", "dynamics", "formula",
    "Position under constant acceleration",
    "One of the core constant-acceleration kinematics equations; it reduces to s₀ + v₀t when a = 0.",
    "FE Handbook: Dynamics — Kinematics of a Particle.",
    answer="s = s₀ + v₀t + ½at²")

add("dyn_04", "dynamics", "quiz",
    "For a particle moving in a circle of radius r at speed v, the centripetal acceleration is:",
    "It always points toward the center of the circle and exists even at constant speed, because velocity direction is still changing.",
    "FE Handbook: Dynamics — Curvilinear Motion.",
    choices=["v²/r", "v/r", "v²r", "vr"], correctIndex=0)

add("dyn_05", "dynamics", "flashcard",
    "Work-energy theorem",
    "This lets you solve for a velocity change directly from work done, without needing acceleration as an intermediate step.",
    "FE Handbook: Dynamics — Work and Energy.",
    answer="The net work done on a particle equals its change in kinetic energy: W = ΔKE = ½mv₂² − ½mv₁²")

add("dyn_06", "dynamics", "formula",
    "Impulse-momentum relationship",
    "Useful for impact and collision problems where force and time are hard to separate but their product (impulse) is known or measurable.",
    "FE Handbook: Dynamics — Impulse and Momentum.",
    answer="J = F·Δt = Δ(mv) = mv₂ − mv₁")

add("dyn_07", "dynamics", "formula",
    "Natural frequency of an undamped spring-mass system",
    "Bigger stiffness k raises the natural frequency; bigger mass m lowers it. This governs everything from vibration isolation to structural resonance.",
    "FE Handbook: Dynamics — Mechanical Vibrations.",
    answer="ωₙ = √(k/m)")

add("dyn_08", "dynamics", "quiz",
    "A damping ratio ζ = 1 describes which vibration case?",
    "ζ < 1 is underdamped (oscillates, decaying), ζ = 1 is critically damped (fastest return without overshoot), ζ > 1 is overdamped (slow, no oscillation).",
    "FE Handbook: Dynamics — Mechanical Vibrations.",
    choices=["Undamped", "Underdamped", "Critically damped", "Overdamped"], correctIndex=2)

add("dyn_09", "dynamics", "handbookLookup",
    "You need the formula for a rigid body's mass moment of inertia during the exam. Where do you look?",
    "The Dynamics section covers kinetics of rigid bodies, including mass moment of inertia for common shapes and the parallel axis theorem in its mass form.",
    "FE Handbook: Dynamics — Kinetics of Rigid Bodies.")

add("dyn_10", "dynamics", "quiz",
    "Angular momentum of a system is conserved when:",
    "This is the rotational analog of linear momentum conservation, and it's why a spinning skater speeds up when pulling their arms in — no external torque acts, but their moment of inertia decreases.",
    "FE Handbook: Dynamics — Angular Momentum.",
    choices=["No external torque acts on the system", "No external force acts on the system",
             "Kinetic energy is conserved", "The system is at rest"], correctIndex=0)

# ---------------------------------------------------------------- MECH OF MATERIALS
add("mom_01", "mechanicsOfMaterials", "formula",
    "Normal (axial) stress in a straight member",
    "This is the most basic stress formula — axial force divided by the cross-sectional area it acts over.",
    "FE Handbook: Mechanics of Materials — Uniaxial Stress-Strain.",
    answer="σ = F / A")

add("mom_02", "mechanicsOfMaterials", "formula",
    "Axial deformation of a bar under load F",
    "L is original length, A is cross-sectional area, E is modulus of elasticity. Longer or more flexible bars stretch more for the same load.",
    "FE Handbook: Mechanics of Materials — Deformation.",
    answer="δ = FL / (AE)")

add("mom_03", "mechanicsOfMaterials", "quiz",
    "Shear stress at the outer surface of a circular shaft in torsion is given by:",
    "T is torque, c is the outer radius, J is the polar moment of inertia of the cross-section — shear stress is maximum at the outer surface and zero at the center.",
    "FE Handbook: Mechanics of Materials — Torsion.",
    choices=["τ = Tc/J", "τ = TJ/c", "τ = T/A", "τ = TL/(JG)"], correctIndex=0)

add("mom_04", "mechanicsOfMaterials", "flashcard",
    "Hooke's law (uniaxial)",
    "This linear relationship only holds up to the material's proportional limit; beyond that, stress and strain are no longer proportional.",
    "FE Handbook: Mechanics of Materials — Stress-Strain Behavior.",
    answer="σ = E·ε, where E is the modulus of elasticity (Young's modulus) and ε is strain.")

add("mom_05", "mechanicsOfMaterials", "quiz",
    "Factor of safety is generally defined as:",
    "A factor of safety greater than 1 means the design's failure load exceeds the expected working load, providing a margin for uncertainty.",
    "FE Handbook: Mechanics of Materials — Design.",
    choices=["Working stress ÷ failure stress", "Failure stress ÷ working (allowable) stress",
             "Applied load × area", "Yield strength × area"], correctIndex=1)

add("mom_06", "mechanicsOfMaterials", "formula",
    "Bending stress in a beam",
    "M is bending moment, c is distance from the neutral axis to the outer fiber, I is the area moment of inertia — stress is maximum at the outer fibers and zero at the neutral axis.",
    "FE Handbook: Mechanics of Materials — Beams, Bending Stress.",
    answer="σ = Mc / I")

add("mom_07", "mechanicsOfMaterials", "quiz",
    "Poisson's ratio describes the relationship between:",
    "When a material stretches axially, it typically contracts laterally; Poisson's ratio is the (negative) ratio of that lateral strain to axial strain.",
    "FE Handbook: Mechanics of Materials — Stress-Strain Behavior.",
    choices=["Axial strain and lateral (transverse) strain", "Stress and temperature",
             "Shear modulus and bulk modulus only", "Yield strength and ultimate strength"], correctIndex=0)

add("mom_08", "mechanicsOfMaterials", "handbookLookup",
    "You need a beam deflection formula for a simply supported beam with a center point load. Where is it?",
    "The Mechanics of Materials section includes a beam deflection table with common support/loading combinations and their max deflection and slope formulas.",
    "FE Handbook: Mechanics of Materials — Beam Deflections table.")

add("mom_09", "mechanicsOfMaterials", "quiz",
    "Mohr's circle is a graphical tool used to find:",
    "By plotting normal and shear stress on perpendicular axes, Mohr's circle lets you read off principal stresses, maximum shear stress, and stresses on any rotated plane.",
    "FE Handbook: Mechanics of Materials — Stress Transformation.",
    choices=["Principal stresses and maximum shear stress at a point", "Beam deflection only",
             "Material density", "Fatigue life directly"], correctIndex=0)

add("mom_10", "mechanicsOfMaterials", "formula",
    "Angle of twist for a circular shaft in torsion",
    "T is applied torque, L is shaft length, J is polar moment of inertia, G is shear modulus — longer or more slender shafts twist more for the same torque.",
    "FE Handbook: Mechanics of Materials — Torsion.",
    answer="θ = TL / (JG)")

# ---------------------------------------------------------------- MATERIALS
add("mat_01", "materialProperties", "quiz",
    "Yield strength is best described as the stress at which:",
    "Beyond the yield point, a material no longer returns to its original shape when unloaded — it has permanent (plastic) deformation.",
    "FE Handbook: Material Properties — Stress-Strain Diagram.",
    choices=["The material fractures", "The material begins permanent (plastic) deformation",
             "The material reaches maximum stress it can carry", "The material starts to melt"], correctIndex=1)

add("mat_02", "materialProperties", "quiz",
    "On a stress-strain curve, ultimate tensile strength is:",
    "Past the ultimate strength point, the material typically necks down and the engineering stress (based on original area) actually decreases until fracture.",
    "FE Handbook: Material Properties — Stress-Strain Diagram.",
    choices=["The same as yield strength", "The maximum stress reached before fracture",
             "The stress at fracture only", "Always less than yield strength"], correctIndex=1)

add("mat_03", "materialProperties", "flashcard",
    "Ductile vs. brittle material behavior",
    "Steel and aluminum are typically ductile; cast iron, ceramics, and glass are typically brittle.",
    "FE Handbook: Material Properties — Mechanical Properties of Materials.",
    answer="Ductile materials undergo large plastic deformation before fracture (visible necking, warning signs); brittle materials fracture suddenly with little to no plastic deformation.")

add("mat_04", "materialProperties", "quiz",
    "The modulus of elasticity (Young's modulus) represents a material's:",
    "It's the slope of the linear (elastic) portion of the stress-strain curve — a measure of stiffness, not strength.",
    "FE Handbook: Material Properties — Stress-Strain Behavior.",
    choices=["Stiffness in the elastic region", "Strength at fracture",
             "Resistance to fatigue", "Density"], correctIndex=0)

add("mat_05", "materialProperties", "formula",
    "True stress vs. engineering stress",
    "As a specimen necks down under tension, its actual (instantaneous) area A shrinks below the original area A₀, so true stress exceeds engineering stress at large strains.",
    "FE Handbook: Material Properties — Stress-Strain Behavior.",
    answer="σ_true = F / A_instantaneous, which is always ≥ engineering stress σ = F / A₀ once necking begins.")

add("mat_06", "materialProperties", "quiz",
    "Quenching (rapid cooling) a steel part during heat treatment is primarily done to:",
    "Rapid cooling traps a hard microstructure (martensite) that wouldn't form under slow cooling; quenched parts are often tempered afterward to reduce brittleness.",
    "FE Handbook: Material Properties — Heat Treatment.",
    choices=["Increase ductility only", "Increase hardness and strength",
             "Reduce the material's cost", "Change its color permanently"], correctIndex=1)

add("mat_07", "materialProperties", "quiz",
    "Injection molding is a manufacturing process best suited for producing:",
    "Molten (or softened) material is forced into a mold cavity under pressure, then cooled and ejected — economical at high volumes once the mold is made.",
    "FE Handbook: Material Properties and Processing — Manufacturing Processes.",
    choices=["High-volume plastic parts from a mold", "Large structural steel beams",
             "Single custom prototypes only", "Sheet metal stamping only"], correctIndex=0)

add("mat_08", "materialProperties", "handbookLookup",
    "You need typical mechanical properties (E, yield strength) for common engineering materials. Where do you look?",
    "The Material Properties section includes tables of typical mechanical and physical properties for metals, plastics, and other common engineering materials.",
    "FE Handbook: Material Properties — Properties of common engineering materials table.")

add("mat_09", "materialProperties", "flashcard",
    "Fatigue endurance limit",
    "Steel typically shows a true endurance limit; many non-ferrous metals like aluminum do not and will eventually fail under enough cycles at any stress.",
    "FE Handbook: Material Properties — Fatigue.",
    answer="The stress level below which a material (notably steel) can withstand an essentially infinite number of load cycles without fatigue failure.")

add("mat_10", "materialProperties", "quiz",
    "Compared to machining from solid stock, additive manufacturing (3D printing) generally:",
    "Additive processes build up material layer by layer, generating far less scrap and enabling internal geometries that would be impossible or very costly to machine.",
    "FE Handbook: Material Properties and Processing — Manufacturing Processes.",
    choices=["Produces more material waste", "Cannot make internal/complex geometries",
             "Generates less scrap and allows more complex internal geometry", "Is always faster for high-volume production"], correctIndex=2)

# ---------------------------------------------------------------- FLUIDS
add("flu_01", "fluidMechanics", "formula",
    "Continuity equation for incompressible flow in a pipe",
    "This just says mass in = mass out for steady incompressible flow — velocity increases where the cross-sectional area decreases.",
    "FE Handbook: Fluid Mechanics — Continuity Equation.",
    answer="A₁V₁ = A₂V₂")

add("flu_02", "fluidMechanics", "formula",
    "Bernoulli's equation (along a streamline, no losses)",
    "Represents conservation of energy per unit weight of fluid: pressure head + velocity head + elevation head stays constant along the streamline.",
    "FE Handbook: Fluid Mechanics — Bernoulli Equation.",
    answer="P/ρg + V²/2g + z = constant")

add("flu_03", "fluidMechanics", "quiz",
    "The Reynolds number is used to predict:",
    "Below about Re ≈ 2300 in a pipe, flow is typically laminar; above roughly 4000 it's typically turbulent, with a transitional range in between.",
    "FE Handbook: Fluid Mechanics — Reynolds Number.",
    choices=["Fluid density", "Whether flow is laminar or turbulent",
             "Pipe material", "Fluid boiling point"], correctIndex=1)

add("flu_04", "fluidMechanics", "formula",
    "Hydrostatic pressure at depth h in a static fluid",
    "ρ is fluid density, g is gravitational acceleration — pressure increases linearly with depth and doesn't depend on the container's shape.",
    "FE Handbook: Fluid Mechanics — Fluid Statics.",
    answer="p = ρgh (plus any pressure at the free surface)")

add("flu_05", "fluidMechanics", "flashcard",
    "Viscosity",
    "Higher viscosity fluids (like honey) resist flow more than lower viscosity fluids (like water) for the same applied shear.",
    "FE Handbook: Fluid Mechanics — Fluid Properties.",
    answer="A fluid's internal resistance to flow, or resistance to shear deformation — relates shear stress to the velocity gradient (τ = μ du/dy).")

add("flu_06", "fluidMechanics", "formula",
    "Darcy-Weisbach head loss due to pipe friction",
    "f is the (Darcy) friction factor from the Moody chart, L and D are pipe length and diameter, V is average velocity.",
    "FE Handbook: Fluid Mechanics — Head Losses, Darcy-Weisbach Equation.",
    answer="h_L = f · (L/D) · (V²/2g)")

add("flu_07", "fluidMechanics", "quiz",
    "Archimedes' principle states that the buoyant force on a submerged object equals:",
    "This is why objects float when their average density is less than the fluid's, and sink when it's greater.",
    "FE Handbook: Fluid Mechanics — Buoyancy.",
    choices=["The weight of the object itself", "The weight of fluid displaced by the object",
             "The pressure at the bottom of the object", "Zero for any submerged object"], correctIndex=1)

add("flu_08", "fluidMechanics", "handbookLookup",
    "You need the Moody diagram to find a friction factor during the exam. Where is it?",
    "The Fluid Mechanics section includes the Moody chart (friction factor vs. Reynolds number and relative roughness) needed for the Darcy-Weisbach equation.",
    "FE Handbook: Fluid Mechanics — Moody Diagram.")

add("flu_09", "fluidMechanics", "quiz",
    "For fully developed laminar flow in a circular pipe, the friction factor f equals:",
    "This closed-form result only applies in the laminar regime (roughly Re < 2300); above that, f must come from the Moody chart or Colebrook equation.",
    "FE Handbook: Fluid Mechanics — Laminar Flow.",
    choices=["64/Re", "0.316/Re^0.25", "Re/64", "Independent of Re"], correctIndex=0)

add("flu_10", "fluidMechanics", "formula",
    "Ideal pump power required to raise flow rate Q against total head H",
    "ρ is fluid density and g is gravitational acceleration; divide by pump efficiency to get the actual shaft power needed.",
    "FE Handbook: Fluid Mechanics — Pump Power.",
    answer="P = ρgQH")

# ---------------------------------------------------------------- THERMO
add("thermo_01", "thermodynamics", "quiz",
    "The first law of thermodynamics for a closed system states that the change in internal energy equals:",
    "This is conservation of energy: energy added as heat minus energy removed as work done by the system.",
    "FE Handbook: Thermodynamics — First Law.",
    choices=["Heat added minus work done by the system", "Work done minus heat added",
             "Heat added plus heat removed", "Zero for any process"], correctIndex=0)

add("thermo_02", "thermodynamics", "formula",
    "Ideal gas law",
    "P is absolute pressure, V is volume, n is moles, R is the universal gas constant, T is absolute temperature.",
    "FE Handbook: Thermodynamics — Ideal Gas.",
    answer="PV = nRT")

add("thermo_03", "thermodynamics", "flashcard",
    "Enthalpy",
    "Enthalpy is especially convenient for constant-pressure processes, since dH = Q at constant pressure with no other work.",
    "FE Handbook: Thermodynamics — Properties.",
    answer="H = U + PV — a combined property useful for flow processes and constant-pressure systems.")

add("thermo_04", "thermodynamics", "formula",
    "Carnot cycle efficiency (ideal heat engine)",
    "This is the theoretical maximum efficiency any heat engine can achieve operating between a hot reservoir Th and cold reservoir Tc (absolute temperatures).",
    "FE Handbook: Thermodynamics — Carnot Cycle.",
    answer="η = 1 − Tc/Th")

add("thermo_05", "thermodynamics", "quiz",
    "The second law of thermodynamics implies that:",
    "This underlies why perpetual motion machines of the second kind (100% efficient heat engines) are impossible, and why entropy of an isolated system never decreases.",
    "FE Handbook: Thermodynamics — Second Law.",
    choices=["Energy can be destroyed", "Heat cannot spontaneously flow from a colder to a hotter body without external work",
             "All processes are reversible", "Entropy of an isolated system always decreases"], correctIndex=1)

add("thermo_06", "thermodynamics", "quiz",
    "For an ideal gas, cp − cv equals:",
    "R is the specific gas constant; this relationship connects the constant-pressure and constant-volume specific heats for any ideal gas.",
    "FE Handbook: Thermodynamics — Specific Heats.",
    choices=["R", "0", "cp × cv", "γ (specific heat ratio)"], correctIndex=0)

add("thermo_07", "thermodynamics", "formula",
    "Work done by a gas during a constant-pressure (isobaric) process",
    "For expansion (ΔV positive), the gas does positive work on its surroundings; for compression, work is done on the gas.",
    "FE Handbook: Thermodynamics — Work.",
    answer="W = P·ΔV")

add("thermo_08", "thermodynamics", "handbookLookup",
    "You need saturated steam property values (like enthalpy of vaporization) during the exam. Where do you look?",
    "The Thermodynamics section includes steam tables and, for HVAC/refrigeration problems, psychrometric charts and refrigerant property tables.",
    "FE Handbook: Thermodynamics — Steam Tables / Property Tables.")

add("thermo_09", "thermodynamics", "quiz",
    "A closed system, unlike an open system, is one in which:",
    "Open systems (control volumes) allow mass flow across their boundary, like a turbine or pump; closed systems only exchange energy, like a piston-cylinder with the valves shut.",
    "FE Handbook: Thermodynamics — Systems.",
    choices=["Mass cannot cross the system boundary, only energy can", "Neither mass nor energy can cross the boundary",
             "Mass and energy can both cross the boundary freely", "The system has no boundary at all"], correctIndex=0)

add("thermo_10", "thermodynamics", "quiz",
    "An isentropic process is one that is:",
    "Isentropic processes are an idealization often used for turbines and compressors to estimate best-case performance.",
    "FE Handbook: Thermodynamics — Processes.",
    choices=["Constant volume", "Constant pressure", "Reversible and adiabatic (constant entropy)", "Constant temperature"], correctIndex=2)

# ---------------------------------------------------------------- HEAT TRANSFER
add("heat_01", "heatTransfer", "formula",
    "Fourier's law of conduction",
    "The negative sign shows heat flows from hot to cold (opposite the direction of increasing temperature); k is thermal conductivity, A is cross-sectional area.",
    "FE Handbook: Heat Transfer — Conduction.",
    answer="q = −kA (dT/dx)")

add("heat_02", "heatTransfer", "quiz",
    "Newton's law of cooling describes convective heat transfer as:",
    "h is the convection heat transfer coefficient, which depends on the fluid, flow conditions, and geometry.",
    "FE Handbook: Heat Transfer — Convection.",
    choices=["q = hAΔT", "q = kAΔT/L", "q = εσAT⁴", "q = mcΔT"], correctIndex=0)

add("heat_03", "heatTransfer", "formula",
    "Stefan-Boltzmann law for radiation from a surface",
    "ε is emissivity (0 to 1), σ is the Stefan-Boltzmann constant, and T is absolute temperature — radiated power scales with the fourth power of temperature.",
    "FE Handbook: Heat Transfer — Radiation.",
    answer="q = εσAT⁴")

add("heat_04", "heatTransfer", "flashcard",
    "Thermal resistance (conduction, plane wall)",
    "Thermal resistances in series or parallel add just like electrical resistances, which is why the electrical-circuit analogy is so useful for multi-layer walls.",
    "FE Handbook: Heat Transfer — Thermal Resistance Networks.",
    answer="R = L / (kA), analogous to electrical resistance, where total heat transfer q = ΔT / R_total.")

add("heat_05", "heatTransfer", "quiz",
    "Which mode of heat transfer can occur through a perfect vacuum with no medium present?",
    "Radiation is electromagnetic energy transfer and needs no medium — it's how the sun's heat reaches Earth through space.",
    "FE Handbook: Heat Transfer — Modes of Heat Transfer.",
    choices=["Conduction", "Convection", "Radiation", "None of them can"], correctIndex=2)

add("heat_06", "heatTransfer", "quiz",
    "A low Biot number (Bi << 1) in a transient conduction problem justifies using:",
    "A low Biot number means internal conduction resistance is much smaller than surface convection resistance, so temperature is nearly uniform throughout the solid at any instant — the assumption behind the lumped capacitance method.",
    "FE Handbook: Heat Transfer — Transient Conduction, Lumped Capacitance.",
    choices=["The lumped capacitance (uniform temperature) approximation", "Steady-state conduction only",
             "The assumption that no convection is occurring", "Only radiation heat transfer analysis"], correctIndex=0)

add("heat_07", "heatTransfer", "handbookLookup",
    "You need typical convection heat transfer coefficients or fin efficiency charts during the exam. Where do you look?",
    "The Heat Transfer section covers conduction, convection correlations, radiation, and extended surfaces (fins), including relevant charts and tables.",
    "FE Handbook: Heat Transfer section — Convection Correlations, Fins.")

add("heat_08", "heatTransfer", "quiz",
    "The overall heat transfer coefficient U in a heat exchanger combines the effects of:",
    "U accounts for convection on both sides of the separating wall plus conduction through the wall itself, all combined the way series thermal resistances combine.",
    "FE Handbook: Heat Transfer — Heat Exchangers.",
    choices=["Conduction and convection resistances in series across all layers", "Only the fluid velocities",
             "Only radiation effects", "Only the wall material's density"], correctIndex=0)

add("heat_09", "heatTransfer", "flashcard",
    "Log mean temperature difference (LMTD)",
    "Because the temperature difference between hot and cold streams changes along a heat exchanger's length, a simple arithmetic average would misrepresent the actual driving temperature difference; LMTD accounts for the exponential-like variation.",
    "FE Handbook: Heat Transfer — Heat Exchangers.",
    answer="The effective average temperature difference used to size a heat exchanger, accounting for the fact that ΔT varies along its length.")

add("heat_10", "heatTransfer", "quiz",
    "The SI units of thermal conductivity k are:",
    "Thermal conductivity tells you how much heat flows per unit area per unit temperature gradient — high for metals, low for insulators.",
    "FE Handbook: Heat Transfer — Conduction, Units.",
    choices=["W/(m·K)", "W/m²", "J/kg·K", "W/K"], correctIndex=0)

# ---------------------------------------------------------------- MEASUREMENTS & CONTROLS
add("ctrl_01", "measurementsControls", "quiz",
    "A strain gauge measures deformation by sensing a change in the sensor's:",
    "As the gauge stretches or compresses with the surface it's bonded to, its wire gets longer/thinner or shorter/thicker, changing its electrical resistance measurably.",
    "FE Handbook: Measurement and Instrumentation — Strain Gauges.",
    choices=["Electrical resistance", "Color", "Magnetic field strength", "Temperature only"], correctIndex=0)

add("ctrl_02", "measurementsControls", "quiz",
    "A thermocouple measures temperature based on:",
    "This is the Seebeck effect — the voltage produced depends predictably on the temperature difference between the junctions.",
    "FE Handbook: Measurement and Instrumentation — Temperature Sensors.",
    choices=["A voltage generated at the junction of two dissimilar metals", "A change in resistance with temperature only",
             "Thermal expansion of a bimetallic strip only", "The speed of sound in a gas"], correctIndex=0)

add("ctrl_03", "measurementsControls", "flashcard",
    "Open-loop vs. closed-loop control",
    "Closed-loop (feedback) control can correct for disturbances and modeling errors that open-loop control cannot.",
    "FE Handbook: Measurement and Instrumentation — Control Systems.",
    answer="Open-loop control acts on a fixed input with no feedback about the actual output; closed-loop (feedback) control measures the output and adjusts the input to reduce error.")

add("ctrl_04", "measurementsControls", "formula",
    "Transfer function of a linear system",
    "It's typically written in the Laplace (s) domain and fully characterizes a linear time-invariant system's input-output behavior.",
    "FE Handbook: Measurement and Instrumentation — Control Systems.",
    answer="G(s) = Output(s) / Input(s), the ratio of the Laplace transforms of output to input, assuming zero initial conditions.")

add("ctrl_05", "measurementsControls", "quiz",
    "A PID controller combines which three actions?",
    "Proportional reacts to current error, Integral eliminates steady-state error by accumulating past error, Derivative anticipates future error from its rate of change.",
    "FE Handbook: Measurement and Instrumentation — PID Control.",
    choices=["Proportional, Integral, Derivative", "Position, Inertia, Damping",
             "Power, Impedance, Delay", "Pressure, Increment, Displacement"], correctIndex=0)

add("ctrl_06", "measurementsControls", "quiz",
    "Negative feedback in a control system loop generally:",
    "Feeding back a signal that opposes the error tends to stabilize the system and reduce sensitivity to disturbances and parameter variation, compared to running open-loop.",
    "FE Handbook: Measurement and Instrumentation — Block Diagrams.",
    choices=["Reduces system error and improves stability compared to open-loop", "Always makes a system unstable",
             "Has no effect on system behavior", "Only works for digital systems"], correctIndex=0)

add("ctrl_07", "measurementsControls", "handbookLookup",
    "You need Laplace transform pairs to solve a control systems problem. Where are they in the handbook?",
    "The Measurement and Instrumentation / Controls section (and sometimes the Mathematics section) includes a Laplace transform table used for converting differential equations into the s-domain.",
    "FE Handbook: Measurement and Instrumentation — Laplace Transforms table.")

add("ctrl_08", "measurementsControls", "quiz",
    "The difference between accuracy and precision is:",
    "You can be precise but not accurate (consistently wrong) or accurate but not precise (right on average, but scattered) — ideally an instrument is both.",
    "FE Handbook: Measurement and Instrumentation — Measurement Concepts.",
    choices=["Accuracy is closeness to the true value; precision is repeatability of measurements", "They mean exactly the same thing",
             "Precision is closeness to true value; accuracy is repeatability", "Accuracy only applies to digital instruments"], correctIndex=0)

add("ctrl_09", "measurementsControls", "quiz",
    "The Nyquist sampling criterion states that to avoid aliasing, the sampling rate must be at least:",
    "Sampling below this rate causes higher frequencies to be misrepresented (aliased) as lower frequencies in the digitized signal.",
    "FE Handbook: Measurement and Instrumentation — Signal Sampling.",
    choices=["Equal to the signal frequency", "Twice the highest frequency component in the signal",
             "Half the highest frequency component", "Independent of the signal frequency"], correctIndex=1)

# ---------------------------------------------------------------- MECH DESIGN
add("des_01", "mechanicalDesign", "quiz",
    "In mechanical design, the factor of safety is chosen higher when:",
    "Greater uncertainty in loading, material properties, or consequences of failure all justify a larger margin between the design's failure point and its expected working conditions.",
    "FE Handbook: Mechanical Design — Design Factors.",
    choices=["Loads and material properties are well known and consequences of failure are minor", "There is significant uncertainty in loads, material properties, or consequences of failure are severe",
             "The part is very inexpensive to replace", "The designer wants a lighter part"], correctIndex=1)

add("des_02", "mechanicalDesign", "quiz",
    "Fatigue failure differs from static (overload) failure in that fatigue:",
    "Fatigue cracks initiate at a stress concentration and grow a little with each cycle until the remaining cross-section suddenly fractures — often with no obvious warning beforehand.",
    "FE Handbook: Mechanical Design — Fatigue.",
    choices=["Occurs under a single large load application", "Occurs from repeated cyclic loading, often well below the material's static strength",
             "Only happens at very high temperatures", "Cannot occur in metals"], correctIndex=1)

add("des_03", "mechanicalDesign", "flashcard",
    "Stress concentration factor, Kt",
    "Sharp corners, holes, and notches all raise local stress above the nominal (average) value — designers round fillets and avoid sharp internal corners specifically to reduce Kt.",
    "FE Handbook: Mechanical Design — Stress Concentrations.",
    answer="A multiplier applied to nominal stress to account for local stress risers like holes, fillets, or notches: σ_max = Kt · σ_nominal.")

add("des_04", "mechanicalDesign", "formula",
    "Approximate relationship between bolt tightening torque and preload (clamping force)",
    "K is a torque coefficient (depends on friction, thread condition), F is desired clamping (preload) force, d is nominal bolt diameter — this is why bolt torque specs matter so much in assembly.",
    "FE Handbook: Mechanical Design — Threaded Fasteners.",
    answer="T ≈ K·F·d")

add("des_05", "mechanicalDesign", "quiz",
    "The gear ratio between a driving gear with N1 teeth and a driven gear with N2 teeth is:",
    "Gear ratio (N2/N1) tells you the speed reduction (or increase) and corresponding torque multiplication between the two shafts.",
    "FE Handbook: Mechanical Design — Gears.",
    choices=["N1/N2", "N2/N1", "N1 × N2", "N1 + N2"], correctIndex=1)

add("des_06", "mechanicalDesign", "quiz",
    "For a shaft that carries pure radial load (no thrust), which bearing type is typically the simplest good choice?",
    "Deep-groove ball bearings handle primarily radial load efficiently and can take modest thrust too; angular contact or tapered roller bearings are chosen when combined radial and significant thrust loads are present.",
    "FE Handbook: Mechanical Design — Bearings.",
    choices=["Deep-groove (radial) ball bearing", "Thrust bearing only",
             "A bearing is never needed for radial load", "Any bearing performs identically"], correctIndex=0)

add("des_07", "mechanicalDesign", "handbookLookup",
    "You need standard screw thread sizes and tap drill data during the exam. Where do you look?",
    "The Mechanical Design and Analysis section covers fasteners, threads, gears, springs, bearings, and welded/bolted joint design formulas.",
    "FE Handbook: Mechanical Design — Fasteners and Threaded Connections.")

add("des_08", "mechanicalDesign", "formula",
    "Spring rate (stiffness) of a helical compression spring",
    "G is shear modulus, d is wire diameter, D is mean coil diameter, N is the number of active coils — stiffer springs use thicker wire, fewer coils, or a smaller coil diameter.",
    "FE Handbook: Mechanical Design — Springs.",
    answer="k = G·d⁴ / (8·D³·N)")

add("des_09", "mechanicalDesign", "quiz",
    "A fillet weld, as opposed to a groove weld, is typically used to join:",
    "Fillet welds are common for T-joints and lap joints because the parts overlap or meet at an angle rather than needing a prepared groove between aligned edges.",
    "FE Handbook: Mechanical Design — Welded Joints.",
    choices=["Two overlapping or perpendicular plates (like a T-joint or lap joint)", "Only two plates butted edge-to-edge",
             "Only round bar stock", "Only cast parts"], correctIndex=0)

add("des_10", "mechanicalDesign", "quiz",
    "When a shaft carries combined bending and torsion, a common failure theory used to combine them into an equivalent stress for ductile materials is:",
    "The distortion-energy (von Mises) theory is the most widely used ductile failure criterion for combined-stress shaft design in mechanical engineering.",
    "FE Handbook: Mechanical Design — Combined Stresses, Failure Theories.",
    choices=["The distortion-energy (von Mises) theory", "Boyle's law",
             "Bernoulli's equation", "The ideal gas law"], correctIndex=0)

# ---------------------------------------------------------------- GENERAL ME
add("gen_01", "generalME", "quiz",
    "The SI unit of force is the:",
    "One newton is the force needed to accelerate a 1 kg mass at 1 m/s².",
    "FE Handbook: Units section, front matter.",
    choices=["Joule", "Newton", "Pascal", "Watt"], correctIndex=1)

add("gen_02", "generalME", "quiz",
    "One horsepower is approximately equal to how many watts?",
    "This conversion shows up constantly in machine and engine power problems — worth having memorized rather than looking up every time.",
    "FE Handbook: Units — Conversion Factors.",
    choices=["100 W", "375 W", "746 W", "1500 W"], correctIndex=2)

add("gen_03", "generalME", "flashcard",
    "Mass vs. weight",
    "Mass stays the same everywhere; weight changes with local gravitational acceleration (which is why the same mass weighs less on the Moon).",
    "FE Handbook: Statics / Dynamics — Basic Concepts.",
    answer="Mass is the amount of matter in an object (constant, in kg or slug); weight is the gravitational force on that mass (W = mg, in N or lbf) and varies with local gravity.")

add("gen_04", "generalME", "quiz",
    "GD&T (Geometric Dimensioning and Tolerancing) on an engineering drawing is used to specify:",
    "GD&T communicates functional requirements (like flatness, perpendicularity, or position tolerance) more precisely and unambiguously than plain linear dimensions alone.",
    "FE Handbook: General ME — Engineering Drawings.",
    choices=["Allowable geometric variation of a part's features and their relationships", "Only the part's material",
             "The manufacturing cost of a part", "The part's paint color"], correctIndex=0)

add("gen_05", "generalME", "quiz",
    "Tolerance stack-up in an assembly refers to:",
    "Designers use worst-case or statistical (RSS) stack-up analysis to make sure a chain of individually-acceptable tolerances doesn't add up to an assembly that doesn't fit or function.",
    "FE Handbook: General ME — Tolerancing.",
    choices=["The cumulative effect of individual part tolerances on the final assembled dimension", "The cost of manufacturing tolerances",
             "A single part's surface finish", "The weight of an assembly"], correctIndex=0)

add("gen_06", "generalME", "handbookLookup",
    "You need to convert a value from US customary units to SI units during the exam. Where do you look?",
    "The front of the FE Reference Handbook has a comprehensive unit conversion table — worth bookmarking since conversions show up across nearly every topic area.",
    "FE Handbook: Units and Conversion Factors, front matter.")

add("gen_07", "generalME", "quiz",
    "CAD, as used in mechanical engineering, stands for:",
    "Modern CAD tools also support simulation (FEA, CFD) and are tightly linked with CAM (computer-aided manufacturing) for downstream production.",
    "FE Handbook: General ME — Design Tools.",
    choices=["Computer-Aided Design", "Computer-Assisted Drafting only, no 3D",
             "Central Analysis Division", "Component Assembly Diagram"], correctIndex=0)

add("gen_08", "generalME", "quiz",
    "When reporting a calculated engineering result, the number of significant figures should generally reflect:",
    "Reporting more digits than your least-precise input value supports overstates the precision of your answer — a common exam and real-world mistake.",
    "FE Handbook: General ME — Numerical Methods / Good Practice.",
    choices=["As many digits as your calculator displays", "The precision of the least-precise input value used in the calculation",
             "Always exactly two decimal places", "It doesn't matter as long as the answer is close"], correctIndex=1)

add("gen_09", "generalME", "quiz",
    "After passing the FE exam and gaining the required work experience, the next licensing exam an engineer typically takes is the:",
    "The FE is usually taken near graduation; the PE (Principles and Practice of Engineering) exam comes later, after several years of qualifying experience, and leads to full professional licensure.",
    "FE Handbook: exam program overview (not a technical topic, but good to know going in).",
    choices=["PE (Principles and Practice of Engineering) exam", "SAT",
             "Another FE exam in a different discipline", "No further exam is required"], correctIndex=0)

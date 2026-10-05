# Formula Student Electronics Study 🏎️⚡

A personal engineering study of **Formula Student vehicle electronics and safety circuits**, centered on the **Brake System Plausibility Device (BSPD)** and the architectural evolution from **25EVO to LEF-26**.

> 🇰🇷 Prefer Korean? Start with the [Korean Learning Guide](./docs/learning-guide-ko.md).

This repository is not a dump of team materials. It is a structured record of how I study a real circuit:

**Requirement → Signal Flow → Circuit Behavior → Timing → Failure Mode → Verification → Design Comparison**

---

## My Role and Scope

This repository documents what I learned during a **team-wide circuit study**.

I do **not** claim that I independently designed, manufactured, or validated the vehicle BSPD hardware.

What I have done here:

- traced the BSPD signal path from schematic material,
- studied the role of comparators, logic, timing, latches, and output stages,
- compared two BSPD architectures,
- reproduced timing calculations,
- built educational RC and Falstad/CircuitJS models,
- organized fault-oriented verification questions,
- separated observations, calculations, simulations, and engineering inferences.

What is still pending:

- direct hardware measurements by me,
- temperature / tolerance / power-up testing on the real board,
- physical validation of proposed improvements,
- full vehicle-level verification.

---

## Key Findings

### 01 — Logic architecture changed

**25EVO**
- open-collector comparator outputs,
- wired logic,
- passive pull-up behavior is part of the decision path.

**LEF-26**
- push-pull comparator outputs,
- explicit OR / AND logic,
- threshold decision and logic combination are more clearly separated.

The important lesson is not simply “old vs new.”  
It is how **output topology changes the way logic can be combined and verified**.

---

### 02 — Timing architecture changed

**25EVO**
- analog RC charging,
- comparator threshold crossing,
- diode-assisted fast discharge.

**LEF-26**
- dedicated LTC6994 timing device,
- no large capacitor as the primary timing element.

For the studied 25EVO values:

`R ≈ 49 kΩ`, `C = 10 µF`

so:

`τ = RC ≈ 0.49 s`

But the ideal delay to a 3.6 V threshold from 0 V is about:

`t ≈ 0.624 s`

This was one of the clearest examples of why **a time constant is not automatically the switching delay**.

See: [RC Delay Simulation](./simulations/rc-delay/)

---

### 03 — Sensor validity is a separate safety path

The BSPD must not only detect an implausible braking + propulsion condition.

It must also detect when a sensor signal itself leaves its expected electrical range.

That means the circuit contains two conceptually different paths:

```text
Brake + drive condition ──> persistence check ──┐
                                                ├─> fault decision
Sensor voltage validity ────────────────────────┘
```

This distinction matters because a sensor fault does not necessarily need to wait for the same persistence delay as the physical plausibility condition.

---

### 04 — Recovery is a system-level problem

The fault detector, shutdown interface, 10-second recovery condition, and state-retention behavior must be understood as a **complete chain**, not only as isolated PCB blocks.

This was especially important when comparing where the BSPD logic ends and where the SDC-side behavior begins.

---

## Evidence Status

| Item | Status |
|---|---|
| Schematic interpretation | ✅ Completed |
| 25EVO ↔ LEF-26 architectural comparison | ✅ Completed |
| RC first-principles calculation | ✅ Completed |
| Educational Python model | ✅ Completed |
| Falstad/CircuitJS comparison model | ✅ Repository model available |
| Fault-oriented test matrix | ✅ Prepared |
| Real-board timing measurement by me | ⏳ Pending |
| Power-up / power-loss measurement | ⏳ Pending |
| Temperature / tolerance test | ⏳ Pending |
| Proposed circuit modifications on hardware | ⏳ Pending |

This table is intentional: **simulation and documentation are not presented as hardware validation**.

---

## Schematic Study

The circuit images are included with permission from the team leader for educational and portfolio documentation.

### 25EVO — RC timing stage

![25EVO RC timing stage](./assets/schematics/25evo-rc-delay.png)

[Read the 25EVO walkthrough →](./schematic-walkthroughs/25evo.md)

### LEF-26 — threshold and timing architecture

![LEF-26 threshold and timing circuit](./assets/schematics/lef26-threshold-timing.png)

[Read the LEF-26 walkthrough →](./schematic-walkthroughs/lef26.md)

> Full schematic assets and reuse notes are documented in [assets/schematics](./assets/schematics/) and [NOTICE.md](./NOTICE.md).

---

## Repository Guide

| Section | Purpose |
|---|---|
| [Korean Learning Guide](./docs/learning-guide-ko.md) | Recommended reading order and study corrections |
| [System Overview](./docs/system-overview.md) | BSPD from a vehicle-system perspective |
| [Fundamentals](./fundamentals/) | Reusable electronics concepts |
| [Safety Circuits](./safety-circuits/) | Fault detection, fail-safe logic, shutdown behavior |
| [25EVO Walkthrough](./schematic-walkthroughs/25evo.md) | Signal-by-signal interpretation |
| [LEF-26 Walkthrough](./schematic-walkthroughs/lef26.md) | Signal-by-signal interpretation |
| [25EVO vs LEF-26](./comparisons/25evo-vs-lef26.md) | Architecture and design trade-offs |
| [RC Simulation](./simulations/rc-delay/) | First-principles timing model |
| [Falstad Comparison](./simulations/falstad/) | Educational repeated-pulse comparison |
| [Verification](./verification/) | Test matrix and measurement template |
| [Improvement Review](./system-analysis/improvement-review-ko.md) | Questions for future design improvement |
| [Sources & Notes](./docs/sources-and-notes.md) | Evidence boundaries and interpretation rules |

---

## Reusable Concepts Learned

- comparator threshold circuits
- open-collector vs push-pull outputs
- pull-up / pull-down behavior
- wired logic
- RC timing and threshold crossing
- fast-discharge paths
- timer ICs
- sensor open/short detection
- latch / reset behavior
- shutdown interfaces
- power-loss default states
- fail-safe reasoning

These notes are kept separate from the vehicle-specific walkthroughs so the knowledge remains useful in future embedded, avionics, and safety-system work.

---

## Verification Mindset

For each block, I try to answer:

1. What requirement is this block satisfying?
2. What signal enters it?
3. What electrical decision is being made?
4. What output state should appear?
5. What happens if a wire opens or shorts?
6. What happens during power loss?
7. How could I verify the explanation?
8. What assumptions remain untested?

This is the main reason this repository exists.

---

## Disclosure

The schematic images originate from team project materials and are reproduced here **with permission from the team leader** for educational and portfolio documentation.

Their presence in this public repository does **not** grant third-party reuse rights or imply that the designs are open source.

See [NOTICE.md](./NOTICE.md).

---

## Engineering Takeaway

The most valuable part of this study was not memorizing a BSPD circuit.

It was learning to move from:

**“What does this component do?”**

to:

**“What requirement is this block satisfying, how can it fail, and what evidence would prove my explanation?”**

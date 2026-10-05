# Formula Student Electronics Study 🏎️⚡

A technical study repository documenting my learning from **Formula Student vehicle electronics and safety circuits**, with a focus on the **Brake System Plausibility Device (BSPD)**.

This repository turns team study work into a structured engineering record:

**Requirement → Circuit → Signal Flow → Timing → Failure Mode → Verification → Design Comparison**

---

## Scope

The main case study is the evolution of the BSPD implementation between **25EVO** and **LEF-26**.

Topics include:

- Comparator threshold circuits
- Open-collector vs. push-pull outputs
- Pull-up / pull-down networks
- Wired logic
- RC timing and fast-discharge paths
- Dedicated timer ICs
- Sensor open/short detection
- Latch and reset behavior
- Shutdown-circuit interfaces
- Fail-safe design
- Design evolution and verification

---

## Repository Map

| Section | Purpose |
|---|---|
| [System Overview](./docs/system-overview.md) | BSPD from a vehicle-system perspective |
| [Fundamentals](./fundamentals/) | Reusable electronics concepts learned during the study |
| [Safety Circuits](./safety-circuits/) | Fault detection, fail-safe logic, latch/reset, shutdown behavior |
| [25EVO vs LEF-26](./comparisons/25evo-vs-lef26.md) | Design evolution and architecture comparison |
| [Schematics](./assets/schematics/) | Team circuit images reproduced with permission |
| [Simulations](./simulations/) | Small numerical checks and circuit-behavior studies |
| [Sources & Notes](./docs/sources-and-notes.md) | Evidence boundaries and interpretation notes |

---

## BSPD at a Glance

A BSPD is a safety circuit that checks whether braking, propulsion, and sensor signals remain physically plausible.

In this study, the system is treated as a sequence of engineering decisions:

```text
Brake / Current Sensors
          ↓
Threshold Comparison
          ↓
Condition Combination
          ↓
Persistence / Timing Check
          ↓
Fault State / Latch
          ↓
Shutdown Interface
          ↓
Vehicle Power Isolation
```

A separate path checks whether sensor voltages leave the expected range so that an invalid sensor signal cannot simply be interpreted as a safe condition.

---

## Design Evolution Studied Here

### 25EVO

```text
Open-collector comparators
        ↓
Wired logic
        ↓
RC timing
        ↓
Fast discharge path
        ↓
Output buffer / SDC interface
```

### LEF-26

```text
Push-pull comparators
        ↓
Logic gate
        ↓
Dedicated timer IC
        ↓
Fault / reset logic
        ↓
SDC interface
```

The engineering value of the comparison is not that one architecture is universally “better”, but that it exposes the trade-offs among **timing accuracy, component tolerance, observability, reset behavior, interface clarity, and verification effort**.

---

## Selected Study Notes

### Fundamentals
- [Comparator Basics](./fundamentals/comparator-basics.md)
- [Open-Collector vs Push-Pull](./fundamentals/open-collector-vs-push-pull.md)
- [Pull-Up, Pull-Down, and Floating Nodes](./fundamentals/pull-up-pull-down.md)
- [RC Timing Circuits](./fundamentals/rc-timing.md)
- [Latch and Reset Logic](./fundamentals/latch-and-reset.md)

### Safety / System Analysis
- [BSPD System Analysis](./safety-circuits/bspd-system-analysis.md)
- [Sensor Fault Detection](./safety-circuits/sensor-fault-detection.md)
- [Fail-Safe Design Principles](./safety-circuits/fail-safe-design.md)

### Comparison
- [25EVO vs LEF-26](./comparisons/25evo-vs-lef26.md)

---

## Verification Project

The first small verification project models the **25EVO RC timing stage** using an idealized RC model.

It checks:

- the difference between the RC time constant and actual threshold-crossing time,
- sensitivity to R/C tolerance,
- why a fast discharge path reduces repeated-pulse accumulation.

See: [RC Delay Simulation](./simulations/rc-delay/)

---

## Documentation Rule

For every circuit or concept, I try to answer:

1. What requirement is being satisfied?
2. What signal enters the block?
3. What physical/electrical decision is made?
4. What is the output state?
5. What happens if a sensor or component fails?
6. How can the behavior be verified?
7. What assumptions or uncertainties remain?

---

## Disclosure / Permission

The schematic images in this repository originate from team project materials and are reproduced here **with permission from the team leader** for educational and portfolio documentation.

Their presence in this public repository does **not** imply an open-source license or permission for third-party reuse.

See [NOTICE.md](./NOTICE.md).

---

## Why This Repository Exists

My goal is not to archive slides.

It is to convert project participation into a reusable engineering knowledge base and to show how I move from:

**reading a circuit → understanding signal flow → questioning design choices → verifying behavior → documenting limitations.**

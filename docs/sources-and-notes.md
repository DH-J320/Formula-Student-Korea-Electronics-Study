# Sources and Interpretation Notes

This repository separates direct evidence from interpretation.

## Evidence types used

### Team schematics
Used to identify actual circuit topology, component roles, and signal connections.

### Team design / study material
Used to understand intended behavior and the evolution between implementations.

### Component datasheets
Used to check output structures, input behavior, timing-device operation, and electrical limitations.

### Calculation / simulation
Used to test whether an explanation is numerically consistent with the circuit.

---

## Confidence labels used in this repository

### Observed
Directly visible in the circuit or documentation.

### Calculated
Derived from visible component values or equations.

### Simulated
Produced from an explicitly stated model.

### Inferred
A plausible engineering explanation that is not explicitly stated in the original design record.

### To verify
Requires measurement, original design rationale, or additional documentation.

---

## Important distinction

A design report may describe goals such as:

- smaller PCB area,
- lower cost,
- improved reliability,
- cleaner timing behavior.

Those are **design intentions** unless a controlled comparison or measurement demonstrates the improvement.

This repository therefore avoids turning a design intention into a quantitative performance claim without supporting evidence.


## Source register (reviewed 2026-10-06, Korea time)

| Source | Use | Evidence boundary |
|---|---|---|
| Supplied 2026 Formula technical regulations study PDF, Art. 60/56 | Hardware independence, persistence/recovery, inspection requirements | Summary only; handwritten study annotations are not regulation text |
| [25EVO BSPD](https://app.notion.com/p/3ed0c49cf9058066b80cff1082333dfc) | Topology, shared outputs, MOSFET output | Revision and receiver loading must be checked |
| [26 BSPD](https://app.notion.com/p/3ed0c49cf905800aa01cd7998c76b9a8) | U1/U2/U4, U8, U3 and thresholds | Study/handover document, not as-built certification |
| [Circuit summary including SDC](https://app.notion.com/p/3ed0c49cf905803ab5b4ec2b4334d569) | Recovery-board placement and SDC relay memory | Do not collapse board and revision boundaries |
| [Improvement proposal](https://app.notion.com/p/3ef0c49cf90580088e9df3ca927a93ac) | Questions for timing and window-comparator review | Proposed claims are reviewed, not repeated as established facts |
| [TI TLV1812-Q1](https://www.ti.com/product/TLV1812-Q1) | Push-pull, rail-to-rail input, POR | TLV182x has a different output topology |
| [TI TLV6700-Q1](https://www.ti.com/product/TLV6700-Q1) | Internal reference and two open-drain outputs | Existing 0.24V lower threshold is not a passive-divider drop-in |
| [ADI LTC6994](https://www.analog.com/en/products/ltc6994-1.html) | Oscillator, RSET, divider and edge-delay architecture | Timer error and real hardware timing need separate checks |
| [CircuitJS source](https://github.com/pfalstad/circuitjs1) | Falstad educational experiment | Simplified input switch and fixed threshold, not the full LM339 circuit |

The 0.24V selection rationale was not found in reviewed team records. The 5V, 200kΩ/10kΩ calculation explains the nominal value, not why designers selected it. A narrower or wider window is not automatically safer.

## Corrections preserved

- HIGH/LOW polarity differs between generations.
- Sensor faults have a parallel path, bypassing the 0.5-second persistence stage.
- 25EVO final PMOS OFF does not leave the output floating when R26 remains attached.
- A study report or simulated waveform is not a hardware measurement.
- Recovery timer placement and latch/state memory placement are distinct questions.

Team schematic images are reproduced with the user's reported team-leader permission. Text is rewritten as educational analysis; the entire private workspace and unrelated team records are not mirrored here.

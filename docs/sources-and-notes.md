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

# Sensor Fault Detection

## Why range checking is necessary

A sensor signal is not trustworthy merely because it is numerically low or high.

Example failure modes:

- wire open
- short to ground
- short to supply
- connector fault
- sensor internal failure

A safety circuit can detect some of these faults by defining an electrically valid window.

---

## Window concept

```text
too low       valid sensor range        too high
  FAULT  |-------------------------|      FAULT
         VL                       VH
```

Two threshold checks can test:

- `Vsensor > VL`
- `Vsensor < VH`

Only when both are true is the sensor considered electrically plausible.

---

## LEF-26 study case

The reviewed material uses upper/lower sensor-voltage checks and combines those decisions so that an out-of-range sensor can force the BSPD decision toward shutdown.

The exact boundary values should always be interpreted together with:

- sensor transfer function,
- resistor tolerances,
- comparator accuracy,
- ADC/measurement evidence if available.

---

## Why the fault path may bypass the 0.5 s plausibility delay

A sustained brake + propulsion combination is a physical-condition plausibility question.

An electrically invalid sensor is different: the system no longer has reliable information.

Therefore a design may choose to make the sensor-invalid path act independently of the persistence delay.

---

## Limitation of voltage-only diagnostics

A voltage inside the allowed range does not prove the sensor is correct.

Examples:

- a mechanically stuck sensor may still output a plausible voltage,
- two failed signals may remain individually in range,
- offset/drift may remain within the window.

So electrical range checking is an important layer, not a complete diagnostic strategy.

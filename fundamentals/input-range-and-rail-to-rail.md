# Input Range and Rail-to-Rail

“Powered from 5 V” does not mean every analog input can safely or accurately operate from 0 V to 5 V.

## Three different concepts

### Supply range
What voltage powers the IC?

### Input common-mode range
What input voltages can the comparator/op-amp correctly interpret?

### Output swing
How close can the output move to the supply rails?

These limits are different.

---

## Rail-to-rail

A device described as rail-to-rail may refer to:

- rail-to-rail input,
- rail-to-rail output,
- or both.

Always check the datasheet wording.

---

## Why it matters in fault detection

A sensor-validity circuit deliberately examines voltages near “too low” and “too high” boundaries.

If those boundaries are close to the comparator's own input limits, the diagnostic circuit itself may become unreliable.

---

## Datasheet checklist

- supply voltage
- common-mode range over temperature
- absolute maximum input
- input offset
- output type
- output swing / saturation
- power-up behavior

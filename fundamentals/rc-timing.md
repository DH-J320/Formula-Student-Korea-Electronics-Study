# RC Timing Circuits

An RC network creates a voltage that changes gradually with time.

## Time constant

`τ = RC`

For an ideal capacitor charging from 0 V toward `VFINAL`:

`V(t) = VFINAL × (1 - exp(-t/RC))`

After one time constant, the capacitor reaches about 63.2% of the final voltage.

---

## Important: τ is not automatically the switching delay

If a comparator changes state at threshold `VTH`, then the delay is the time required for the capacitor voltage to reach that threshold.

`t = -RC × ln(1 - VTH/VFINAL)`

So the actual switching delay depends on:

- R
- C
- supply/final voltage
- comparator threshold
- initial capacitor voltage

---

## Fast-reset diode

A diode can create different charge and discharge paths.

For example:

```text
fault persists:
slow RC charge → threshold crossing

fault disappears:
diode path → fast discharge
```

This is useful when short repeated pulses should not accumulate residual capacitor voltage.

---

## Sources of error

An analog timing circuit may be affected by:

- capacitor tolerance
- resistor tolerance
- leakage current
- diode drop
- comparator hysteresis
- initial conditions
- temperature

This is one reason a later design may replace an analog RC delay with a dedicated timer IC.

---

## Verification approach

For any RC timing circuit:

1. Trace the actual charging path.
2. Trace the actual discharging path.
3. Calculate `τ`.
4. Identify the switching threshold.
5. Calculate threshold-crossing time.
6. Check component tolerances.
7. Compare with measurement.

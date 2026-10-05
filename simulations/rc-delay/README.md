# RC Delay Simulation

This mini-project checks the analog timing intuition used in the 25EVO BSPD study.

## Model

Ideal capacitor charging:

`V(t) = VFINAL × (1 - exp(-t/RC))`

Nominal parameters used:

- `R = 49 kΩ`
- `C = 10 µF`
- `VFINAL = 5 V`
- `VTH = 3.6 V`

---

## Questions

1. Is the switching delay equal to the RC time constant?
2. How much does capacitor tolerance move the threshold-crossing time?
3. Why does a low-resistance diode discharge path help with repeated pulses?

---

## Nominal result

`τ = RC ≈ 0.49 s`

But the ideal threshold crossing is approximately:

`tTH = -RC ln(1 - VTH/VFINAL) ≈ 0.62 s`

This shows why simply reading “RC = 0.49 s” does not prove that the circuit switches at 0.49 s.

---

## Files

- [simulate_rc_delay.py](./simulate_rc_delay.py) — reproduces the ideal charging and tolerance sweep
- `rc_delay_nominal.png` — generated voltage/time plot
- `rc_delay_tolerance.png` — simple capacitance tolerance comparison

---

## Limitations

The model does not include:

- comparator hysteresis
- capacitor ESR / leakage
- diode forward-voltage variation
- exact source/output impedance
- temperature
- PCB leakage/parasitics

It is a first-principles verification, not a substitute for measurement.

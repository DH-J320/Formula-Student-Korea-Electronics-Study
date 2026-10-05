# Fail-Safe Design Principles

Fail-safe design asks a different question from ordinary functional design:

> If something fails, which state does the system naturally move toward?

---

## 1. Define the safe state

Before reading the circuit, define what the system should do when it cannot confidently verify a safe condition.

For a shutdown-related circuit, the desired response is often to remove or inhibit propulsion rather than continue operating with unknown information.

---

## 2. Analyze loss of signal

For each important node:

- wire open?
- short to ground?
- short to supply?
- upstream output becomes high-impedance?

Pull-up/pull-down choices and output topology directly affect the answer.

---

## 3. Analyze loss of power

Ask separately:

- what happens if the BSPD loses its logic supply?
- what happens if only a sensor supply disappears?
- what happens if the output-stage supply disappears?

A circuit that behaves safely for one failure may behave differently for another.

---

## 4. Do not rely on software alone for hardware safety requirements

A hardware safety chain can provide independent protection from:

- firmware bugs,
- processor lockup,
- software timing errors,
- corrupted state.

Independence is itself a safety feature.

---

## 5. Verification should include faults

A useful test matrix includes:

| Test | Expected observation |
|---|---|
| Normal acceleration | no shutdown |
| Normal braking | no shutdown |
| Sustained conflicting condition | shutdown after required persistence |
| Short conflicting pulse | no latched false shutdown if below persistence requirement |
| Sensor below valid range | shutdown |
| Sensor above valid range | shutdown |
| Repeated short pulses | no unintended accumulation beyond design intent |
| Recovery condition | re-enable only after defined reset/recovery logic |

---

## Engineering lesson

Fail-safe behavior comes from **topology + default states + interfaces + recovery logic**, not from a single “safety component.”

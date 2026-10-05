# 25EVO vs LEF-26 BSPD

This comparison focuses on **architecture and engineering trade-offs**, not only component replacement.

---

## 1. High-level comparison

| Topic | 25EVO | LEF-26 |
|---|---|---|
| Comparator output | Open-collector | Push-pull |
| Condition combination | Wired logic | Explicit logic gate |
| Persistence timing | Analog RC threshold crossing | Dedicated timer IC |
| Fast reset of timing state | Diode-assisted discharge path | Timer restarts when input condition clears |
| Sensor range fault | Separate comparator/fault path | Separate upper/lower range checks |
| Recovery / state retention | Interacts with SDC-side logic | Recovery/latch functions shown within BSPD design material |
| Main verification concern | R/C tolerance, residual voltage, threshold | timer configuration, input polarity, power-up state, real boundary timing |

---

## 2. Output architecture

### 25EVO

Open-collector comparator outputs allow a shared node to be controlled through wired logic.

This makes passive pull-up behavior part of the logic itself.

### LEF-26

Push-pull comparator outputs actively drive both logic states, so an explicit logic gate is used to combine the decisions.

### Engineering trade-off

The newer structure separates:

- threshold decision,
- logic combination,
- timing.

That can make each function easier to reason about independently, but it also introduces dedicated logic/timing devices whose configuration must be verified.

---

## 3. 0.5 s persistence implementation

### 25EVO — RC timing

Visible values in the studied timing path include:

- charging resistance: approximately `10 kΩ + 39 kΩ`
- capacitor: `10 µF`
- comparison threshold: approximately `3.6 V` in the analyzed stage
- fast discharge path containing a diode and `470 Ω` resistor

The nominal RC time constant is:

`τ = 49 kΩ × 10 µF ≈ 0.49 s`

But `τ` is not the actual switching delay.

For an ideal 0→5 V charge crossing 3.6 V:

`t ≈ -RC ln(1 - 3.6/5) ≈ 0.62 s`

This distinction is one of the most important lessons from the study.

### LEF-26 — timer IC

The later design uses a dedicated timing device to decide whether the input condition remains asserted for the configured duration.

This removes the large timing capacitor from the main delay-setting mechanism, but the design must still verify:

- RSET / divider configuration
- input polarity
- power-up behavior
- actual measured switching boundary

---

## 4. Repeated short inputs

### RC implementation

Residual capacitor voltage can make repeated pulses important.

The diode-assisted low-resistance discharge path reduces the retained charge when the fault condition disappears.

### Dedicated timer implementation

A short input that clears before the configured interval does not propagate as a completed delayed event; the timing process restarts with the next qualifying condition.

---

## 5. Sensor fault path

Both architectures treat sensor validity as a separate safety problem from the normal brake/current plausibility delay.

This prevents an invalid sensor signal from being silently interpreted as a safe operating state.

---

## 6. Recovery and latch placement

The study material shows a difference in where recovery/state-retention logic is represented.

The important lesson is architectural:

> A safety function can be distributed across boards, but the system requirement still belongs to the complete signal chain.

Therefore board-level analysis must not stop at the connector pin.

---

## 7. What cannot be concluded from schematics alone

A schematic comparison can support statements about:

- topology
- component count
- nominal timing mechanism
- signal polarity
- likely tolerance sensitivities

It cannot by itself prove:

- better EMC performance
- higher vehicle reliability
- lower failure rate
- better thermal behavior
- lower total cost
- smaller final PCB area

Those require measurement, layout/BOM evidence, or controlled testing.

---

## 8. Key engineering takeaway

The most valuable change is not “RC is bad and an IC is good.”

It is the shift from a tightly coupled analog behavior toward more explicitly separated functions.

That changes **what must be measured and verified**.

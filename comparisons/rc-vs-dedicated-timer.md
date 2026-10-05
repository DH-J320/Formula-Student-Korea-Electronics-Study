# RC Timing vs Dedicated Timer IC

Replacing an RC threshold delay with a dedicated timer changes both the design and the verification strategy.

| Question | RC + Comparator | Dedicated Timer |
|---|---|---|
| What sets delay? | R, C, threshold | configuration resistor / divider / device architecture |
| Main analog sensitivity | capacitor tolerance, leakage, initial voltage | configuration tolerance, internal timing accuracy |
| Internal state visibility | capacitor voltage directly measurable | timer state less directly visible |
| Reset behavior | depends on discharge path | defined by timer input behavior |
| Repeated short pulses | residual charge can matter | depends on timer restart/retrigger behavior |
| Debugging | oscilloscope capacitor node | input/output timing measurement |
| Design risk | assuming τ equals delay | assuming nominal programmed delay equals measured delay |

---

## 25EVO lesson

The RC network makes the timing mechanism physically visible: the capacitor voltage can be probed directly.

But the delay is sensitive to the actual capacitor and threshold.

A fast diode discharge path is therefore an important part of the timing behavior, not a minor accessory.

---

## LEF-26 lesson

A dedicated timer separates condition logic from timing.

That can remove the large timing capacitor from the delay-setting mechanism, but it adds configuration questions:

- correct timer variant?
- correct input polarity?
- correct divider code?
- correct resistance?
- startup state?
- actual measured delay?

---

## Conclusion

The useful engineering question is not:

> Which method is more modern?

It is:

> Which uncertainties does each method create, and how will we verify them?

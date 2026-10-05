# Shutdown Interface

The final BSPD signal is meaningful only if the receiving shutdown circuit interprets it correctly.

## Why an output buffer may exist

A comparator output may be logically correct but still be unsuitable to directly drive the next subsystem.

Possible interface requirements include:

- voltage level
- source current
- sink current
- polarity
- isolation
- default state
- wire-break behavior

Therefore an output-stage MOSFET or optocoupler should be analyzed as an **interface contract**, not just an extra switch.

---

## 25EVO study lesson

The studied final-output section converts the upstream comparator/wired-logic state into a defined approximate HIGH/LOW output.

A pull-up defines the upstream high-impedance node, and the output buffer creates a stronger, explicit output state.

The statement “this exists because the SDC requires it” should be treated as an inference until the receiving input requirements or original design rationale are checked.

---

## Questions at the connector

For every safety signal crossing between boards:

1. What voltage is HIGH?
2. What voltage is LOW?
3. Who sources current?
4. Who sinks current?
5. What happens if the connector opens?
6. Are grounds shared?
7. Is isolation used?
8. Which state is considered safe?

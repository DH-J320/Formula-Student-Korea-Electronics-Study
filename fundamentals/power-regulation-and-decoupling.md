# Power Regulation and Decoupling

Safety logic is only as meaningful as the supply that powers it.

## 12 V to 5 V logic supply

A vehicle low-voltage rail may be converted to a local 5 V rail for:

- comparators
- logic gates
- timer ICs
- pull-up networks
- indicator circuits

A regulator block should be read as part of the safety system, not as an unrelated support circuit.

---

## Decoupling capacitors

Small capacitors placed close to IC supply pins help provide a local low-impedance current path for fast switching events.

Larger capacitors support slower supply transients.

Their roles are different from a capacitor deliberately used to create a timing delay.

---

## Questions for a regulator block

1. input-voltage range?
2. output voltage/tolerance?
3. dropout requirement?
4. required input/output capacitance?
5. thermal dissipation?
6. behavior during vehicle transients?
7. what happens to downstream safety outputs as the rail rises or falls?

---

## Safety lesson

Power-up and brown-out behavior can briefly place logic in states that never appear in a steady-state truth table.

Those transitions should be considered during verification.

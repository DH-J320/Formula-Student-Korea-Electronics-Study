# Power Loss and Default State

Steady-state logic analysis is incomplete if it does not ask what happens when power disappears.

## Failure cases to separate

- sensor loses power
- comparator/logic rail loses power
- BSPD output-stage rail loses power
- receiving shutdown board loses power
- ground wire opens
- signal wire opens

These cases may produce different voltages.

---

## Passive components matter

Pull-up and pull-down resistors can define a node after an active output becomes high-impedance.

That means fail-safe behavior can depend on passive topology even when all active ICs are off.

---

## Verification method

During a controlled bench test:

1. establish normal operation,
2. interrupt one supply at a time,
3. observe the BSPD output,
4. observe the receiving shutdown input,
5. record whether the final vehicle-level state is safe.

The system boundary matters more than the output pin of a single IC.

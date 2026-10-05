# Latch and Reset Logic

A transient event and a persistent system state are different things.

A latch allows a short event to change a state that remains stored after the original event disappears.

---

## Why a safety system may need a latch

Without state retention:

```text
fault appears → shutdown
fault disappears → immediate recovery
```

With a latch or controlled reset:

```text
fault appears → fault state stored
                     ↓
       recovery condition checked
                     ↓
              reset / re-enable
```

This avoids uncontrolled reactivation.

---

## Questions to ask

When analyzing a latch/reset block:

1. What sets the fault state?
2. What resets it?
3. Is reset automatic or external?
4. Must the safe condition persist before reset?
5. What happens during power cycling?
6. What state is preferred if a control signal disconnects?

---

## Timing and reset are separate concepts

A **fault persistence delay** answers:

> Has the unsafe condition lasted long enough to trigger?

A **reactivation delay** answers:

> Has the system been safe long enough to permit recovery?

Those timers should not be confused even if both appear in the same safety circuit.

# BSPD System Analysis

## 1. Functional requirement

The BSPD must distinguish among:

- normal propulsion,
- normal braking,
- a sustained implausible braking + propulsion condition,
- invalid sensor signals.

The circuit therefore contains both **plausibility logic** and **sensor-validity logic**.

---

## 2. Plausibility path

Conceptually:

```text
current threshold exceeded?
            +
brake threshold exceeded?
            ↓
      combine conditions
            ↓
   persistence / timing
            ↓
       fault request
```

A short transient should not necessarily be treated the same as a sustained unsafe condition.

---

## 3. Sensor-validity path

A sensor must not be trusted merely because its voltage happens to correspond to a low-demand condition.

A separate window check can ask:

```text
LOWER LIMIT < sensor voltage < UPPER LIMIT ?
```

If not, the circuit can request shutdown independently of the normal plausibility timing path.

---

## 4. Output and shutdown interface

The BSPD logic ultimately has to interact with the vehicle shutdown system.

That means the final output stage is not just “another logic gate.”

It must be analyzed in terms of:

- voltage level,
- source/sink capability,
- default state,
- behavior if a wire opens,
- behavior if power is lost,
- compatibility with the receiving shutdown input.

---

## 5. Recovery

Fault detection and recovery are separate engineering problems.

A robust analysis traces:

```text
fault occurs
    ↓
shutdown requested
    ↓
fault disappears
    ↓
safe condition persists
    ↓
reset / reactivation permitted
```

---

## 6. Failure-oriented reading method

For every block, I use four questions:

### Normal
What happens when every input is valid?

### Triggered
What happens when the intended unsafe condition occurs?

### Open circuit
What happens if the signal wire disconnects?

### Short / rail fault
What happens if the signal is forced to ground or supply?

This approach is more useful than tracing only the happy path.

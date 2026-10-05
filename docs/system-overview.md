# BSPD System Overview

## 1. Why the BSPD exists

The Brake System Plausibility Device (BSPD) is a safety function that decides whether the combination of braking, propulsion, and sensor signals remains plausible.

The key idea is simple:

> A vehicle that is being strongly braked should not continue receiving substantial propulsion for an extended period, and invalid sensor signals must not silently appear safe.

---

## 2. System-level signal flow

```text
Brake Sensor ──────┐
                   ├─> Threshold / Validity Checks ──┐
Current Sensor ────┘                                 │
                                                     ├─> Safety Decision
Sensor Validity Checks ──────────────────────────────┘
                                                           ↓
                                                    Persistence Check
                                                           ↓
                                                     Fault / Latch
                                                           ↓
                                                    Shutdown Interface
                                                           ↓
                                               Vehicle power isolation
```

This decomposition is more useful than memorizing individual components because each block answers a different engineering question.

---

## 3. The questions each block answers

### Sensor input
What physical quantity is being measured?

### Threshold comparison
Has the signal crossed the condition that matters to the safety requirement?

### Sensor validity
Is the sensor signal itself believable?

### Logic combination
Which combination of conditions constitutes a fault?

### Timing
Must the condition persist, or should it cause immediate action?

### Latch / reset
Should the system remember a fault after the triggering signal disappears?

### Shutdown interface
How is the safety decision converted into a signal that can safely affect the vehicle power system?

---

## 4. Two different fault classes

### Plausibility fault
A physically unsafe combination persists long enough to be considered real.

Example concept:

```text
strong braking + substantial drive
                ↓
         persistence check
                ↓
             shutdown
```

### Sensor fault
A sensor voltage leaves its expected electrical range.

```text
sensor voltage outside valid range
                ↓
        immediate fault path
                ↓
             shutdown
```

These paths should be analyzed separately because the timing requirement for a plausibility condition and the reaction to an invalid sensor do not have to be identical.

---

## 5. Why this is useful beyond Formula Student

The same reasoning pattern appears in many safety-critical systems:

**measure → validate → decide → time-filter → latch → act → verify**

This is directly transferable to avionics, propulsion-control electronics, battery safety, and other embedded safety systems.

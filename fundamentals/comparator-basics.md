# Comparator Basics

A comparator converts an analog voltage relationship into a digital decision.

## Basic rule

For a conventional comparator:

- if `V+ > V-`, one output state is produced,
- if `V+ < V-`, the opposite state is produced.

The exact electrical form of that output depends on the output stage.

---

## Why comparators appear in safety circuits

A sensor usually produces a continuous voltage.

A safety circuit often needs a discrete decision:

- above a threshold?
- below a threshold?
- inside an allowed window?
- outside an allowed window?

Comparators provide that transition from **measurement** to **decision**.

---

## Threshold example

A resistor divider can create a reference voltage:

```text
VCC
 |
R1
 |
 +---- VREF
 |
R2
 |
GND
```

`VREF = VCC × R2 / (R1 + R2)`

A sensor voltage can then be compared with `VREF`.

---

## Window detection

Two comparators can check whether a signal stays between a lower and an upper boundary:

```text
lower limit < sensor voltage < upper limit
```

This is useful for detecting sensor open-circuit, short-circuit, or otherwise implausible electrical states.

---

## Datasheet questions

Before using a comparator, check:

1. Supply-voltage range
2. Input common-mode range
3. Output structure
4. Propagation delay
5. Input offset / threshold accuracy
6. Power-up behavior
7. Whether external pull-up components are required

---

## Engineering lesson

A comparator is not merely “an op-amp used digitally.”

Its **input range, output structure, switching behavior, and power-up state** matter to the safety logic around it.

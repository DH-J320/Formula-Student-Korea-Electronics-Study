# Logic Gates and Signal Polarity

A common source of mistakes in circuit analysis is reading HIGH as “fault” or LOW as “safe” without tracing the entire signal chain.

## Active-high vs active-low

A signal name and its electrical voltage are not the same thing as its physical meaning.

Examples:

- HIGH may mean **valid**
- LOW may mean **fault**
- or the opposite

The only reliable method is to trace:

```text
physical condition
→ comparator result
→ gate input
→ gate output
→ timer polarity
→ final shutdown meaning
```

---

## De Morgan's law in real circuits

Inverted signals often make a circuit look like it is using the “wrong” gate.

For example:

`NOT(A AND B) = (NOT A) OR (NOT B)`

So two active-low comparator decisions combined by an OR gate can represent the same physical condition that might otherwise be described as an AND.

---

## Debugging method

Build a truth table with both:

1. electrical state: HIGH / LOW
2. physical state: brake exceeded / current exceeded / fault / valid

Never keep only one of the two.

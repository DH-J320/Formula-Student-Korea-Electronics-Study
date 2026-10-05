# Open-Collector vs Push-Pull Outputs

The logical result may be HIGH or LOW in both cases, but the electrical behavior is very different.

---

## Open-collector

An open-collector output can actively pull the signal LOW, but it does not actively drive it HIGH.

A pull-up resistor provides the HIGH state.

```text
+5 V
 |
 Rpull-up
 |
 +------ signal
 |
 transistor
 |
GND
```

### Consequences

- LOW is actively driven.
- HIGH is created by the external pull-up.
- Multiple compatible open-collector outputs can share a node.
- If any output pulls LOW, the shared node becomes LOW.

This makes wired logic possible.

---

## Push-pull

A push-pull output actively drives both directions.

```text
VCC
 |
high-side device
 |
 +------ output
 |
low-side device
 |
GND
```

### Consequences

- Fast, actively driven HIGH and LOW states
- No pull-up normally required
- Outputs should not normally be tied directly together because one device could drive HIGH while another drives LOW

---

## Why this mattered in the BSPD study

The older and newer circuits combine comparator decisions differently:

- one architecture uses open-collector behavior and wired logic,
- another uses push-pull outputs followed by an explicit logic gate.

The important engineering question is not only “what logic value appears?” but also:

> Who is physically driving the node, and what happens when several outputs interact?

---

## Practical checklist

When reading a schematic, identify:

1. Is the output open-collector/open-drain or push-pull?
2. Where is the pull-up resistor?
3. What voltage rail defines HIGH?
4. Can multiple outputs share the node?
5. What state occurs during power-up or loss of power?

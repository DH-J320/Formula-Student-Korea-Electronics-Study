# Pull-Up, Pull-Down, and Floating Nodes

A high-impedance node has no guaranteed logic state unless another component defines it.

---

## Pull-up

A pull-up resistor gives a node a default HIGH state.

```text
VCC
 |
 R
 |
 +------ signal
```

Another device can still pull the signal LOW because the resistor limits current.

---

## Pull-down

A pull-down resistor gives a node a default LOW state.

```text
signal
 |
 R
 |
GND
```

---

## Floating vs high-impedance

These terms are related but not identical.

A device output can be **high-impedance** while the actual signal line is **not floating** because an external pull-up or pull-down resistor still defines the voltage.

This distinction is especially important when reading open-collector circuits.

---

## Safety perspective

For a safety-related node, ask:

- What state appears if the driving component disconnects?
- What state appears if power disappears?
- Does the passive resistor bias the circuit toward the safe or unsafe state?
- Could a broken wire create a falsely safe reading?

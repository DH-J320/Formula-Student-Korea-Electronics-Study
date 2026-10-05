# Voltage Dividers and Threshold Design

A comparator threshold often begins with a resistor divider.

## Divider equation

`VREF = VCC × Rbottom / (Rtop + Rbottom)`

This is simple, but a safety threshold requires more than plugging numbers into the equation.

---

## What changes the real threshold?

- resistor tolerance
- supply variation
- comparator input offset
- input bias current
- source impedance
- temperature
- hysteresis network

Therefore a nominal `2.50 V` reference is not automatically an exact switching boundary.

---

## Scaling limitation

A passive divider can only scale a voltage toward ground.

It cannot turn a lower voltage into a higher reference.

This matters when selecting devices with internal references: the external signal/reference network must be compatible with the device's actual threshold architecture.

---

## Verification

For a threshold circuit:

1. calculate nominal VREF,
2. calculate tolerance extremes,
3. check comparator input range,
4. sweep the sensor voltage slowly,
5. measure rising/falling switch points,
6. compare with the required safe boundary.

# BSPD Verification Test Matrix

This is a conceptual verification plan derived from the circuit study.

| ID | Scenario | Expected safety behavior | What to record |
|---|---|---|---|
| T01 | normal propulsion, no braking | remain enabled | comparator states, final output |
| T02 | strong braking, low drive | remain enabled | comparator states, timer input |
| T03 | brake + drive conflict shorter than persistence requirement | no completed shutdown event | pulse width, timer/capacitor state |
| T04 | brake + drive conflict longer than persistence requirement | shutdown request | trigger-to-output delay |
| T05 | current sensor below valid range | fault | threshold voltage, response time |
| T06 | current sensor above valid range | fault | threshold voltage, response time |
| T07 | brake sensor below valid range | fault | threshold voltage, response time |
| T08 | brake sensor above valid range | fault | threshold voltage, response time |
| T09 | repeated short conflict pulses | no unintended accumulation | residual capacitor/timer state |
| T10 | fault clears | remain in defined post-fault state | latch state |
| T11 | safe state maintained for recovery interval | reactivation permitted as designed | recovery time |
| T12 | reset command | reset only under valid conditions | input/output sequence |
| T13 | BSPD power interruption | fail-safe response | shutdown line voltage |
| T14 | signal wire open | fail-safe response where required | node voltage |
| T15 | signal short to GND | defined fault behavior | current/voltage |
| T16 | signal short to supply | defined fault behavior | current/voltage |

---

## Measurement principle

For each test, capture both:

1. **electrical state** — voltage / waveform / timing
2. **logical interpretation** — why the circuit considers that state safe or unsafe

That prevents a test report from becoming only a list of oscilloscope screenshots without engineering explanation.

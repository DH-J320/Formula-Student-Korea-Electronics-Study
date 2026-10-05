"""Idealized RC timing study based on the 25EVO BSPD learning exercise.

This is an educational first-principles model, not a SPICE simulation of the
complete vehicle circuit.
"""

import math
import numpy as np
import matplotlib.pyplot as plt

R_CHARGE = 49_000.0       # ohm
C_NOMINAL = 10e-6         # F
V_FINAL = 5.0             # V
V_THRESHOLD = 3.6         # V


def capacitor_voltage(t, resistance, capacitance, v_final=V_FINAL):
    tau = resistance * capacitance
    return v_final * (1.0 - np.exp(-t / tau))


def threshold_crossing_time(resistance, capacitance,
                            v_threshold=V_THRESHOLD,
                            v_final=V_FINAL):
    if not 0 < v_threshold < v_final:
        raise ValueError("threshold must be between 0 and final voltage")
    return -resistance * capacitance * math.log(
        1.0 - v_threshold / v_final
    )


def main():
    tau = R_CHARGE * C_NOMINAL
    t_threshold = threshold_crossing_time(R_CHARGE, C_NOMINAL)

    print(f"Nominal tau: {tau:.4f} s")
    print(f"Ideal threshold crossing: {t_threshold:.4f} s")

    # Nominal charging curve
    t = np.linspace(0, 1.5, 1000)
    v = capacitor_voltage(t, R_CHARGE, C_NOMINAL)

    plt.figure(figsize=(8, 4.5))
    plt.plot(t, v, label="Capacitor voltage")
    plt.axhline(V_THRESHOLD, linestyle="--", label="Comparator threshold")
    plt.axvline(t_threshold, linestyle="--", label=f"Crossing ≈ {t_threshold:.3f} s")
    plt.xlabel("Time [s]")
    plt.ylabel("Voltage [V]")
    plt.title("Ideal RC Charging and Threshold Crossing")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig("rc_delay_nominal.png", dpi=180)

    # Simple capacitance tolerance sweep
    capacitances = {
        "-20% C": 0.8 * C_NOMINAL,
        "Nominal C": C_NOMINAL,
        "+20% C": 1.2 * C_NOMINAL,
    }

    plt.figure(figsize=(8, 4.5))
    for label, capacitance in capacitances.items():
        voltage = capacitor_voltage(t, R_CHARGE, capacitance)
        crossing = threshold_crossing_time(R_CHARGE, capacitance)
        plt.plot(t, voltage, label=f"{label} (t={crossing:.3f}s)")

    plt.axhline(V_THRESHOLD, linestyle="--", label="Threshold")
    plt.xlabel("Time [s]")
    plt.ylabel("Voltage [V]")
    plt.title("Effect of Capacitance Tolerance on RC Delay")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig("rc_delay_tolerance.png", dpi=180)


if __name__ == "__main__":
    main()

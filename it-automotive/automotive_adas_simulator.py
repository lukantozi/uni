#!/usr/bin/env python3
"""
ADAS Simulator for an IT and Automotive project.

Scenario:
- An ego vehicle follows a lead vehicle on a straight road.
- Radar and camera measurements are simulated with noise and possible faults.
- A simple ADAS controller generates warning and braking commands.
- The script saves a CSV log and a plot so students can analyse results.
"""

from __future__ import annotations

import argparse
import csv
import math
import os
import random
from dataclasses import dataclass
from typing import Dict, List, Tuple

import matplotlib.pyplot as plt
import numpy as np


# ==============================
# Data models
# ==============================


@dataclass
class VehicleState:
    """State of the ego vehicle (the controlled car)."""

    position_m: float
    speed_mps: float
    acceleration_mps2: float = 0.0


@dataclass
class LeadVehicleState:
    """State of the lead vehicle (the obstacle / car ahead)."""

    position_m: float
    speed_mps: float
    acceleration_mps2: float = 0.0


@dataclass
class SensorReading:
    """Fused-like container for a single sensor measurement."""

    distance_m: float
    relative_speed_mps: float
    is_valid: bool
    source: str


@dataclass
class ControllerOutput:
    """Controller decision at one time step."""

    warning: bool
    brake_command: float  # 0.0 to 1.0
    requested_deceleration_mps2: float
    degraded_mode: bool
    selected_distance_m: float
    selected_rel_speed_mps: float
    estimated_ttc_s: float
    decision_reason: str


# ==============================
# Utility functions
# ==============================


def clamp(value: float, min_value: float, max_value: float) -> float:
    """Limit a value to the specified numeric range."""

    return max(min_value, min(value, max_value))


# ==============================
# Scenario definitions
# ==============================


def lead_vehicle_acceleration(time_s: float, scenario: str) -> float:
    """Return lead-vehicle acceleration for a given scenario.

    Students can add more scenarios here. The goal is to create different
    traffic situations and then compare controller behaviour.
    """

    if scenario == "normal_following":
        # Almost constant speed with very small speed variation.
        return 0.3 * math.sin(0.35 * time_s)

    if scenario == "sudden_brake":
        # Lead vehicle brakes hard for a short period.
        if 5.0 <= time_s <= 7.5:
            return -5.8
        return 0.0

    if scenario == "cut_in":
        # The lead vehicle suddenly appears closer and then stabilizes.
        return -1.0 if 3.5 <= time_s <= 4.5 else 0.0

    if scenario == "stop_and_go":
        if 4.0 <= time_s <= 7.0:
            return -3.2
        if 8.5 <= time_s <= 11.5:
            return 2.0
        return 0.0

    if scenario == "urban_noise":
        return 0.8 * math.sin(0.7 * time_s)

    raise ValueError(f"Unknown scenario: {scenario}")


# ==============================
# Sensor simulator
# ==============================


class SensorSimulator:
    """Generates radar and camera measurements.

    The model is intentionally simple:
    - radar is usually more robust in distance measurement,
    - camera may be less stable in bad visibility,
    - faults can be injected to emulate real automotive edge cases.
    """

    def __init__(self, rng: random.Random):
        self.rng = rng

    def read_radar(
        self,
        true_distance_m: float,
        true_relative_speed_mps: float,
        time_s: float,
        fault_mode: str,
    ) -> SensorReading:
        """Simulate a radar measurement."""

        # Default noise values. Radar distance is usually fairly good.
        distance_noise = self.rng.gauss(0.0, 0.45)
        rel_speed_noise = self.rng.gauss(0.0, 0.25)
        is_valid = True

        # New fault: add combined sensor noise
        # both sensors stay valid but become noisier between 3 and 9 s. 
        if fault_mode == "combined_sensor_noise" and 3.0 <= time_s <= 9.0:
            distance_noise += self.rng.gauss(0.0, 1.5)
            rel_speed_noise += self.rng.gauss(0.0, 0.8)

        # Fault injection: dropout means no valid radar data.
        if fault_mode == "radar_dropout" and 4.0 <= time_s <= 7.0:
            is_valid = False

        # Fault injection: radar distance spike makes the obstacle appear farther.
        if fault_mode == "radar_spike" and 5.0 <= time_s <= 5.6:
            distance_noise += 7.5

        measured_distance = max(0.0, true_distance_m + distance_noise)
        measured_relative_speed = true_relative_speed_mps + rel_speed_noise


        return SensorReading(
            distance_m=measured_distance,
            relative_speed_mps=measured_relative_speed,
            is_valid=is_valid,
            source="radar",
        )

    def read_camera(
        self,
        true_distance_m: float,
        true_relative_speed_mps: float,
        time_s: float,
        fault_mode: str,
    ) -> SensorReading:
        """Simulate a camera-based perception measurement."""

        distance_noise = self.rng.gauss(0.0, 1.0)
        rel_speed_noise = self.rng.gauss(0.0, 0.5)
        is_valid = True

        if fault_mode == "combined_sensor_noise" and 3.0 <= time_s <= 9.0:
            distance_noise += self.rng.gauss(0.0, 2.5)
            rel_speed_noise += self.rng.gauss(0.0, 1.0)

        # Fog / low visibility makes the camera more noisy.
        if fault_mode == "fog_camera_loss" and 3.0 <= time_s <= 9.0:
            distance_noise += self.rng.gauss(0.0, 3.2)
            rel_speed_noise += self.rng.gauss(0.0, 1.2)

        # Full camera loss for a time window.
        if fault_mode == "camera_dropout" and 6.0 <= time_s <= 9.0:
            is_valid = False

        measured_distance = max(0.0, true_distance_m + distance_noise)
        measured_relative_speed = true_relative_speed_mps + rel_speed_noise

        return SensorReading(
            distance_m=measured_distance,
            relative_speed_mps=measured_relative_speed,
            is_valid=is_valid,
            source="camera",
        )


# ==============================
# Controller
# ==============================


class AEBController:
    """Very simple AEB / FCW controller.

    FCW = Forward Collision Warning
    AEB = Automatic Emergency Braking

    The controller is deliberately readable rather than industrial-grade.
    That makes it easier for students to understand and improve.
    """

    def __init__(self):
        # Students can tune these thresholds and study the consequences.
        self.warning_ttc_s = 3.5 # was 3.0
        self.brake_stage_1_ttc_s = 2.8 # was 2.3
        self.brake_stage_2_ttc_s = 1.4
        self.max_deceleration_mps2 = 8.0

        # Basic filtering memory to reduce noise in the selected signal.
        self.filtered_distance_m = None
        self.filtered_rel_speed_mps = None
        self.alpha = 0.55  # was 0.35; more responsive TTC smoothing

    def select_measurement(
        self,
        radar: SensorReading,
        camera: SensorReading,
    ) -> Tuple[float, float, bool, str]:
        """Choose which sensor measurement should be used.

        Strategy:
        - Prefer radar when valid.
        - If radar is invalid, use camera.
        - If both are invalid, switch to degraded mode and assume a
          conservative emergency-like condition.
        """

        degraded_mode = False
        reason = "radar_primary"

        if radar.is_valid:
            selected_distance = radar.distance_m
            selected_rel_speed = radar.relative_speed_mps
        elif camera.is_valid:
            selected_distance = camera.distance_m
            selected_rel_speed = camera.relative_speed_mps
            degraded_mode = True
            reason = "camera_fallback"
        else:
            # Both sensors lost: degraded mode
            degraded_mode = True

            # if filtered estimate present, reuse it with safety margin
            if (self.filtered_distance_m is not None and self.filtered_rel_speed_mps is not None):
                safety_margin_m = 5.0
                selected_distance = max(0.0, self.filtered_distance_m - safety_margin_m)
                selected_rel_speed = self.filtered_rel_speed_mps
                reason = "both_invalid_last_good_with_margin"
            else:
                # filtered estimate not present, fall back to conservative guess 
                selected_distance = 5.0
                selected_rel_speed = -8.0
                degraded_mode = True
                reason = "both_invalid_conservative_fallback"

        # Light filtering to make the decision signal easier to analyse.
        if self.filtered_distance_m is None:
            self.filtered_distance_m = selected_distance
            self.filtered_rel_speed_mps = selected_rel_speed
        else:
            self.filtered_distance_m = (
                self.alpha * selected_distance + (1 - self.alpha) * self.filtered_distance_m
            )
            self.filtered_rel_speed_mps = (
                self.alpha * selected_rel_speed + (1 - self.alpha) * self.filtered_rel_speed_mps
            )

        return self.filtered_distance_m, self.filtered_rel_speed_mps, degraded_mode, reason

    def compute_ttc(self, distance_m: float, relative_speed_mps: float) -> float:
        """Compute time-to-collision.

        Conventions in this model:
        - relative_speed_mps = lead_speed - ego_speed
        - negative value means the ego vehicle is closing in.
        - TTC is meaningful only when closing speed is negative.
        """

        closing_speed = -relative_speed_mps
        if closing_speed <= 0.05:
            return float("inf")
        return distance_m / closing_speed

    def step(self, radar: SensorReading, camera: SensorReading) -> ControllerOutput:
        """Controller logic executed once per simulation step."""

        distance_m, rel_speed_mps, degraded_mode, reason = self.select_measurement(radar, camera)
        ttc_s = self.compute_ttc(distance_m, rel_speed_mps)

        warning = False
        brake_command = 0.0
        requested_deceleration = 0.0
        decision_reason = reason

        if ttc_s <= self.warning_ttc_s:
            warning = True
            decision_reason += " | fcw"

        # Multi-stage braking. The lower the TTC, the stronger the brake.
        if ttc_s <= self.brake_stage_1_ttc_s:
            brake_command = 0.45
            requested_deceleration = 0.45 * self.max_deceleration_mps2
            decision_reason += " | brake_stage_1"

        if ttc_s <= self.brake_stage_2_ttc_s:
            brake_command = 0.85
            requested_deceleration = 0.85 * self.max_deceleration_mps2
            decision_reason += " | brake_stage_2"

        # In degraded mode we slightly bias towards safety.
        if degraded_mode and warning:
            requested_deceleration += 0.5
            brake_command = clamp(requested_deceleration / self.max_deceleration_mps2, 0.0, 1.0)
            decision_reason += " | degraded_bias"

        requested_deceleration = clamp(requested_deceleration, 0.0, self.max_deceleration_mps2)

        return ControllerOutput(
            warning=warning,
            brake_command=brake_command,
            requested_deceleration_mps2=requested_deceleration,
            degraded_mode=degraded_mode,
            selected_distance_m=distance_m,
            selected_rel_speed_mps=rel_speed_mps,
            estimated_ttc_s=ttc_s,
            decision_reason=decision_reason,
        )


# ==============================
# Simulation core
# ==============================


def run_simulation(
    scenario: str,
    fault_mode: str,
    duration_s: float,
    dt_s: float,
    seed: int,
    output_dir: str,
) -> Dict[str, float]:
    """Run the entire simulation and save outputs.

    Returns summary metrics that are useful for a report or regression testing.
    """

    rng = random.Random(seed)
    sensor_sim = SensorSimulator(rng)
    controller = AEBController()

    # Initial conditions are designed so that different scenarios remain interesting.
    ego = VehicleState(position_m=0.0, speed_mps=24.0)
    lead = LeadVehicleState(position_m=38.0, speed_mps=20.0)

    # Scenario-specific initial states. These are tuned so that the output is
    # interesting enough for classroom analysis and controller tuning.
    if scenario == "sudden_brake":
        ego.speed_mps = 26.0
        lead.position_m = 34.0
        lead.speed_mps = 21.0
    elif scenario == "cut_in":
        lead.position_m = 58.0
        lead.speed_mps = 22.0
    elif scenario == "stop_and_go":
        ego.speed_mps = 18.0
        lead.position_m = 28.0
        lead.speed_mps = 16.0
    elif scenario == "urban_noise":
        ego.speed_mps = 15.0
        lead.position_m = 22.0
        lead.speed_mps = 13.5

    os.makedirs(output_dir, exist_ok=True)
    csv_path = os.path.join(output_dir, f"simulation_log_{scenario}_{fault_mode}.csv")
    plot_path = os.path.join(output_dir, f"simulation_plot_{scenario}_{fault_mode}.png")

    rows: List[Dict[str, float]] = []

    collision = False
    min_true_distance = float("inf")
    min_ttc = float("inf")
    max_brake = 0.0
    degraded_steps = 0

    steps = int(duration_s / dt_s)
    for step in range(steps + 1):
        time_s = step * dt_s

        # Update lead vehicle according to the scenario profile.
        lead.acceleration_mps2 = lead_vehicle_acceleration(time_s, scenario)
        lead.speed_mps = max(0.0, lead.speed_mps + lead.acceleration_mps2 * dt_s)

        # Special case for the cut-in scenario: around 4 seconds the lead vehicle
        # appears much closer, emulating a lane cut-in manoeuvre.
        if scenario == "cut_in" and abs(time_s - 4.0) < dt_s / 2:
            lead.position_m = ego.position_m + 12.0
            lead.speed_mps = max(0.0, ego.speed_mps - 5.5)

        lead.position_m += lead.speed_mps * dt_s

        # True relative quantities.
        true_distance_m = lead.position_m - ego.position_m
        true_relative_speed_mps = lead.speed_mps - ego.speed_mps

        # Generate sensor readings from the ground truth.
        radar = sensor_sim.read_radar(true_distance_m, true_relative_speed_mps, time_s, fault_mode)
        camera = sensor_sim.read_camera(true_distance_m, true_relative_speed_mps, time_s, fault_mode)

        # Controller decision.
        control = controller.step(radar, camera)

        # Convert requested deceleration into ego vehicle dynamics.
        # A small drag term makes the baseline more realistic.
        drag_decel = 0.08 * ego.speed_mps
        ego.acceleration_mps2 = -(control.requested_deceleration_mps2 + drag_decel)
        ego.speed_mps = max(0.0, ego.speed_mps + ego.acceleration_mps2 * dt_s)
        ego.position_m += ego.speed_mps * dt_s

        true_distance_after_update = lead.position_m - ego.position_m

        if control.degraded_mode:
            degraded_steps += 1

        min_true_distance = min(min_true_distance, true_distance_after_update)
        min_ttc = min(min_ttc, control.estimated_ttc_s)
        max_brake = max(max_brake, control.requested_deceleration_mps2)

        if true_distance_after_update <= 0.0 and not collision:
            collision = True

        rows.append(
            {
                "time_s": round(time_s, 3),
                "ego_pos_m": ego.position_m,
                "ego_speed_mps": ego.speed_mps,
                "ego_acc_mps2": ego.acceleration_mps2,
                "lead_pos_m": lead.position_m,
                "lead_speed_mps": lead.speed_mps,
                "lead_acc_mps2": lead.acceleration_mps2,
                "true_distance_m": true_distance_after_update,
                "true_relative_speed_mps": true_relative_speed_mps,
                "radar_distance_m": radar.distance_m,
                "radar_rel_speed_mps": radar.relative_speed_mps,
                "radar_valid": int(radar.is_valid),
                "camera_distance_m": camera.distance_m,
                "camera_rel_speed_mps": camera.relative_speed_mps,
                "camera_valid": int(camera.is_valid),
                "selected_distance_m": control.selected_distance_m,
                "selected_rel_speed_mps": control.selected_rel_speed_mps,
                "estimated_ttc_s": control.estimated_ttc_s if math.isfinite(control.estimated_ttc_s) else 999.0,
                "warning": int(control.warning),
                "brake_command": control.brake_command,
                "requested_deceleration_mps2": control.requested_deceleration_mps2,
                "degraded_mode": int(control.degraded_mode),
                "decision_reason": control.decision_reason,
            }
        )

    # Save CSV log.
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    # Create plots. Matplotlib default styling is intentionally used.
    time_values = [r["time_s"] for r in rows]
    true_distance_values = [r["true_distance_m"] for r in rows]
    ttc_values = [min(r["estimated_ttc_s"], 10.0) for r in rows]
    ego_speed_values = [r["ego_speed_mps"] for r in rows]
    lead_speed_values = [r["lead_speed_mps"] for r in rows]
    brake_values = [r["requested_deceleration_mps2"] for r in rows]

    fig = plt.figure(figsize=(10, 10))

    ax1 = fig.add_subplot(4, 1, 1)
    ax1.plot(time_values, true_distance_values, label="True distance [m]")
    ax1.set_ylabel("Distance [m]")
    ax1.grid(True)
    ax1.legend(loc="best")

    ax2 = fig.add_subplot(4, 1, 2)
    ax2.plot(time_values, ego_speed_values, label="Ego speed [m/s]")
    ax2.plot(time_values, lead_speed_values, label="Lead speed [m/s]")
    ax2.set_ylabel("Speed [m/s]")
    ax2.grid(True)
    ax2.legend(loc="best")

    ax3 = fig.add_subplot(4, 1, 3)
    ax3.plot(time_values, ttc_values, label="Estimated TTC [s]")
    ax3.axhline(controller.warning_ttc_s, linestyle="--", label="Warning threshold")
    ax3.axhline(controller.brake_stage_1_ttc_s, linestyle=":", label="Brake stage 1")
    ax3.axhline(controller.brake_stage_2_ttc_s, linestyle="-.", label="Brake stage 2")
    ax3.set_ylabel("TTC [s]")
    ax3.grid(True)
    ax3.legend(loc="best")

    ax4 = fig.add_subplot(4, 1, 4)
    ax4.plot(time_values, brake_values, label="Requested deceleration [m/s²]")
    ax4.set_xlabel("Time [s]")
    ax4.set_ylabel("Brake / decel")
    ax4.grid(True)
    ax4.legend(loc="best")

    fig.suptitle(f"ADAS simulation | scenario={scenario} | fault={fault_mode}")
    fig.tight_layout(rect=[0, 0.02, 1, 0.98])
    fig.savefig(plot_path, dpi=160)
    plt.close(fig)

    summary = {
        "scenario": scenario,
        "fault_mode": fault_mode,
        "collision": float(collision),
        "min_true_distance_m": min_true_distance,
        "min_estimated_ttc_s": min_ttc,
        "max_requested_deceleration_mps2": max_brake,
        "degraded_mode_ratio": degraded_steps / len(rows),
        "csv_path": csv_path,
        "plot_path": plot_path,
    }

    return summary


# ==============================
# Command-line interface
# ==============================


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the ADAS simulator for the IT and Automotive project.")
    parser.add_argument(
        "--scenario",
        default="sudden_brake",
        choices=["normal_following", "sudden_brake", "cut_in", "stop_and_go", "urban_noise"],
        help="Traffic scenario to simulate.",
    )
    parser.add_argument(
        "--fault",
        default="none",
        choices=["none", "radar_dropout", "radar_spike", "fog_camera_loss", "camera_dropout", "combined_sensor_noise"],
        help="Injected sensor fault mode.",
    )
    parser.add_argument("--duration", type=float, default=12.0, help="Simulation length in seconds.")
    parser.add_argument("--dt", type=float, default=0.1, help="Simulation step in seconds.")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for repeatable results.")
    parser.add_argument(
        "--output_dir",
        default="simulation_outputs",
        help="Directory where the CSV log and plot will be saved.",
    )
    return parser


if __name__ == "__main__":
    args = build_arg_parser().parse_args()

    summary = run_simulation(
        scenario=args.scenario,
        fault_mode=args.fault,
        duration_s=args.duration,
        dt_s=args.dt,
        seed=args.seed,
        output_dir=args.output_dir,
    )

    print("Simulation finished.")
    for key, value in summary.items():
        print(f"{key}: {value}")

    print("\nSuggested student activities:")
    print("1. Compare baseline and fault-injected scenarios.")
    print("2. Tune TTC thresholds and evaluate safety vs comfort.")
    print("3. Improve degraded-mode behaviour and justify your design.")
    print("4. Add one extra scenario and document the results.")

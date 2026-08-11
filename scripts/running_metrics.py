#!/usr/bin/env python3
"""Deterministic calculations for marathon coaching decks."""

import argparse
import json
import math


DISTANCES_KM = {"5k": 5.0, "10k": 10.0, "half": 21.0975, "marathon": 42.195}


def parse_time(value: str) -> float:
    parts = [float(p) for p in value.split(":")]
    if len(parts) == 2:
        return parts[0] * 60 + parts[1]
    if len(parts) == 3:
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    raise ValueError("Use MM:SS or HH:MM:SS")


def fmt_time(seconds: float) -> str:
    seconds = int(round(seconds))
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def vdot(distance_km: float, seconds: float) -> float:
    minutes = seconds / 60
    velocity = distance_km * 1000 / minutes
    vo2 = -4.60 + 0.182258 * velocity + 0.000104 * velocity * velocity
    fraction = 0.8 + 0.1894393 * math.exp(-0.012778 * minutes) + 0.2989558 * math.exp(-0.1932605 * minutes)
    return vo2 / fraction


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--height-cm", type=float)
    ap.add_argument("--weight-kg", type=float)
    ap.add_argument("--monthly-km", type=float)
    ap.add_argument("--rest-hr", type=float)
    ap.add_argument("--max-hr", type=float)
    ap.add_argument("--goal-time")
    ap.add_argument("--race-distance", choices=DISTANCES_KM)
    ap.add_argument("--race-time")
    args = ap.parse_args()

    out = {}
    if args.height_cm and args.weight_kg:
        out["bmi"] = round(args.weight_kg / (args.height_cm / 100) ** 2, 1)
    if args.monthly_km is not None:
        out["weekly_equivalent_km"] = round(args.monthly_km * 12 / 52, 1)
    if args.goal_time:
        sec = parse_time(args.goal_time)
        out["marathon_goal_pace_per_km"] = fmt_time(sec / DISTANCES_KM["marathon"])
    if args.rest_hr is not None and args.max_hr is not None:
        zones = {}
        for name, low, high in [("Z1", .50, .60), ("Z2", .60, .70), ("Z3", .70, .80), ("Z4", .80, .90), ("Z5", .90, 1.00)]:
            reserve = args.max_hr - args.rest_hr
            zones[name] = [round(args.rest_hr + low * reserve), round(args.rest_hr + high * reserve)]
        out["hrr_zones_bpm"] = zones
    if args.race_distance and args.race_time:
        d1 = DISTANCES_KM[args.race_distance]
        t1 = parse_time(args.race_time)
        out["vdot"] = round(vdot(d1, t1), 1)
        out["riegel_equivalents"] = {
            name: fmt_time(t1 * (d2 / d1) ** 1.06) for name, d2 in DISTANCES_KM.items()
        }
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

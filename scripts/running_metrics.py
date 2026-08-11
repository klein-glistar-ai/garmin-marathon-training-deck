#!/usr/bin/env python3
"""Deterministic calculations for marathon coaching decks."""

import argparse
import json
import math


DISTANCES_KM = {"5k": 5.0, "10k": 10.0, "half": 21.0975, "marathon": 42.195}
HR_BANDS = [
    ("low_aerobic", "低强度有氧", (0.65, 0.79), (0.59, 0.74)),
    ("high_aerobic", "高强度有氧", (0.79, 0.88), (0.74, 0.84)),
    ("threshold", "阈值/门槛", (0.88, 0.92), (0.85, 0.89)),
    ("anaerobic_endurance", "无氧耐力", (0.93, 0.95), (0.89, 0.93)),
    ("anaerobic_power", "无氧爆发", (0.96, 1.00), (0.94, 1.00)),
]


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
    ap.add_argument("--age", type=float)
    ap.add_argument("--hr-method", choices=("auto", "mhr", "hrr"), default="auto")
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
    resolved_max_hr = args.max_hr
    max_hr_source = "observed_or_supplied"
    if resolved_max_hr is None and args.age is not None:
        resolved_max_hr = round(208 - 0.7 * args.age)
        max_hr_source = "estimated_208_minus_0.7_age"
    method = args.hr_method
    if method == "auto":
        method = "hrr" if resolved_max_hr is not None and args.rest_hr is not None else "mhr"
    if method == "hrr" and (resolved_max_hr is None or args.rest_hr is None):
        ap.error("HRR requires --rest-hr plus --max-hr or --age")
    if method == "mhr" and resolved_max_hr is None:
        ap.error("MHR requires --max-hr or --age")
    if resolved_max_hr is not None:
        zones = {}
        for key, label, mhr_band, hrr_band in HR_BANDS:
            low, high = hrr_band if method == "hrr" else mhr_band
            if method == "hrr":
                reserve = resolved_max_hr - args.rest_hr
                bpm = [round(args.rest_hr + low * reserve), round(args.rest_hr + high * reserve)]
            else:
                bpm = [round(resolved_max_hr * low), round(resolved_max_hr * high)]
            zones[key] = {
                "label": label,
                "percent": [round(low * 100), round(high * 100)],
                "bpm": bpm,
            }
        out["heart_rate_method"] = method
        out["maximum_hr_bpm"] = round(resolved_max_hr)
        out["maximum_hr_source"] = max_hr_source
        if method == "hrr":
            out["heart_rate_reserve_bpm"] = round(resolved_max_hr - args.rest_hr)
        out["heart_rate_zones"] = zones
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

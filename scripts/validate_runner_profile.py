#!/usr/bin/env python3
"""Validate a normalized runner profile and produce concise follow-up questions."""

import argparse
import json
from pathlib import Path


def get(data, path):
    current = data
    for key in path.split("."):
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def present(value):
    return value is not None and value != "" and value != []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("profile", help="Path to normalized runner profile JSON")
    args = ap.parse_args()
    data = json.loads(Path(args.profile).read_text(encoding="utf-8"))

    missing_critical = []
    missing_recommended = []
    questions = []

    goal_missing = [
        label for path, label in [
            ("goal.race_date", "比赛日期"),
            ("goal.distance_km", "比赛距离"),
            ("goal.target_time", "目标成绩"),
        ] if not present(get(data, path))
    ]
    if goal_missing:
        missing_critical.extend(goal_missing)
        questions.append("目标与时间：请补充" + "、".join(goal_missing) + "。")

    load_missing = []
    if not present(get(data, "training.monthly_km")) or get(data, "training.monthly_km_confirmed") is not True:
        load_missing.append("近3个月跑量的明确口径（每月还是合计）")
    if not present(get(data, "training.weekly_runs")):
        load_missing.append("当前每周跑步次数")
    if load_missing:
        missing_critical.extend(load_missing)
    for path, label in [
        ("training.recent_longest_run_km", "近6–8周最长跑距离"),
        ("performance.pb_dates_or_recency", "PB日期或近期测试成绩"),
    ]:
        if not present(get(data, path)):
            missing_recommended.append(label)
            load_missing.append(label)
    if load_missing:
        questions.append("当前能力与负荷：请补充" + "、".join(load_missing) + "。")

    safety_missing = []
    for path, label in [
        ("health.current_pain_status", "当前疼痛状态"),
        ("health.red_flag_symptoms", "是否存在肿胀、跛行、夜间痛、胸痛、晕厥等红旗症状"),
    ]:
        if not present(get(data, path)):
            missing_critical.append(label)
            safety_missing.append(label)
    for path, label in [
        ("training.available_training_days", "每周可训练日期"),
        ("training.preferred_long_run_day", "偏好的长跑日"),
    ]:
        if not present(get(data, path)):
            missing_recommended.append(label)
            safety_missing.append(label)

    level = get(data, "athlete.training_level")
    if not present(level):
        years = get(data, "athlete.running_years")
        level = "systematic" if isinstance(years, (int, float)) and years >= 2 else "unknown"
    if level == "systematic":
        hr_missing = []
        if not present(get(data, "heart_rate.rest_hr")):
            hr_missing.append("静息心率")
        if not present(get(data, "heart_rate.max_hr")):
            hr_missing.append("可信的最大心率及来源")
        if hr_missing:
            missing_recommended.extend(hr_missing)
            safety_missing.extend(hr_missing)
    if safety_missing:
        questions.append("安全与执行：请补充" + "、".join(safety_missing) + "。")

    readiness = "needs_input" if missing_critical else ("provisional" if missing_recommended else "ready")
    result = {
        "readiness": readiness,
        "inferred_training_level": level,
        "missing_critical": list(dict.fromkeys(missing_critical)),
        "missing_recommended": list(dict.fromkeys(missing_recommended)),
        "questions": questions[:3],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

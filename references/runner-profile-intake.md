# Runner profile intake

## Accepted input

Accept natural language, screenshots, photographed forms, tables, spreadsheets, or JSON. Extract visible information into the schema below. Preserve the original phrase for any value whose unit or time window is unclear.

## Normalized schema

```json
{
  "athlete": {
    "name": null,
    "age": null,
    "sex": null,
    "height_cm": null,
    "weight_kg": null,
    "city": null,
    "running_years": null,
    "training_level": null
  },
  "goal": {
    "race_name": null,
    "race_date": null,
    "distance_km": 42.195,
    "target_time": null
  },
  "training": {
    "monthly_km": null,
    "monthly_km_confirmed": false,
    "raw_volume_text": null,
    "volume_period_months": null,
    "weekly_runs": null,
    "recent_longest_run_km": null,
    "available_training_days": null,
    "preferred_long_run_day": null,
    "strength_training_available": null
  },
  "performance": {
    "pb_5k": null,
    "pb_10k": null,
    "pb_half": null,
    "pb_marathon": null,
    "pb_dates_or_recency": null,
    "recent_race_or_test": null
  },
  "heart_rate": {
    "rest_hr": null,
    "max_hr": null,
    "max_hr_source": null
  },
  "health": {
    "injury_history": null,
    "current_pain_status": null,
    "pain_score_0_10": null,
    "red_flag_symptoms": null,
    "relevant_medical_clearance": null,
    "female_stage_or_symptoms": null
  },
  "delivery": {
    "format": "pptx",
    "visual_direction": null,
    "sponsors": []
  }
}
```

Use ISO dates and `HH:MM:SS` times when possible. `monthly_km_confirmed` is true only when the source clearly says the value is per month. “近3个月跑量560km” is ambiguous and must not automatically become either 560 km/month or 187 km/month.

## Readiness rules

Treat these as critical for a prescriptive race plan:

- Race date, distance, and target time.
- Recent volume with a confirmed time basis, plus weekly running frequency.
- Current pain status and whether red-flag symptoms are present.

Ask for these when they materially affect the plan:

- Recent longest run and a recent race/test or PB recency.
- Available training days and preferred long-run day.
- Resting and credible maximum HR for a systematic runner who needs HRR zones.
- City for environment and course preparation.

Treat height, weight, name, sponsor list, and visual preferences as optional unless the requested analysis depends on them. Female physiological stage and symptoms are sensitive and optional; ask only when relevant, explain why, and allow the athlete to decline.

## Question policy

Ask no more than three grouped questions per round:

1. Goal and timing: missing race, date, distance, or target.
2. Current ability and load: ambiguous volume basis, weekly frequency, longest run, or fitness recency.
3. Safety and execution: current pain/red flags, training availability, and heart-rate inputs.

Do not send a long questionnaire. Omit a group when its information is already sufficient. If only optional information is missing, generate a provisional report and list the assumptions instead of blocking.

## Example normalized from the supplied runner card

```json
{
  "athlete": {
    "name": "于女士",
    "age": 51,
    "sex": "女",
    "height_cm": 163,
    "weight_kg": 53,
    "city": "北京",
    "running_years": 9,
    "training_level": "systematic"
  },
  "goal": {
    "race_name": "南京马拉松",
    "race_date": "2026-11-22",
    "distance_km": 42.195,
    "target_time": "03:30:00"
  },
  "training": {
    "monthly_km": 187,
    "monthly_km_confirmed": true,
    "raw_volume_text": "近3个月总计560km，约187km/月",
    "volume_period_months": 3,
    "weekly_runs": 4,
    "recent_longest_run_km": null,
    "available_training_days": null
  },
  "performance": {
    "pb_5k": "00:21:46",
    "pb_10k": "00:45:15",
    "pb_half": "01:38:00",
    "pb_marathon": "03:31:00",
    "pb_dates_or_recency": null
  },
  "heart_rate": {
    "rest_hr": 43,
    "max_hr": 185,
    "max_hr_source": "observed_or_supplied"
  },
  "health": {
    "injury_history": "髂胫束摩擦综合征",
    "current_pain_status": "轻至中度，仍能跑",
    "pain_score_0_10": null,
    "red_flag_symptoms": null
  }
}
```

This example still needs one concise safety/load follow-up covering the longest recent run, PB recency, pain score or next-day response, red flags, and available training days before a final prescriptive schedule.

# Marathon Training Deck Builder

An OpenAI Codex skill for turning a runner profile supplied as text, an image, a table, or JSON into a sourced, visually verified coaching presentation. It checks information completeness first and asks concise follow-up questions when critical data is missing.

## What it covers

- Athlete data normalization and deterministic metrics
- Missing-information detection with up to three grouped questions
- Pace, MHR/HRR, VDOT, and race-equivalent analysis
- Phased marathon planning with strength and decision gates
- Injury traffic lights and explicit medical boundaries
- Symptom-led female physiology adaptation
- Sponsor integration through training validation rather than claims
- Optional profile-based synthetic runner cover imagery with identity disclosure
- Slide-level sources, rendering, image-fit checks, and overflow QA

## Install

Copy this repository into your Codex skills directory, then invoke:

```text
$build-marathon-training-deck
```

The skill entry point is `SKILL.md`. The intake schema and coaching methodology are in `references/`. `scripts/validate_runner_profile.py` checks readiness, while `scripts/running_metrics.py` provides deterministic calculations.

## Example

```bash
python3 scripts/running_metrics.py \
  --height-cm 163 --weight-kg 53 --monthly-km 187 \
  --rest-hr 43 --max-hr 185 --hr-method hrr --goal-time 3:30:00 \
  --race-distance marathon --race-time 3:31:00
```

## License

MIT

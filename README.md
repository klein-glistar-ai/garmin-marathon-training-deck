# Marathon Training Deck Builder

An OpenAI Codex skill for turning an athlete profile, marathon goal, injury constraints, local conditions, wearable data, and sponsor requirements into a sourced, visually verified coaching presentation.

## What it covers

- Athlete data normalization and deterministic metrics
- Pace, HRR, VDOT, and race-equivalent analysis
- Phased marathon planning with strength and decision gates
- Injury traffic lights and explicit medical boundaries
- Symptom-led female physiology adaptation
- Sponsor integration through training validation rather than claims
- Slide-level sources, rendering, image-fit checks, and overflow QA

## Install

Copy this repository into your Codex skills directory, then invoke:

```text
$build-marathon-training-deck
```

The skill entry point is `SKILL.md`. Detailed methodology and QA checks are in `references/`, while `scripts/running_metrics.py` provides deterministic calculations.

## Example

```bash
python3 scripts/running_metrics.py \
  --height-cm 163 --weight-kg 53 --monthly-km 187 \
  --rest-hr 43 --max-hr 185 --goal-time 3:30:00 \
  --race-distance marathon --race-time 3:31:00
```

## License

MIT

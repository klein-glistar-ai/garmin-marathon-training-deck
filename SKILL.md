---
name: build-marathon-training-deck
description: Build or revise an evidence-based marathon coaching presentation from an athlete profile, target race, injury constraints, local conditions, wearable data, and sponsor requirements. Use for PPT/PPTX training-plan decks that need quantified athlete analysis, pace and heart-rate zones, phased schedules, injury and female-physiology safeguards, race-course strategy, brand-consistent sponsor integration, source notes, and slide-by-slide visual QA.
---

# Build Marathon Training Deck

Turn incomplete runner information into a coach-ready, sourced presentation. Keep coaching decisions explicit, medical uncertainty visible, sponsor content useful, and every visual verified after rendering.

## Required workflow

1. Normalize the brief before calculating anything.
   - Resolve ambiguous units such as “近3个月跑量” versus “每月跑量”.
   - Record race date, target, available weeks, training frequency, recent monthly volume, PB dates, injury status, age, sex, location, and sponsor constraints.
   - Label each important statement as fact, calculation, coaching inference, assumption, or item to verify.
2. Build the athlete model.
   - Calculate BMI, recent weekly-equivalent volume, goal pace, heart-rate zones, and race-equivalent ability.
   - Use maximum-heart-rate percentages for beginners or when only maximum HR is available. Use heart-rate reserve for systematic runners when resting HR and a credible observed maximum HR are available.
   - Use `scripts/running_metrics.py` for deterministic calculations.
   - Read `references/methodology.md` before selecting training load, pace bands, injury modifications, or physiological adaptations.
3. Research unstable facts.
   - Verify current race date, official route, aid rules, course map, local climate, AQI guidance, and current product specifications from primary or official sources.
   - Put direct source URLs in speaker notes on the slide they support.
4. Design the training logic before styling.
   - Use progressive phases, cutback weeks, peak specificity, and taper.
   - Include strength work and explicit decision gates.
   - For active pain, use symptom traffic lights and substitution rules; do not diagnose the cause as fact.
5. Integrate sponsor products by training function.
   - Map each product to a real athlete need, a test session, and a failure signal.
   - Use official product images or user-provided assets. Never synthesize a branded product photo or invent specifications.
   - Keep the entire product visible with contain fitting unless the brief explicitly requests a crop.
   - Separate roles such as monitoring, hydration/electrolytes, carbohydrate, amino-acid supplement, footwear, and apparel.
6. Create the deck with a coherent visual system.
   - Use one dominant brand system, consistent grid, restrained accents, and large readable type.
   - Prefer one message per slide and outcome-led titles.
   - Add a concise source note and uncertainty language where evidence is limited.
7. Render and verify before delivery.
   - Render every slide, inspect every slide image, and run the presentation overflow test.
   - Use `references/qa-checklist.md` as the release gate.

## Recommended narrative

Use this sequence unless the brief requires another structure:

1. Executive conclusion and athlete snapshot
2. Body, performance, volume, and heart-rate analysis
3. Environment and injury-risk model
4. Phased training plan, weekly structure, long runs, and strength
5. Race course, pacing, fueling, and equipment strategy
6. Female physiology adaptation when relevant
7. Sponsor validation matrix
8. Decision gates and explicit unknowns

## Coaching boundaries

- Do not present injury causation, menopause status, anemia, or clinical diagnoses as established without evidence.
- Age alone does not establish menopause. Treat cycle stage and symptoms as information to collect, not a fixed scheduling template.
- Do not promise that a supplement prevents fatigue, injury, dehydration, or improves performance.
- Do not let sponsor placement override safety, product-role clarity, or testing requirements.
- If PBs are old or current race evidence is missing, describe them as historical ability and add a validation workout or tune-up race.

## Resources

- `references/methodology.md`: calculations, planning logic, injury safeguards, female-physiology handling, and sponsor framework.
- `references/qa-checklist.md`: content, evidence, visual, and export release checks.
- `scripts/running_metrics.py`: BMI, weekly-equivalent volume, goal pace, MHR/HRR zones, Riegel equivalents, and Daniels-style VDOT estimates.

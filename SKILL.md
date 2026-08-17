---
name: build-marathon-training-deck
description: Turn a runner profile supplied as natural language, an image, a table, or structured data into an evidence-based marathon coaching report or PPTX. Use when Codex must first check whether athlete, goal, current-load, health, heart-rate, and scheduling information is sufficient; ask concise grouped follow-up questions when critical fields are missing or ambiguous; then produce quantified analysis, pace and heart-rate zones, phased training, injury and female-physiology safeguards, race strategy, optional profile-based synthetic cover imagery, sponsor integration, source notes, and visual QA.
---

# Build Marathon Training Deck

Turn incomplete runner information into a coach-ready, sourced presentation. Keep coaching decisions explicit, medical uncertainty visible, sponsor content useful, and every visual verified after rendering.

## Intake gate

1. Accept the runner profile as text, image, table, spreadsheet, or JSON. Extract it without inventing missing values.
2. Read `references/runner-profile-intake.md`, normalize the profile, and record the exact raw wording for ambiguous fields such as recent running volume.
3. Run `scripts/validate_runner_profile.py` on the normalized JSON.
4. Follow the returned readiness:
   - `ready`: generate the report directly.
   - `provisional`: generate only when missing items do not materially change safety or load; show assumptions and verification items.
   - `needs_input`: ask the returned questions and wait. Ask no more than three grouped questions in one round.
5. Merge answers into the existing profile. Do not ask again for supplied information and do not restart the analysis.

Never hide an ambiguity behind an assumption when it changes weekly volume, plan length, injury safety, or goal pace.

## Required workflow

1. Confirm the intake gate has passed before calculating anything.
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
6. Build the cover visual deliberately.
   - Read `references/cover-visuals.md` when the brief requests a personalized runner image or when a synthetic cover portrait is an approved deliverable.
   - Treat a generated runner as an illustrative representation, never as the athlete's real likeness. Base it only on explicitly supplied traits and disclose the synthetic status on-slide or in an adjacent note.
   - Match the destination frame before generation. Request complete-body framing and use contain fitting when the brief requires the full image to remain visible.
   - Keep apparel brand-neutral unless authentic approved assets are supplied. Never generate sponsor logos, branded product photos, race evidence, or fake screenshots.
7. Create the deck with a coherent visual system.
   - Use one dominant brand system, consistent grid, restrained accents, and large readable type.
   - Prefer one message per slide and outcome-led titles.
   - Add a concise source note and uncertainty language where evidence is limited.
8. Humanize audience-facing Simplified Chinese.
   - Read `references/copy-editing.md` after calculations and coaching decisions are frozen, but before final rendering.
   - When the `qu-ai-wei` skill is available, invoke it in embedded mode on all visible Simplified Chinese copy.
   - Preserve every number, date, source, uncertainty qualifier, medical boundary, and stable training term. Do not rewrite MP, HRR, RPE, VDOT, PB, PacePro, or goal labels merely to sound different.
   - Remove mechanical contrasts, slogan-like claims, repeated labels, abstract process language, and other copy that sounds written for a template rather than for the athlete.
   - Rerender after the copy pass because natural wording changes line length and pagination.
9. Render and verify before delivery.
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

- `references/runner-profile-intake.md`: input schema, readiness rules, grouped follow-up questions, and a worked profile example.
- `references/methodology.md`: calculations, planning logic, injury safeguards, female-physiology handling, and sponsor framework.
- `references/qa-checklist.md`: content, evidence, visual, and export release checks.
- `references/cover-visuals.md`: safe profile-based runner-image generation, disclosure, composition, and fit rules.
- `references/copy-editing.md`: protected facts, embedded `qu-ai-wei` workflow, coaching voice, and post-edit layout checks.
- `scripts/validate_runner_profile.py`: deterministic readiness and missing-information check for normalized runner JSON.
- `scripts/running_metrics.py`: BMI, weekly-equivalent volume, goal pace, MHR/HRR zones, Riegel equivalents, and Daniels-style VDOT estimates.

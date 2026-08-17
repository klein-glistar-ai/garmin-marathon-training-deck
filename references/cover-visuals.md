# Profile-based cover visuals

Use this workflow only when the user requests a generated runner image or clearly approves synthetic cover imagery.

## Identity boundary

- Create an illustrative synthetic person, not a claimed likeness of the athlete.
- Use only explicit profile traits such as age range, sex, athletic context, city, clothing preference, and requested mood.
- Do not infer facial identity, ethnicity, disability, pregnancy, medical condition, or body composition beyond supplied information.
- Add concise disclosure such as `AI 合成人物示意 · 非本人照片` when the image could otherwise be mistaken for the athlete.
- If a real athlete photo is supplied, preserve identity and use it only as authorized by the user; do not silently replace it with a generated lookalike.

## Generation specification

Define the destination frame first, then prompt for:

- `photorealistic-natural` use case;
- the exact landscape, portrait, or square aspect needed by the slide;
- complete-body, half-body, or headshot framing that matches the media slot;
- negative space and subject placement that support the surrounding title;
- the deck palette and lighting without generating logos or branded apparel;
- one person, realistic anatomy, no text, no watermark, and no race-result evidence.

Example prompt core:

```text
Create a premium photorealistic sports editorial image representing the supplied runner profile, not a real identifiable person. Match the cover's portrait frame. Show the complete body with breathing room on every side. Use brand-neutral technical apparel, realistic anatomy, and the deck's restrained black and cyan palette. No text, logos, watermark, race bib, medal, product close-up, or cropped limbs.
```

## Asset handling

1. Save the selected image into the project workspace; do not leave a deck dependency only in a generated-image cache.
2. Use a versioned filename and preserve the original generation.
3. Insert with `contain` when full display is required. Use `cover` only when the crop is explicitly approved and visually inspected.
4. Record the prompt, synthetic disclosure, and local asset path in speaker notes or source notes.
5. Inspect the rendered cover at full slide size for cropped limbs, distorted anatomy, weak contrast, or misleading identity cues.

## Product boundary

Synthetic people may support storytelling. Sponsor watches, shoes, supplements, hats, socks, logos, packaging, screenshots, course maps, and race evidence must use authentic user-provided or official assets.

# Natural Chinese copy pass

Use this pass after the athlete model, calculations, training logic, and evidence are frozen. Its purpose is to improve how the report speaks to the athlete, not to reopen the analysis.

## Protected information

Create a short ledger before editing. Treat these items as locked:

- all numbers, dates, distances, durations, paces, heart rates, percentages, and weekly volumes;
- source attribution and the strength of the evidence;
- facts, assumptions, coaching inferences, and items still awaiting verification;
- medical limitations, pain stop rules, and uncertainty about diagnosis or physiology;
- stable running terms and abbreviations, including MP, HRR, RPE, VDOT, PB, PacePro, LSD, and A/B/C goals;
- sponsor product names and only those product claims supported by current official sources.

If a rewrite changes any locked item, reject it and restore the original meaning.

## Embedded `qu-ai-wei` workflow

When the `qu-ai-wei` skill is installed, invoke it in embedded mode on the complete visible Simplified Chinese copy. Return the revised copy directly into the presentation source rather than producing a separate editing report.

Edit in this order:

1. Rewrite titles so they state the coaching conclusion in plain language.
2. Replace model-facing or process-facing labels with athlete-facing language.
3. Shorten abstract noun stacks and explain the action or decision directly.
4. Remove habitual rhetorical patterns such as repeated “不是……而是……”, artificial three-part slogans, and excessive “红线/闭环/抓手/赋能”.
5. Read every slide as a coach speaking to one serious runner: calm, specific, direct, and never promotional.
6. Compare the result against the protected-information ledger.

## Voice examples

Prefer:

- “3:10可以冲，前提是把半马能力带到全程”
- “前5km先稳住，30km后再看是否加速”
- “经期是否减量，看症状，不按日历硬套”

Avoid template language such as:

- “结论先行：能力成立，但耐力迁移仍需验证”
- “共同未知：赛事条件与个体响应”
- “以三次正确决策构建比赛闭环”

The examples illustrate tone only. Never copy their athlete-specific conclusions into another runner's report.

## Layout verification

Natural Chinese often changes line length. After applying the copy pass:

- rebuild and rerender the deck;
- inspect every edited title, card, table cell, footer, and speaker-note marker;
- check for orphaned punctuation, awkward abbreviation breaks, clipped bottom lines, and newly tiny type;
- rerun overflow and collision tests before release.

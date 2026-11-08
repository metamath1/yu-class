## Overview

This is a **lecture-notes design system** built for Korean-language technical slide decks — the visual register of a careful, considered classroom handout rather than a marketing keynote. The base atmosphere is a **pure white canvas** (`{colors.canvas}` — #ffffff) with **dark-navy ink** (`{colors.ink}` — #1a2e4a) for titles. There is no tinted background, no gradient, no decorative panel. The whole system rests on the strength of one signature device — a **single horizontal yellow accent line** that runs edge-to-edge under every slide title (`{colors.accent-yellow}` — #fcd203, 2.5pt). That line is the only piece of color voltage in the whole layout, and it carries the entire visual identity of the deck.

Brand voltage comes from the **navy + yellow + restraint** triplet — navy for headlines and structural emphasis, a single saturated yellow for the title-rule and rare highlights, and otherwise an extended grayscale palette (`#3c3c3c`, `#555555`, `#696969`, `#888888`) doing all the supporting work. The yellow is warm and high-saturation, deliberately closer to a mechanical-pencil highlighter than a brand color — it functions as a *reading guide* more than a logo accent. Flow diagrams use **extremely pale rounded rectangles** (`{colors.surface-flowbox}` — #f8f8f8) with **hairline borders** (`{colors.hairline}` — #dcdcdc) so the structure ghosts onto the canvas without competing with the type.

The system has three surface treatments that recur across the deck:
1. **White canvas** (`{colors.canvas}`) — the slide floor on every slide
2. **Ghost rounded boxes** (`{colors.surface-flowbox}` — #f8f8f8) — flow-chart nodes, code blocks, comparison columns
3. **Light-gray code block** (`{colors.surface-code}` — #f8f8f8 with no border) — Python source with GitHub-flavored syntax colors

There is no dark surface mode. The deck never inverts to a dark slide; the cream-to-dark rhythm that drives marketing sites is replaced here by a much quieter cadence — **white slide, white slide, white slide** — with the yellow rule under each title acting as the only consistent metronome. This is intentional: the design treats every slide as a textbook page, where structural sameness aids learning.

**Key Characteristics:**
- White canvas (`{colors.canvas}` — #ffffff) with dark-navy headlines (`{colors.ink}` — #1a2e4a). No tint, no gradient, no full-bleed colored bands anywhere in the deck.
- Signature horizontal yellow rule (`{colors.accent-yellow}` — #fcd203, 2.5pt) running edge-to-edge below the title and sub-title on every content slide — the deck's defining visual element.
- Pretendard sans-serif system (Korean modern humanist) at four weights: Pretendard Light for body, Pretendard SemiBold for content-slide titles, Pretendard ExtraBold for emphasized words, and Noto Sans CJK KR Bold for the cover-slide display. Pairs with Consolas for code blocks.
- Body-text hierarchy lives almost entirely in grayscale: `{colors.body-strong}` (#3c3c3c) for lead paragraphs, `{colors.body}` (#555555) for bullets, `{colors.muted}` (#696969) for sub-titles, `{colors.muted-soft}` (#888888) for captions.
- Flow-chart nodes are very-pale rounded rectangles (`{colors.surface-flowbox}` — #f8f8f8 fill, `{colors.hairline}` — #dcdcdc 0.8pt border) connected by thin gray lines (`{colors.connector}` — #696969 1.8pt). The diagrams ghost onto the canvas rather than asserting themselves.
- Code blocks use a borderless light-gray block with **GitHub-flavored syntax colors**: purple keywords (`{colors.code-keyword}` — #7c3aed), teal identifiers (`{colors.code-identifier}` — #008080), orange numerics (`{colors.code-number}` — #e67e00), green strings (`{colors.code-string}` — #22863a), gray comments (`{colors.code-comment}` — #6a9955).
- Border radius is binary in practice: `{rounded.lg}` (≈0.10" / 7pt) for every flow-chart box and code container, square corners for the title-rule and the cover frame.
- Slide rhythm is uniform: title block (≈0.85" tall) → yellow rule → sub-title in muted gray → 0.30–0.50" gap → body content. Bottom of slide carries a tiny "page mark" — a small gray square at the lower-left and an optional short navy underline.

## 청자 중심 문구 원칙

제목, 소제목, 본문, 그림 설명, 하단 문구를 모두 청자가 볼 학습 내용으로 검토한다. 아래 원칙은 배치 패턴보다 우선한다.

- **화면에 필요한 정보만 쓴다.** 그 장에서 이해할 개념, 비교, 입력과 결과, 청자가 할 행동에 기여하는 문장을 사용한다. 여백을 채우거나 매 장을 요약하려고 문장을 덧붙이지 않는다.
- **제작자의 작업 보고를 넣지 않는다.** 자료 정리·집계·편집·생성·검수·재구성 과정에서 제작자가 한 일을 보고하려는 문장은 제외한다. 그 과정 자체가 학습 주제인 경우에는 청자가 배울 원리나 결과를 본문으로 설명한다. 근거 확인에 필요한 작업 기록은 발표자 노트에 둔다.
- **핵심 설명은 본문에 통합한다.** 용어의 뜻이나 도식의 입력·출력 관계가 학습에 필요하면 해당 용어, 단계, 그림 옆에서 설명한다. 본문을 다시 읽어 주는 하단 문장으로 만들지 않는다.
- **수치의 의미는 수치 가까이에서 밝힌다.** 표의 제목, 열 이름, 단위와 합계 이름으로 무엇을 센 것인지 설명한다. 분석자의 처리 내역을 표 밖에 길게 달지 않는다. 해석을 바꾸는 조건이나 한계는 청자에게 필요한 내용이므로 수치 옆에 짧게 남긴다.
- **소제목과 그림 설명도 선택 사항이다.** 제목과 본문에 이미 있는 정보를 반복하면 생략한다. 그림 설명은 그림에서 무엇을 읽어야 하는지 알려 주고, 내용 없는 강조나 진위·완성도에 대한 자기평가를 덧붙이지 않는다.
- **사전 작업 맥락을 가정하지 않는다.** 앞선 대화나 제작 요청을 알아야 뜻이 통하는 지시어, 설명 없는 자료명, 도구 사용 기록은 삭제하거나 화면에 보이는 개념으로 구체화한다.
- **저장 전에는 발표자 노트를 가리고 문구를 검토한다.** 청자가 문장의 대상과 의미를 알 수 있는지, 그 장의 학습 목표에 필요한지, 삭제하면 이해가 손상되는지 확인한다. 필요한 뜻이 있으면 본문을 고치고, 추가 정보가 없으면 삭제한다. 하단 문장을 자동으로 넣는 패턴은 사용하지 않는다.

시연 프롬프트, 학습자가 답할 질문, 실행에 필요한 링크, 수치의 단위·가정, 해석에 필요한 출처는 그 역할이 분명하면 유지한다. 문장이 놓인 위치만으로 삭제 여부를 정하지 않는다.

## Colors

### Brand & Accent
- **Yellow / Accent** (`{colors.accent-yellow}` — #fcd203): The signature highlighter yellow used for the horizontal title-rule on every content slide and for the vertical accent bar on the cover. Used **only** as a 2.5pt rule — never as a fill color, never on text, never on shapes. The most-recognized element of the deck.
- **Navy / Ink** (`{colors.ink}` — #1a2e4a): The titlebar color. Used on every slide title, on the cover-slide display headline, and on the small navy footer-mark line at the lower-left of content slides. Warm dark navy, not pure black, not a brand-saturated blue.
- **Accent Purple** (`{colors.accent-purple}` — #7c3aed): Used inside code blocks for keywords (`if`, `else`, `for`, `def`). Also appears occasionally in flow-chart context labels for "AI-side" or generative-process content as a quiet differentiator from the navy used for "traditional" content. Never used as a UI fill.
- **Accent Teal** (`{colors.accent-teal}` — #008080): Used inside code blocks for variable names and identifiers. Also occasionally as a flow-box fill on the rare comparison slides where two processes need a color split (paired with a muted rose).
- **Accent Orange** (`{colors.accent-orange}` — #e67e00): Used inside code blocks for numeric literals.
- **Accent Green** (`{colors.accent-green}` — #22863a): Used inside code blocks for string literals.

### Surface
- **Canvas** (`{colors.canvas}` — #ffffff): The default slide floor on every slide. Pure white — explicitly not cream, not off-white.
- **Surface Flowbox** (`{colors.surface-flowbox}` — #f8f8f8): The pale-gray fill used on flow-chart rounded rectangles and code-block backgrounds. One step off canvas — visible only because of the hairline border, not because of the fill itself.
- **Surface Card** (`{colors.surface-card}` — #fafafa): A barely-tinted card surface used for the cover-slide title frame and for occasional emphasized callout boxes. Sits between canvas and flowbox.
- **Hairline** (`{colors.hairline}` — #dcdcdc): The 0.8pt border on flow-chart boxes and on the cover-slide title frame. Light gray, low-contrast — the border is structural, not decorative.
- **Hairline Soft** (`{colors.hairline-soft}` — #e1e1e1): Reserved for the rare interior divider inside multi-row tables.
- **Connector** (`{colors.connector}` — #696969): The 1.8pt gray line connecting flow-chart boxes. Same hex as `{colors.muted}`. Connectors are always horizontal or vertical — never diagonal, never curved.

### Text
- **Ink** (`{colors.ink}` — #1a2e4a): All slide-title text. Same dark navy as the brand accent — title color and structural-mark color are deliberately the same value.
- **Title Body** (`{colors.title-body}` — #232323): Used inside flow-chart boxes for the box headline (e.g., "데이터 입력"). Slightly off-pure-black, warmer than `{colors.body-strong}`.
- **Body Strong** (`{colors.body-strong}` — #3c3c3c): Lead paragraphs directly under the yellow rule (typically 21–23pt). The most prominent body color.
- **Body** (`{colors.body}` — #555555): Default running-text and bulleted-list color (typically 16–18pt).
- **Muted** (`{colors.muted}` — #696969): Sub-titles immediately under the slide headline (16pt), and second-level captions.
- **Muted Soft** (`{colors.muted-soft}` — #888888): Footer captions, fine-print, citation lines, the "footer mark" dot at lower-left.
- **On Code** (`{colors.on-code}` — #232323): Default text color inside code blocks (operators, parentheses, default identifiers without role-specific coloring).

### Semantic
The system carries no formal success / warning / error tokens — the deck is academic, not transactional. The closest equivalents:
- **Highlight Yellow** (`{colors.accent-yellow}` — #fcd203): Doubles as the only "draw attention here" cue when used as a horizontal rule under a phrase.
- **Cherry Red** (`{colors.warn-red}` — #c00000 / #ee0000): Appears once or twice in the deck for emphatic correction marks. Rare; treat as out-of-system.

## Typography

### Font Family

The system runs **Pretendard** as its primary face for everything that isn't code — a Korean-language modern humanist sans designed specifically for screen reading. Used at four weights: **Pretendard Light** for body, **Pretendard SemiBold** for content-slide titles, **Pretendard ExtraBold** for inline emphasis, and **Noto Sans CJK KR Bold** as a heavier display alternative on the cover. **Consolas** handles all code blocks. The fallback stack walks `Pretendard, "Noto Sans KR", "Apple SD Gothic Neo", "Malgun Gothic", -apple-system, sans-serif` for prose and `Consolas, "D2Coding", "JetBrains Mono", monospace` for code.

The display/body split is editorial in spirit but uses one family rather than two:
- Noto Sans CJK KR Bold (54pt) → cover h1 only
- Pretendard SemiBold (36pt) → every content-slide title
- Pretendard Light (16–23pt) → body, sub-titles, captions, flow-box content
- Pretendard ExtraBold → inline emphasized words inside Light paragraphs
- Consolas (16pt) → code blocks

The single-family discipline is deliberate. The Pretendard Light at body sizes carries an unusually thin stroke for a Korean sans, which gives the deck its "considered lecture notes" register — closer to a Hangeul textbook than to a corporate slide. The 36pt SemiBold title sits a full weight-step above body without needing a different face.

### Hierarchy

| Token | Size | Weight | Use |
|---|---|---|---|
| `{typography.cover-display}` | 54pt | Bold | Cover slide h1 — Noto Sans CJK KR Bold, navy |
| `{typography.title}` | 36pt | SemiBold | Every content-slide title — Pretendard SemiBold, navy |
| `{typography.lead}` | 23pt | Light | Lead paragraph directly under the yellow rule — Pretendard Light, `{colors.body-strong}` |
| `{typography.body-lg}` | 21pt | Light | Secondary lead text, large bullets |
| `{typography.body-md}` | 20pt | Light | Default body text on text-heavy slides |
| `{typography.body-sm}` | 18pt | Light | Sub-headers (cover subtitle, flow-box headlines, list labels) |
| `{typography.body-xs}` | 17pt | Light | Sub-captions, secondary labels |
| `{typography.caption}` | 16pt | Light | Sub-title beneath every content-slide title; bullet lists; "default" classroom-handout body size |
| `{typography.caption-sm}` | 14pt | Light | Footer captions, source citations, fine-print |
| `{typography.code}` | 16pt | Regular | Code blocks — Consolas |
| `{typography.emphasis}` | inherit | ExtraBold | Inline emphasized words inside a Light paragraph (rare) |

### Principles

Title weight is **always SemiBold at 36pt**, never the heavier ExtraBold. The cover headline is the only place the deck goes above this — and it switches face to Noto Sans CJK KR Bold rather than pushing Pretendard heavier, because Pretendard at very large sizes can read as fragile.

Body type stays at Light (weight 300) for almost everything. This is the deck's defining typographic decision and the source of its quiet, classroom-handout register. Switching body to Regular (weight 400) — even one weight up — would noticeably change the personality of the deck toward "corporate slide." The thin strokes are the voice.

Korean-Latin mixing is consistent: a phrase like "전통적 프로그래밍과 AI 프로그래밍의 차이" runs Pretendard Light/SemiBold across both scripts. The deck never uses a separate Latin-only face for English words inside Korean sentences; Pretendard's Latin coverage is intentionally used.

Numbers in body copy use Pretendard. Numbers inside code blocks use Consolas (in `{colors.accent-orange}`).

### Note on Font Substitutes

If Pretendard is unavailable, **Noto Sans KR Light** is the closest open-source approximation — both are humanist Korean sans designed for screen reading. **Apple SD Gothic Neo** at "Thin" weight is the closest macOS fallback. **Malgun Gothic** is the Windows fallback but reads heavier than Pretendard Light, so font-size compensation may be needed.

For Consolas, **D2Coding** (a popular Korean monospace) is an excellent substitute and arguably handles Korean fallback glyphs better; **JetBrains Mono** is acceptable but reads slightly more "developer-tool" than the textbook tone the deck is aiming for.

The cover-slide display face — **Noto Sans CJK KR Bold** — has no closer substitute since it's already the most widely-shipped CJK heavy weight available; if even Noto is unavailable, fall back to **Pretendard ExtraBold at 54pt** rather than reaching for a non-CJK display.

## Layout

### Slide Format
- **Slide size:** 13.33" × 7.50" (960pt × 540pt), 16:9 widescreen.
- **Outer margin:** ~0.72" left/right, ~0.36" top.
- **Title band:** y = 0.36" → 1.21" (height ~0.85") — slide title sits here.
- **Sub-title band:** y = 1.15" → 1.59" (height ~0.44") — muted-gray sub-title.
- **Yellow rule:** y = 1.54", running x = 0.71" → 12.59" (full inner width). 2.5pt stroke.
- **Body region:** y = 1.85" → 6.00", roughly 4.15" of vertical space.
- **Footer mark zone:** y = 6.00" → 7.20", reserved for the small navy underline + gray dot at the lower-left corner.

### Spacing System
- **Base unit:** 0.10" (≈7pt).
- **Tokens:** `{spacing.xxs}` 0.05" · `{spacing.xs}` 0.10" · `{spacing.sm}` 0.20" · `{spacing.md}` 0.30" · `{spacing.lg}` 0.50" · `{spacing.xl}` 0.75" · `{spacing.xxl}` 1.00".
- **Title-to-yellow-rule gap:** ~0.40" (`{spacing.lg}` minus padding).
- **Yellow-rule-to-body gap:** ~0.30" (`{spacing.md}`) — body lead paragraph starts at y = 1.85".
- **Flow-box internal padding:** 0.15" all sides; the box height for a two-line flow node sits at ~1.15".
- **Flow-box gap (horizontal):** ~1.25" between adjacent boxes — the connector line lives in this gap.
- **Body-paragraph-to-flow-diagram gap:** ~0.40" (`{spacing.lg}`).
- **Flow-diagram-to-trailing-paragraph gap:** ~0.85" — the trailing paragraph at the bottom of the slide is *visibly separated* from the diagram, not flush.

### Grid & Container
- **Inner content width:** ~11.90" (slide width minus 0.72" margins on each side).
- **3-up flow grid:** three boxes of 3.00" × 1.15" with 1.25" connector gaps. Total spans the full inner width.
- **2-up comparison grid (Software 1.0 vs. AI):** two columns of ~5.50" each, with a center divider of empty space (~0.40"). Each column carries its own internal vertical flow stack.
- **Code-and-diagram split:** for slides showing source code beside its execution flow, the code block takes the left ~5.50" at ~3.30" tall and the right-side flow column takes the remaining ~5.50".

### Whitespace Philosophy

The deck breathes in two directions: **horizontal generosity** (the yellow rule runs edge-to-edge regardless of how short the title is — never to the title's text length only) and **vertical restraint** (lead paragraphs sit close under the rule, around 0.30" below it, so the rule visually anchors the title to the body). The bottom third of every slide is intentionally underused — most slides leave 1–2 inches of trailing whitespace below the diagram or list, which is what gives the deck its "lecture handout" register rather than a "marketing slide" register. Don't fill the trailing whitespace. It's load-bearing.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, no border | Slide canvas, title block, lead paragraphs, code blocks |
| Hairline rule | 0.8pt `{colors.hairline}` border | Flow-chart rounded rectangles, the cover-slide title frame |
| Yellow rule | 2.5pt `{colors.accent-yellow}` stroke | The signature horizontal title-rule on every content slide; the vertical accent on the cover |
| Connector rule | 1.8pt `{colors.connector}` stroke | Lines connecting flow-chart boxes |
| Footer rule | 1.8pt `{colors.ink}` stroke, ~5.7" wide | The short navy underline at lower-left of content slides |

The elevation philosophy is **lines first, fills almost never**. There are no drop shadows anywhere in the system. Even the flow-chart rounded rectangles are nearly invisible without their 0.8pt border. The yellow horizontal rule and the connector lines do all the work that a marketing system would assign to color blocks and elevation. This is what gives the deck its "drafted on graph paper" feel.

### Decorative Depth
- The lower-left corner of every content slide carries a tiny "page mark" — a small gray square (~0.10" × 0.10") in `{colors.muted-soft}`, sometimes accompanied by a 5.7"-wide navy underline (`{colors.ink}`, 1.8pt). This mark functions as an unobtrusive page identifier — the equivalent of a textbook's running header.
- Code blocks carry their own internal "depth" through GitHub-flavored syntax coloring rather than through borders or shadows: purple keywords pop against the gray block, orange numerics pull the eye to literals, green strings carry value text. The block itself stays flat and borderless.
- Flow-chart connectors are always **straight orthogonal lines** — never elbow connectors, never curved Bezier paths, never arrowheads. The line carries direction implicitly through left-to-right or top-to-bottom layout.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0 | The yellow title-rule, the navy footer-rule, all connector lines, the cover-slide title frame |
| `{rounded.md}` | ~0.07" / 5pt | Inline highlighter-style boxes (rare) |
| `{rounded.lg}` | ~0.10" / 7pt | Flow-chart rounded rectangles, code-block containers, comparison columns |
| `{rounded.xl}` | ~0.15" / 11pt | The cover-slide outer frame |
| `{rounded.full}` | 50% | Reserved for occasional small icon discs (rare; the deck is mostly aniconic) |

The system is essentially a binary radius choice in practice: **square corners for rules and frames, gently rounded rectangles for nodes and code blocks**. There are no extreme pill shapes, no full-circle decorative dots beyond the lower-left page mark.

### Photography & Illustrations
The deck rarely uses photography. When it does (e.g., a contextual real-world image on a "comparison" slide), the photo is dropped in as a clean rectangle with no border, no rounded corners, and no caption styling — it sits in the layout the same way a flow-box would sit. The photo is never full-bleed and never crosses the yellow title-rule.

When iconography appears, icons are **monochromatic at body-text color** (`{colors.body}` — #555555) — no filled colored discs around them, no two-tone glyphs.

The Python logo and other tool logos appear at native color but small enough (~0.6" × 0.6") that they read as visual punctuation rather than as branded callouts.

## Components

### Slide Header

**`slide-header`** — The top region of every content slide. Contains, in vertical order: the slide title in `{typography.title}` (Pretendard SemiBold 36pt, `{colors.ink}`), an optional sub-title in `{typography.caption}` (Pretendard Light 16pt, `{colors.muted}`), and the **yellow rule** (`{colors.accent-yellow}` 2.5pt, full inner width). Include a sub-title only when it adds information the audience needs beyond the title and body. Total header band height ~1.18". The yellow rule sits at y = 1.54" and is the structural anchor that every body element below it is measured from.

**`slide-title`** — Pretendard SemiBold 36pt in `{colors.ink}` (#1a2e4a). Always single-line; if a title needs a second concept, it goes into the sub-title rather than wrapping the title. Left-aligned at x ≈ 0.72".

**`slide-subtitle`** — Pretendard Light 16pt in `{colors.muted}` (#696969). Sits ~0.05" below the title baseline. Used for the "what this slide is really about" gloss — a single short phrase, never two lines.

**`title-rule-yellow`** — The signature 2.5pt horizontal stroke in `{colors.accent-yellow}` (#fcd203). Runs edge-to-edge from x = 0.71" to x = 12.59" regardless of title length. Square caps. Never replaced with a different color, never thickened past 2.5pt, never split into segments.

### Cover Slide

**`cover-frame`** — A bordered rectangle holding the cover title and subtitle. Background `{colors.canvas}` (sometimes `{colors.surface-card}`), 1pt `{colors.hairline}` border, rounded `{rounded.xl}`. Spans roughly x = 0.89" → 12.45", y = 1.81" → 6.39". This is the only place in the deck where a content area is fully bordered.

**`cover-accent-bar`** — A vertical 2.5pt stroke in `{colors.accent-yellow}` running the full height of the cover-frame's left edge. The cover's analog of the horizontal title-rule: same color, same weight, rotated 90°.

**`cover-display`** — Noto Sans CJK KR Bold at 54pt in `{colors.ink}`. Two lines allowed (e.g., a topic line + a "summary" or "introduction" qualifier line). Left-aligned, sits inside the cover-frame.

**`cover-subtitle`** — Pretendard Light at 18pt in `{colors.muted-soft}`, with bullet phrases separated by a middle dot ` · `. Sits below the cover-display. Used to list the deck's core descriptors in three or four short phrases.

### Body / Content

**`lead-paragraph`** — The body lead immediately under the yellow rule. Pretendard Light at 21–23pt in `{colors.body-strong}` (#3c3c3c). Two lines maximum; if longer, break across visual sections. Left-aligned at x ≈ 0.76".

**`body-paragraph`** — Default running text inside content slides. Pretendard Light at 16–20pt in `{colors.body}` (#555555). Used in trailing summary paragraphs at the bottom of slides and inside the long descriptive sections.

**`body-bullet-list`** — Indented bulleted list, Pretendard Light at 16pt in `{colors.body}`. Bullet markers are filled small dots in `{colors.muted}`. Indent ~0.20" per level. Never numbered unless the content is intrinsically ordered (process steps).

**`emphasis-inline`** — Pretendard ExtraBold inline within a Light body paragraph. Used for keyword emphasis (concept terms, command names). Same color as surrounding text — emphasis carries through weight, not color.

### Flow Diagrams

**`flow-box`** — The pale rounded rectangle used as a flow-chart node. Background `{colors.surface-flowbox}` (#f8f8f8), 0.8pt border in `{colors.hairline}` (#dcdcdc), rounded `{rounded.lg}` (~0.10"). Standard size ≈ 3.00" × 1.15" for a 3-up horizontal flow, ~3.00" × 0.90" for vertical stack rows. Internal text is centered, two lines max — first line in 18pt `{colors.title-body}` (#232323) for the box headline, second line in 16pt `{colors.body}` for the descriptor. Internal padding ~0.15".

**`flow-connector-h`** — Horizontal connector between adjacent flow-boxes. 1.8pt stroke in `{colors.connector}` (#696969). Length matches the gap between boxes (~1.25"). No arrowheads. Direction is implied by left-to-right layout.

**`flow-connector-v`** — Vertical connector between stacked flow-boxes. Same 1.8pt `{colors.connector}` stroke. Length ~0.45" between vertically-adjacent boxes.

**`flow-stack`** — A vertical column of 3–4 `{component.flow-box}` instances connected by `{component.flow-connector-v}`. Used in "process" slides where each step is a phase. The stack centers horizontally inside its column.

**`flow-comparison-2up`** — Two `{component.flow-stack}` instances placed side by side under a single yellow title-rule, with a sub-headline above each stack labeling the column (e.g., a left column for one approach and a right column for an alternative). Used on every "A vs. B" slide. Optional thin vertical divider between columns is ~0.40" of empty whitespace — never an actual ruled line.

**`flow-box-emphasis`** — A variant of `{component.flow-box}` with a colored fill instead of `{colors.surface-flowbox}` — typically `{colors.accent-teal}` at 30% opacity or `{colors.accent-purple}` at 30% opacity, used to differentiate two paths in an A-vs-B comparison. Border drops to 0pt when filled. Use sparingly: most flow-boxes stay in the default ghosted style.

### Code Blocks

**`code-block`** — A borderless light-gray container holding source code. Background `{colors.surface-flowbox}` (#f8f8f8), no border, rounded `{rounded.lg}`, internal padding ~0.20" all sides. Width fits the slide region (typically ~5.50" on split-layout slides, ~11.40" on full-width code slides). Text in `{typography.code}` — Consolas at 16pt — with **GitHub-flavored syntax colors**:
- `{colors.code-keyword}` (#7c3aed) — `if`, `else`, `for`, `def`, `import`, `return`, `class`, `True`, `False`, `None`
- `{colors.code-identifier}` (#008080) — variable names, function names being defined or called
- `{colors.code-number}` (#e67e00) — numeric literals
- `{colors.code-string}` (#22863a) — string literals with surrounding quotes
- `{colors.code-comment}` (#6a9955) — `#`-prefixed comments
- `{colors.on-code}` (#232323) — operators, parentheses, default text
- Built-in functions like `print`, `len` — Pretendard ExtraBold weight applied to the existing identifier color

Line numbers are not displayed. Indentation is rendered as four spaces. There is no language label header.

**`code-inline`** — Consolas at body-text size used inline within prose paragraphs (e.g., referencing a variable name `temperature` inside a sentence). Slightly tinted background `{colors.surface-flowbox}` with ~0.08" horizontal padding, no border. Color follows the same syntax-color scheme as code-block (so an inline `if` stays purple).

### Footer Mark

**`footer-mark`** — The minimal page identifier at the lower-left of every content slide. Two parts: a small gray square (`{colors.muted-soft}` fill, ~0.10" × 0.10") at approximately x = 0.05", y = 6.95"; and an optional short navy underline (`{colors.ink}`, 1.8pt, ~5.72" wide) at y = 6.02". The square dot appears on every content slide; the navy underline appears on slides that benefit from a "this is content territory" anchor at the lower-left, which is most narrative slides. Never label these — no page numbers, no chapter names. The mark is silent.

### Highlight / Emphasis

**`text-highlight-underline`** — A single line of body text with a thin yellow rule underneath it (matching `{colors.accent-yellow}`, 1pt). Used at most once per slide for the line of body copy that carries the slide's takeaway. The underline runs only the width of the highlighted text, not edge-to-edge.

**`emphasized-quote`** — Body text wrapped in Korean quote marks (`"…"`) inside a Pretendard Light paragraph. The deck never uses italic — italicized Korean reads poorly — so quoted phrases substitute for italic emphasis.

## Do's and Don'ts

### Do
- Anchor every content slide on the **horizontal yellow rule under the title**. Without it, the slide reads as off-system within two seconds.
- Use Pretendard Light for body copy and accept how thin it looks. The thin stroke is the deck's voice — dialing it up to Regular or Medium changes the personality entirely.
- Use Pretendard SemiBold (not ExtraBold) at exactly 36pt for content titles. Reserve ExtraBold for inline emphasis only.
- Keep flow-boxes deliberately ghosted: `#f8f8f8` fill, `#dcdcdc` 0.8pt hairline, no shadow. The diagram should read as *structure*, not as *graphics*.
- Use Consolas with GitHub-flavored syntax colors (purple / teal / orange / green) for every code block. Don't switch to a "developer dark" theme.
- Leave 1–2 inches of trailing whitespace at the bottom of most slides. The empty space carries the textbook register.
- **[2025 revision — REMOVED]** ~~Keep the lower-left page-mark dot present on every content slide.~~ The gray dot (`{component.footer-mark}`) has been retired from all slides. It added visual noise without meaningful payoff at presentation scale. Do NOT add it to new slides.
- Use the navy footer underline at lower-left only when the slide benefits from a structural anchor; omit it on quiet text-only slides.

### Don't
- Don't use a tinted or cream canvas. White is the deck's floor.
- Don't change the yellow rule's color, weight, or width. It stays at 2.5pt `#fcd203` running edge-to-edge — even when the title is a single short word.
- Don't add a colored band, full-bleed rectangle, or header strip behind the title. The yellow rule alone does that work.
- Don't add drop shadows to flow-boxes or code blocks. The system is line-driven, not elevation-driven.
- Don't add arrowheads to flow-connectors. Direction is layout-implicit.
- Don't use bold serif faces (Times, Cambria) for titles. Pretendard SemiBold is the title voice; switching to a serif would push the deck into a "academic-paper" register that doesn't match the surrounding rhythm.
- Don't fill the bottom third of slides just because there's room. Trailing whitespace is a feature.
- Don't increase title weight past SemiBold. Pretendard ExtraBold at 36pt reads as shouting; the deck stays measured.
- Don't introduce a new accent color. The system runs on navy + yellow + grayscale + four code-syntax colors. A fifth band — green callout, blue card — would break the discipline immediately.
- Don't add diagonal connectors or curved Bezier arrows in flow diagrams. Orthogonal only.
- **[2025 revision — accent-bar rule]** Never place a left-side navy accent bar (`{colors.ink}`, full box height) on a `ROUNDED_RECTANGLE`. The bar's square corners will protrude past the rounded corners of the card, creating a visible misalignment. Rule: if a card carries a full-height left accent bar, the card **must** use `RECTANGLE` (not `ROUNDED_RECTANGLE`). If rounded corners are required for stylistic reasons, use a narrow inset bar that starts and ends `{spacing.xs}` (0.10") inside the top and bottom edges so it never reaches the rounded corners.
- **[2025 revision — top accent bar rule]** The same constraint applies to horizontal top accent bars. A top-edge yellow bar (`{colors.accent-yellow}`) placed on a `ROUNDED_RECTANGLE` will spill outside the rounded top-left and top-right corners. Rule: any card that carries a flush top or bottom accent bar **must** use `RECTANGLE`. If rounded corners are required, inset the bar by `{spacing.xs}` (0.10") from each side so it stays clear of the rounded corners.
- **[2025 revision — emoji rule]** Do not use Unicode emoji (🏢, 👤, 🔥, etc.) in slide text. Emoji render correctly in PowerPoint on macOS/Windows but are replaced with broken glyphs or empty boxes in LibreOffice headless PDF export and some web-based viewers. Rule: replace all decorative emoji with plain text labels, short Korean/English words, or level-pill rectangles. If a visual marker is needed, use a small filled `RECTANGLE` shape in the appropriate brand color instead.
- **[2025 revision — connector arrow rule]** Do not use Unicode `▶` alone as an arrowhead, and do not pass hardcoded x-offsets to connector helpers. It shifts unpredictably relative to its LINE because text-box baseline alignment varies by renderer. Rule: always calculate connector positions from actual card-boundary coordinates. Given a card at `(x, w)`, its right edge is `x + w`; the next card's left edge is `next_x`. The gap is `next_x - (x + w)`. Place the LINE from `x + w + 0.01` to the midpoint of the gap, then place the `▶` tip centred at the midpoint. If the gap is smaller than 0.20", reduce the tip size to `fontSize: 7` and shorten the line accordingly. Never pass absolute offsets that were valid for one slide's layout but will silently overlap on another.

## Slide Layout Patterns

The deck uses a small, repeating set of layout patterns rather than one-off custom layouts per slide. Pick one and commit.

| Pattern | Description |
|---|---|
| **Cover** | `{component.cover-frame}` containing `{component.cover-display}` and `{component.cover-subtitle}`, with `{component.cover-accent-bar}` on the left edge. One per deck. |
| **Title + lead + flow-3up** | `{component.slide-header}`, then a `{component.lead-paragraph}` of 1–2 lines, then a horizontal 3-up `{component.flow-stack}` of `{component.flow-box}` nodes connected by `{component.flow-connector-h}`. The deck's most common pattern. |
| **Title + comparison-2up** | `{component.slide-header}`, then two `{component.flow-stack}` columns side by side under sub-column-labels. Used for "A approach vs. B approach" slides. |
| **Title + code-and-flow** | `{component.slide-header}`, then a left `{component.code-block}` paired with a right `{component.flow-stack}` showing the code's execution as flow nodes. Used for "this code does this" explanations. |
| **Title + bullet-list** | `{component.slide-header}`, then a single `{component.body-bullet-list}` filling the body region. Used for vocabulary/definition slides and concept summaries. |
| **Title + image** | `{component.slide-header}`, then a single rectangular image filling roughly half the body region. Used sparingly for screenshots, photos, or external diagrams. |
| **Walk-through (empty)** | `{component.slide-header}` with the word "Walk-through" as the title — no body content. The empty body region is intentional; the slide is a verbal-handoff cue during live presentation. |
| **Hands-on practice (empty)** | `{component.slide-header}` with a "Hands on Practice NN" sub-title and a `{component.footer-mark}` carrying a "실습" (practice) caption. Body is left empty — the slide is a live-coding handoff cue. |

### Pattern Discipline
The deck's coherence comes from sticking to these eight patterns across 30+ slides. When in doubt, fall back to **Title + lead + flow-3up** rather than inventing a custom layout.

## Iteration Guide

1. Focus on ONE component at a time. Reference its YAML key (`{component.flow-box}`, `{component.code-block}`, `{component.title-rule-yellow}`).
2. Variants of an existing component (`-emphasis`, `-h`, `-v`, `-2up`) live as separate entries in `components:`.
3. Use `{token.refs}` everywhere — never inline hex.
4. The yellow rule, the SemiBold 36pt title, and the Pretendard Light body are non-negotiable. Don't tune any of these three for individual slides.
5. White canvas + navy ink + yellow rule + grayscale supporting palette is the trinity. Don't introduce a fourth surface tone (no cream sections, no green cards, no dark slides).
6. When in doubt about emphasis: bigger Pretendard Light before bolder weight, and yellow underline before a colored callout.
7. Every slide needs `{component.slide-header}` (with the yellow rule). The `{component.footer-mark}` dot has been retired — do not add it.

## Known Gaps

- Pretendard is open-source but isn't always pre-installed in cloud rendering environments (LibreOffice headless, some web-based PPT viewers). When rendering in those environments, fall back to Noto Sans KR Light and accept that titles will read slightly heavier.
- The exact shade of the navy footer-underline (`#1a2e4a`) is the same hex as the title color. If a deck-wide find/replace ever changes title color, the footer-underline must be changed at the same time — the system doesn't separate them.
- Code-block syntax coloring is hand-applied per character run inside the .pptx. There is no automatic syntax highlighter; if code is updated, syntax colors must be re-applied manually using the documented `{colors.code-*}` palette.
- The deck's "Walk-through" and "Hands-on Practice" patterns are intentionally empty — they carry no body content because they're live-presentation cues. Don't fill them with placeholder content; the empty body is the design.
- Animation, slide transitions, and live-coding overlays are out of scope — this document covers static slide design only.
- **[2025 revision]** The lower-left `{component.footer-mark}` gray dot has been removed from the system. Its documented coordinates (square at x = 0.05", y = 6.95") are now obsolete. Do not add the dot to any new slide.

# TASK

Create a premium animated short for the Instagram channel *Kasa Önü* in the **Kasa Önü Harmanı** visual language described in section 5: one continuous film on a cash-register receipt where giant kinetic typography carries the hook and punchlines, paper cut-out scenes carry places, people and events, and one living ink line carries every transition, chart and diagram. It must feel like a single unbroken piece of hand-made motion design, never a slideshow and never three styles glued together.

# 1. PROJECT CONFIGURATION — EDIT SETTINGS ONLY HERE

**Topic:** {{KONU}}

- Storyboard: {{STORYBOARD}}
- Voiceover: {{SES}}
- Subtitles: Disabled
- Duration without voiceover: 30 seconds
- Format: {{BICIM}}
- Frame rate: 30 fps
- Sound effects: {{EFEKT}}
- Background music: {{MUZIK}}
- Final video format: MP4 (out/final.mp4)

This is the only editable section and the single source of truth. The topic is free text, a sentence or a paragraph; every object, fact, label, number and scene must come from it or from the narration, never from examples elsewhere in this prompt. The same prompt must work for unrelated subjects. All on-screen text is in the language of the topic. If the topic names real products or companies, use their authentic logos and colours, never invented branding.

# 2. HOW TO WORK — CLAUDE CODE

You are running in Claude Code inside a project folder.

- **Build:** create the animation here as `index.html` (plus JS/CSS files if useful). Expose `window.seek(t)` (t in seconds) that draws the exact frame for time t deterministically: no dependence on requestAnimationFrame timing, `Date.now()` or unseeded `Math.random()`. Timing is proportional to the resolved duration, never hard-coded.
- **Render:** drive headless Chrome (Chrome DevTools Protocol, Puppeteer or Playwright; install what is missing), call `seek(i / fps)` for every frame, capture at the configured native resolution and encode with ffmpeg to `out/final.mp4` (H.264, yuv420p).
- **Voiceover enabled:** the recording is in this folder and its duration is the master clock. Get word-level timestamps with Whisper (mlx-whisper or openai-whisper; install if missing) and align each visual idea to the moment it is spoken. Mux the recording into the final MP4. Never invent narration or timestamps.
- **Voiceover disabled:** use the fixed duration and let the pictures, concise on-screen text and moving diagrams carry the explanation.
- **Sound effects enabled:** fetch CC0 sounds from Openverse, `https://api.openverse.org/v1/audio/?q=<search>&license=cc0` (no key needed). Keep them sparse and tied to meaningful moments, place them with ffmpeg at exact timestamps, list sources in `CREDITS.md`.
- **Background music enabled:** use only the music file the user placed in this folder, mixed well below the narration with ducking. Do not synthesize music.
- **Storyboard enabled:** first write a scene table (time, idea, composition, motion, on-screen text) and render PNG preview frames of the key scenes, then stop and ask for approval. Disabled: plan internally and deliver the finished video.

# 3. QUALITY STANDARD

- **An explanation, not a demo reel.** Decide what the viewer must understand, then make the graphics themselves explain it: objects that transform, diagrams that build, numbers that move. Decoration that teaches nothing is cut.
- **Connected storytelling.** Scenes grow out of each other; an element from one idea becomes the start of the next. It must never feel like a slideshow of separate cards.
- **Clear hierarchy.** One main idea per moment, one focal point, generous margins, text readable on a phone and held still long enough to read.
- **Smooth.** Easing on everything, no jitter, no popping, no frame where nothing is decided.

# 4. VERIFICATION

Render many frames as PNG across the whole timeline and look at them. Fix overflowing, overlapping, unreadable, empty or broken frames, and anything that looks generic rather than in this style, until you are proud of the result. Then render the final MP4 and report briefly what it shows.

# 5. STYLE — "KASA ÖNÜ HARMANI" (receipt paper + paper cut-out scenes + one living ink line + kinetic type)

## 5.1 What this style is
The whole video happens on **one long cash-register receipt** (the brand surface of the channel *Kasa Önü*). Three crafts share that receipt, each used only where it is strongest:

| Moment in the story | Craft to use | Why |
|---|---|---|
| The hook (first 1.5 s) and every spoken punchline word | **Kinetic typography** | Words are the image; huge, cropped, fast, readable |
| Any place, person, object or event: a market stall, a shelf, a street, someone walking to the back of a market, a mother with a shopping bag | **Paper cut-out** | Warm, local, handmade; people believe and feel it |
| Every transition, every chart, arrow, price curve, path or diagram | **The ink line** (monoline morph) with kinetic numbers | Nothing ever cuts; one idea grows out of the previous one |

The three never appear as separate "segments". They hand over to each other inside the same frame: a paper object is traced by the line and its paper peels away, leaving the line, which morphs into the next idea; or the line draws an outline and paper pieces drop into it; or a giant word compresses into the line, which becomes the base of a chart. The viewer should feel one continuous hand-made film.

## 5.2 Palette (exact; no gradients anywhere)
- Receipt paper `#F3EFE4` (the ground of every frame; never replaced by coloured full-screen fields)
- Ink `#1C1B18` (the line, body text, outlines)
- Kasa orange `#FF5A1F` (the brand accent: the line's tip dot, the one key word per beat, price stickers, the "truth" moment). Max ~10 % of any frame.
- Receipt grey `#8C8880` (small labels, dashed receipt rules, secondary info)
- Paper cut-out tones, used only on cut-out pieces: terracotta `#C56B50`, mustard `#E8B65C`, sage `#8A9B7C`, dusty blue `#7C9DA5`, pale card `#FFF8EB`, charcoal `#243139`. Mostly muted; orange stays the loudest colour on screen.
Background colour changes are forbidden. Mood changes (evening, night) are shown on the cut-out pieces themselves (a paper sky strip turning dusty blue, a paper moon, bulbs lighting up), never by recolouring the receipt.

## 5.3 The receipt (brand frame)
- The receipt fills the frame edge to edge in the hook (camera pushed in), then the camera eases out over 0.6 s to reveal a 940 × 1620 receipt with zig-zag torn top and bottom edges on a dark `#201F1B` desk, a soft drop shadow, and faint deterministic paper grain.
- Receipt furniture appears only after the hook: header "✻ KASA ÖNÜ ✻" (Space Mono Bold, letter-spaced), a dashed rule, a row "<SERİ ADI> · <NO>" left and a thin orange **progress line** under it that grows with time, and a footer row with a dotted leader. These are quiet (grey/ink, small); they frame, never compete.
- Content lives in a stage area inside the receipt; keep essentials inside it and out of the top 220 px and bottom 380 px of the 1080 × 1920 frame (platform UI).

## 5.4 Kinetic typography (hook and punchlines)
- Fonts: **Space Grotesk Bold** for words and numbers, **Space Mono Bold** for receipt labels and prices in tags (local copies are provided in `fonts/`).
- **Hook rule (first 1.5 s):** frame 0 already shows the hook: at most 5 words, giant (160–260 px), ink with one word in orange, allowed to crop at the frame edges as long as every word is readable. Motion starts on frame 0 (a word rising through a baseline mask, a word slamming in with a 1.08 overshoot, letters tracking tight). No receipt furniture, no small text, no empty frame. At ~1.5 s the hook words compress into the ink line (scaleY → 0 toward their baseline) or are carried off by the line as the camera pulls back to the receipt.
- Punchline words during the story: one word or number at a time at hero size (140–220 px), entering by masked rise, by slam, or by being written by the line; leaving by collapsing into the line. Explanatory text is short (max 7 words) at 56–72 px. Never subtitles, never paragraphs.
- Numbers roll digit by digit (each digit a vertical column) in 0.5–0.8 s; prices are always set in the receipt mono with "₺".

## 5.5 Paper cut-out (scenes, people, events)
- Build every scene from 6–20 distinct cut pieces: stall awnings in strips, crates, tomatoes, shelves, a market aisle in 3 depth layers, people as simple paper figures (head, scarf or cap, body block, arms; friendly dot eyes; no detailed faces).
- Material: slightly irregular cut edges (generate a deterministic jittered polygon per piece), thin lighter edge on top/left, a soft warm shadow offset down-right (4–10 px, 25 % charcoal, blur 6–10 px) that grows when a piece lifts, fine fibre texture generated once and cached per piece.
- Motion: pieces slide in and settle with a tiny rotation overshoot; layers have parallax under camera moves; a person walking is a stepped stop-motion cycle (8–12 poses per second) while the camera moves smoothly; objects fold, flip (tags), lift and drop.
- Walking deeper into a place (e.g. to the back shelf of a market): move the camera forward through parallax layers (foreground shelves slide past and out, background grows), the figure walks in stop-motion, and the **ink line traces the path** on the floor behind them like a receipt route.
- Paper sits on the receipt: it casts a shadow on it, it never hides the receipt furniture.

## 5.6 The ink line (transitions, charts, diagrams)
- One continuous ink monoline, 12 px at 1080 width, round caps and joins, with a small **orange dot at its moving tip** (the pen). It is the only thing allowed to connect one beat to the next.
- **Morph:** every scene change happens through the line. Sample both shapes to 240 points (`getPointAtLength`), align closed shapes for best rotation and direction, interpolate with easeInOutCubic over 0.45–0.7 s. If two shapes are far apart, route through an intermediate state: the drawing unravels into one curve, the curve travels, then curls into the next drawing.
- **Draw-on / draw-off:** new strokes are drawn with dashoffset in reading order; old strokes retract the same way. The orange tip dot rides the end of whatever stroke is currently being drawn.
- **Handover with paper:** (a) *paper → line:* the line traces the outline of the current paper object, the paper piece lifts and peels off (shadow grows, piece slides away), the traced outline remains and morphs on; (b) *line → paper:* the line draws a silhouette, paper pieces drop into it and settle, the line retracts.
- **Charts and diagrams are drawn by the line and labelled with kinetic type:** a price curve drawn left to right with the orange dot riding it; the "real value" as a dashed ink rule; bars as outlined rectangles that fill with a paper piece; arrows as the line itself. Values land as kinetic numbers at the line's endpoints. A giant number can compress into a thin rule that becomes the chart's axis.
- Secondary motion: 3 short speed lines behind fast moves; a decaying wobble `A·e^(-6t)·sin(18t)` (3–5°) after landings.

## 5.7 Composition habits
- One focal point per beat, slightly above centre (y ≈ 44 % of frame). Paper scenes may fill the stage; diagrams keep generous empty paper around them.
- Scale contrast: one hero element + a few small precise labels. Never more than 7 words of readable text on screen at once (hook: 5).
- Alternate scene types in the story rhythm: type → paper → line/chart → paper → type, so the eye gets a new material every 1–2 s without ever cutting.

## 5.8 Rhythm, camera, loop
- A meaningful visual change at least every 1.5 s; with voiceover, each visual idea lands on the word that names it (use the narration's word timestamps).
- Camera: a virtual 2D camera over the receipt. Push-in for the hook, pull-back to reveal the receipt, slow 3 % push-ins on held beats, forward dolly with parallax for walking scenes, short zoom-through on the line's tip into the next idea.
- **Loop:** the last 0.4 s rebuild the hook frame exactly, so the final frame equals frame 0 and the video loops seamlessly; the last spoken words lead into the first spoken words.

## 5.9 Technical implementation
- One HTML page, 1080 × 1920. Layers (bottom → top): desk colour, receipt (SVG with zig-zag clip path, grain canvas cached once), receipt furniture, paper layer (SVG groups per cut piece with filter-free shadows drawn as offset blurred copies or precomputed shadow paths), line layer (SVG path + orange tip circle), type layer (HTML/SVG text with masks), camera wrapper transform.
- Everything is a pure function of `t` in `window.seek(t)`: per-beat local progress `k = clamp((t - start)/dur)`, easing, attribute writes. No CSS transitions, no requestAnimationFrame dependence, no unseeded randomness (seed jitter with a hash of the piece id).
- Stop-motion accents: quantise the local time of paper pieces to 1/12 s where wanted (`tq = floor(t*12)/12`), keep camera, line and type at full 30 fps.
- Shared utilities: `samplePath`, `morph(a,b,k)`, `draw(path,k)`, `rollNumber(el,from,to,k)`, `paperPiece(id, polygon, colour)`, `peel(piece,k)`, `drop(piece,k)`, easing set (easeOutBack 1.7, easeInOutCubic, easeInCubic).

## 5.10 Sound (search terms)
Paper: "paper slide", "paper flip", "paper crumple short", "cardboard tap". Line: "marker draw", "pen scratch", "swish". Type: "whoosh short", "thud soft", "stamp". Shop: "cash register ding", "coins", "receipt printer". Sparse: one sound per meaningful event, never a continuous bed. If audio hosts are blocked, synthesise equivalents and note it in CREDITS.md.

## 5.11 Content rules for this channel (Kasa Önü standard)
- Tell the topic as our own short story in Turkish, located in everyday Turkish life (pazar, bakkal, market, mahalle, kasa). The viewer understands the trick from the story.
- Never show statistics, studies, surveys, percentages as evidence, or theory names (no "çapa etkisi", no "araştırmaya göre", no "satıcıysan").
- No question endings like "yoruma yaz"; the ending loops into the beginning.
- Frame 0 must be a complete, readable hook (≤5 words) with motion starting immediately.

## 5.12 Cheap shortcuts to avoid
1. **Using the three crafts as separate chapters** → they hand over inside the same frame (trace-and-peel, outline-and-drop, word-to-rule).
2. **Coloured full-screen backgrounds or gradients** → always the receipt; mood lives on paper pieces.
3. **Cross-fading or cutting between scenes** → the ink line morphs or carries every change.
4. **Flat vector shapes called "paper"** → irregular cut edges, edge highlight, real offset shadows, parallax layers, stop-motion accents.
5. **Small text in the hook or wall-of-words beats** → ≤5 giant words at frame 0, ≤7 readable words later.
6. **Explaining the trick with a theory label** → let the story and the drawn chart show it.

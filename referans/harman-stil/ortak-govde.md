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

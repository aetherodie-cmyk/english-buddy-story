# Story Learning Prototype

An experimental learning project for mobile-first, story-based vocabulary learning.

**Episode 01: The Wrong Message → Episode 02: three paths**

Read four opening scenes, choose A/B/C to enter the matching Episode 02 story, and explore the other paths afterward. Tap vocabulary for help and listen to scenes, paths, or words.

## Privacy

No identifying information or detailed learning records are stored. Voice, speed, and the A/B/C story choice are saved only in your browser’s localStorage. Nothing is sent to a learning service.

No analytics, login, database, backend, API keys, or Learning Record integration. Narration uses the browser/device speech synthesis feature; available voices depend on the device.

## Publish

GitHub Pages serves `index.html` directly from the root of `main`. Artwork is in `assets/`; styles and scripts are embedded; no build or framework is required. The frozen source pack is kept in `content/story-pack-v2.1/`. After changing Episode 02 story or vocabulary sources, run `python3 scripts/build_episode2.py` to refresh the HTML.

Site: https://aetherodie-cmyk.github.io/english-buddy-story/

## Prototype worklog — 2026-09-20

Student feedback: narration was silent on iPhone in both Safari and Chrome.

Added visible speech start/end/error/timeout feedback and a system-default voice test. Playback now retains the active utterance, resumes a paused engine, and avoids cancelling an idle engine. Speech still starts directly from a tap. No backend or new data storage was added.

Validation: browser interaction regression checks and simulated speech lifecycle/error tests passed. These tests do not establish audible output on a physical iPhone; that remains the next verification.

## Story visual rules

**No text inside story illustrations.** All story text, vocabulary, grammar, titles, and teaching notes belong in HTML.

See [Story Visual Guide](docs/STORY_VISUAL_GUIDE.md) for Mia / Leo character references and panel layout rules.

### Visual update — 2026-09-20

Decision: illustrations provide setting, characters, atmosphere, and visual memory anchors; they must not duplicate teaching text. Replaced the old images with one text-free 2×2 storyboard, displayed as four complete panels using CSS. The hero now uses a plain gradient. Story wording is unchanged. Restored device-only A/B/C choice persistence as requested.

Validation: mobile widths 320–430px and desktop widths 768/1280px passed panel aspect-ratio and overflow checks. All four panel positions, the PNG load, 13 vocabulary cards, voice controls, and A/B/C persistence passed browser smoke tests. Story prose and narration were compared against the previous version and are unchanged. Physical iPhone audio remains a separate verification.

### Episode 02 update — 2026-09-20

Added the frozen v2.1 A/B/C paths and three illustrations. Choosing a path opens its story immediately; the other two remain available at the end. Added ten verified L3/L4 vocabulary cards using the supplied lemma mapping, including `observed` → `observe`. Existing voice settings and device-only choice storage remain in use. Language Discovery follows the Episode 02 story in a collapsed section.

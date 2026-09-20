# Story Learning Prototype

An experimental learning project for mobile-first, story-based vocabulary learning.

**Episode 01: The Wrong Message**

Read four story scenes, tap vocabulary cards, listen to scenes or words, and choose A/B/C to explore a possible continuation.

## Privacy

No personal learning data stored. Only voice and speed preferences are saved in your browser’s localStorage. Story choices are not saved or transmitted.

No analytics, login, database, backend, API keys, or Learning Record integration. Narration uses the browser/device speech synthesis feature; available voices depend on the device.

## Publish

GitHub Pages serves `index.html` directly from the root of `main`. Images, styles, and scripts are embedded; no build or framework is required.

Site: https://aetherodie-cmyk.github.io/english-buddy-story/

## Prototype worklog — 2026-09-20

Student feedback: narration was silent on iPhone in both Safari and Chrome.

Added visible speech start/end/error/timeout feedback and a system-default voice test. Playback now retains the active utterance, resumes a paused engine, and avoids cancelling an idle engine. Speech still starts directly from a tap. No backend or new data storage was added.

Validation: browser interaction regression checks and simulated speech lifecycle/error tests passed. These tests do not establish audible output on a physical iPhone; that remains the next verification.

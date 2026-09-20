# CODEX HANDOFF — v2.1

Use this v2 pack instead of v1.

## Do not rewrite frozen story copy
Use `episode-01/story.md` and all three files under `episode-02/`.

## Vocabulary
Use the 10 verified target words in `LEARNING_PLAN.md`. Level badges may now be shown exactly as recorded there. Do not promote Foundation Words to Target Words.

## UX
EP01 four scenes → A/B/C → matching EP02 immediately.
Save choice in localStorage. After the chosen path, allow `Explore another path`.
Vocabulary help is on-demand. Language Discovery is after-story and collapsible.
Keep Scene Listen, Word Listen, Voice selector, Story/Word speed, Try Voice and saved settings.
No long quiz.

## Images
Use supplied image assets. Follow `STORY_VISUAL_GUIDE.md`: no instructional text inside illustrations, no face/key-object cropping on mobile.

## Do not add
EP03, login, database, analytics, Google Sheet, Learning Record, Telegram integration, runtime AI, Mini App, production Bot changes.

## Deploy
Public `aetherodie-cmyk/english-buddy-story`; keep private English Buddy repo unchanged. Deploy GitHub Pages and mobile smoke-test.

## Acceptance
EP01 loads; all images load; A/B/C route correctly; all three EP02 paths work; other paths remain explorable; vocabulary popup/TTS/voice settings/localStorage work; no PII/secrets; no horizontal overflow; Pages HTTP 200.

Report repo URL, Pages URL, commit, deployment status, HTTP result, mobile test, and browser-TTS limitations.


## Vocabulary mapping
Use `VOCABULARY_MAPPING.csv` / `.md` as the implementation source of truth for popup content and lemma mapping. Natural forms such as `observed` must map to `observe`. Do not write new vocabulary definitions in code.

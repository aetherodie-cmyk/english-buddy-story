# Story Visual Guide

**No text inside story illustrations.**

Illustrations provide setting, characters, atmosphere, and visual memory anchors. Story prose, vocabulary, grammar, captions, scene titles, and teaching instructions must be rendered in HTML, never baked into the artwork. A phone may be visible, but its display must not contain readable story text.

## Episode 01 character visual reference

[Approved storyboard: Episode 01](../assets/episode01-scenes.png)

This image is the visual reference for future episodes; reuse the reference image when commissioning or generating artwork. These are fictional story characters, not student identities.

### Mia

- Teenage schoolgirl with long, dark brown hair, slightly wavy loose strands and a soft fringe.
- Large brown eyes, softly shaped face, expressive worried/curious gaze.
- White collared school shirt with a muted burgundy ribbon at the neck.
- Dark navy/charcoal outer jacket and a dark backpack with visible shoulder straps.
- Smartphone is a recurring prop; keep its screen free of readable text.

### Leo

- Teenage schoolboy with short, tousled dark brown/near-black hair.
- Slim build, youthful face, reserved expression, often shown looking back over his shoulder.
- Dark hooded jacket, dark trousers, and a black backpack.
- Preserve these visible clothes; do not invent a new school crest or uniform identity.

### Emma

- Teenage schoolgirl with warm brown hair, tied up or loosely gathered.
- Slightly lighter outer layer than Mia, with the same school-age appearance and cinematic anime style.
- More outwardly expressive than Mia, while remaining part of the same visual world.

## Style, light, and color

Cinematic anime illustration with detailed hair, expressive eyes, natural proportions, and carefully shaded school interiors. Avoid chibi proportions or switching to a different rendering style between episodes.

Use deep navy, charcoal, and cool blue-gray shadows, contrasted with warm amber sunset or light from a classroom doorway. The mood is quiet, mysterious, and curious. Preserve character identity under changing light; amber highlights do not imply a new hair color.

## Character consistency

Episode 02 and later must keep Mia and Leo's face shape, hairstyle, hair/eye color, age impression, build, and established clothing recognizable. Change pose, framing, expression, or lighting as the story requires. A wardrobe change should be an explicit story/design decision, not an accidental redesign.

Use the approved image as a reference, not just a text prompt. Compare new artwork against it before acceptance. Do not add typography, captions, labels, vocabulary, or visible teaching material.

## Episode 01 panel mapping and presentation

The supplied 1536×1024 image is a 2×2 storyboard, in reading order:

1. Top left: Mia receives a mysterious message.
2. Top right: Mia meets Leo in the corridor.
3. Bottom left: Mia investigates near the stairs with her phone light.
4. Bottom right: Mia approaches the mysterious classroom.

Each panel has a 3:2 aspect ratio. The site uses one unchanged PNG, with CSS `background-size: 200% 200%` and the corresponding corner position. This isolates each panel without cropping its contents. Keep the storyboard dividers; do not crop faces to fill a taller card.

On mobile, panel width is 100% of the card. On desktop, keep the existing two-column story cards and show the complete panel with neutral space as needed. Do not stretch the art or use `object-fit: cover` to fill a mismatched aspect ratio.

## Episode 02 path artwork

The three supplied images in `assets/` show Follow Leo, Room 403, and Tell Emma. Render the full image for each path and preserve faces, phones, the photograph, and other story clues. Use the same Mia and Leo references above; the supplied Tell Emma image establishes Emma's first visual reference.

## Before publishing

- Verify four panels in the correct order and no text inside artwork.
- Check faces and important props remain visible on mobile and desktop.
- Preserve the formal English text in HTML and the narration text.
- Check vocabulary popups, voice controls, and A/B/C selection/persistence.
- Keep the site independent of the English Buddy Bot and Learning Record.

"""Render the frozen Episode 02 story pack into the static site."""

import csv
import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "content/story-pack-v2.1"
PAGE = ROOT / "index.html"


with (PACK / "VOCABULARY_MAPPING.csv").open(encoding="utf-8-sig", newline="") as file:
    words = list(csv.DictReader(file))

forms = {
    form.strip().lower(): row["lemma"]
    for row in words
    for form in row["forms"].split(",")
}


def inline_markup(line):
    pieces = re.split(r"(\*\*[^*]+\*\*)", line)
    rendered = []
    for piece in pieces:
        if piece.startswith("**") and piece.endswith("**"):
            surface = piece[2:-2]
            lemma = forms.get(surface.lower())
            if lemma:
                rendered.append(
                    f'<button class="word" data-word="{html.escape(lemma)}">'
                    f"{html.escape(surface)}</button>"
                )
            else:
                rendered.append(f"<strong>{html.escape(surface)}</strong>")
        else:
            rendered.append(html.escape(piece))
    return "".join(rendered)


paths = {
    "A": ("Follow Leo", "path-a-follow-leo.jpg", "Mia watches Leo and a stranger outside the science building"),
    "B": ("Room 403", "path-b-room-403.jpg", "Mia finds a photograph in Room 403"),
    "C": ("Tell Emma", "path-c-tell-emma.jpg", "Mia and Emma compare the messages on their phones"),
}

articles = []
for letter, (title, image_name, alt) in paths.items():
    source = (PACK / "episode-02" / f"path-{letter.lower()}.md").read_text()
    paragraphs = [item.strip() for item in source.split("\n\n") if item.strip()][1:]
    prose = "\n".join(f"<p>{inline_markup(item)}</p>" for item in paragraphs)
    articles.append(
        f'''<article class="path-card" data-path="{letter}" hidden>
  <div class="path-image-wrap"><img src="assets/{image_name}" alt="{html.escape(alt)}" width="500" height="346" loading="lazy"></div>
  <div class="path-copy">
    <div class="kicker">EPISODE 02 · PATH {letter}</div>
    <h2>{html.escape(title)}</h2>
    <div class="path-prose">{prose}</div>
    <button class="listen" data-episode2-listen="{letter}">🔊 Listen to this path</button>
  </div>
</article>'''
    )

section = '''<!-- EPISODE 02 START -->
<section class="episode-two" id="episode-2" hidden>
  <div class="episode-heading"><div class="kicker">THE STORY CONTINUES</div><h2>Episode 02</h2><p id="path-intro"></p></div>
  ''' + "\n".join(articles) + '''
  <details class="discovery episode-discovery">
    <summary>Language Discovery · 展開學習線索</summary>
    <div class="discovery-inner">
      <h3>Look a little closer</h3>
      <div class="grammar"><strong>✦ Grammar · Although A, B</strong><p>Although entering alone made her nervous, she wanted to determine why everyone seemed afraid of this room.</p><p>although 引出讓步：雖然一件事成立，另一件事仍然發生。</p></div>
      <div class="grammar"><strong>✦ Writing · Show, don't just tell</strong><p>Mia was nervous. → The answer did nothing to reduce Mia's anxiety.</p><p>用動作或感受讓讀者看見情緒。</p></div>
      <div class="grammar"><strong>✦ Reading · Infer from clues</strong><p>人物的行動、訊息與三角形符號，讓你推測他們可能知道什麼？可從故事找到支持自己想法的線索。</p></div>
    </div>
  </details>
  <nav class="explore" aria-label="Explore another path"><div class="kicker">CURIOUS ABOUT ANOTHER CHOICE?</div><h3>Explore another path</h3><div class="options" id="explore-options"></div></nav>
</section>
<!-- EPISODE 02 END -->'''

data = {
    row["lemma"]: {
        "level": row["level"],
        "zh": row["zh_core"],
        "example": row["story_example"],
        "explanation": row["popup_explanation"],
    }
    for row in words
}

page = PAGE.read_text()
page = re.sub(
    r"<!-- EPISODE 02 START -->.*?<!-- EPISODE 02 END -->|<div class=\"footer-note\">Episode 02 · Coming soon.*?</div>",
    section,
    page,
    count=1,
    flags=re.S,
)
new_data = "const episode2Vocab=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";"
if "const episode2Vocab=" in page:
    page = re.sub(r"const episode2Vocab=.*?;", new_data, page, count=1)
else:
    page = page.replace("const scenes=", new_data + "\nconst scenes=", 1)
PAGE.write_text(page)

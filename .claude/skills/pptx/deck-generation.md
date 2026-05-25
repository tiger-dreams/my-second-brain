# Deck Generation Guide

Use this guide when you create or maintain a PowerPoint deck as code.

This is not a personal template. It is a reusable operating guide for people who want to generate PPTX files with `pptxgenjs`, keep the deck editable, and avoid losing manual PowerPoint changes.

---

## When to Use This

Use this workflow when:

- You are creating a new deck from notes, a script, a meeting log, or a rough outline.
- The deck will be revised repeatedly.
- You want the source of truth to be a JavaScript file, not only the final `.pptx`.
- You may manually edit the PPTX and later need to sync those changes back to code.

If you are only editing an existing company template, start with [editing.md](editing.md). If you need API syntax details, use [pptxgenjs.md](pptxgenjs.md).

---

## Recommended Folder Structure

Keep each deck self-contained.

```text
docs/deck/
├── create_deck_<slug>.js
├── deck_<slug>.pptx
├── assets/
│   ├── slide03_reference.png
│   └── slide12_screenshot.jpg
└── README.md                 # optional: source notes, run command, caveats
```

For larger repositories, this structure also works:

```text
decks/<slug>/
├── create_deck_<slug>.js
├── output/
│   └── <slug>.pptx
└── assets/
```

Choose one structure and keep paths relative to the script.

```js
const path = require("path");

const asset = (...parts) => path.join(__dirname, "assets", ...parts);
const outPath = path.join(__dirname, "deck_example.pptx");
```

Avoid absolute paths such as `/Users/name/Desktop/image.png`; they will break on another machine.

---

## Source of Truth

The JavaScript generator should be the source of truth.

```text
outline / notes / assets
        ↓
create_deck_<slug>.js
        ↓
deck_<slug>.pptx
```

If someone edits the PPTX directly, do not leave that change only in PowerPoint. Read the updated PPTX and reflect the change back into the JS file before regenerating.

---

## Basic Workflow

1. Define the audience and the one-sentence thesis.
2. Write the slide spine before designing individual slides.
3. Set design tokens at the top of the JS file: colors, fonts, slide size, margins.
4. Create small reusable helpers for page numbers, section tags, cards, dividers, and image placement.
5. Store all images in `assets/`.
6. Generate the PPTX.
7. Inspect the output as images or in PowerPoint.
8. Fix the JS, regenerate, and repeat.
9. If PPTX was edited manually, reverse-sync those edits into JS.

---

## Minimal Generator Skeleton

```js
"use strict";

const pptxgen = require("pptxgenjs");
const path = require("path");

const pptx = new pptxgen();
pptx.layout = "LAYOUT_WIDE";

const C = {
  bg: "FAF9F5",
  ink: "141413",
  muted: "6C6A64",
  accent: "CC785C",
  card: "EFE9DE",
  hairline: "E6DFD8",
};

const FONT = "Arial";
const SW = 13.33;
const SH = 7.5;
const ML = 0.8;
const CW = SW - ML * 2;
const TOTAL = 3;

let slideNo = 0;
const originalAddSlide = pptx.addSlide.bind(pptx);
pptx.addSlide = (...args) => {
  const slide = originalAddSlide(...args);
  slide._slideNo = ++slideNo;
  return slide;
};

function pageNo(slide) {
  return String(slide._slideNo).padStart(2, "0");
}

function motif(slide) {
  slide.addShape(pptx.ShapeType.rect, {
    x: ML, y: 0.28, w: 1.1, h: 0.025,
    fill: { color: C.accent },
    line: { color: C.accent },
  });
  slide.addText(`${pageNo(slide)} / ${TOTAL}`, {
    x: SW - 1.8, y: 0.22, w: 1.5, h: 0.28,
    fontFace: FONT,
    fontSize: 9,
    color: C.muted,
    align: "right",
    margin: 0,
  });
}

{
  const slide = pptx.addSlide();
  slide.background = { color: C.bg };
  motif(slide);
  slide.addText("Deck title", {
    x: ML, y: 1.2, w: CW, h: 0.8,
    fontFace: FONT,
    fontSize: 44,
    color: C.ink,
    margin: 0,
  });
}

pptx.writeFile({ fileName: path.join(__dirname, "deck_example.pptx") });
```

---

## Practical Rules

### Use Stable Slide Numbers

Do not type page numbers manually on each slide. Assign slide numbers when `addSlide()` is called and render them through a helper.

This prevents errors when a slide is inserted or deleted.

### Keep Assets Local

Put visual assets in `assets/` and reference them with `path.join(__dirname, ...)`.

If an image was pasted manually into PowerPoint, extract it from `ppt/media/` and save it into `assets/` before regenerating the deck.

### Preserve Image Ratio

Check the source image size before deciding width and height.

```bash
python3 - <<'EOF'
from PIL import Image
img = Image.open("assets/example.png")
w, h = img.size
print(w, h, "ratio=", w / h)
EOF
```

Then place the image by ratio:

```js
const imgH = 4.2;
const imgW = imgH * 1.355;
slide.addImage({ path: asset("photo.jpg"), x: 7.0, y: 1.5, w: imgW, h: imgH });
```

### Avoid Emoji in Slides

Emoji rendering varies across PowerPoint, Google Slides, LibreOffice, and operating systems. Use icons, simple shapes, or text labels instead.

For icon-heavy decks, prefer converting SVG icons to PNG before embedding if Google Slides compatibility matters.

### Be Careful With Fonts

Use fonts that are installed on the target machine. If a font does not render, PowerPoint will silently fall back and line breaks may change.

For cross-machine decks, prefer common fonts or document the font requirement in the deck folder.

### Reduce Mixed-Language Line Break Problems

Korean and English mixed in one text box can wrap awkwardly. If a line breaks strangely:

- Rewrite the phrase in Korean.
- Make the text box wider.
- Reduce font size slightly.
- Split the phrase into separate text boxes.
- Use shorter labels instead of full sentences.

### Use Duplicate Slides for Simple Click/Tap Reveals

For compatibility, use adjacent duplicate slides for simple before/after reveals instead of relying on complex animations.

Example:

- Slide 03: English quote
- Slide 04: Same layout, Korean translation

This works reliably in PowerPoint, Google Slides, PDF export, and screen sharing.

---

## Reverse-Sync Manual PPTX Edits

When the PPTX was edited directly, inspect the actual slide XML and copy those changes back to JS.

Use raw XML parsing rather than assuming the JS still matches the PPTX.

```bash
python3 - <<'EOF'
import zipfile, re

pptx = "docs/deck/deck_example.pptx"
EMU = 914400

for slide_num in [19, 20]:
    print(f"\n=== Slide {slide_num} ===")
    with zipfile.ZipFile(pptx) as z:
        raw = z.read(f"ppt/slides/slide{slide_num}.xml").decode("utf-8")

    for sp in re.findall(r"<p:sp>(.*?)</p:sp>", raw, re.DOTALL):
        off = re.search(r'<a:off x="(-?\d+)" y="(-?\d+)"', sp)
        ext = re.search(r'<a:ext cx="(\d+)" cy="(\d+)"', sp)
        texts = re.findall(r"<a:t[^>]*>(.*?)</a:t>", sp)
        if off and ext and texts:
            x = int(off.group(1)) / EMU
            y = int(off.group(2)) / EMU
            w = int(ext.group(1)) / EMU
            h = int(ext.group(2)) / EMU
            print(f"TEXT x={x:.3f} y={y:.3f} w={w:.3f} h={h:.3f} | {' / '.join(texts)}")

    for pic in re.findall(r"<p:pic>(.*?)</p:pic>", raw, re.DOTALL):
        off = re.search(r'<a:off x="(-?\d+)" y="(-?\d+)"', pic)
        ext = re.search(r'<a:ext cx="(\d+)" cy="(\d+)"', pic)
        rid = re.search(r'r:embed="([^"]+)"', pic)
        if off and ext:
            x = int(off.group(1)) / EMU
            y = int(off.group(2)) / EMU
            w = int(ext.group(1)) / EMU
            h = int(ext.group(2)) / EMU
            print(f"IMAGE rid={rid.group(1) if rid else '-'} x={x:.3f} y={y:.3f} w={w:.3f} h={h:.3f}")
EOF
```

If images were pasted manually, inspect slide relationships and extract the media:

```bash
python3 - <<'EOF'
import zipfile, pathlib

pptx = "docs/deck/deck_example.pptx"
out = pathlib.Path("docs/deck/assets")
out.mkdir(parents=True, exist_ok=True)

with zipfile.ZipFile(pptx) as z:
    for name in z.namelist():
        if name.startswith("ppt/media/"):
            target = out / pathlib.Path(name).name
            target.write_bytes(z.read(name))
            print("extracted", target)
EOF
```

Rename extracted assets to meaningful names such as `slide20_file_tree.png`, then update the JS to use those files.

---

## QA Checklist

Run these checks before handing off the deck.

```bash
node -c docs/deck/create_deck_<slug>.js
node docs/deck/create_deck_<slug>.js
```

Check slide count and page number sequence:

```bash
python3 - <<'EOF'
import zipfile, re

pptx = "docs/deck/deck_example.pptx"
total = 22

with zipfile.ZipFile(pptx) as z:
    slides = sorted(
        [n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)],
        key=lambda n: int(re.search(r"(\d+)", n).group(1)),
    )
    pages = []
    for n in slides:
        raw = z.read(n).decode("utf-8")
        text = "".join(re.findall(r"<a:t[^>]*>(.*?)</a:t>", raw))
        m = re.search(r"(\d{2}) / " + str(total), text)
        pages.append(m.group(1) if m else "??")

print("slide_count", len(slides))
print("sequence_ok", pages == [f"{i:02d}" for i in range(1, total + 1)])
print("pages", pages)
EOF
```

If available, render previews:

```bash
python scripts/office/soffice.py --headless --convert-to pdf output.pptx
pdftoppm -jpeg -r 150 output.pdf slide
```

Inspect for:

- Wrong slide number sequence
- Text overflow
- Odd line breaks
- Missing images
- Low contrast
- Uneven margins
- Manually edited PPTX changes not reflected in JS

---

## Handoff Rule

When the final deck is delivered, keep these files together:

- `create_deck_<slug>.js`
- generated `.pptx`
- `assets/`
- any short README or source notes

A deck is maintainable only when another person can regenerate it without your local machine, private folders, or memory of manual edits.

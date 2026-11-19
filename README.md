# The Learning Brain

Illustrated pages on how the brain builds, stores, and uses knowledge: 139 topic pages in 11 groups (the brain-region tour plus 10 series), each with labelled brain drawings, the key studies in plain language, activities and sources. The first 115 topics also have a short video.

Everything runs in the visitor's browser. There is no server code, database or build step on the host: the `site/` folder is the whole website.

## Folders

| Folder | What it holds |
|---|---|
| `site/` | **The published website.** `index.html` is the home page, `site/<id>/` holds one topic page (with its `episode.mp4` and `poster.jpg`), and `site/assets/nav.js` is the shared menu. |
| `src/gen/` | Page generators (`<id>.py`) and the shared kits (`common.py`, `dlkit.py`, `pkit.py` for activity-first pages, `wkit.py`). A generator writes `src/<folder>/template.html`. |
| `src/<folder>/` | Each page's `template.html`, `build.py`, styles and captions (`srt.json`). |
| `src/nav/` | `site.json` (every series and topic, in order), `related.json` (3 related topics per page), `nav_src.js` + `nav.css` (the menu). |
| `src/shared/` | Inputs every build needs: `brain.js` (the brain drawings), base CSS and page scripts. |
| `src/tools/` | `build_site.py` (builds pages into `site/`) and `make_nav.py` (builds `site/assets/nav.js`). |
| `src/tests/` | `check_site.py`, a full check of the built site. |

Page ids and folders are the same except `hippocampus` (source in `src/hippo/`) and `test-that-teaches` (source in `src/feature/`).

## Build

Requires Python 3. Run from `src/`:

```bash
cd src
python3 tools/build_site.py              # menu + every page
python3 tools/build_site.py p03 w07      # just these pages (the menu is always rebuilt)
python3 tools/build_site.py --gen p03    # rerun gen/p03.py first, after editing the generator
```

Preview locally (pages need a web server, not a double-click):

```bash
cd site && python3 -m http.server 8000   # then open http://localhost:8000/
```

## Links and the menu

- **The menu, previous/next links, related topics and the home page's topic cards all come from one file, `site/assets/nav.js`.** Each page loads it with `<script src="../assets/nav.js" data-page="<id>">`, and it works out every link from its own address. That means the site works at a domain root (Vercel) or in a sub-folder (GitHub Pages).
- **Links to other pages inside page content** are written in the sources as `@@LB:<id>@@` (for example `@@LB:lb10@@` or `@@LB:home@@#pagesT`). `build_site.py` turns them into relative links (`../lb10/`, `../#pagesT`) and stops with an error if a token names a page that doesn't exist.

## Adding things

**A topic to an existing series.** Write `src/gen/<id>.py` (copy a neighbour), create `src/<id>/build.py` (copy a neighbour's and change the id), add the topic to that series in `src/nav/site.json`, give it 3 related ids in `src/nav/related.json`, then run `python3 tools/build_site.py --gen <id>`. Every other page picks up the new menu entry automatically, because they all load the same `nav.js`.

**A new series.** Add it to `site.json` with a home-page anchor (e.g. `"anchor": "xyT"`), add related lists, and add a matching section to `src/gen/home.py` with the next `cg<N>` grid id. Then build the new pages and `home`.

## Checks

```bash
pip install playwright && playwright install chromium
cd src
python3 tests/check_site.py               # every page at desktop width
python3 tests/check_site.py --phone p03   # also at 390 px with reduced motion
```

For each page it checks JavaScript errors, that the page opens at the top, sideways scrolling, accessibility (axe-core), that the menu opens, that previous/next and related links appear, and that every link to another page, every video and every poster resolves.

## Publishing

- **Vercel:** import this repository. `vercel.json` already tells Vercel to publish `site/` with no build step and to add trailing slashes (needed so each page finds its own video). Every push to `main` then goes live.
- **GitHub Pages:** see `.github/workflows/pages.yml` (needs a public repository on a free plan).

Videos are about 600 MB in total, and the largest is 8 MB. That is within GitHub's limits (100 MB per file; repositories ideally under 1 GB). Replacing a video keeps the old copy in the history, so if videos will be re-cut often, consider hosting them elsewhere and linking to them.

## Standards the pages follow

- Illinois colours: navy `#13294B`, orange `#FF5F05`.
- Fonts: Fraunces, Source Sans 3, Montserrat.
- WCAG AA contrast, and labelled brain regions.
- Plain wording.
- Every number traced to a source.
- Activities that teach, with every branch checked.
- Pages open at the top.
- "In popular culture" sections appear on brain-region pages only.

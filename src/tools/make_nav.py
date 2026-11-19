"""Build the shared menu.
Writes:
  ../site/assets/nav.js  - the one menu file every page loads at run time
  nav/nav.html           - the <script> tag that build.py scripts put into each page (__NAV__)
  nav/coll.js            - empty stub (the topic cards now come from assets/nav.js)
Run from src/:  python3 tools/make_nav.py
To add a series: append it to nav/site.json, add 3 related ids per new page to nav/related.json,
run this, then build the new pages (tools/build_site.py)."""
import json, os

S = json.load(open('nav/site.json'))
R = json.load(open('nav/related.json'))
ids = [it['id'] for g in S for it in g['items']]
assert len(ids) == len(set(ids)), 'duplicate page ids in site.json'
for k, v in R.items():
    for x in v:
        assert x in ids, f'related.json: {k} lists unknown page {x}'

j = lambda o: json.dumps(o, ensure_ascii=False, separators=(',', ':'))
src = open('nav/nav_src.js').read()
out = src.replace('__SITE__', j(S)).replace('__REL__', j(R)).replace('__CSS__', j(open('nav/nav.css').read()))
os.makedirs('../site/assets', exist_ok=True)
open('../site/assets/nav.js', 'w').write(out)
open('nav/nav.html', 'w').write('<script src="__ROOT__assets/nav.js" data-page="__CURRENT__"></script>\n')
open('nav/coll.js', 'w').write('/* renderColl() is defined by assets/nav.js */\n')
print('nav built:', len(ids), 'topics in', len(S), 'series,', len(R), 'related lists')

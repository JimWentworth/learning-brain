"""Build the whole site into ../site/.
Run from src/:
  python3 tools/build_site.py            # rebuild the menu and every page
  python3 tools/build_site.py lb02 p01   # only these pages (plus the menu)
  python3 tools/build_site.py --gen ...  # also rerun gen/<id>.py first (rewrites <folder>/template.html)

For each page: <folder>/build.py fills <folder>/template.html into <folder>/index.html (not committed),
then this script turns @@LB:<id>@@ link tokens into relative links and writes site/<id>/index.html.
Media (episode.mp4, poster.jpg) live directly in site/<id>/ and are never touched here."""
import json, os, re, subprocess, sys

os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')   # always run from src/
FOLDER = {'hippocampus': 'hippo', 'test-that-teaches': 'feature'}   # page id -> source folder, where they differ

args = sys.argv[1:]
regen = '--gen' in args
want = [a for a in args if not a.startswith('--')]

subprocess.run([sys.executable, 'tools/make_nav.py'], check=True)
S = json.load(open('nav/site.json'))
ids = [it['id'] for g in S for it in g['items']] + ['home']
known = set(ids)
for w in want:
    assert w in known, f'unknown page id {w}'

def rel(frm, to):
    up = '' if frm == 'home' else '../'
    return (up or './') if to == 'home' else f'{up}{to}/'

def export(pid):
    d = FOLDER.get(pid, pid)
    if regen and os.path.exists(f'gen/{d}.py'):
        subprocess.run([sys.executable, f'gen/{d}.py'], check=True)
    subprocess.run([sys.executable, f'{d}/build.py'], check=True)
    h = open(f'{d}/index.html').read()
    def tok(m):
        assert m.group(1) in known, f'{pid}: link to unknown page {m.group(1)}'
        return rel(pid, m.group(1))
    h = re.sub(r'@@LB:([a-z0-9-]+)@@', tok, h)
    h = h.replace('__ROOT__', '' if pid == 'home' else '../')
    for bad in ('claude.ai/artifact', '@@LB:', '__NAV__', '__CURRENT__'):
        assert bad not in h, f'{pid}: leftover {bad}'
    out = '../site/index.html' if pid == 'home' else f'../site/{pid}/index.html'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(h)

for pid in (want or ids):
    export(pid)
print('built', len(want or ids), 'pages into site/')

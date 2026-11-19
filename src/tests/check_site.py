"""Check the built site the way a visitor sees it.
Serves ../site/ under a sub-folder (/learning-brain/, like GitHub Pages; a domain root works the same way),
then for every page (or the ids given): JS errors, opens at the top, no sideways scroll, axe accessibility
violations, the menu opens and lists links, previous/next and related links render, every same-site link
and the video resolve.
Needs: pip install playwright && playwright install chromium
Run from src/:  python3 tests/check_site.py [--phone] [page ids...]"""
import asyncio, functools, http.server, json, os, sys, threading, urllib.request, urllib.error
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HERE, '../../site'))
AXE = os.path.join(HERE, 'vendor/axe.min.js')
PREFIX = '/learning-brain/'

class H(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        p = path.split('?')[0].split('#')[0]
        if not p.startswith(PREFIX): return '/nonexistent'
        return os.path.join(SITE, p[len(PREFIX):])
    def log_message(self, *a): pass

class Server(http.server.ThreadingHTTPServer):
    def handle_error(self, request, client_address): pass   # the browser drops video streams mid-file; ignore

def serve():
    s = Server(('127.0.0.1', 0), H)
    threading.Thread(target=s.serve_forever, daemon=True).start()
    return f'http://127.0.0.1:{s.server_address[1]}{PREFIX}'

checked = {}
def ok(u):
    if u not in checked:
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, method='HEAD'), timeout=10); checked[u] = r.status == 200
        except urllib.error.HTTPError:
            checked[u] = False
    return checked[u]

async def main():
    args = sys.argv[1:]; phone = '--phone' in args; want = [a for a in args if not a.startswith('--')]
    S = json.load(open(os.path.join(HERE, '../nav/site.json')))
    ids = want or ['home'] + [it['id'] for g in S for it in g['items']]
    base = serve(); problems = 0
    sizes = [(1280, 'no-preference')] + ([(390, 'reduce')] if phone else [])
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for w, rm in sizes:
            ctx = await b.new_context(viewport={'width': w, 'height': 900}, reduced_motion=rm)
            for pid in ids:
                pg = await ctx.new_page(); errs = []
                pg.on('pageerror', lambda e: errs.append(str(e)[:120]))
                url = base if pid == 'home' else f'{base}{pid}/'
                await pg.goto(url); await pg.wait_for_timeout(500)
                bad = []
                if errs: bad.append('js: ' + '; '.join(errs))
                if await pg.evaluate('scrollY'): bad.append('not at top')
                if await pg.evaluate('document.documentElement.scrollWidth>innerWidth'): bad.append('sideways scroll')
                await pg.add_script_tag(path=AXE)
                v = await pg.evaluate("axe.run(document,{resultTypes:['violations']}).then(r=>r.violations.map(v=>v.id+'('+v.nodes.length+')'))")
                if v: bad.append('axe: ' + ', '.join(v))
                await pg.click('#lbnavBtn')
                n = await pg.evaluate("document.getElementById('lbnavPanel').hidden?-1:document.querySelectorAll('#lbnavBody a').length")
                if n < 1: bad.append(f'menu did not open or is empty ({n})')
                await pg.keyboard.press('Escape')
                if pid != 'home' and await pg.evaluate("document.querySelectorAll('#lbmore .lbpn a,#lbmore .lbrel a').length") < 3:
                    bad.append('previous/next or related links missing')
                if pid == 'home':
                    c = await pg.evaluate("document.querySelectorAll('.coll .card').length")
                    if c != sum(len(g['items']) for g in S): bad.append(f'home shows {c} topic cards')
                links = await pg.evaluate("[...document.querySelectorAll('a[href]')].map(a=>a.href).concat([...document.querySelectorAll('video')].map(v=>v.currentSrc||v.querySelector('source')?.src||'').filter(Boolean),[...document.querySelectorAll('video[poster]')].map(v=>v.poster))")
                for l in {l.split('#')[0] for l in links if l.startswith(base)}:
                    if not ok(l): bad.append('broken: ' + l[len(base):])
                if bad:
                    problems += 1; print(w, pid, bad)
                await pg.close()
            await ctx.close()
        await b.close()
    print(f'checked {len(ids)} pages at {len(sizes)} size(s), {len(checked)} distinct links; pages with problems: {problems}')

asyncio.run(main())

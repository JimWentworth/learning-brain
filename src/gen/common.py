CSS=open('shared/lb_css.txt').read()
PRE=open('shared/lb_pre.txt').read()
QUIZFN=open('shared/lb_quizfn.txt').read()
EXTRA_CSS='''
.screen{position:relative;background:var(--night-2);border:1px solid var(--night-line);border-radius:8px;min-height:340px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;padding:18px}
.screen:focus-visible{outline:3px solid #FCB316;outline-offset:3px}
.keys{display:flex;gap:12px;flex-wrap:wrap;justify-content:center}
.keys[hidden]{display:none}
.keys button{appearance:none;min-width:150px;min-height:56px;border-radius:12px;border:2px solid #8FA3C2;background:#13294B;color:#fff;font:800 20px var(--body);cursor:pointer}
.keys button small{display:block;font:600 13px var(--body);color:#C9D3E3}
.lbox{background:#fff;border:1px solid var(--rule);border-radius:10px;padding:22px;margin-top:22px}
.lres{display:grid;gap:10px;margin:14px 0 0;max-width:600px}
.lres .row{display:grid;grid-template-columns:190px minmax(0,1fr) 90px;gap:10px;align-items:center;font-size:16px}
@media (max-width:520px){.lres .row{grid-template-columns:120px minmax(0,1fr) 80px}}
.lres .bar{height:16px;background:#E3E8EF;border-radius:8px;overflow:hidden}.lres .bar i{display:block;height:100%;border-radius:8px}
.lres b{text-align:right;font-variant-numeric:tabular-nums}
.pmsg b.h{display:block;font-size:19px;margin-bottom:4px}
.pbtn.sec{background:transparent;color:var(--ink);border:2px solid var(--ink)}
.pbtn:disabled{background:#C9D1DC;color:#3D4A5C;cursor:default}
'''
def page(o):
    hero_js=o['hero_js']
    pre=PRE
    import re
    a=pre.index('BR.R.hip.lab');b=pre.index('\n',pre.index("stage('heroBrain'"))
    pre=pre[:a]+hero_js+pre[b:]
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{o['title']}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,600;0,9..144,800;0,9..144,900;1,9..144,300;1,9..144,600&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
<style>
{CSS}{EXTRA_CSS}{o.get('css','')}
__COLLCSS__
</style>
<style>.vnote{{margin:14px 0 0;padding:10px 14px;border-left:4px solid #FF5F05;background:rgba(255,255,255,.06);color:var(--night-ink);font-size:17px;line-height:1.5;max-width:68ch}}.vnote b{{color:#FCB316}}</style>
</head>
<body>
<a class="skip" href="#main">Skip to the article</a>
__NAV__

<header class="hero" aria-labelledby="title">
  <div class="hero-inner">
    <div>
      <div class="label">{o.get('label','The Learning Brain · Topic '+o['n'])}</div>
      <h1 id="title">{o['h1']} <em>{o['em']}</em></h1>
      <p class="dek">{o['dek']}</p>
      <div class="byline"><span>About {o['read']} minutes to read</span><span><a href="#watchT">Watch the video</a></span>{o['jumps']}</div>
    </div>
    <div class="hero-brain"><canvas id="heroBrain" role="img" aria-label="{o['hero_aria']}"></canvas></div>
  </div>
</header>

<section class="watch" aria-labelledby="watchT">
  <div class="wide">
    <h2 class="label" id="watchT" style="margin-bottom:14px">Watch · {o['mins']}</h2>
    <div class="frame"><video id="ep" controls playsinline preload="metadata" poster="poster.jpg" src="episode.mp4"></video></div>
    <div class="meta"><span><b>{o['vtitle']}</b> · {o.get('epi','The Learning Brain, episode '+o['n'])}</span><span>Captions are on; turn them off in the player.</span></div>
    {('<p class="vnote"><b>About this video.</b> '+o['vnote']+'</p>') if o.get('vnote') else ''}
    <details class="transcript"><summary>Read the transcript</summary><p id="transcript"></p></details>
  </div>
</section>

<main id="main">
<article>
{o['body']}
  <div class="wide">
    <h2 class="sec" style="max-width:700px;margin-left:auto;margin-right:auto"><span class="n">Why it matters for learning</span>{o['tips_h']}</h2>
    <ol class="tips">
{o['tips']}
    </ol>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Your turn</span>Check what stuck</h2>
    <p>Answer from memory, without scrolling back.</p>
    <div class="quiz" id="quiz"></div>
  </div>

  <div class="wide lbmore" id="lbmore"></div>

  <footer class="sources">
    <div class="col">
      <p class="label" style="color:var(--ink-2)">Sources</p>
      <ol>
{o['sources']}
      </ol>
      <p style="font-size:16px;color:var(--ink-2)">The brain drawing and both activities are simplified illustrations, not the original experiments.</p>
    </div>
  </footer>
</article>
</main>

{pre}{o['js']}
/* ---------- quiz ---------- */
const Q={o['quiz']};
{QUIZFN}renderColl('coll','{o['id']}');
}})();
</script>
</body>
</html>
'''

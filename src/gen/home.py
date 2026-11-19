import json
CSS=open('shared/lb_css.txt').read()
PRE=open('shared/lb_pre.txt').read()
a=PRE.index('BR.R.hip.lab');b=PRE.index('\n',PRE.index("stage('heroBrain'"))
HERO="stage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.47,s:fitS(W,H,1.32),t,active:['pfc','hip','amy','par','cer','vta'],labels:[],deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});"
PRE=PRE[:a]+HERO+PRE[b:]
PRE=PRE[:PRE.index('(function(){const v=$(\'ep\')')]
html=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Learning Brain: How the Brain Builds, Stores, and Uses Knowledge</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,600;0,9..144,800;0,9..144,900;1,9..144,300;1,9..144,600&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
<style>
{CSS}
__COLLCSS__
.start{{list-style:none;padding:0;margin:22px 0 0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}}
@media (max-width:820px){{.start{{grid-template-columns:minmax(0,1fr)}}}}
.start li{{background:#fff;border:1px solid var(--rule);border-top:6px solid var(--orange);border-radius:0 0 8px 8px;padding:18px 20px}}
.start .who{{font:800 14px var(--body);letter-spacing:.1em;text-transform:uppercase;color:var(--accent-ink);margin:0 0 6px}}
.start h3{{font-size:23px;margin:0 0 8px;line-height:1.2}}
.start p{{margin:0;font-size:17px;line-height:1.5}}
.ov{{max-width:700px;margin:0 auto 4px;font-size:19px;line-height:1.55}}
.grp{{margin:44px 0 0}}
.grp h2.sec{{max-width:700px;margin-left:auto;margin-right:auto}}
.series{{list-style:none;padding:0;margin:22px 0 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}}
.scard{{background:var(--night);color:var(--night-ink);border-radius:8px;padding:18px 20px;display:flex;flex-direction:column;gap:6px}}
.scard .sn{{font:800 14px var(--body);letter-spacing:.1em;text-transform:uppercase;color:var(--orange)}}
.scard h3{{font-size:24px;line-height:1.15;margin:0}}
.scard h3 a{{color:#fff;text-decoration-color:var(--orange);text-underline-offset:3px}}
.scard p{{margin:0;font-size:17px;line-height:1.45;color:#E9EEF6}}
.scard .sm{{color:#C9D3E3;font-size:16px}}
.scard .ill{{margin-top:auto;padding-top:6px;font-weight:700;color:#FCB316}}
.scard .ill a{{color:#FCB316}}
.scard a:focus-visible{{outline:3px solid #FCB316;outline-offset:2px}}
.homefoot{{max-width:700px;margin:56px auto 40px;padding:0 24px;font-size:16px;color:var(--ink-2);line-height:1.5}}
</style>
</head>
<body>
<a class="skip" href="#main">Skip to the overview</a>
__NAV__

<header class="hero" aria-labelledby="title">
  <div class="hero-inner">
    <div>
      <div class="label">Illustrated pages</div>
      <h1 id="title">The Learning Brain <em>How the brain builds, stores, and uses knowledge</em></h1>
      <p class="dek">Illustrated pages on the science of learning, with activities and, on most pages, a short video, for instructors and students.</p>
      <div class="byline"><span><a href="#pagesT">All topics</a></span><span><a href="#pcT">Perception</a></span><span><a href="#lgT">Language and Learning</a></span></div>
    </div>
    <div class="hero-brain"><canvas id="heroBrain" role="img" aria-label="Drawing of the side of the brain with several regions that matter for learning glowing orange: the prefrontal cortex, the parietal lobe, the cerebellum, and, deep inside, the hippocampus, the amygdala and the midbrain dopamine area."></canvas></div>
  </div>
</header>

<main id="main">
<article>
  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>139</strong><span>illustrated pages, each with activities</span></div>
      <div role="listitem"><strong>10</strong><span>series, from The Learning Brain to Language and Learning</span></div>
      <div role="listitem"><strong>12</strong><span>brain-region pages, starting with a map</span></div>
      <div role="listitem"><strong>~2 min</strong><span>video on each of the first 115 topics</span></div>
    </div>
  </div>

  <div class="wide">
    <h2 class="sec" style="max-width:700px;margin-left:auto;margin-right:auto"><span class="n">Where to start</span>Pick a way in</h2>
    <ul class="start">
      <li><p class="who">New to the brain</p><h3><a href="@@LB:map@@">A map of the learning brain</a></h3><p>Which parts of the brain handle which parts of learning, and how they work together.</p></li>
      <li><p class="who">Teaching this term</p><h3><a href="@@LB:test-that-teaches@@">The test that teaches</a></h3><p>Why answering questions builds memory better than rereading, and how to use it in class.</p></li>
      <li><p class="who">Studying</p><h3><a href="@@LB:lb10@@">Retrieval practice</a></h3><p>Why pulling knowledge back out is what makes it stay, with a test you can try on yourself.</p></li>
    </ul>
  </div>

  <section class="grp" aria-labelledby="pagesT">
    <div class="wide">
      <h2 class="sec" id="pagesT" style="max-width:700px;margin-left:auto;margin-right:auto"><span class="n">Illustrated pages</span>Read, watch and try</h2>
      <p class="ov">Each page has labelled brain drawings, the key studies in plain language, and activities that let you see the effect in yourself. Most also have a short video.</p>
    </div>
  </section>

  <section class="grp" aria-labelledby="brT">
    <div class="wide">
      <h2 class="sec" id="brT" style="max-width:700px;margin-left:auto;margin-right:auto"><span class="n">12 topics</span>Brain regions</h2>
      <p class="ov">A tour of the parts of the brain that matter most for learning, from the hippocampus to the reward system, each with examples from film and popular culture.</p>
      <div class="coll" id="cg0"></div>
    </div>
  </section>

  <section class="grp" aria-labelledby="lbT">
    <div class="wide">
      <h2 class="sec" id="lbT" style="max-width:700px;margin-left:auto;margin-right:auto"><span class="n">18 topics</span>The Learning Brain</h2>
      <p class="ov">The core ideas of the science of learning: attention, prediction, retrieval, spacing, feedback, motivation and transfer.</p>
      <div class="coll" id="cg1"></div>
    </div>
  </section>

  <section class="grp" aria-labelledby="mT">
    <div class="wide">
      <h2 class="sec" id="mT" style="max-width:700px;margin-left:auto;margin-right:auto"><span class="n">12 topics</span>Memory</h2>
      <p class="ov">Follows a single memory from the moment it is noticed to the moment it is recalled and rewritten, and ends by turning that life into course design.</p>
      <div class="coll" id="cg2"></div>
    </div>
  </section>

  <section class="grp" aria-labelledby="aiT">
    <div class="wide">
      <h2 class="sec" id="aiT" style="max-width:700px;margin-left:auto;margin-right:auto"><span class="n">12 topics</span>Generative AI</h2>
      <p class="ov">What AI does to learning, from the evidence so far: when it helps, when it harms, and how to design so students still do the thinking.</p>
      <div class="coll" id="cg3"></div>
    </div>
  </section>

  <section class="grp" aria-labelledby="hT">
    <div class="wide">
      <h2 class="sec" id="hT" style="max-width:700px;margin-left:auto;margin-right:auto"><span class="n">12 topics</span>Habits of the Learner</h2>
      <p class="ov">For students: sleep, exercise, food, stress, phones, motivation and procrastination, with the evidence and its limits, and something to try in every topic.</p>
      <div class="coll" id="cg4"></div>
    </div>
  </section>

  <section class="grp" aria-labelledby="blT">
    <div class="wide">
      <h2 class="sec" id="blT" style="max-width:700px;margin-left:auto;margin-right:auto"><span class="n">12 topics</span>Belonging</h2>
      <p class="ov">For instructors: how belonging, feedback, role models and course structure shape who succeeds, with what the evidence supports and something to try in every topic.</p>
      <div class="coll" id="cg5"></div>
    </div>
  </section>

  <section class="grp" aria-labelledby="nmT">
    <div class="wide">
      <h2 class="sec" id="nmT" style="max-width:700px;margin-left:auto;margin-right:auto"><span class="n">12 topics</span>Neuromyths</h2>
      <p class="ov">For instructors: twelve popular ideas about the brain, where each came from, what the evidence shows, and what to do instead.</p>
      <div class="coll" id="cg6"></div>
    </div>
  </section>

  <section class="grp" aria-labelledby="dlT">
    <div class="wide">
      <h2 class="sec" id="dlT" style="max-width:700px;margin-left:auto;margin-right:auto"><span class="n">12 topics</span>Digital Learning</h2>
      <p class="ov">For instructors: slides, video, notes, devices, reading and course formats, with what the evidence supports and something to try in every topic.</p>
      <div class="coll" id="cg7"></div>
    </div>
  </section>

  <section class="grp" aria-labelledby="asT">
    <div class="wide">
      <h2 class="sec" id="asT" style="max-width:700px;margin-left:auto;margin-right:auto"><span class="n">13 topics</span>Assessment That Teaches</h2>
      <p class="ov">For instructors: quizzing, feedback, retakes, cumulative exams and integrity in the age of AI, with what the evidence supports and something to try in every topic.</p>
      <div class="coll" id="cg8"></div>
    </div>
  </section>

  <section class="grp" aria-labelledby="pcT">
    <div class="wide">
      <h2 class="sec" id="pcT" style="max-width:700px;margin-left:auto;margin-right:auto"><span class="n">12 topics</span>Perception</h2>
      <p class="ov">How the brain turns light and sound into a best guess, and what that means for diagrams, slides, graphs and reading. Every topic starts with something to try.</p>
      <div class="coll" id="cg9"></div>
    </div>
  </section>

  <section class="grp" aria-labelledby="lgT">
    <div class="wide">
      <h2 class="sec" id="lgT" style="max-width:700px;margin-left:auto;margin-right:auto"><span class="n">12 topics</span>Language and Learning</h2>
      <p class="ov">How the brain handles language, how words and reading are learned, and how writing, explaining and gesture help people learn. Every topic starts with something to try.</p>
      <div class="coll" id="cg10"></div>
    </div>
  </section>

  <p class="homefoot">Each page lists its sources at the end. Activities are simplified illustrations of the original experiments, not the experiments themselves.</p>
</article>
</main>
<div id="collTmp" hidden></div>

{PRE}
/* split the shared collection cards into one grid per group */
renderColl('collTmp','home');
let gi=-1;[...$('collTmp').children].forEach(n=>{{if(n.classList.contains('collsub')){{gi++;return}}const g=$('cg'+gi);if(g)g.appendChild(n)}});
$('collTmp').remove();
}})();
</script>
</body>
</html>
'''
open('home/template.html','w').write(html)

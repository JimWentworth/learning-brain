import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='b05',n='5',label='The Learning Brain · Belonging · Topic 5',epi='The Learning Brain, Belonging, episode 5',
title='Values Affirmation: A Promising Idea, Tested',h1='Values affirmation',em='Promising ideas deserve testing, not faith',read='7',mins='2 minutes',vtitle='Values affirmation',
dek='Can a brief writing exercise narrow an achievement gap? A 2006 study in Science said yes. Bigger, careful replications mostly did not. Here is what that means for your course.',
jumps='<span><a href="#vT">Try the exercise</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, and the amygdala, deep inside, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.amy.lab=[330,740];BR.R.amy.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc','amy'],labels:['pfc','amy'],labelT:{pfc:0.8,amy:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.vals{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;max-width:560px}
.vals[hidden]{display:none}
.vals button{min-height:44px;padding:6px 14px;border-radius:999px;border:2px solid #8FA3C2;background:transparent;color:#fff;font:600 16px var(--body);cursor:pointer}
.vals button[aria-pressed="true"]{border-color:#FCB316;background:#22375C}
.vals button:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.qq{font:600 clamp(18px,2.2vw,21px)/1.45 var(--body);color:#fff;max-width:42ch;margin:0;text-align:center}
.wform{display:flex;flex-direction:column;gap:10px;align-items:center;width:100%;max-width:560px}
.wform[hidden]{display:none}
.wform textarea{width:100%;min-height:150px;font:500 17px/1.5 var(--body);border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;padding:10px 12px;box-sizing:border-box;resize:vertical}
.wform textarea:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.gfb{font:600 16px/1.45 var(--body);color:#FFB38A;min-height:1.4em;margin:0;text-align:center}''',
body='''  <div class="col lede">
    <p>The exercise is called values affirmation. Students choose values that matter to them, like family, friends, music or sport, and write briefly about why. The theory: reminding students of a larger sense of self buffers the threat of being judged through a stereotype.</p>
    <p>In the original study, by Geoffrey Cohen and colleagues in 2006, seventh graders did the exercise early in the school year. For African American students, it reduced the racial achievement gap in the course by about 40%, and follow-ups reported benefits lasting two years.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>~40%</strong><span>of the gap closed in the original 2006 study</span></div>
      <div role="listitem"><strong>No effect</strong><span>in a large, careful replication in the same district</span></div>
      <div role="listitem"><strong>&gt;0.10</strong><span>benefits larger than this could be ruled out</span></div>
      <div role="listitem"><strong>Not reliable</strong><span>may help in some settings, but no one can yet predict where</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Bigger tests</span>Mostly empty</h2>
    <p>Then came bigger tests. A study across the original district reported a smaller benefit. But a large, careful replication by Paul Hanselman and colleagues in the same district found no effect, and could rule out benefits larger than about 0.1. Other replications, including one by John Protzko and Joshua Aronson, and one in college physics, also came up empty.</p>
    <p>So values affirmation is not a reliable fix. It may help in some settings, perhaps where threat is high and the exercise is delivered with care. But no one can yet predict where.</p>
  </div>

  <section class="night" aria-labelledby="vT">
    <div class="col">
      <h2 class="sec" id="vT"><span class="n">Try it</span>Try the exercise</h2>
      <p>Experience what students do: pick two or three values that matter to you, and write briefly about why. It is private: nothing you write is saved or leaves this page. About 3 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="vScreen">
          <p class="qq" id="vQ" aria-live="polite">Pick two or three values that matter most to you.</p>
          <div class="vals" id="vV" role="group" aria-label="Values"></div>
          <form class="wform" id="vF" hidden><label class="sr-only" for="vI">Why these values matter to you</label><textarea id="vI"></textarea><button class="nbtn" type="submit">Done</button></form>
          <p class="gfb" id="vFb" aria-live="polite"></p>
          <div class="mrow" style="justify-content:center"><button class="nbtn" id="vGo" type="button" disabled>Write about them</button></div>
        </div>
        <div>
          <p class="phase" id="vPhase">Choose</p>
          <p class="mtitle" id="vTitle">Your values</p>
          <p class="mtext" id="vText" aria-live="polite">Choose the ones that matter to you, not the ones that sound good.</p>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>An experiment, not a fix</h2>
    <p>The original results were striking, and the best replications did not find them. If you use the exercise, you are running an experiment, and it should not replace the structural work in the rest of this series.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">For teaching</h3>
      <p>If you try it, treat it as an experiment. Keep it brief, private and ungraded, early in the term or before a high-stakes test. Track what happens. And don’t let it replace the structural work in the rest of this series.</p>
    </aside>
  </div>
''',
tips_h='Promising ideas deserve testing, not faith.',
tips='''      <li><b>Brief, private, ungraded</b><span>If you try it at all.</span></li>
      <li><b>Track what happens</b><span>It is an experiment.</span></li>
      <li><b>Not a replacement</b><span>For structural work.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1126/science.1128317">Cohen, G. L., Garcia, J., Apfel, N., &amp; Master, A. (2006). Reducing the racial achievement gap: A social-psychological intervention. <i>Science, 313</i>(5791), 1307–1310.</a></li>
        <li><a href="https://doi.org/10.1037/edu0000141">Hanselman, P., Rozek, C. S., Grigg, J., &amp; Borman, G. D. (2017). New evidence on self-affirmation effects and theorized sources of heterogeneity from large-scale replications. <i>Journal of Educational Psychology, 109</i>(3), 405–424.</a></li>
        <li><a href="https://doi.org/10.1177/1948550616646426">Protzko, J., &amp; Aronson, J. (2016). Context moderates affirmation effects on the ethnic achievement gap. <i>Social Psychological and Personality Science, 7</i>(6), 500–507.</a></li>
        <li><a href="https://doi.org/10.1103/PhysRevPhysEducRes.17.020121">A 2021 replication of values-affirmation exercises in introductory physics. <i>Physical Review Physics Education Research, 17</i>, 020121.</a></li>''',
quiz='''[
 {q:'In the original 2006 study, the racial achievement gap closed by about…',o:['40%','5%','100%'],a:0,f:'With follow-ups reporting benefits lasting two years.'},
 {q:'A large, careful replication in the same district found…',o:['No effect, ruling out benefits above about 0.1','A bigger effect','The same 40%'],a:0,f:'Hanselman and colleagues, 2017.'},
 {q:'If you try values affirmation, treat it as…',o:['An experiment: brief, private, ungraded, tracked','A guaranteed fix','A graded assignment'],a:0,f:'And don’t let it replace structural work.'}]''',
js=BASE+r'''
/* ---------- try the exercise ---------- */
const VAL=['Family','Friends','Music','Sport','Faith or spirituality','Creativity','Humour','Learning','Helping others','Nature','Independence','Community','Art','Honesty'];
$('vV').innerHTML=VAL.map(v=>`<button type="button" aria-pressed="false">${v}</button>`).join('');
const picked=()=>[...$('vV').querySelectorAll('button[aria-pressed="true"]')].map(b=>b.textContent);
$('vV').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;const on=b.getAttribute('aria-pressed')==='true';if(!on&&picked().length>=3){$('vFb').textContent='Three at most.';return}$('vFb').textContent='';b.setAttribute('aria-pressed',String(!on));const n=picked().length;$('vGo').disabled=n<2;$('vText').textContent=n<2?'Pick at least two.':`You picked: ${picked().join(', ')}.`});
$('vGo').addEventListener('click',()=>{const p=picked();$('vV').hidden=true;$('vGo').hidden=true;$('vF').hidden=false;$('vI').value='';const lst=p.length>2?p.slice(0,-1).join(', ')+' and '+p[p.length-1]:p.join(' and ');$('vQ').textContent=`Why do ${lst.toLowerCase()} matter to you? Describe a time when one of them was important.`;$('vPhase').textContent='Write';$('vTitle').textContent='A few sentences';$('vText').textContent='No one will read it. Spelling doesn’t matter.';$('vI').focus()});
$('vF').addEventListener('submit',e=>{e.preventDefault();const n=$('vI').value.trim().split(/\s+/).filter(Boolean).length;if(n<10){$('vFb').textContent=`A few sentences, at least 10 words (you have ${n}).`;$('vI').focus();return}
 $('vFb').textContent='';$('vI').value='';$('vF').hidden=true;$('vQ').textContent='Done. Your writing has been cleared.';$('vPhase').textContent='Reflect';$('vTitle').textContent='That’s the whole exercise';
 $('vText').textContent='In the original study, students did something like this, briefly, early in the year. Notice how it felt. If you try it with students, keep it this short, private and ungraded, and track what happens: in the best replications, it made no measurable difference to grades.';
 const r=$('vGo');r.hidden=false;r.disabled=false;r.textContent='Start over';r.onclick=()=>{r.onclick=null;$('vV').hidden=false;$('vV').querySelectorAll('button').forEach(b=>b.setAttribute('aria-pressed','false'));r.textContent='Write about them';r.disabled=true;$('vQ').textContent='Pick two or three values that matter most to you.';$('vPhase').textContent='Choose';$('vTitle').textContent='Your values';$('vText').textContent='Choose the ones that matter to you, not the ones that sound good.'};r.focus()});
'''+grid('''[
 ['In the original 2006 study, the racial achievement gap in the course closed by about…',['40%','10%','90%'],0,'Cohen and colleagues, 2006.'],
 ['The original exercise was done by…',['Seventh graders, early in the school year','College seniors','Teachers'],0,'Students wrote briefly about values that mattered to them.'],
 ['A large, careful replication in the same district found…',['No effect','A 40% effect','A bigger effect for everyone'],0,'Hanselman and colleagues, 2017.'],
 ['That replication could rule out benefits larger than about…',['0.1','1','10'],0,'Precise enough to say: not a big effect.'],
 ['Other replications, including in college physics, found…',['No effect','Large effects','Harm'],0,'Several came up empty.'],
 ['So values affirmation is…',['Not a reliable fix; it may help in some settings','A proven fix','Harmful'],0,'No one can yet predict where.']]''','The pattern: a striking early result shrank or vanished in larger tests. Treat the exercise as an experiment, not a fix.'))
import json as _j;o['vnote']=_j.load(open('gen/vnotes.json'))['b05']
open('b05/template.html','w').write(page(o))

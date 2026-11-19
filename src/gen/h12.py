import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='h12',n='12',label='The Learning Brain · Habits of the Learner · Topic 12',epi='The Learning Brain, Habits of the Learner, episode 12',
title='Procrastination and the Pomodoro Technique',h1='Procrastination and the Pomodoro technique',em='Don’t wait to feel ready; start the timer',read='7',mins='2 minutes',vtitle='Procrastination and the Pomodoro technique',
dek='Procrastination isn’t simple laziness. It feels better now and worse later. Planned breaks and a first short block can help you start.',
jumps='<span><a href="#zT">Start the timer</a></span><span><a href="#sT">Split it into steps</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, and the amygdala, deep inside, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.amy.lab=[330,740];BR.R.amy.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc','amy'],labels:['pfc','amy'],labelT:{pfc:0.8,amy:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.qq{font:600 clamp(18px,2.2vw,21px)/1.45 var(--body);color:#fff;max-width:42ch;margin:0;text-align:center}
.jb{display:flex;gap:8px;flex-wrap:wrap;justify-content:center}
.jb[hidden]{display:none}
.pclock{font:800 64px/1 var(--body);color:#FCB316;margin:0;font-variant-numeric:tabular-nums}
.pclock.onbrk{color:#7DD3A8}
.splan{display:grid;gap:10px;width:100%;max-width:560px}
.splan label{display:block;font:600 14px var(--body);color:#C9D3E3}
.splan input{display:block;width:100%;margin-top:4px;box-sizing:border-box;min-height:44px;font:500 17px var(--body);border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;padding:0 12px}
.splan input:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.splan .row2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
@media (max-width:520px){.splan .row2{grid-template-columns:1fr}}
.splan input{min-width:0}
.gfb{font:600 16px/1.45 var(--body);color:#FFB38A;min-height:1.4em;margin:0}
.sout{margin:8px 0;padding-left:22px;color:#E9EEF6;font-size:17px;line-height:1.6}''',
body='''  <div class="col lede">
    <p>You plan to start the essay tonight. Then tomorrow. Then the night before it is due. If that sounds familiar, you are in large company. A major review by Piers Steel cites estimates that most college students procrastinate, and that almost half do so consistently and in ways that cause problems.</p>
    <p>It is not simple laziness. Procrastination means putting off something you intend to do, even though you expect to be worse off for the delay.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>Most</strong><span>college students procrastinate; almost half consistently</span></div>
      <div role="listitem"><strong>Less stress</strong><span>early in the term for procrastinators, but more stress and illness later</span></div>
      <div role="listitem"><strong>Retracted</strong><span>the famous 2002 deadlines study, in 2026, after a failed replication</span></div>
      <div role="listitem"><strong>87</strong><span>Dutch students: fixed breaks felt less tiring than self-chosen ones</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Short-term relief</span>Then the bill arrives</h2>
    <p>In two semester-long studies, Dianne Tice and Roy Baumeister found that procrastinators actually felt less stressed and healthier early in the term. But late in the term they reported more stress and illness, and they earned lower grades on every assignment.</p>
    <h2 class="sec"><span class="n">Deadlines</span>Worth trying, not proven</h2>
    <p>A well-known 2002 study by Dan Ariely and Klaus Wertenbroch reported that evenly spaced deadlines beat one final deadline. But a careful replication by Kyle Hyndman and Alberto Bisin, published in 2026, did not find that advantage, and the journal retracted the original paper in September 2026 after analysts raised concerns about its data. So interim deadlines are worth trying, as a way to split up the work, but not a proven fix.</p>
    <h2 class="sec"><span class="n">Pomodoro</span>Decide your breaks before you start</h2>
    <p>Then there is the Pomodoro technique: work in a short timed block, then take a planned break. In a Dutch study of 87 university students, by Felicitas Biwer and colleagues, those given fixed breaks, such as 6 minutes after every 24, felt less tired and distracted, and more motivated, than students who chose their own breaks, and got about the same work done. Later studies have found smaller or no differences. So the exact numbers matter less than deciding your breaks before you start.</p>
  </div>

  <section class="night" aria-labelledby="pT">
    <div class="col">
      <h2 class="sec" id="zT"><span class="n">Try it</span>Start the timer</h2>
      <p>Pick the task you are avoiding and a block length, and start. The timer switches to a planned break on its own. Keep this page open while you work.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="zScreen">
          <p class="qq" id="zQ" aria-live="polite">Choose a block and a break.</p>
          <div class="jb" id="zLen" role="group" aria-label="Block and break"><button class="nbtn" type="button" data-w="25" data-b="5">25 + 5 minutes</button><button class="nbtn ghost" type="button" data-w="24" data-b="6">24 + 6, as in the study</button><button class="nbtn ghost" type="button" data-w="12" data-b="3">12 + 3, to get started</button></div>
          <p class="pclock" id="zC" aria-live="off">25:00</p>
          <div class="jb"><button class="nbtn" id="zGo" type="button">Start</button><button class="nbtn ghost" id="zStop" type="button" hidden>Stop</button></div>
          <p class="prog" id="zProg" aria-live="polite"></p>
        </div>
        <div>
          <p class="phase" id="zPhase">Ready</p>
          <p class="mtitle" id="zTitle">One block on the task you’re avoiding</p>
          <p class="mtext" id="zText" aria-live="polite">Don’t wait to feel ready. Notice the relief once you start: that’s the feeling to remember.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="night" aria-labelledby="sT">
    <div class="col">
      <h2 class="sec" id="sT"><span class="n">Try it</span>Split it into steps</h2>
      <p>Enter a big assignment and its due date. The page splits it into four dated steps, so you have interim deadlines of your own. Nothing you enter leaves this page.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="sScreen">
          <form class="splan" id="sF">
            <label for="sA">Assignment<input id="sA" autocomplete="off" placeholder="e.g. History essay"></label>
            <div class="row2"><label for="sS">Start date<input id="sS" type="date"></label><label for="sD">Due date<input id="sD" type="date"></label></div>
            <div class="mrow"><button class="nbtn" type="submit">Make my steps</button><button class="nbtn ghost" type="button" id="sCopy" hidden>Copy the steps</button></div>
            <p class="gfb" id="sFb" aria-live="polite"></p>
          </form>
        </div>
        <div>
          <p class="phase" id="sPhase">Plan</p>
          <p class="mtitle" id="sTitle">Four dated steps</p>
          <div id="sOut"><p class="mtext">Outline, first draft, revision, final check: each with its own date.</p></div>
        </div>
      </div>
    </div>
  </section>

'''+GRID_HTML+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Short studies; not just a time problem</h2>
    <p>These are short studies, and much procrastination research is correlational. And if avoidance is tied to anxiety or low mood, talk to someone. It is not just a time problem.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Try this</h3>
      <p>Start with one 25-minute block on the task you are avoiding. Decide your breaks before you begin, and keep them short. Split big assignments into dated steps. And notice the relief once you start. That is the feeling to remember.</p>
    </aside>
  </div>
''',
tips_h='Don’t wait to feel ready. Start the timer.',
tips='''      <li><b>One block, now</b><span>On the task you’re avoiding.</span></li>
      <li><b>Breaks decided in advance</b><span>And kept short.</span></li>
      <li><b>Dated steps</b><span>For every big assignment.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1037/0033-2909.133.1.65">Steel, P. (2007). The nature of procrastination: A meta-analytic and theoretical review of quintessential self-regulatory failure. <i>Psychological Bulletin, 133</i>(1), 65–94.</a></li>
        <li><a href="https://doi.org/10.1111/j.1467-9280.1997.tb00460.x">Tice, D. M., &amp; Baumeister, R. F. (1997). Longitudinal study of procrastination, performance, stress, and health: The costs and benefits of dawdling. <i>Psychological Science, 8</i>(6), 454–458.</a></li>
        <li><a href="https://doi.org/10.1177/09567976261460772">Hyndman, K., &amp; Bisin, A. (2026). Replication of “Procrastination, Deadlines, and Performance: Self-Control by Precommitment.” <i>Psychological Science</i>. The original 2002 article by Ariely and Wertenbroch was retracted in September 2026.</a></li>
        <li><a href="https://doi.org/10.1111/bjep.12593">Biwer, F., Wiradhany, W., oude Egbrink, M. G. A., &amp; de Bruin, A. B. H. (2023). Understanding effort regulation: Comparing ‘Pomodoro’ breaks and self-regulated breaks. <i>British Journal of Educational Psychology, 93</i>(S2), 353–367.</a></li>''',
quiz='''[
 {q:'Early in the term, procrastinators reported…',o:['Less stress and illness than others','More stress','The same'],a:0,f:'Late in the term, it reversed, and their grades were lower.'},
 {q:'The famous 2002 study on evenly spaced deadlines…',o:['Failed to replicate and was retracted in 2026','Was confirmed many times','Was never tested'],a:0,f:'Interim deadlines are worth trying, not a proven fix.'},
 {q:'In the Dutch study, fixed breaks compared with self-chosen breaks…',o:['Felt less tiring and distracting','Felt worse','Doubled the work done'],a:0,f:'Later studies found smaller or no differences.'}]''',
js=BASE+r'''
/* ---------- start the timer ----------
   Work block, then break, repeating; counts completed blocks. */
let pw=25,pb=5,pt=null,ps=0,phase='work',blocks=0;
const fm=s=>`${Math.floor(s/60)}:${String(s%60).padStart(2,'0')}`;
function setLen(w,b){pw=w;pb=b;if(!pt){$('zC').textContent=fm(w*60);$('zC').classList.remove('onbrk')}document.querySelectorAll('#zLen button').forEach(x=>{const on=+x.dataset.w===w;x.classList.toggle('ghost',!on);x.setAttribute('aria-pressed',on)})}
$('zLen').addEventListener('click',e=>{const b=e.target.closest('button');if(b)setLen(+b.dataset.w,+b.dataset.b)});
function tick(){ps--;$('zC').textContent=fm(ps);
 if(ps%60===0&&ps>0)$('zProg').textContent=`${ps/60} minute${ps===60?'':'s'} left ${phase==='work'?'in this block':'of your break'}`;else if(ps%60===55&&phase==='work')$('zProg').textContent='';
 if(ps<=0){if(phase==='work'){blocks++;phase='brk';ps=pb*60;$('zC').classList.add('onbrk');$('zPhase').textContent='Break';$('zTitle').textContent=`Block ${blocks} done`;$('zText').textContent=`Take your ${pb}-minute break: stand up, look away from screens. The next block starts on its own.`;$('zQ').textContent='Break time.';$('zProg').textContent=`${blocks} block${blocks===1?'':'s'} done`}
  else{phase='work';ps=pw*60;$('zC').classList.remove('onbrk');$('zPhase').textContent='Working';$('zTitle').textContent=`Block ${blocks+1}`;$('zText').textContent='Back to the task. Same one, if you can.';$('zQ').textContent='Work on the task.'}
  $('zC').textContent=fm(ps)}
 pt=setTimeout(tick,1000)}
$('zGo').addEventListener('click',()=>{if(pt)return;phase='work';ps=pw*60;blocks=0;$('zLen').hidden=true;$('zGo').hidden=true;$('zStop').hidden=false;$('zStop').focus();$('zQ').textContent='Work on the task.';$('zPhase').textContent='Working';$('zTitle').textContent='Block 1';$('zText').textContent='Just this block. Phone notifications off.';$('zProg').textContent='';pt=setTimeout(tick,1000)});
$('zStop').addEventListener('click',()=>{clearTimeout(pt);pt=null;$('zLen').hidden=false;$('zGo').hidden=false;$('zStop').hidden=true;$('zGo').focus();$('zC').classList.remove('onbrk');$('zC').textContent=fm(pw*60);$('zQ').textContent='Choose a block and a break.';$('zPhase').textContent='Stopped';$('zTitle').textContent=blocks?`${blocks} block${blocks===1?'':'s'} done`:'You started';$('zText').textContent=blocks?'Well done. Notice how it feels to have started: that’s the feeling to remember next time.':'Starting is the hard part. Next time, try to finish one block.';$('zProg').textContent=''});
setLen(25,5);
/* ---------- split it into steps ----------
   4 steps at 25%, 55%, 80% and 95% of the way from start to due date. */
const iso=d=>d.toISOString().slice(0,10);const today=new Date();$('sS').value=iso(today);$('sD').value=iso(new Date(today.getTime()+21*864e5));
const nice=d=>d.toLocaleDateString(undefined,{weekday:'short',month:'short',day:'numeric'});
let stepsTxt='';
$('sF').addEventListener('submit',e=>{e.preventDefault();const a=$('sA').value.trim()||'Assignment';const s=new Date($('sS').value+'T12:00'),d=new Date($('sD').value+'T12:00');
 if(isNaN(s)||isNaN(d)){$('sFb').textContent='Please enter both dates.';return}
 const days=Math.round((d-s)/864e5);if(days<4){$('sFb').textContent='Give yourself at least four days between start and due date to split it into steps.';return}
 $('sFb').textContent='';
 const st=[[0.25,'Outline: main points and sources'],[0.55,'First draft, rough is fine'],[0.8,'Revise: structure, then sentences'],[0.95,'Final check and submit early']].map(([f,t])=>[new Date(s.getTime()+Math.round(days*f)*864e5),t]);
 stepsTxt=`${a}: due ${nice(d)}\n`+st.map(([dt,t],i)=>`${i+1}. ${nice(dt)}: ${t}`).join('\n');
 $('sOut').innerHTML=`<p class="gh">${a.replace(/[<&]/g,'')}: due ${nice(d)}</p><ol class="sout">${st.map(([dt,t])=>`<li><b>${nice(dt)}</b>: ${t}</li>`).join('')}</ol><p class="mtext">Put these dates in your calendar. Evenly spaced deadlines are worth trying, though the evidence that they beat a single deadline did not hold up.</p>`;
 $('sTitle').textContent=`${days} days, four steps`;$('sCopy').hidden=false;$('sCopy').textContent='Copy the steps'});
$('sCopy').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(stepsTxt);$('sCopy').textContent='Copied'}catch(err){$('sCopy').textContent='Copy not available: select the text instead'}});
'''+grid('''[
 ['Most college students…',['Procrastinate, and almost half do so consistently','Never procrastinate','Procrastinate only in their first year'],0,'Estimates cited in Steel, 2007.'],
 ['Early in the term, procrastinators reported…',['Less stress and illness','More stress and illness','The same'],0,'Tice and Baumeister, 1997.'],
 ['Late in the term, procrastinators…',['Reported more stress and illness, and had lower grades','Caught up completely','Did better'],0,'Short-term relief, long-term costs.'],
 ['The 2002 finding that evenly spaced deadlines beat one final deadline…',['Failed to replicate, and the paper was retracted','Was confirmed','Was never tested'],0,'Hyndman and Bisin, 2026.'],
 ['In the Dutch study, students with fixed breaks felt…',['Less tired and distracted, and more motivated','More tired','No different'],0,'Biwer and colleagues, 2023.'],
 ['Later studies of fixed versus self-chosen breaks found…',['Smaller or no differences','Much bigger differences','That breaks hurt'],0,'Decide your breaks before you start; the exact numbers matter less.']]''','The pattern: procrastination trades short-term relief for long-term cost. Planned blocks and breaks help you start; the deadline evidence is weaker than it looked.'))
open('h12/template.html','w').write(page(o))

import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='h06',n='6',label='The Learning Brain · Habits of the Learner · Topic 6',epi='The Learning Brain, Habits of the Learner, episode 6',
title='Stress and the Exam: Two Techniques Tested with Students',h1='Stress and the exam',em='Nerves are energy; point them at the test',read='7',mins='2 minutes',vtitle='Stress and the exam',
dek='Your heart races, your palms sweat, and the first question looks unfamiliar. Exam stress is common, and two simple techniques have been tested with students.',
jumps='<span><a href="#wT">Write it out</a></span><span><a href="#bT">Which thought helps?</a></span>',
hero_aria='Drawing of the side of the brain with the amygdala, deep inside, and the prefrontal cortex, at the front, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.amy.lab=[330,740];BR.R.amy.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['amy','pfc'],labels:['amy','pfc'],labelT:{amy:0.8,pfc:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS+'''
.qq{font:600 clamp(18px,2.2vw,21px)/1.45 var(--body);color:#fff;max-width:42ch;margin:0;text-align:center}
.jb{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}
.jb[hidden]{display:none}
.wform{display:flex;flex-direction:column;gap:10px;align-items:center;width:100%;max-width:560px}
.wform[hidden]{display:none}
.wform textarea{width:100%;min-height:200px;font:500 17px/1.5 var(--body);border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;padding:10px 12px;box-sizing:border-box;resize:vertical}
.wform textarea:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.wclock{font:800 40px var(--body);color:#FCB316;margin:0}
.wclock[hidden]{display:none}
.wprompts{margin:0;padding-left:20px;color:#E9EEF6;font-size:16px;line-height:1.5;max-width:46ch}
.wprompts[hidden]{display:none}
.reap{background:#0F2240;border:1px solid #3A4E72;border-radius:10px;padding:12px 14px;max-width:46ch;color:#E9EEF6;font-size:18px;line-height:1.5;margin:0}
.reap[hidden]{display:none}
.reap b{display:block;font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#FCB316;margin-bottom:4px}''',
body='''  <div class="col lede">
    <p>Worry takes up working memory, the mental space you need to solve problems. So at the University of Chicago, Gerardo Ramirez and Sian Beilock asked students to write about their exam worries for 10 minutes, just before a test. They reported the results in 2011.</p>
    <p>In the lab, students under pressure who sat quietly scored about 12% lower than on an earlier test. Those who wrote about their worries improved by about 5%. In ninth-grade biology classes, anxious students who wrote about their worries scored nearly one grade point higher on their final exam: say, a B+ instead of a B−. Students low in anxiety did not need it.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>10 minutes</strong><span>of writing about exam worries, just before the test</span></div>
      <div role="listitem"><strong>−12% vs +5%</strong><span>under pressure: sitting quietly, against writing about worries</span></div>
      <div role="listitem"><strong>~1 grade point</strong><span>higher for anxious ninth graders who wrote first</span></div>
      <div role="listitem"><strong>2018</strong><span>a large replication project did not find the effect again</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Be careful</span>Worth trying, not guaranteed</h2>
    <p>In 2018, a large project that repeated 21 high-profile social-science experiments did not find the writing effect again. So treat expressive writing as worth trying, not guaranteed.</p>
    <h2 class="sec"><span class="n">Reappraisal</span>Your body getting ready</h2>
    <p>The second idea is reappraisal. At Harvard, Jeremy Jamieson and colleagues told students preparing for the GRE that feeling keyed up can actually help performance. They scored higher on the maths section of a practice test, and one to three months later, on the real GRE too.</p>
  </div>

  <section class="night" aria-labelledby="wT">
    <div class="col">
      <h2 class="sec" id="wT"><span class="n">Try it</span>Write it out</h2>
      <p>A private space to try the technique before your next exam. Choose a length, write honestly about your worries, and finish with a reappraisal. Nothing you write is saved or leaves this page; it is cleared when you finish.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="wScreen">
          <p class="qq" id="wQ" aria-live="polite">How long do you want to write?</p>
          <div class="jb" id="wLen" role="group" aria-label="Writing time"><button class="nbtn" type="button" data-m="10">10 minutes, as in the study</button><button class="nbtn ghost" type="button" data-m="5">5 minutes</button><button class="nbtn ghost" type="button" data-m="2">2-minute practice</button></div>
          <ol class="wprompts" id="wP" hidden><li>What exactly are you worried about in this exam?</li><li>What would happen if it went badly? How likely is that, really?</li><li>How does the worry feel in your body right now?</li></ol>
          <form class="wform" id="wF" hidden><label class="sr-only" for="wI">Your worries</label><textarea id="wI" spellcheck="false"></textarea><button class="nbtn ghost" type="submit">I’m done early</button></form>
          <p class="wclock" id="wC" hidden aria-live="off"></p>
          <p class="reap" id="wR" hidden><b>Now, before you start</b>Your racing heart is your body getting ready: more blood and oxygen to your brain and muscles. People who see that arousal as helpful tend to perform better. Point it at the first question.</p>
          <p class="prog" id="wProg" aria-live="polite"></p>
        </div>
        <div>
          <p class="phase" id="wPhase">Ready</p>
          <p class="mtitle" id="wTitle">Unload, then reframe</p>
          <p class="mtext" id="wText" aria-live="polite">Writing about worries may free up working memory. Reframing the nerves turns them into energy.</p>
          <div class="mrow"><button class="nbtn ghost" id="wReset" type="button" hidden>Start over</button></div>
        </div>
      </div>
    </div>
  </section>

'''+cls_html('bT','Which thought helps?','Eight things a student might tell themselves just before an exam. For each, decide: does it help (reappraising the nerves as energy, or facing the worry), or work against them? You’ll get feedback after each one.',[('H','Helps',''),('A','Works against you','')],'Helps or works against you?','Which thought helps?','The question is always: does it treat the nerves as a threat, or as energy?')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Small studies; severe anxiety is different</h2>
    <p>These studies are small, and some findings have not held up. And severe anxiety is different: it deserves real support from a counsellor or doctor.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Try this</h3>
      <p>Before an exam, spend 10 minutes writing honestly about your worries. When your heart races, tell yourself this is your body getting ready. Practise under test-like conditions. And if anxiety feels overwhelming, talk to your campus counselling service.</p>
    </aside>
  </div>
''',
tips_h='Nerves are energy. Point them at the test.',
tips='''      <li><b>Write out the worry</b><span>Ten minutes, just before. Worth trying, not guaranteed.</span></li>
      <li><b>Reframe the racing heart</b><span>Your body getting ready.</span></li>
      <li><b>Overwhelmed?</b><span>Talk to your campus counselling service.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1126/science.1199427">Ramirez, G., &amp; Beilock, S. L. (2011). Writing about testing worries boosts exam performance in the classroom. <i>Science, 331</i>(6014), 211–213.</a></li>
        <li><a href="https://doi.org/10.1038/s41562-018-0399-z">Camerer, C. F., Dreber, A., Holzmeister, F., et al. (2018). Evaluating the replicability of social science experiments in Nature and Science between 2010 and 2015. <i>Nature Human Behaviour, 2</i>, 637–644.</a></li>
        <li><a href="https://doi.org/10.1016/j.jesp.2009.08.015">Jamieson, J. P., Mendes, W. B., Blackstock, E., &amp; Schmader, T. (2010). Turning the knots in your stomach into bows: Reappraising arousal improves performance on the GRE. <i>Journal of Experimental Social Psychology, 46</i>(1), 208–212.</a></li>''',
quiz='''[
 {q:'Under pressure, students who wrote about their worries before a test…',o:['Improved by about 5%','Dropped by about 12%','Didn’t change'],a:0,f:'Those who sat quietly dropped by about 12%.'},
 {q:'What happened when a large project repeated the writing study in 2018?',o:['It did not find the effect again','It found a bigger effect','It was never repeated'],a:0,f:'Worth trying, not guaranteed.'},
 {q:'Students told that feeling keyed up can help…',o:['Scored higher on GRE maths, in practice and on the real test','Felt calmer but scored the same','Scored lower'],a:0,f:'Jamieson and colleagues, 2010.'}]''',
js=BASE+r'''
/* ---------- write it out ----------
   Choose 10/5/2 minutes; prompts + textarea + countdown; at the end (or "done early") the text is cleared and a reappraisal is shown. */
let wr=null;
function stopW(){if(wr&&wr.tm)clearTimeout(wr.tm);wr=null}
function finish(early){if(!wr)return;stopW();$('wI').value='';$('wF').hidden=true;$('wP').hidden=true;$('wC').hidden=true;$('wR').hidden=false;$('wQ').textContent=early?'Done.':'Time’s up.';$('wProg').textContent='';
 $('wPhase').textContent='Reframe';$('wTitle').textContent='Your writing has been cleared';$('wText').textContent='The point was to get the worry out of your head, not to keep it. Now read the reappraisal, and take one slow breath before the first question.';$('wReset').hidden=false;$('wReset').focus()}
$('wLen').addEventListener('click',e=>{const b=e.target.closest('button');if(!b||wr)return;wr={};let s=+b.dataset.m*60;
 $('wLen').hidden=true;$('wR').hidden=true;$('wP').hidden=false;$('wF').hidden=false;$('wC').hidden=false;$('wQ').textContent='Write honestly about your worries. Some prompts, if they help:';
 $('wPhase').textContent='Writing';$('wTitle').textContent='Just write';$('wText').textContent='Spelling and grammar don’t matter. No one will read it.';
 const show=()=>{$('wC').textContent=`${Math.floor(s/60)}:${String(s%60).padStart(2,'0')}`;if(s%60===0&&s>0)$('wProg').textContent=`${s/60} minute${s===60?'':'s'} left`;else if(s%60===55)$('wProg').textContent=''};
 show();const tick=()=>{if(!wr)return;s--;show();if(s<=0)finish(false);else wr.tm=setTimeout(tick,1000)};wr.tm=setTimeout(tick,1000);$('wI').focus()});
$('wF').addEventListener('submit',e=>{e.preventDefault();finish(true)});
$('wReset').addEventListener('click',()=>{stopW();$('wI').value='';$('wR').hidden=true;$('wReset').hidden=true;$('wLen').hidden=false;$('wQ').textContent='How long do you want to write?';$('wPhase').textContent='Ready';$('wTitle').textContent='Unload, then reframe';$('wText').textContent='Writing about worries may free up working memory. Reframing the nerves turns them into energy.';$('wLen').querySelector('button').focus()});
'''+cls_js("{H:'Helps',A:'Works against you'}",'''[
 ['“My heart’s racing. That’s my body getting ready to perform.”','H','Helps: this is reappraisal, treating arousal as energy.'],
 ['“I must calm down completely before I can do anything.”','A','Works against you: trying to suppress arousal is hard. Reframing it tends to work better.'],
 ['“I’m nervous because this matters to me. Good.”','H','Helps: it reframes the nerves as a sign you care, and as fuel.'],
 ['“If I fail this, my whole future is over.”','A','Works against you: catastrophizing feeds the worry that takes up working memory.'],
 ['Writing down exactly what you are worried about, ten minutes before the exam','H','Helps, maybe: it may free up working memory, though a large replication did not find the effect.'],
 ['“Don’t think about failing. Don’t think about failing.”','A','Works against you: trying not to think about something tends to keep it in mind.'],
 ['“The first question looks unfamiliar. I’ll start with one I know and come back.”','H','Helps: it turns the jolt into a plan.'],
 ['“Everyone else looks calm, so something must be wrong with me.”','A','Works against you: nerves are common, and other people’s calm is often only on the surface.']]''','Helps or works against you?',r'''
 if(right>=7){title='You can reframe it';text=`${right} of 8 right. Treat the racing heart as energy, face the worry rather than fighting it, and turn it into a plan.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Suppressing or catastrophizing tends to backfire; reframing the arousal tends to help.`}
 else{title='Worth another look';text=`${right} of 8 right. Helpful thoughts treat the nerves as energy, or name the worry and make a plan. Unhelpful ones fight the feeling or blow it up.`}''')+grid('''[
 ['Under pressure, students who sat quietly before the test scored…',['About 12% lower than before','About the same','About 5% higher'],0,'Ramirez and Beilock, 2011.'],
 ['Students who wrote about their worries first…',['Improved by about 5%','Dropped by about 12%','Didn’t change'],0,'Writing may free up working memory.'],
 ['Anxious ninth graders who wrote first scored…',['Nearly one grade point higher','A full letter grade lower','The same'],0,'Students low in anxiety didn’t need it.'],
 ['In a large 2018 replication project, the writing effect…',['Was not found again','Doubled','Was confirmed exactly'],0,'Worth trying, not guaranteed.'],
 ['GRE students told that feeling keyed up can help scored higher…',['On maths, in practice and on the real GRE','Only in practice','Not at all'],0,'Jamieson and colleagues, 2010.'],
 ['Severe anxiety…',['Deserves real support from a counsellor or doctor','Is solved by writing','Is solved by reappraisal'],0,'These techniques are for everyday exam nerves.']]''','The pattern: unloading the worry and reframing the arousal can help ordinary exam nerves, but the evidence is mixed, and severe anxiety needs real support.'))
open('h06/template.html','w').write(page(o))

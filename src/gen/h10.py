import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='h10',n='10',label='The Learning Brain · Habits of the Learner · Topic 10',epi='The Learning Brain, Habits of the Learner, episode 10',
title='Intrinsic Motivation: Find Your Own Reason',h1='Intrinsic motivation',em='Find your own reason, then let it pull you',read='7',mins='2 minutes',vtitle='Intrinsic motivation',
dek='Studying because you want to feels different from studying because you have to. That difference matters, and some of it is in your control: choice, progress, people, and a reason of your own.',
jumps='<span><a href="#rT">Find your reason</a></span><span><a href="#bT">Which need does it feed?</a></span>',
hero_aria='Drawing of the side of the brain with the ventral tegmental area, deep in the midbrain, part of the brain’s reward system, and the striatum, glowing orange and labelled.',
hero_js="BR.R.vta.lab=[360,720];BR.R.vta.al='left';BR.R.str.lab=[200,-60];BR.R.str.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['vta','str'],labels:['vta','str'],labelT:{vta:0.8,str:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS+'''
.qq{font:600 clamp(18px,2.2vw,21px)/1.45 var(--body);color:#fff;max-width:42ch;margin:0;text-align:center}
.rform{display:grid;gap:10px;width:100%;max-width:560px}
.rform label{display:block;font:600 14px var(--body);color:#C9D3E3}
.rform input,.rform textarea{display:block;width:100%;margin-top:4px;box-sizing:border-box;font:500 17px/1.5 var(--body);border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;padding:8px 12px}
.rform textarea{min-height:130px;resize:vertical}
.rform input:focus-visible,.rform textarea:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.rprompt{margin:0;color:#E9EEF6;font-size:16px;line-height:1.5}
.rprompt b{color:#FCB316}
.gfb{font:600 16px/1.45 var(--body);color:#FFB38A;min-height:1.4em;margin:0}
.rout{background:#0F2240;border:1px solid #3A4E72;border-radius:10px;padding:12px 14px;color:#E9EEF6;font-size:17px;line-height:1.5;margin:10px 0;white-space:pre-wrap}
.rout[hidden]{display:none}''',
body='''  <div class="col lede">
    <p>Think of something you study because you want to, and something you study only because it is required. Psychologists call the first intrinsic motivation: doing something because it is interesting or meaningful to you.</p>
    <p>Self-determination theory, developed by Edward Deci and Richard Ryan, says intrinsic motivation grows when three needs are met: autonomy (some say in what you do), competence (feeling yourself get better), and relatedness (feeling connected to others).</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>128</strong><span>experiments: expected, tangible rewards reduced later free choice to continue</span></div>
      <div role="listitem"><strong>Positive feedback</strong><span>did the opposite, and raised interest</span></div>
      <div role="listitem"><strong>41</strong><span>studies: choice raised intrinsic motivation, effort and performance</span></div>
      <div role="listitem"><strong>2 to 4</strong><span>successive choices gave the strongest effect</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Rewards</span>They can backfire</h2>
    <p>A meta-analysis of 128 experiments, by Deci, Richard Koestner and Ryan, found that expected, tangible rewards for an interesting task reduced people’s later free choice to keep doing it. Positive feedback did the opposite, and raised interest.</p>
    <h2 class="sec"><span class="n">Choice</span>A few choices help</h2>
    <p>Across 41 studies, reviewed by Erika Patall, Harris Cooper and Jorgianne Civey Robinson, having choices increased intrinsic motivation, effort and performance. Effects were strongest with a few successive choices, around two to four, rather than one.</p>
    <h2 class="sec"><span class="n">Relevance</span>Write the connection</h2>
    <p>In high school science classes, Chris Hulleman and Judith Harackiewicz asked 262 ninth graders to write about how the material connected to their own lives. Students who had expected to do poorly became more interested in science and earned higher grades. Later studies found similar benefits in college courses, especially for lower-performing students.</p>
  </div>

  <section class="night" aria-labelledby="rT">
    <div class="col">
      <h2 class="sec" id="rT"><span class="n">Try it</span>Find your reason</h2>
      <p>Try the relevance exercise on a course of your own. Write a few sentences on how it connects to your life or goals, then add one small choice you’ll make. Nothing you write leaves this page unless you copy it.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="rScreen">
          <form class="rform" id="rF">
            <label for="rC">A course or topic you find hard to care about<input id="rC" autocomplete="off" placeholder="e.g. Statistics"></label>
            <p class="rprompt"><b>Prompts, if they help:</b> Where might you use this, now or later? Who do you know who uses it? What problem would it help you solve? What part is even slightly interesting?</p>
            <label for="rW">How does it connect to your life or goals?<textarea id="rW"></textarea></label>
            <label for="rCh">One small choice you’ll make (what to do first, where, or with whom)<input id="rCh" autocomplete="off" placeholder="e.g. Start with the problem set I find most useful, in the library"></label>
            <div class="mrow"><button class="nbtn" type="submit">Make my note</button><button class="nbtn ghost" type="button" id="rCopy" hidden>Copy the note</button></div>
            <p class="gfb" id="rFb" aria-live="polite"></p>
          </form>
        </div>
        <div>
          <p class="phase" id="rPhase">Relevance</p>
          <p class="mtitle" id="rTitle">Your own reason</p>
          <p class="mtext" id="rText" aria-live="polite">A few honest sentences are enough. You won’t love every subject; the aim is to find some reason of your own.</p>
          <div class="rout" id="rOut" hidden aria-live="polite"></div>
        </div>
      </div>
    </div>
  </section>

'''+cls_html('bT','Which need does it feed?','Nine things a student might do. For each, decide which of the three needs it mainly feeds: autonomy (having a say), competence (seeing yourself improve), or relatedness (connection with others). You’ll get feedback after each one.',[('A','Autonomy','having a say'),('C','Competence','seeing progress'),('R','Relatedness','connection')],'Autonomy, competence or relatedness?','Which need does it feed?','The question is always: is it about choice, progress, or people?')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Lab puzzles; rewards still have a place</h2>
    <p>Many reward studies used simple lab puzzles. Rewards can still help you start a dull task. And you will not love every subject. The aim is to find some reason of your own.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Try this</h3>
      <p>For each course, write a few sentences on how it connects to your life or goals. Make small choices, like which problem set comes first, and where you study. Track your own progress, not just grades. And study with people who make the work feel shared.</p>
    </aside>
  </div>
''',
tips_h='Find your own reason. Then let it pull you.',
tips='''      <li><b>Write the connection</b><span>A few sentences per course.</span></li>
      <li><b>Make small choices</b><span>What first, and where.</span></li>
      <li><b>Track your progress</b><span>And study with people who make it shared.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1037/0033-2909.125.6.627">Deci, E. L., Koestner, R., &amp; Ryan, R. M. (1999). A meta-analytic review of experiments examining the effects of extrinsic rewards on intrinsic motivation. <i>Psychological Bulletin, 125</i>(6), 627–668.</a></li>
        <li><a href="https://doi.org/10.1037/0033-2909.134.2.270">Patall, E. A., Cooper, H., &amp; Robinson, J. C. (2008). The effects of choice on intrinsic motivation and related outcomes: A meta-analysis of research findings. <i>Psychological Bulletin, 134</i>(2), 270–300.</a></li>
        <li><a href="https://doi.org/10.1126/science.1177067">Hulleman, C. S., &amp; Harackiewicz, J. M. (2009). Promoting interest and performance in high school science classes. <i>Science, 326</i>(5958), 1410–1412.</a></li>''',
quiz='''[
 {q:'Expected, tangible rewards for an interesting task…',o:['Reduced later free choice to keep doing it','Increased it','Made no difference'],a:0,f:'Positive feedback did the opposite.'},
 {q:'Choice had the strongest effect with…',o:['Two to four successive choices','One big choice','Dozens of choices'],a:0,f:'From a meta-analysis of 41 studies.'},
 {q:'Writing about how science connected to their lives helped most…',o:['Students who expected to do poorly','Students who already loved science','No one'],a:0,f:'Hulleman and Harackiewicz, 2009.'}]''',
js=BASE+r'''
/* ---------- find your reason ----------
   Course + connection (at least 15 words) + optional choice -> a short note to keep; copy button. */
let note='';
$('rF').addEventListener('submit',e=>{e.preventDefault();const c=$('rC').value.trim()||'this course',w=$('rW').value.trim(),ch=$('rCh').value.trim();const n=w.split(/\s+/).filter(Boolean).length;
 if(n<15){$('rFb').textContent=`Write a little more: a few sentences, at least 15 words (you have ${n}).`;$('rW').focus();return}
 $('rFb').textContent='';
 note=`Why ${c} matters to me\n${w}`+(ch?`\n\nMy choice: ${ch}`:'');
 $('rOut').textContent=note;$('rOut').hidden=false;$('rCopy').hidden=false;$('rCopy').textContent='Copy the note';
 $('rTitle').textContent='Keep it where you’ll see it';$('rText').textContent='Reread it when the course feels pointless. In the study, several short reflections like this, across a semester, raised interest and grades for students who expected to do poorly.'+(ch?' And your choice gives you some say in how you work.':' Add one small choice too: a few choices give the strongest boost.')});
$('rCopy').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(note);$('rCopy').textContent='Copied'}catch(err){$('rCopy').textContent='Copy not available: select the text instead'}});
'''+cls_js("{A:'Autonomy',C:'Competence',R:'Relatedness'}",'''[
 ['Choosing which problem set to do first','A','Autonomy: a small choice gives you some say in how you work.'],
 ['Picking your own topic for an essay, from a short list','A','Autonomy: a few choices raised motivation most.'],
 ['Deciding where and when you study this week','A','Autonomy: your plan, not someone else’s.'],
 ['Keeping a log of practice scores to see them rise','C','Competence: seeing your own progress, not just grades.'],
 ['Getting specific feedback on what you did well','C','Competence: positive feedback raised interest in the meta-analysis.'],
 ['Starting with a problem you can just about solve, then stepping up','C','Competence: challenges you can meet build the feeling of getting better.'],
 ['Joining a study group that meets weekly','R','Relatedness: people who make the work feel shared.'],
 ['Explaining a hard idea to a classmate who’s stuck','R','Relatedness: and it’s a real test of what you know.'],
 ['Telling a friend what you’re working on and why it matters to you','R','Relatedness: connection, and a reason of your own said out loud.']]''','Autonomy, competence or relatedness?',r'''
 if(right>=8){title='You can see the three needs';text=`${right} of 9 right. Choice feeds autonomy, progress feeds competence, and people feed relatedness. Look for all three in how you study.`}
 else if(right>=5){title='Mostly there';text=`${right} of 9 right. You missed ${missed}. Ask: is it about having a say, seeing yourself improve, or being with others?`}
 else{title='Worth another look';text=`${right} of 9 right. Autonomy is having a say; competence is seeing yourself get better; relatedness is connection with others.`}''')+grid('''[
 ['Expected, tangible rewards for an interesting task…',['Reduced later free choice to keep doing it','Increased it','Made no difference'],0,'Deci, Koestner and Ryan, 1999: 128 experiments.'],
 ['Positive feedback…',['Raised interest','Lowered interest','Made no difference'],0,'From the same meta-analysis.'],
 ['Having choices…',['Increased motivation, effort and performance','Overwhelmed people','Made no difference'],0,'Patall, Cooper and Robinson, 2008: 41 studies.'],
 ['The strongest effect of choice came with…',['Two to four successive choices','A single choice','As many choices as possible'],0,'A few small choices, not one big one.'],
 ['Writing about how science connected to their lives helped most…',['Students who expected to do poorly','Students who expected to do well','Teachers'],0,'Hulleman and Harackiewicz, 2009.'],
 ['The three needs in self-determination theory are…',['Autonomy, competence and relatedness','Rewards, deadlines and grades','Talent, effort and luck'],0,'Deci and Ryan.']]''','The pattern: motivation grows with a say, a sense of progress, connection, and a reason of your own; expected rewards can backfire.'))
import json as _j;o['vnote']=_j.load(open('gen/vnotes.json'))['h10']
open('h10/template.html','w').write(page(o))

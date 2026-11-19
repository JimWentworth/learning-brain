import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='b06',n='6',label='The Learning Brain · Belonging · Topic 6',epi='The Learning Brain, Belonging, episode 6',
title='Wise Feedback: High Standards, and Belief Students Can Reach Them',h1='Wise feedback',em='High standards, and belief that students can reach them. Say both.',read='7',mins='2 minutes',vtitle='Wise feedback',
dek='Critical feedback can be read two ways: my teacher thinks I can do better, or my teacher thinks people like me can’t do this. For students who expect to be stereotyped, that ambiguity is real.',
jumps='<span><a href="#bT">Which note is wise?</a></span><span><a href="#fT">Write a wise note</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, and the temporal lobe, at the side, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.tem.lab=[600,770];BR.R.tem.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc','tem'],labels:['pfc','tem'],labelT:{pfc:0.8,tem:1.0},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS+'''
.splan{display:grid;gap:10px;width:100%;max-width:600px}
.splan label{display:block;font:600 14px var(--body);color:#C9D3E3}
.splan input{display:block;width:100%;margin-top:4px;box-sizing:border-box;min-height:44px;font:500 17px var(--body);border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;padding:0 12px}
.splan input:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.gfb{font:600 16px/1.45 var(--body);color:#FFB38A;min-height:1.4em;margin:0}
.pout{background:#0F2240;border:1px solid #3A4E72;border-radius:10px;padding:12px 14px;color:#E9EEF6;font-size:17px;line-height:1.6;margin:10px 0;white-space:pre-wrap}
.pout[hidden]{display:none}''',
body='''  <div class="col lede">
    <p>In a middle school study by David Yeager, Valerie Purdie-Vaughns, Julio Garcia, Geoffrey Cohen and colleagues, seventh graders wrote essays about a personal hero, and their teachers marked them up. Some students also got a handwritten note: “I’m giving you these comments because I have very high expectations, and I know that you can reach them.” Others got a neutral note.</p>
    <p>Far more of the African American students who got the high-expectations note chose to revise their essay, and the difference was largest among those who most distrusted school.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>88% vs 34%</strong><span>of African American students improved their scores, with and without the note, when revision was required</span></div>
      <div role="listitem"><strong>More revised</strong><span>when the note was optional, especially those who distrusted school</span></div>
      <div role="listitem"><strong>Not significant</strong><span>the difference for white students, most of whom revised anyway</span></div>
      <div role="listitem"><strong>A few dozen</strong><span>students per group: small studies</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Required revision</span>Better drafts, too</h2>
    <p>In a second study, revision was required. 88% of African American students with the note improved their scores, compared with 34% without. White students also benefited a little, but that difference was not significant.</p>
    <h2 class="sec"><span class="n">Two things at once</span>The bar, and the belief</h2>
    <p>The note did two things at once. It held the bar high, and it said: I believe you can reach it. Earlier research found that praise alone, or high standards alone, worked less well.</p>
  </div>

'''+cls_html('bT','Which note is wise?','Nine notes a teacher might write on a draft. For each, decide: is it wise feedback (high standards plus belief), praise alone, or standards alone? You’ll get feedback after each one.',[('W','Wise','standards + belief'),('P','Praise alone','no standard'),('S','Standards alone','no belief')],'Wise, praise alone, or standards alone?','Which note is wise?','The question is always: does it say both “the bar is high” and “I believe you can reach it”?')+'''
  <section class="night" aria-labelledby="fT">
    <div class="col">
      <h2 class="sec" id="fT"><span class="n">Try it</span>Write a wise note</h2>
      <p>Enter the assignment, the most important thing to fix, and a concrete next step. The page builds a note that names the standard, says you believe the student can reach it, and gives the step. Edit it to sound like you.</p>
      <form class="splan" id="fF">
        <label for="fA">Assignment<input id="fA" autocomplete="off" placeholder="e.g. lab report"></label>
        <label for="fI">The most important thing to improve<input id="fI" autocomplete="off" placeholder="e.g. your conclusion doesn’t use your data"></label>
        <label for="fS">One concrete next step<input id="fS" autocomplete="off" placeholder="e.g. rewrite the conclusion citing two of your measurements"></label>
        <div class="mrow"><button class="nbtn" type="submit">Build my note</button><button class="nbtn ghost" type="button" id="fCopy" hidden>Copy the note</button></div>
        <p class="gfb" id="fFb" aria-live="polite"></p>
      </form>
      <div class="pout" id="fOut" hidden aria-live="polite"></div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Small studies; the message has to be true</h2>
    <p>These studies were small, with a few dozen students per group. And the message has to be true. It only works if you really do help students reach the standard.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">For teaching</h3>
      <p>State your high standards plainly. Say that you believe each student can reach them. Give specific next steps, not just a grade. And build in time to revise.</p>
    </aside>
  </div>
''',
tips_h='High standards, and belief that students can reach them. Say both.',
tips='''      <li><b>Name the standard</b><span>Plainly.</span></li>
      <li><b>Say you believe</b><span>Each student can reach it.</span></li>
      <li><b>A next step, and time</b><span>Specific steps, and time to revise.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1037/a0033906">Yeager, D. S., Purdie-Vaughns, V., Garcia, J., Apfel, N., Brzustoski, P., Master, A., Hessert, W. T., Williams, M. E., &amp; Cohen, G. L. (2014). Breaking the cycle of mistrust: Wise interventions to provide critical feedback across the racial divide. <i>Journal of Experimental Psychology: General, 143</i>(2), 804–824.</a></li>''',
quiz='''[
 {q:'When revision was required, the share of African American students with the note who improved was…',o:['88%, against 34% without','34%, against 88% without','About the same'],a:0,f:'Yeager and colleagues, 2014.'},
 {q:'The wise note combined…',o:['High standards and belief the student can reach them','Praise alone','Standards alone'],a:0,f:'Praise alone, or standards alone, worked less well.'},
 {q:'Wise feedback only works if…',o:['You really do help students reach the standard','It is handwritten','It is anonymous'],a:0,f:'The message has to be true.'}]''',
js=BASE+cls_js("{W:'Wise',P:'Praise alone',S:'Standards alone'}",'''[
 ['“I’m giving you these comments because I have high expectations, and I know you can reach them.”','W','Wise: the exact pairing from the study.'],
 ['“Great job! Really nice work.”','P','Praise alone: warm, but no standard and no path to improve.'],
 ['“This isn’t at the level I expect. Redo it.”','S','Standards alone: the bar is clear, but nothing says the student can reach it.'],
 ['“This is a demanding course, and your argument isn’t there yet. I’ve seen you do this kind of thinking, so I know you can. Start by tightening your thesis.”','W','Wise: standard, belief and a next step.'],
 ['“Don’t worry about the grade, you tried hard.”','P','Praise alone, and it can signal low expectations.'],
 ['“Several errors. See rubric.”','S','Standards alone: easy to read as “people like me can’t do this”.'],
 ['“My comments are detailed because I hold everyone to a high standard, and I’m confident you’ll meet it with this revision.”','W','Wise: high standard, applied to everyone, with belief.'],
 ['“You’re so talented, you’ll be fine.”','P','Praise alone: it praises ability, not the work, and gives no standard.'],
 ['“Meets 2 of 5 criteria.”','S','Standards alone: accurate, but silent on whether the student can get there.']]''','Wise, praise alone, or standards alone?',r'''
 if(right>=8){title='You can write it';text=`${right} of 9 right. Wise feedback says both: the bar is high, and I believe you can reach it. Then it gives a step.`}
 else if(right>=5){title='Mostly there';text=`${right} of 9 right. You missed ${missed}. Look for both halves: a clear standard, and belief in the student.`}
 else{title='Worth another look';text=`${right} of 9 right. Praise alone has no standard; standards alone have no belief. Wise feedback has both.`}''')+r'''
/* ---------- write a wise note ---------- */
let wnote='';
$('fF').addEventListener('submit',e=>{e.preventDefault();const a=$('fA').value.trim()||'assignment',i=$('fI').value.trim(),s=$('fS').value.trim();
 if(!i||!s){$('fFb').textContent='Please fill in what to improve and a next step.';(i?$('fS'):$('fI')).focus();return}$('fFb').textContent='';
 wnote=`I’m giving you these comments on your ${a} because I hold this course to a high standard, and I know you can reach it.\n\nThe most important thing to work on: ${i}.\n\nNext step: ${s}. I’ll look at your revision with you if that would help.`;
 $('fOut').textContent=wnote;$('fOut').hidden=false;$('fCopy').hidden=false;$('fCopy').textContent='Copy the note'});
$('fCopy').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(wnote);$('fCopy').textContent='Copied'}catch(err){$('fCopy').textContent='Copy not available: select the text instead'}});
''')
import json as _j;o['vnote']=_j.load(open('gen/vnotes.json'))['b06']
open('b06/template.html','w').write(page(o))

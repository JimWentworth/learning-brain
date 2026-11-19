import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='b01',n='1',label='The Learning Brain · Belonging · Topic 1',epi='The Learning Brain, Belonging, episode 1',
title='Do I Belong Here? Belonging Uncertainty and a One-Hour Exercise',h1='Do I belong here?',em='Belonging is a story, and stories can change',read='7',mins='2 minutes',vtitle='Do I belong here?',
dek='Two new students each fail their first quiz. One thinks everyone struggles at first; the other wonders whether people like them belong. Same event, different story, and the story can shape what happens next.',
jumps='<span><a href="#bT">Which response helps?</a></span><span><a href="#mT">Draft your early-term message</a></span>',
hero_aria='Drawing of the side of the brain with the amygdala, deep inside, and the prefrontal cortex, at the front, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.amy.lab=[330,740];BR.R.amy.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['amy','pfc'],labels:['amy','pfc'],labelT:{amy:0.8,pfc:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS+'''
.plan fieldset{border:1px solid #3A4E72;border-radius:10px;padding:10px 14px;margin:0 0 12px}
.plan legend{font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#FCB316;padding:0 6px}
.plan label{display:flex;gap:10px;align-items:flex-start;padding:6px 0;color:#E9EEF6;font-size:17px;line-height:1.4;cursor:pointer}
.plan input{margin-top:4px;width:18px;height:18px;accent-color:#FCB316;flex:none}
.pout{background:#0F2240;border:1px solid #3A4E72;border-radius:10px;padding:12px 14px;color:#E9EEF6;font-size:17px;line-height:1.6;margin:10px 0;white-space:pre-wrap}
.pout[hidden]{display:none}''',
body='''  <div class="col lede">
    <p>Psychologists call this belonging uncertainty. When students aren’t sure they fit, everyday setbacks, like a low grade or a cold remark, can feel like proof. The worry is more common for students whose group is underrepresented, or negatively stereotyped, in that setting.</p>
    <p>In a classic study, Gregory Walton and Geoffrey Cohen tested a one-hour exercise with 92 first-year students at a selective university. Students read surveys and stories from older students: worries about belonging were common at first, and faded with time. Then they wrote an essay and gave a short speech, in their own words, for future students.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>92</strong><span>first-year students, one hour, one campus</span></div>
      <div role="listitem"><strong>About half</strong><span>of the achievement gap closed for African American students, over three years</span></div>
      <div role="listitem"><strong>Fewer</strong><span>doctor visits, and better self-reported health</span></div>
      <div role="listitem"><strong>No awareness</strong><span>in senior year that the exercise had made a difference</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The message</span>Normal, shared, and it changes</h2>
    <p>Over the next three years, the exercise raised the grades of the African American students, and cut their achievement gap with white students by about half. They also reported better health, and fewer doctor visits. And in senior year, they showed no awareness that the exercise had made a difference.</p>
    <p>The message never said college is easy. It said: struggle is normal, it is shared, and it changes. That changed how students read their own setbacks.</p>
  </div>

'''+cls_html('bT','Which response helps?','Eight things an instructor might say or do after early setbacks. For each, decide: does it help students read the setback as normal and temporary, or does it work against that? You’ll get feedback after each one.',[('H','Helps',''),('W','Works against it','')],'Helps or works against it?','Which response helps?','The question is always: does it say struggle is normal, shared, and changes, without pretending it’s easy?')+'''
  <section class="night" aria-labelledby="mT">
    <div class="col">
      <h2 class="sec" id="mT"><span class="n">Try it</span>Draft your early-term message</h2>
      <p>Pick one line for each part of the message, and get a draft to adapt for your course. The best version uses real words from your own former students.</p>
      <form class="plan" id="mF">
        <fieldset><legend>It’s normal</legend>
          <label><input type="radio" name="m1" value="Most students find the first weeks of this course hard. If you do too, you’re in good company." checked>Most students find the start hard</label>
          <label><input type="radio" name="m1" value="Feeling unsure in the first few weeks is one of the most common experiences in this course.">Feeling unsure early is very common</label>
        </fieldset>
        <fieldset><legend>It’s shared</legend>
          <label><input type="radio" name="m2" value="Last year, a student told me: “[paste a real quote from a former student about struggling at first, and what changed]”" checked>A former student’s words (you add a real quote)</label>
          <label><input type="radio" name="m2" value="When I surveyed last year’s class, [your number] said they had worried at first about whether they could do well here.">What last year’s survey showed (you add your own number)</label>
        </fieldset>
        <fieldset><legend>It changes</legend>
          <label><input type="radio" name="m3" value="For most students, it gets better within a few weeks, as the material and the routines become familiar." checked>It gets better within a few weeks</label>
          <label><input type="radio" name="m3" value="A low score on the first quiz is information, not a verdict. Many of the students who did best by the end started slowly.">A first low score is information, not a verdict</label>
        </fieldset>
        <fieldset><legend>Back it up</legend>
          <label><input type="radio" name="m4" value="Come to office hours this week, even just to say hello. That’s what they’re for." checked>Invite them to office hours</label>
          <label><input type="radio" name="m4" value="Study groups start next week. Sign up by Friday, and I’ll put you in one.">Point them to a study group</label>
        </fieldset>
        <div class="mrow"><button class="nbtn" type="submit">Make my draft</button><button class="nbtn ghost" type="button" id="mCopy" hidden>Copy the draft</button></div>
      </form>
      <div class="pout" id="mOut" hidden aria-live="polite"></div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>One campus, a small sample</h2>
    <p>This was one campus and a small sample. Later and larger studies, in the next topic, found smaller effects that depended on the setting. A message cannot replace a course that actually welcomes students.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">For teaching</h3>
      <p>Early in the term, tell students that most people find the start hard, and that it gets better. Share stories from former students, including students like them. Have students write advice to next year’s class. And respond to early setbacks as normal, not as a verdict.</p>
    </aside>
  </div>
''',
tips_h='Belonging isn’t a trait students have or lack. It is a story, and stories can change.',
tips='''      <li><b>Normal, shared, changes</b><span>Say all three, early.</span></li>
      <li><b>Real stories</b><span>From former students, including students like them.</span></li>
      <li><b>Setbacks aren’t verdicts</b><span>Respond to early struggles as normal.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1126/science.1198364">Walton, G. M., &amp; Cohen, G. L. (2011). A brief social-belonging intervention improves academic and health outcomes of minority students. <i>Science, 331</i>(6023), 1447–1451.</a></li>''',
quiz='''[
 {q:'The one-hour exercise told students that early worries about belonging were…',o:['Common, and faded with time','A sign to change course','Rare'],a:0,f:'Struggle is normal, shared, and changes.'},
 {q:'Over three years, the achievement gap for African American students…',o:['Closed by about half','Widened','Didn’t change'],a:0,f:'They also reported better health and fewer doctor visits.'},
 {q:'Did the message say college is easy?',o:['No','Yes','It didn’t mention difficulty'],a:0,f:'It said struggle is normal, shared, and changes.'}]''',
js=BASE+cls_js("{H:'Helps',W:'Works against it'}",'''[
 ['“Lots of students find the first quiz hard. Here’s what helped last year’s class.”','H','Helps: it says the struggle is normal and shared, and points to what changes it.'],
 ['“This should be easy if you’re prepared for this course.”','W','Works against it: a struggling student hears that they don’t belong.'],
 ['Sharing a short quote from a former student about feeling lost in week two, and what changed','H','Helps: real stories from students like them make the message believable.'],
 ['Posting the grade distribution with a note that the bottom third probably won’t pass','W','Works against it: it turns an early setback into a verdict.'],
 ['“A low first score is information, not a verdict. Let’s look at what to change.”','H','Helps: it frames the setback as temporary and fixable.'],
 ['Telling a struggling student that some people just aren’t cut out for this field','W','Works against it: it confirms the worst reading of the setback.'],
 ['Asking students to write advice for next year’s class about getting through the start','H','Helps: saying the message in their own words was central to the exercise.'],
 ['“Don’t worry, college is easy once you get going.”','W','Works against it: the message never said college is easy. If it isn’t, students conclude the problem is them.']]''','Helps or works against it?',r'''
 if(right>=7){title='You have the message';text=`${right} of 8 right. Struggle is normal, it is shared, and it changes, without pretending it’s easy.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Watch for messages that turn setbacks into verdicts, or that promise it will be easy.`}
 else{title='Worth another look';text=`${right} of 8 right. Helpful responses say early struggle is common and temporary, and point to what helps. Unhelpful ones make it a verdict, or deny it.`}''')+r'''
/* ---------- draft your early-term message ---------- */
let draft='';
$('mF').addEventListener('submit',e=>{e.preventDefault();const v=n=>document.querySelector(`input[name="${n}"]:checked`).value;
 draft=['Dear all,',v('m1'),v('m2'),v('m3'),v('m4'),'See you in class.'].join('\n\n');$('mOut').textContent=draft;$('mOut').hidden=false;$('mCopy').hidden=false;$('mCopy').textContent='Copy the draft'});
$('mCopy').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(draft);$('mCopy').textContent='Copied'}catch(err){$('mCopy').textContent='Copy not available: select the text instead'}});
''')
open('b01/template.html','w').write(page(o))

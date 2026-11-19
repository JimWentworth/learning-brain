import sys,json;sys.path.insert(0,'gen')
from common import page
from memjs import *
# links to other topics: @@LB:<id>@@ tokens, turned into relative links by tools/build_site.py
def L(mid,text):
    u=f'@@LB:{mid}@@'
    return f'<a href="{u}">{text}</a>' if u else text
o=dict(id='m12',n='12',label='The Learning Brain · Memory · Topic 12',epi='The Learning Brain, Memory, episode 12',
title='Designing for Memory: Turning the Science into a Course',h1='Designing for memory',em='How learning lasts',read='7',mins='2 minutes',vtitle='Designing for memory',
dek='The life of a memory, turned into course design: guard attention and ask for meaning, give it time and sleep, come back after some forgetting, and make retrieval the main event.',
jumps='<span><a href="#bT">Rate the techniques</a></span><span><a href="#cT">When to review</a></span>',
hero_aria='Drawing of the side of the brain with the hippocampus, deep inside, and the prefrontal cortex, at the front, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.hip.lab=[640,770];BR.R.hip.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['hip','pfc'],labels:['hip','pfc'],labelT:{hip:0.8,pfc:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS+'''
.calc{background:#fff;border:1px solid var(--rule);border-radius:10px;padding:22px;max-width:700px;margin:0 auto}
.calc label{font-weight:700;display:block;margin-bottom:8px}
.calc input[type=range]{width:100%;accent-color:#C2410C}
.calc .presets{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}
.calc .presets button{min-height:44px;border-radius:999px;border:2px solid var(--ink);background:#fff;color:var(--ink);font:700 16px var(--body);padding:0 14px;cursor:pointer}
.calc .presets button[aria-pressed=true]{background:var(--ink);color:#fff}
.calc .out{font-size:19px;line-height:1.5;margin:10px 0 0}
.calc .out b{font-size:24px}''',
body='''  <div class="col lede">
    <p>Over twelve topics, this series followed a memory from the moment it is noticed to the moment it is recalled and rewritten. This last topic turns that life into a course design.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>1,350+</strong><span>people in a study of how long to wait before reviewing</span></div>
      <div role="listitem"><strong>20–40%</strong><span>of the time until a test a week away: the best gap before review</span></div>
      <div role="listitem"><strong>5–10%</strong><span>for a test a year away</span></div>
      <div role="listitem"><strong>2 of 10</strong><span>study techniques rated high: practice testing and spaced practice</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">At encoding</span>Get it in, with meaning</h2>
    <p>Guard attention (topic 2, '''+L('m02','attention is the gate')+'''). Ask for meaning, not just form (topic 3, '''+L('m03','depth and meaning')+'''). Have students generate answers rather than copy them (topic 4, '''+L('m04','make it, don’t take it')+'''). And connect new material to what they already know (topic 5, '''+L('m05','building on what’s there')+''').</p>
    <h2 class="sec"><span class="n">Then give it time</span>Let it settle</h2>
    <p>Memories stabilize over hours and days (topic 6, '''+L('m06','from fragile to stable')+'''), and sleep does much of that work (topic 7, '''+L('m07','what sleep does')+'''). Don’t schedule against it.</p>
    <h2 class="sec"><span class="n">Come back</span>After some forgetting</h2>
    <p>In 2008, Nicholas Cepeda, Harold Pashler and colleagues taught more than 1,350 people a set of facts, reviewed them after a gap, and tested them up to a year later. The best gap grew with how long the memory had to last. As a share of the time until the test, it fell from about 20 to 40% for a test a week away to about 5 to 10% for a test a year away.</p>
  </div>

  <section aria-labelledby="cT" style="margin:24px 0 40px">
    <div class="col">
      <h2 class="sec" id="cT"><span class="n">Try it</span>When to review</h2>
      <p>Choose how far away the test is. The calculator estimates a good gap between first learning and review, using the 2008 findings. Treat it as a rough guide: the study measured a few points, and this fills in between them.</p>
    </div>
    <div class="wide">
      <div class="calc">
        <label for="cDays">Days until the test: <span id="cDv">30</span></label>
        <input type="range" id="cDays" min="7" max="365" value="30" step="1" aria-describedby="cOut">
        <div class="presets" role="group" aria-label="Common test delays"><button type="button" data-d="7">1 week</button><button type="button" data-d="30" aria-pressed="true">1 month</button><button type="button" data-d="70">10 weeks</button><button type="button" data-d="180">6 months</button><button type="button" data-d="365">1 year</button></div>
        <p class="out" id="cOut" aria-live="polite"></p>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Make retrieval the main event</span>Recall, vary, correct</h2>
    <p>Quiz often, ask for recall before showing answers, vary the cues and settings (topic 10, '''+L('m10','cues and context')+'''), and correct errors with feedback (topic 11, '''+L('m11','retrieval rewrites memory')+''').</p>
    <p>In 2013, John Dunlosky, Katherine Rawson and colleagues reviewed ten study techniques. They rated just two as high utility: practice testing and distributed (spaced) practice. Five, including rereading and highlighting, some of the techniques students use most, were rated low.</p>
  </div>

'''+cls_html('bT','Rate the techniques','The ten techniques from the 2013 review. For each, guess the rating it got: high, moderate or low utility. You’ll get feedback after each one.',[('H','High',''),('M','Moderate',''),('L','Low','')],'What rating did it get?','How useful?','Ratings weigh how well each technique works and how widely the benefit holds.')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Measure it in your course</h2>
    <p>Much of this evidence comes from labs and simple materials. Classroom studies mostly point the same way, but effects vary, so measure what changes in your own course.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">For your next course</h3>
      <p>Pick one unit. Add a short weekly quiz, mix earlier topics into later quizzes, and swap one review session for retrieval. Then compare results with last year.</p>
    </aside>
  </div>
''',
tips_h='Memory is how learning lasts',
tips='''      <li><b>A short weekly quiz</b><span>Low stakes, with feedback.</span></li>
      <li><b>Mix earlier topics in</b><span>So reviews come after some forgetting.</span></li>
      <li><b>Swap one review for retrieval</b><span>Then compare with last year.</span></li>''',
sources='''        <li><a href="https://pubmed.ncbi.nlm.nih.gov/19076480/">Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., &amp; Pashler, H. (2008). Spacing effects in learning: A temporal ridgeline of optimal retention. <i>Psychological Science</i>.</a></li>
        <li><a href="https://doi.org/10.1177/1529100612453266">Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., &amp; Willingham, D. T. (2013). Improving students’ learning with effective learning techniques. <i>Psychological Science in the Public Interest</i>.</a></li>''',
quiz='''[
 {q:'Which two study techniques were rated high utility in the 2013 review?',o:['Practice testing and spaced practice','Rereading and highlighting','Summarizing and imagery'],a:0,f:'Five, including rereading and highlighting, were rated low.'},
 {q:'For a test a year away, the best gap before review was about',o:['5 to 10% of the time until the test','50%','A day'],a:0,f:'For a test a week away, it was about 20 to 40%.'},
 {q:'Much of this evidence comes from labs. What should you do?',o:['Measure what changes in your own course','Ignore it','Assume it works the same everywhere'],a:0,f:'Classroom studies mostly point the same way, but effects vary.'}]''',
js=BASE+cls_js("{H:'High',M:'Moderate',L:'Low'}",'''[
 ['Practice testing: quizzing yourself, or taking practice tests.','H','High: it helped across many materials, ages and kinds of test.'],
 ['Distributed practice: spreading study out over time.','H','High: the benefit held widely, and grows with longer gaps for longer retention.'],
 ['Elaborative interrogation: asking yourself why a fact is true.','M','Moderate: promising, but tested mostly with lists of facts.'],
 ['Self-explanation: explaining how new information relates to what you know, or how you solved a step.','M','Moderate: it helps in many studies, but takes time and needs more classroom tests.'],
 ['Interleaved practice: mixing different kinds of problems in one session.','M','Moderate: strong results in some areas, like maths, but less tested elsewhere.'],
 ['Summarization: writing summaries of what you read.','L','Low: it helps students who are already good at summarizing, but many need training first.'],
 ['Highlighting and underlining.','L','Low: little benefit in most studies, despite being very popular.'],
 ['The keyword mnemonic: linking a new word to a familiar word and an image.','L','Low: it helps for some material, like foreign vocabulary, but the benefit is narrow.'],
 ['Imagery for text: forming mental pictures while reading.','L','Low: it helps mainly with text that’s easy to picture.'],
 ['Rereading.','L','Low: the most common technique, but its benefits are small next to testing and spacing.']]''','What rating did it get?',r'''
 if(right>=9){title='You know the evidence';text=`${right} of 10 right. Two techniques stand out: practice testing and spaced practice. The most popular ones, rereading and highlighting, were rated low.`}
 else if(right>=5){title='Mostly there';text=`${right} of 10 right. You missed ${missed}. The short version: test yourself, and spread it out. Rereading and highlighting feel productive but do little.`}
 else{title='Worth another look';text=`${right} of 10 right. Only two were rated high: practice testing and spaced practice. Five were rated low, including rereading and highlighting, which students use most.`}''')+r'''
/* ---------- when to review ----------
   Cepeda et al. (2008): optimal gap about 20-40% of a 1-week test delay, about 5-10% of a 1-year delay.
   Interpolated on a log-time scale between those two points; rough guide only. */
function gap(d){const t=Math.max(0,Math.min(1,(Math.log(d)-Math.log(7))/(Math.log(365)-Math.log(7))));return[0.20+(0.05-0.20)*t,0.40+(0.10-0.40)*t]}
const PRE={7:'a week',30:'a month',70:'10 weeks',180:'6 months',365:'a year'};
const fmtD=d=>PRE[d]||(d<14?d+' days':d<60?Math.round(d/7)+' weeks':Math.round(d/30.4)+' months');
function fmtR(lo,hi){const r=(a,b,u)=>a===b?`${a} ${u}${a===1?'':'s'}`:`${a} to ${b} ${u}s`;
 if(hi<21)return r(Math.max(1,Math.round(lo)),Math.max(1,Math.round(hi)),'day');
 if(hi<90)return r(Math.max(1,Math.round(lo/7)),Math.round(hi/7),'week');
 return r(Math.max(1,Math.round(lo/30.4)),Math.round(hi/30.4),'month')}
function cUpd(){const d=+$('cDays').value;$('cDv').textContent=d;const [a,b]=gap(d);
 $('cOut').innerHTML=`For a test in ${fmtD(d)}, review after about <b>${fmtR(a*d,b*d)}</b>: roughly ${Math.round(a*100)} to ${Math.round(b*100)}% of the time until the test.`;
 document.querySelectorAll('.presets button').forEach(x=>x.setAttribute('aria-pressed',+x.dataset.d===d?'true':'false'))}
$('cDays').addEventListener('input',cUpd);
document.querySelectorAll('.presets button').forEach(x=>x.addEventListener('click',()=>{$('cDays').value=x.dataset.d;cUpd()}));
cUpd();
''')
open('m12/template.html','w').write(page(o))

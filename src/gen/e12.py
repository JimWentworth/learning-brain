import sys,json;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
def L(mid,text):
    u=f'@@LB:{mid}@@'
    return f'<a href="{u}">{text}</a>' if u else text
MAP=[('e01','Tests that teach','recall beats rereading'),('e02','Quizzing in real classes','small quizzes, often'),('e03','Do quizzes cause anxiety?','low stakes calm nerves'),
 ('e04','Test before you teach','guess first, then learn'),('e05','Feedback that works','usable, about the work'),('e06','Specifications grading','promising, little controlled evidence'),
 ('e07','Better multiple choice','plausible wrong answers'),('e08','The case for cumulative exams','bring earlier material back'),('e09','Mastery and retakes','a second chance, with new learning'),
 ('e10','Make the task transparent','purpose, task, criteria'),('e11','Integrity in the age of AI','make the thinking show')]
maphtml='\n'.join(f'      <li><b>{i+1}. {L(m,t)}</b><span>{d}</span></li>' for i,(m,t,d) in enumerate(MAP))
o=sbase('e','Assessment That Teaches',12,'Designing Assessment That Teaches','Designing assessment that teaches','Every test is a chance to learn. Design it that way.','Designing assessment that teaches',
'Across this series, one idea has run through every episode: assessment is not only how we measure learning. Done well, it is how learning happens.',
'<span><a href="#bT">Before, during or after?</a></span><span><a href="#pT">Plan one unit</a></span>')
o['hero_aria'],o['hero_js']=hero(['pfc','hip'],{'pfc':([40,-60],'left'),'hip':([640,770],'left')},'Drawing of the side of the brain with the prefrontal cortex, at the front, and the hippocampus, deep inside, glowing orange and labelled.')
o.update(css=RECALL_CSS+CLS_CSS+'''
.amap{list-style:none;padding:0;margin:14px 0 6px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px 18px}
@media (max-width:640px){.amap{grid-template-columns:1fr}}
.amap li{border-left:3px solid #FF5F05;padding:4px 0 4px 10px}
.amap b{display:block;color:#13294B}.amap span{color:#3A4E72;font-size:16px}
.stages{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:18px 0 6px}
@media (max-width:640px){.stages{grid-template-columns:1fr}}
.stages div{border:1px solid #C9D3E3;border-radius:10px;padding:12px 14px;background:#fff}
.stages b{display:block;font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#13294B;margin-bottom:4px}
.stages span{color:#3A4E72}
.plan fieldset{border:1px solid #3A4E72;border-radius:10px;padding:10px 14px;margin:0 0 12px}
.plan legend{font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#FCB316;padding:0 6px}
.plan label{display:flex;gap:10px;align-items:flex-start;padding:6px 0;color:#E9EEF6;font-size:17px;line-height:1.4;cursor:pointer}
.plan input{margin-top:4px;width:18px;height:18px;accent-color:#FCB316;flex:none}
.pout{background:#0F2240;border:1px solid #3A4E72;border-radius:10px;padding:12px 14px;color:#E9EEF6;font-size:17px;line-height:1.5;margin:10px 0}
.pout[hidden]{display:none}
.pout ol{margin:6px 0 0;padding-left:22px}''',
body='''  <div class="col lede">
    <p>The thread through all of it is simple: the more an assessment asks students to retrieve, think and improve, the more it teaches. None of this needs a full course redesign. Each change is small, and each one can be tried in a single unit.</p>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The map</span>Eleven topics</h2>
    <ul class="amap">
'''+maphtml+'''
    </ul>
    <h2 class="sec"><span class="n">The design</span>Before, during, and after</h2>
    <div class="stages" role="list">
      <div role="listitem"><b>Before</b><span>Pose a few pretest questions to focus attention. Make the purpose, task and criteria of each assignment transparent, with an example of good work.</span></div>
      <div role="listitem"><b>During</b><span>Quiz often, low stakes, with questions that require recall and plausible wrong answers. Give feedback that says what to do next, and leave room to use it.</span></div>
      <div role="listitem"><b>After</b><span>Make later exams cumulative, so earlier material comes back. Offer retakes or revisions on key outcomes, with new learning in between. Design for integrity, with visible process.</span></div>
    </div>
  </div>

'''+cls_html('bT','Before, during or after?','Nine steps from the series. For each, decide where it belongs: before a unit, during it, or after it. You’ll get feedback after each one.',[('B','Before',''),('D','During',''),('A','After','')],'Before, during or after?','Before, during or after?','The question is always: when in the unit does this step do its work?')+'''
  <section class="night" aria-labelledby="pT">
    <div class="col">
      <h2 class="sec" id="pT"><span class="n">Try it</span>Plan one unit</h2>
      <p>Pick one change for before, one for during, and one for after your next unit. Tell students why you are making it. Then look at what they learned, and keep what works.</p>
      <form class="plan" id="pForm">
        <fieldset><legend>Before</legend>
          <label><input type="radio" name="pb" value="Open the unit with two or three ungraded pretest questions on the ideas that matter most." checked>Pretest questions</label>
          <label><input type="radio" name="pb" value="Rewrite the main assignment with its purpose, steps and criteria, and share an annotated example.">A transparent assignment</label>
        </fieldset>
        <fieldset><legend>During</legend>
          <label><input type="radio" name="pd" value="Give a short, low-stakes quiz every week, with recall questions and plausible wrong answers." checked>Weekly low-stakes quizzes</label>
          <label><input type="radio" name="pd" value="Give one specific, usable comment on each draft, with a chance to revise.">Usable feedback, with a revision</label>
        </fieldset>
        <fieldset><legend>After</legend>
          <label><input type="radio" name="pa" value="Put some questions from earlier units on the unit exam, and tell students in advance." checked>Cumulative questions</label>
          <label><input type="radio" name="pa" value="Allow one retake on the key outcome, after a short correction step, with fresh questions and a deadline.">A retake with a study step</label>
          <label><input type="radio" name="pa" value="Add a visible-process step to the main assignment: an outline, a draft, or a short conversation.">Visible process for integrity</label>
        </fieldset>
        <div class="mrow"><button class="nbtn" type="submit">Make my plan</button><button class="nbtn ghost" type="button" id="pCopy" hidden>Copy the plan</button></div>
      </form>
      <div class="pout" id="pOut" hidden aria-live="polite"></div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Not every popular practice holds up</h2>
    <p>Exam wrappers, short reflections after a test, showed no effect on grades in one well-designed single-course study. Specifications grading has mixed evidence. Check what happens in your own course.</p>
  </div>
'''+box('Pick one change for before, during and after your next unit. Tell students why you are making it. Then look at what they learned, and keep what works. Share this tip with students: use every test as practice for the next one.'),
tips_h='Every test is a chance to learn. Design it that way.',
tips='''      <li><b>Before</b><span>Pretests; transparent assignments.</span></li>
      <li><b>During</b><span>Frequent low-stakes quizzes; usable feedback.</span></li>
      <li><b>After</b><span>Cumulative exams; retakes; visible process.</span></li>''',
sources='''        <li>Soicher, R. N., &amp; Gurung, R. A. R. (2017). Do exam wrappers increase metacognition and performance? A single course intervention. <i>Psychology Learning &amp; Teaching, 16</i>(1), 64–73.</li>
        <li>The studies behind each step are listed on each topic’s page.</li>''',
quiz='''[
 {q:'The thread through this series is that the more an assessment asks students to retrieve, think and improve…',o:['The more it teaches','The more stressful it is','The less it measures'],a:0,f:'Assessment as a way to learn.'},
 {q:'Exam wrappers, in one well-designed study…',o:['Showed no effect on grades','Doubled grades','Weren’t tested'],a:0,f:'Not every popular practice holds up.'},
 {q:'Does this need a full course redesign?',o:['No: each change can be tried in one unit','Yes','Only for large classes'],a:0,f:'Small changes, checked.'}]''',
js=BASE+cls_js("{B:'Before',D:'During',A:'After'}",'''[
 ['Asking two or three questions students can’t yet answer','B','Before: pretests focus attention on what matters (topic 4).'],
 ['Sharing the purpose, task and criteria, with an example','B','Before: transparency, so students aim at the right target (topic 10).'],
 ['A short, low-stakes quiz every week','D','During: frequent quizzing builds memory and calms nerves (topics 2 and 3).'],
 ['Writing wrong answers from real misconceptions','D','During: plausible options make multiple choice teach (topic 7).'],
 ['One specific comment on what to change, with a chance to revise','D','During: feedback that can be used (topic 5).'],
 ['Questions from earlier units on the next exam','A','After: cumulative exams bring material back (topic 8).'],
 ['A retake after a short correction step','A','After: mastery with new learning in between (topic 9).'],
 ['A short conversation about how the student wrote the paper','A','After: visible process, for integrity (topic 11).'],
 ['Checking whether students learned more, not just whether they liked it','A','After: keep what works.']]''','Before, during or after?',r'''
 if(right>=8){title='You have the design';text=`${right} of 9 right. Before: pretests and transparency. During: quizzes, good options, usable feedback. After: cumulative exams, retakes, visible process.`}
 else if(right>=5){title='Mostly there';text=`${right} of 9 right. You missed ${missed}. Ask when in the unit each step does its work.`}
 else{title='Worth another look';text=`${right} of 9 right. Before sets the target; during is practice and feedback; after brings material back and gives second chances.`}''')+r'''
/* ---------- plan one unit ---------- */
let planTxt='';
$('pForm').addEventListener('submit',e=>{e.preventDefault();const v=n=>document.querySelector(`input[name="${n}"]:checked`).value;
 const st=[['Before',v('pb')],['During',v('pd')],['After',v('pa')]];
 planTxt='Assessment plan for my next unit\n'+st.map(([a,b],i)=>`${i+1}. ${a}: ${b}`).join('\n')+'\n4. Tell students why. Then look at what they learned, and keep what works.';
 $('pOut').innerHTML='<b>Your plan</b><ol>'+st.map(([a,b])=>`<li><b>${a}:</b> ${b}</li>`).join('')+'<li><b>Then:</b> tell students why, look at what they learned, and keep what works.</li></ol>';$('pOut').hidden=false;$('pCopy').hidden=false;$('pCopy').textContent='Copy the plan'});
$('pCopy').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(planTxt);$('pCopy').textContent='Copied'}catch(err){$('pCopy').textContent='Copy not available: select the text instead'}});
''')
open('e12/template.html','w').write(page(o))

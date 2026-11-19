import sys,json;sys.path.insert(0,'gen')
from common import page
from memjs import *
# links to other topics: @@LB:<id>@@ tokens, turned into relative links by tools/build_site.py
def L(mid,text):
    u=f'@@LB:{mid}@@'
    return f'<a href="{u}">{text}</a>' if u else text
MAP=[('a01','Prediction','what a language model is'),('a02','Offloading','what to keep in your own head'),('a03','The jagged frontier','where AI helps and where it misleads'),
 ('a04','Crutch or tutor','practice that helps or harms'),('a05','A tutor built on learning science','design decides'),('a06','Confident and wrong','calibration'),
 ('a07','Automation bias','practise disagreeing'),('a08','Thinking alongside AI','from making to checking'),('a09','Writing is thinking','protect an unaided stage'),
 ('a10','Creativity and sameness','keep ideas different'),('a11','Trust, but verify','lateral reading')]
maphtml='\n'.join(f'      <li><b>{i+1}. {L(m,t)}</b><span>{d}</span></li>' for i,(m,t,d) in enumerate(MAP))
o=dict(id='a12',n='12',label='The Learning Brain · Generative AI · Topic 12',epi='The Learning Brain, Generative AI, episode 12',
title='Designing for Both: AI That Raises Performance and Learning',h1='Designing for both',em='Before, during, and after AI',read='7',mins='2 minutes',vtitle='Designing for both',
dek='Across the series, one pattern repeats. When AI does the thinking, performance can rise while learning falls. When AI makes students think, both can rise.',
jumps='<span><a href="#bT">Before, during or after?</a></span><span><a href="#pT">Plan one assignment</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, the parietal lobe, at the top, and the hippocampus, deep inside, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.par.lab=[1060,40];BR.R.par.al='right';BR.R.hip.lab=[640,770];BR.R.hip.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc','par','hip'],labels:['pfc','par','hip'],labelT:{pfc:0.8,par:1.0,hip:1.2},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS+'''
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
    <p>Across eleven topics, one pattern repeats. When AI does the thinking, performance can rise while learning falls. When AI makes students think, both can rise. We saw it in maths classrooms, physics courses, consulting firms and essay writing.</p>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The map</span>Eleven topics, one pattern</h2>
    <ul class="amap">
'''+maphtml+'''
    </ul>
    <h2 class="sec"><span class="n">The design</span>Before, during, and after AI</h2>
    <div class="stages" role="list">
      <div role="listitem"><b>Before AI: commit</b><span>Students predict, draft and generate ideas on their own, so there is something to learn from, and something to compare against.</span></div>
      <div role="listitem"><b>During AI: think</b><span>The tool hints rather than solves, asks before it tells, and runs on correct material. Students explain its reasoning back, and look for a flaw.</span></div>
      <div role="listitem"><b>After AI: check</b><span>Students verify sources, check their confidence against results, and do some practice without AI, so everyone can see what they can do alone.</span></div>
    </div>
  </div>

'''+cls_html('bT','Before, during or after?','Nine steps from the series. For each, decide where it belongs in an assignment: before AI, during AI, or after AI. You’ll get feedback after each one.',[('B','Before AI','commit'),('D','During AI','think'),('A','After AI','check')],'Before, during or after AI?','Before, during or after?','The question is always: what does this step make the student do?')+'''
  <section class="night" aria-labelledby="pT">
    <div class="col">
      <h2 class="sec" id="pT"><span class="n">Try it</span>Plan one assignment</h2>
      <p>Pick one step for each stage, and get a plan you can copy into your course notes.</p>
      <form class="plan" id="pForm">
        <fieldset><legend>Before AI</legend>
          <label><input type="radio" name="pb" value="Students write their own first attempt or outline, unaided." checked>A first attempt or outline, unaided</label>
          <label><input type="radio" name="pb" value="Students predict the answer and rate their confidence.">A prediction, with a confidence rating</label>
          <label><input type="radio" name="pb" value="Students generate three ideas of their own before any AI.">Three ideas of their own</label>
        </fieldset>
        <fieldset><legend>During AI</legend>
          <label><input type="radio" name="pd" value="Students use a hint-only tutor, loaded with correct solutions." checked>A hint-only tutor, loaded with correct solutions</label>
          <label><input type="radio" name="pd" value="Students ask the AI to critique their draft, and explain which suggestions they accept and why.">AI critiques the student’s own draft</label>
          <label><input type="radio" name="pd" value="Students explain the AI’s reasoning back, and find one flaw in it.">Explain the AI’s reasoning back, and find a flaw</label>
        </fieldset>
        <fieldset><legend>After AI</legend>
          <label><input type="radio" name="pa" value="Students verify every AI-supplied source, and show how." checked>Verify every AI source, and show how</label>
          <label><input type="radio" name="pa" value="Students compare their confidence with their results.">Compare confidence with results</label>
          <label><input type="radio" name="pa" value="Students do a short practice task without AI.">A short practice task without AI</label>
        </fieldset>
        <div class="mrow"><button class="nbtn" type="submit">Make my plan</button><button class="nbtn ghost" type="button" id="pCopy" hidden>Copy the plan</button></div>
      </form>
      <div class="pout" id="pOut" hidden aria-live="polite"></div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">The evidence</span>Strongest where it is oldest</h2>
    <p>The evidence for this pattern is strongest where it is oldest: retrieval, generation and metacognition. The AI studies are newer and smaller, so treat each one as a hypothesis to test in your own course. Run small comparisons, and share what you find.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">For your next course</h3>
      <p>Pick one assignment. Add a commit step before AI, a hint-only tutor or a critique step during it, and a verify step after. Then compare unassisted performance with last year.</p>
    </aside>
  </div>
''',
tips_h='Designed well, AI and the brain make each other stronger',
tips='''      <li><b>Before: commit</b><span>Predict, draft or generate ideas alone.</span></li>
      <li><b>During: think</b><span>Hints, not answers; explain it back.</span></li>
      <li><b>After: check</b><span>Verify, calibrate, and practise without AI.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1073/pnas.2422633122">Bastani, H., et al. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. <i>Proceedings of the National Academy of Sciences, 122</i>(26), e2422633122.</a></li>
        <li><a href="https://doi.org/10.1038/s41598-025-97652-6">Kestin, G., Miller, K., et al. (2025). AI tutoring outperforms in-class active learning. <i>Scientific Reports, 15</i>, 17458.</a></li>
        <li>The other studies are listed on each topic’s page.</li>''',
quiz='''[
 {q:'When AI does the thinking…',o:['Performance can rise while learning falls','Both always rise','Both always fall'],a:0,f:'When AI makes students think, both can rise.'},
 {q:'Which step belongs before AI?',o:['Students draft or predict on their own','Students verify sources','The tutor gives hints'],a:0,f:'So there is something to learn from, and to compare against.'},
 {q:'Where is the evidence for this pattern strongest?',o:['Retrieval, generation and metacognition','The newest AI studies','Brain scans alone'],a:0,f:'Treat each AI study as a hypothesis to test in your own course.'}]''',
js=BASE+cls_js("{B:'Before AI',D:'During AI',A:'After AI'}",'''[
 ['Students draft their ideas and structure on their own','B','Before AI: the unaided draft is where much of the thinking happens (topic 9).'],
 ['Students predict their answer and rate their confidence','B','Before AI: it gives them something to check against, and shows their calibration (topic 6).'],
 ['Students generate ideas alone','B','Before AI: so the AI’s suggestion doesn’t pull everyone to the same place (topic 10).'],
 ['The tutor gives a hint, not the answer','D','During AI: the student still has to produce the answer (topics 4 and 5).'],
 ['Students explain the AI’s reasoning back, and find one flaw','D','During AI: it keeps them judging the output instead of accepting it (topics 6 and 7).'],
 ['The tutor runs on the instructor’s correct solutions','D','During AI: accurate feedback is what makes a tutor teach (topic 5).'],
 ['Students verify every AI-supplied source','A','After AI: fluent output is not evidence (topic 11).'],
 ['Students compare their confidence with their results','A','After AI: so they learn how far their feeling of knowing can be trusted (topic 6).'],
 ['Students do some practice without AI','A','After AI: so everyone can see what they can do alone (topic 4).']]''','Before, during or after AI?',r'''
 if(right>=8){title='You have the design';text=`${right} of 9 right. Commit before, think during, check after: each stage makes the student do something the AI can’t do for them.`}
 else if(right>=5){title='Mostly there';text=`${right} of 9 right. You missed ${missed}. Before: commit. During: think. After: check.`}
 else{title='Worth another look';text=`${right} of 9 right. Before AI, students commit to their own work. During, the tool makes them think. After, they check.`}''')+r'''
/* ---------- plan one assignment ---------- */
let planTxt='';
$('pForm').addEventListener('submit',e=>{e.preventDefault();const v=n=>document.querySelector(`input[name="${n}"]:checked`).value;
 const st=[['Before AI',v('pb')],['During AI',v('pd')],['After AI',v('pa')]];
 planTxt='Assignment plan\n'+st.map(([a,b],i)=>`${i+1}. ${a}: ${b}`).join('\n')+'\n4. Afterwards: compare unassisted performance with last year.';
 $('pOut').innerHTML='<b>Your plan</b><ol>'+st.map(([a,b])=>`<li><b>${a}:</b> ${b}</li>`).join('')+'<li><b>Afterwards:</b> compare unassisted performance with last year.</li></ol>';$('pOut').hidden=false;$('pCopy').hidden=false;$('pCopy').textContent='Copy the plan'});
$('pCopy').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(planTxt);$('pCopy').textContent='Copied'}catch(err){$('pCopy').textContent='Copy not available: select the text instead'}});
''')
open('a12/template.html','w').write(page(o))

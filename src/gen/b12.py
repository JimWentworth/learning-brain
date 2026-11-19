import sys,json;sys.path.insert(0,'gen')
from common import page
from memjs import *
def L(mid,text):
    u=f'@@LB:{mid}@@'
    return f'<a href="{u}">{text}</a>' if u else text
MAP=[('b01','Do I belong here?','struggle is normal, shared, and changes'),('b02','Belonging at scale','the message has to be true'),('b03','What the room says','cues are cheap to change'),
 ('b04','Stereotype threat, carefully','lower the stakes of identity'),('b05','Values affirmation','an experiment, not a fix'),('b06','Wise feedback','high standards and belief'),
 ('b07','The teacher’s mindset','ability grows'),('b08','First in the family','teach the unwritten rules'),('b09','Seeing yourself','show many future selves'),
 ('b10','Structure is inclusive','more class time active'),('b11','Impostor feelings','normalize doubt')]
maphtml='\n'.join(f'      <li><b>{i+1}. {L(m,t)}</b><span>{d}</span></li>' for i,(m,t,d) in enumerate(MAP))
o=dict(id='b12',n='12',label='The Learning Brain · Belonging · Topic 12',epi='The Learning Brain, Belonging, episode 12',
title='Designing for Belonging: Before, During and After',h1='Designing for belonging',em='Belonging is built in small moments. Design them on purpose.',read='7',mins='2 minutes',vtitle='Designing for belonging',
dek='Across this series, belonging is not a fixed trait. It is a question students keep asking, and our courses answer it, often without meaning to.',
jumps='<span><a href="#bT">Before, during or after?</a></span><span><a href="#pT">Plan one unit</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, the amygdala and the hippocampus, deep inside, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.amy.lab=[60,750];BR.R.amy.al='left';BR.R.hip.lab=[900,760];BR.R.hip.al='right';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc','amy','hip'],labels:['pfc','amy','hip'],labelT:{pfc:0.8,amy:1.0,hip:1.2},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
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
    <p>Across eleven topics, the same idea keeps returning. Students keep asking whether they belong, and every part of a course answers: the room, the feedback, the structure, the people they see, the rules we explain or leave unsaid.</p>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The map</span>Eleven topics</h2>
    <ul class="amap">
'''+maphtml+'''
    </ul>
    <h2 class="sec"><span class="n">The design</span>Before, during, and after</h2>
    <div class="stages" role="list">
      <div role="listitem"><b>Before</b><span>Check what the room and materials say. Plan structure into class time. Share that early struggle is common and temporary.</span></div>
      <div role="listitem"><b>During</b><span>Active learning with clear structure. Wise feedback. A range of people students can see themselves in. Ability as something that grows, in words and policies.</span></div>
      <div role="listitem"><b>After</b><span>Look at outcomes by group, not just averages. Read feedback for signs of doubt. Spell out the unwritten rules. Tell students what you changed.</span></div>
    </div>
    <p>Before high-stakes moments, like a first exam, you might consider a brief values affirmation, knowing that effects are small and vary by setting. And present tests as a chance to show growth, not a verdict on a group.</p>
  </div>

'''+cls_html('bT','Before, during or after?','Nine steps from the series. For each, decide where it belongs: before a unit, during it, or after it. You’ll get feedback after each one.',[('B','Before',''),('D','During',''),('A','After','')],'Before, during or after?','Before, during or after?','The question is always: when in the unit does this step do its work?')+'''
  <section class="night" aria-labelledby="pT">
    <div class="col">
      <h2 class="sec" id="pT"><span class="n">Try it</span>Plan one unit</h2>
      <p>Pick one change for before, one for during, and one for after your next unit. Then check whether it worked.</p>
      <form class="plan" id="pForm">
        <fieldset><legend>Before</legend>
          <label><input type="radio" name="pb" value="Share that early struggle is common and temporary, with a real story from a former student." checked>Share the belonging message, with a real story</label>
          <label><input type="radio" name="pb" value="Check who appears in my examples, slides and readings, and widen it.">Audit examples, slides and readings</label>
          <label><input type="radio" name="pb" value="Plan at least one structured active task into every class session.">Plan structure into class time</label>
        </fieldset>
        <fieldset><legend>During</legend>
          <label><input type="radio" name="pd" value="Give wise feedback: high standards, belief the student can reach them, and a specific next step." checked>Wise feedback on the first assignment</label>
          <label><input type="radio" name="pd" value="Use structured group work with clear roles, and call on students fairly, with think time.">Structured groups and fair calling</label>
          <label><input type="radio" name="pd" value="Offer a revision or retake, and talk about ability as something that grows.">A revision or retake, and growth language</label>
        </fieldset>
        <fieldset><legend>After</legend>
          <label><input type="radio" name="pa" value="Look at outcomes by group, not just the average." checked>Outcomes by group, not just averages</label>
          <label><input type="radio" name="pa" value="Hand out a short guide to the unwritten rules: office hours, emails, extensions.">Spell out the unwritten rules</label>
          <label><input type="radio" name="pa" value="Ask for anonymous feedback, and tell students what I changed because of it.">Close the loop on feedback</label>
        </fieldset>
        <div class="mrow"><button class="nbtn" type="submit">Make my plan</button><button class="nbtn ghost" type="button" id="pCopy" hidden>Copy the plan</button></div>
      </form>
      <div class="pout" id="pOut" hidden aria-live="polite"></div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Many small, consistent signals</h2>
    <p>Many of these effects are modest, and some depend on context. No single fix works alone. The aim is many small, consistent signals.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">For teaching</h3>
      <p>Pick one change for before, one for during, and one for after your next unit. Then check whether it worked.</p>
    </aside>
  </div>
''',
tips_h='Belonging is built in small moments. Design them on purpose.',
tips='''      <li><b>Before</b><span>Room, materials, message, structure.</span></li>
      <li><b>During</b><span>Active, wise, varied, growth-minded.</span></li>
      <li><b>After</b><span>Outcomes by group; close the loop.</span></li>''',
sources='''        <li>The studies behind each step are listed on each topic’s page.</li>''',
quiz='''[
 {q:'When should the belonging message come?',o:['Early, before the first setbacks','After the final exam','Only if students ask'],a:0,f:'And then back it up.'},
 {q:'After a unit, look at outcomes…',o:['By group, not just averages','Only as an average','Not at all'],a:0,f:'Averages can hide gaps.'},
 {q:'Is there a single fix for belonging?',o:['No: many small, consistent signals','Yes: values affirmation','Yes: one welcome speech'],a:0,f:'No single fix works alone.'}]''',
js=BASE+cls_js("{B:'Before',D:'During',A:'After'}",'''[
 ['Checking who appears in your examples, slides and readings','B','Before: what the room and materials say (topic 3).'],
 ['Telling students that early struggle is common and temporary','B','Before: early, ahead of the first setbacks (topics 1 and 2).'],
 ['Planning structured active tasks into class time','B','Before: structure has to be planned in (topic 10).'],
 ['Giving feedback with high standards, belief and a next step','D','During: wise feedback (topic 6).'],
 ['Using group work with clear roles, and fair, predictable calling','D','During: structure that reaches every student (topic 10).'],
 ['Inviting speakers and alumni from varied backgrounds','D','During: a range of people students can see themselves in (topic 9).'],
 ['Looking at outcomes by group, not just the average','A','After: averages can hide gaps (topic 2).'],
 ['Telling students what you changed because of their feedback','A','After: closing the loop.'],
 ['Reading course feedback for signs of doubt','A','After: impostor feelings and belonging doubts often show up there (topic 11).']]''','Before, during or after?',r'''
 if(right>=8){title='You have the design';text=`${right} of 9 right. Before: room, message, structure. During: active, wise, varied. After: outcomes by group, and close the loop.`}
 else if(right>=5){title='Mostly there';text=`${right} of 9 right. You missed ${missed}. Ask when in the unit each step does its work.`}
 else{title='Worth another look';text=`${right} of 9 right. Before sets up the room, message and structure; during is how you teach and give feedback; after is checking outcomes and closing the loop.`}''')+r'''
/* ---------- plan one unit ---------- */
let planTxt='';
$('pForm').addEventListener('submit',e=>{e.preventDefault();const v=n=>document.querySelector(`input[name="${n}"]:checked`).value;
 const st=[['Before',v('pb')],['During',v('pd')],['After',v('pa')]];
 planTxt='Belonging plan for my next unit\n'+st.map(([a,b],i)=>`${i+1}. ${a}: ${b}`).join('\n')+'\n4. Then: check whether it worked.';
 $('pOut').innerHTML='<b>Your plan</b><ol>'+st.map(([a,b])=>`<li><b>${a}:</b> ${b}</li>`).join('')+'<li><b>Then:</b> check whether it worked.</li></ol>';$('pOut').hidden=false;$('pCopy').hidden=false;$('pCopy').textContent='Copy the plan'});
$('pCopy').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(planTxt);$('pCopy').textContent='Copied'}catch(err){$('pCopy').textContent='Copy not available: select the text instead'}});
''')
open('b12/template.html','w').write(page(o))

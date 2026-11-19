import sys,json;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
def L(mid,text):
    u=f'@@LB:{mid}@@'
    return f'<a href="{u}">{text}</a>' if u else text
MAP=[('d01','Words and pictures','pictures that explain'),('d02','Cut the extras','leave out what doesn’t explain'),('d03','Don’t read your slides','say it; keep captions'),
 ('d04','How long should a video be?','one idea, six minutes or less'),('d05','Questions inside the video','ask often'),('d06','Speed-watching','spend saved time on practice'),
 ('d07','Laptop or longhand?','method over medium'),('d08','The laptop next to you','devices on purpose'),('d09','Paper or screen?','print or slow down for hard reading'),
 ('d10','Online, blended, face to face','redesign, don’t just record'),('d11','Lecture recordings','review, don’t replace')]
maphtml='\n'.join(f'      <li><b>{i+1}. {L(m,t)}</b><span>{d}</span></li>' for i,(m,t,d) in enumerate(MAP))
o=base(12,'Designing for Screens: Before, During and After','Designing for screens','The screen is just the window. What students do there is the lesson.','Designing for screens',
'Slides, video, notes, devices, reading and course formats. Put together, a clear picture emerges: screens are neither the problem nor the answer. Design is.',
'<span><a href="#bT">Before, during or after?</a></span><span><a href="#pT">Plan one unit</a></span>')
o['hero_aria'],o['hero_js']=hero(['pfc','hip'],{'pfc':([40,-60],'left'),'hip':([640,770],'left')},'Drawing of the side of the brain with the prefrontal cortex, at the front, which directs attention, and the hippocampus, deep inside, which helps form memories, glowing orange and labelled.')
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
    <p>One thread runs through this whole series: attention and working memory are limited. Good digital design protects them. It removes what distracts, segments what overloads, and asks students to retrieve and think.</p>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The map</span>Eleven topics</h2>
    <ul class="amap">
'''+maphtml+'''
    </ul>
    <h2 class="sec"><span class="n">The design</span>Before, during, and after</h2>
    <div class="stages" role="list">
      <div role="listitem"><b>Before</b><span>Plan short video segments, each around one idea. Build slides with a key visual and few words, and cut extras that don’t explain. Offer key readings in a printable form.</span></div>
      <div role="listitem"><b>During</b><span>Put questions inside videos and lectures. Set device norms, and use devices on purpose. Teach note-taking methods, not just a medium. Use in-person time for what only people in a room can do.</span></div>
      <div role="listitem"><b>After</b><span>Guide how students use recordings and speed controls: to review, spaced over time, with saved time spent on practice. Check outcomes, not just clicks and views.</span></div>
    </div>
  </div>

'''+cls_html('bT','Before, during or after?','Nine steps from the series. For each, decide where it belongs: before a unit, during it, or after it. You’ll get feedback after each one.',[('B','Before',''),('D','During',''),('A','After','')],'Before, during or after?','Before, during or after?','The question is always: when in the unit does this step do its work?')+'''
  <section class="night" aria-labelledby="pT">
    <div class="col">
      <h2 class="sec" id="pT"><span class="n">Try it</span>Plan one unit</h2>
      <p>Pick one change for before, one for during, and one for after your next online or recorded unit. Then look at what students actually did and learned.</p>
      <form class="plan" id="pForm">
        <fieldset><legend>Before</legend>
          <label><input type="radio" name="pb" value="Split each long video into segments of six minutes or less, one idea each." checked>Short segments, one idea each</label>
          <label><input type="radio" name="pb" value="Rebuild key slides: a few key words, one explanatory visual, and no decorative extras.">Lean slides with one strong visual</label>
          <label><input type="radio" name="pb" value="Offer a printable version of the key readings.">Printable key readings</label>
        </fieldset>
        <fieldset><legend>During</legend>
          <label><input type="radio" name="pd" value="Put one or two low-stakes questions between video segments and in live lectures, with quick feedback." checked>Questions inside videos and lectures</label>
          <label><input type="radio" name="pd" value="Set device norms on the first day: devices on purpose, a laptop section, accommodations protected.">Clear device norms</label>
          <label><input type="radio" name="pd" value="Teach note-taking: main ideas in students’ own words, sketches of key diagrams, and pauses to revise.">Teach note-taking</label>
        </fieldset>
        <fieldset><legend>After</legend>
          <label><input type="radio" name="pa" value="Tell students how to use recordings: weekly review, not a binge, and not a replacement for class." checked>Guidance on recordings</label>
          <label><input type="radio" name="pa" value="Tell students the evidence on playback speed: up to double is usually fine; spend saved time on practice.">Guidance on speed-watching</label>
          <label><input type="radio" name="pa" value="Check outcomes, not just clicks and views: what did students answer, and where did they struggle?">Check outcomes, not clicks</label>
        </fieldset>
        <div class="mrow"><button class="nbtn" type="submit">Make my plan</button><button class="nbtn ghost" type="button" id="pCopy" hidden>Copy the plan</button></div>
      </form>
      <div class="pout" id="pOut" hidden aria-live="polite"></div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Strong starting points</h2>
    <p>Many of these findings come from short lab studies, and some, like note-taking, are still debated. Treat them as strong starting points, then watch what happens in your own course.</p>
  </div>
'''+box('Pick one change for before, one for during, and one for after your next online or recorded unit. Then look at what students actually did and learned. Share this tip with students: one task, one screen, one goal per study session.'),
tips_h='The screen is just the window. What students do there is the lesson.',
tips='''      <li><b>Before</b><span>Short segments, lean slides, printable readings.</span></li>
      <li><b>During</b><span>Questions, device norms, note-taking.</span></li>
      <li><b>After</b><span>Recordings and speed, for review; check outcomes.</span></li>''',
sources='''        <li>The studies behind each step are listed on each topic’s page.</li>''',
quiz='''[
 {q:'The thread through this series is that…',o:['Attention and working memory are limited','Screens are always bad','Technology fixes learning'],a:0,f:'Good design protects them.'},
 {q:'After a unit, check…',o:['Outcomes, not just clicks and views','Only how many people watched','Nothing'],a:0,f:'Watching is not learning.'},
 {q:'Are all these findings settled?',o:['No: many are short lab studies, and some are debated','Yes, all of them','None are supported'],a:0,f:'Strong starting points.'}]''',
js=BASE+cls_js("{B:'Before',D:'During',A:'After'}",'''[
 ['Splitting a long lecture video into short segments','B','Before: segmenting is planned when you build the videos (topic 4).'],
 ['Cutting the decorative clip art from your slides','B','Before: coherence is built into the materials (topics 2 and 3).'],
 ['Making a printable version of the key reading','B','Before: so it’s ready when students need it (topic 9).'],
 ['Asking a quick question after each video segment','D','During: questions keep attention and build memory (topic 5).'],
 ['Running a poll on devices, then “lids down”','D','During: devices used on purpose (topic 8).'],
 ['Pausing so students can revise their notes','D','During: notes that select and rephrase (topic 7).'],
 ['Suggesting a weekly review of recordings, not a binge','A','After: recordings for review, spaced over time (topic 11).'],
 ['Telling students to spend time saved by speed-watching on practice','A','After: guidance on how to use saved time (topic 6).'],
 ['Looking at what students answered, not just how many views a video got','A','After: check outcomes, not clicks.']]''','Before, during or after?',r'''
 if(right>=8){title='You have the design';text=`${right} of 9 right. Before: segments, lean slides, readings. During: questions, devices, notes. After: recordings, speed, outcomes.`}
 else if(right>=5){title='Mostly there';text=`${right} of 9 right. You missed ${missed}. Ask when in the unit each step does its work.`}
 else{title='Worth another look';text=`${right} of 9 right. Before is building the materials; during is how class and videos run; after is guiding review and checking outcomes.`}''')+r'''
/* ---------- plan one unit ---------- */
let planTxt='';
$('pForm').addEventListener('submit',e=>{e.preventDefault();const v=n=>document.querySelector(`input[name="${n}"]:checked`).value;
 const st=[['Before',v('pb')],['During',v('pd')],['After',v('pa')]];
 planTxt='Screen design plan for my next unit\n'+st.map(([a,b],i)=>`${i+1}. ${a}: ${b}`).join('\n')+'\n4. Then: look at what students actually did and learned.';
 $('pOut').innerHTML='<b>Your plan</b><ol>'+st.map(([a,b])=>`<li><b>${a}:</b> ${b}</li>`).join('')+'<li><b>Then:</b> look at what students actually did and learned.</li></ol>';$('pOut').hidden=false;$('pCopy').hidden=false;$('pCopy').textContent='Copy the plan'});
$('pCopy').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(planTxt);$('pCopy').textContent='Copied'}catch(err){$('pCopy').textContent='Copy not available: select the text instead'}});
''')
open('d12/template.html','w').write(page(o))

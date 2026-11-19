import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('e','Assessment That Teaches',10,'Make the Task Transparent','Make the task transparent','Say why. Say what. Say how it will be judged. Then let students show what they can do.','Make the task transparent',
'An assignment says: write a ten-page paper on a topic of your choice. Some students know exactly what that means. Others have no idea what a good one looks like.',
'<span><a href="#aT">Make an assignment transparent</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['pfc'],{'pfc':([40,-60],'left')},'Drawing of the side of the brain with the prefrontal cortex, at the front, which plans and organizes work toward a goal, glowing orange and labelled.')
o.update(css=RECALL_CSS+'''
.plan fieldset{border:1px solid #3A4E72;border-radius:10px;padding:10px 14px;margin:0 0 12px}
.plan legend{font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#FCB316;padding:0 6px}
.plan label{display:block;color:#C9D3E3;font:600 14px var(--body);margin:0 0 8px}
.plan textarea,.plan input{display:block;width:100%;box-sizing:border-box;margin-top:4px;font:500 17px/1.45 var(--body);border-radius:8px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;padding:8px 10px}
.plan textarea{min-height:76px;resize:vertical}
.plan textarea:focus-visible,.plan input:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.pout{background:#fff;color:#13294B;border-radius:10px;padding:14px 16px;font-size:17px;line-height:1.5;margin:10px 0}
.pout[hidden]{display:none}
.pout .ptitle{font:800 19px var(--display);margin:0 0 6px;color:#13294B}
.pout p,.pout li{color:#13294B}
.pout ol,.pout ul{margin:4px 0 8px;padding-left:22px}
.pmiss{color:#FFB38A;font-weight:700;margin:6px 0 0}''',
body='''  <div class="col lede">
    <p>The Transparency in Learning and Teaching project, started by Mary-Ann Winkelmes at the University of Chicago and expanded at the University of Illinois, asks instructors to make three things explicit for each assignment: its purpose, the task, and the criteria for success.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>3 things</strong><span>purpose, task and criteria, made explicit</span></div>
      <div role="listitem"><strong>2 assignments</strong><span>made more transparent during one term</span></div>
      <div role="listitem"><strong>More</strong><span>academic confidence, belonging, and awareness of skills</span></div>
      <div role="listitem"><strong>Larger</strong><span>benefits for first-generation, low-income and underrepresented students</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The study</span>Just two assignments</h2>
    <p>In a national study published in 2016, instructors at minority-serving institutions made just two assignments more transparent during a term. Students in the more transparent courses reported greater academic confidence, a stronger sense of belonging, and more awareness of the skills they were building. The benefits were larger for first-generation, low-income and underrepresented students.</p>
    <h2 class="sec"><span class="n">Why</span>Decoding takes energy</h2>
    <p>Some students arrive knowing the unwritten rules of college assignments. Others spend their energy decoding the instructions instead of doing the work. Rubrics and examples are part of transparency: sharing what good work looks like, and why, helps students aim for it.</p>
    <h2 class="sec"><span class="n">A caution</span>Self-reported, not randomized</h2>
    <p>Many of the outcomes were self-reported, and the studies were not randomized trials. But the change is small, low cost, and consistent with the belonging research in the Belonging series.</p>
  </div>

  <section class="night" aria-labelledby="aT">
    <div class="col">
      <h2 class="sec" id="aT"><span class="n">Try it</span>Make an assignment transparent</h2>
      <p>Take an assignment you already set. Write its purpose, the steps, and the criteria, and the page puts them together as a handout. Nothing you enter leaves this page.</p>
      <form class="plan" id="aForm">
        <label for="aName">Assignment name<input id="aName" type="text" maxlength="80" placeholder="For example: Research paper"></label>
        <fieldset><legend>Purpose</legend>
          <label for="aP">In one or two sentences: what skills or knowledge will this build, and why does it matter beyond this course?<textarea id="aP" maxlength="400" placeholder="This assignment builds your ability to…"></textarea></label></fieldset>
        <fieldset><legend>Task</legend>
          <label for="aT1">The steps, one per line<textarea id="aT1" maxlength="600" placeholder="Choose a question…&#10;Find three sources…&#10;Draft an outline…"></textarea></label></fieldset>
        <fieldset><legend>Criteria</legend>
          <label for="aC">How the work will be judged, one criterion per line<textarea id="aC" maxlength="600" placeholder="A clear, arguable claim…&#10;Evidence from at least three sources…"></textarea></label>
          <label for="aE">Where students can see an annotated example (optional)<input id="aE" type="text" maxlength="120" placeholder="For example: the example on the course site, discussed in class"></label></fieldset>
        <div class="mrow"><button class="nbtn" type="submit">Make the handout</button><button class="nbtn ghost" type="button" id="aCopy" hidden>Copy the handout</button></div>
      </form>
      <p class="pmiss" id="aMiss" aria-live="polite"></p>
      <div class="pout" id="aOut" hidden></div>
    </div>
  </section>

'''+GRID_HTML+box('For your next assignment, write one sentence on its purpose, a short list of steps, and the criteria you will use. Share an annotated example. Discuss it in class before students begin. Share this tip with students: ask why this task matters, and what good looks like.'),
tips_h='Say why. Say what. Say how it will be judged. Then let students show what they can do.',
tips='''      <li><b>Purpose</b><span>Skills, knowledge, why it matters.</span></li>
      <li><b>Task</b><span>The steps, in order.</span></li>
      <li><b>Criteria</b><span>With an annotated example.</span></li>''',
sources='''        <li>Winkelmes, M.-A., Bernacki, M., Butler, J., Zochowski, M., Golanics, J., &amp; Weavil, K. H. (2016). A teaching intervention that increases underserved college students’ success. <i>Peer Review, 18</i>(1/2), 31–36.</li>''',
quiz='''[
 {q:'Transparent assignments make explicit…',o:['Purpose, task and criteria','Only the due date','Only the grade'],a:0,f:'The TILT framework.'},
 {q:'In the 2016 study, instructors made how many assignments more transparent?',o:['Two','Twenty','All of them'],a:0,f:'A small change.'},
 {q:'Benefits were larger for…',o:['First-generation, low-income and underrepresented students','Students who already knew the rules','No one in particular'],a:0,f:'Decoding takes energy.'}]''',
js=BASE+r'''
/* ---------- transparent assignment ---------- */
const esc=s=>s.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const lines=s=>s.split('\n').map(x=>x.trim()).filter(Boolean);
let aTxt='';
$('aForm').addEventListener('submit',e=>{e.preventDefault();const nm=$('aName').value.trim()||'Assignment',P=$('aP').value.trim(),T=lines($('aT1').value),C=lines($('aC').value),E=$('aE').value.trim();
 const miss=[!P&&'a purpose',!T.length&&'at least one step',!C.length&&'at least one criterion'].filter(Boolean);
 if(miss.length){$('aMiss').textContent='Add '+(miss.length>1?miss.slice(0,-1).join(', ')+' and '+miss[miss.length-1]:miss[0])+' first.';$('aOut').hidden=true;$('aCopy').hidden=true;return}
 $('aMiss').textContent=C.length<2?'Tip: most criteria lists have two to five items.':'';
 $('aOut').innerHTML=`<p class="ptitle">${esc(nm)}</p><p><b>Purpose.</b> ${esc(P)}</p><p><b>Task.</b></p><ol>${T.map(x=>`<li>${esc(x)}</li>`).join('')}</ol><p><b>Criteria for success.</b></p><ul>${C.map(x=>`<li>${esc(x)}</li>`).join('')}</ul>${E?`<p><b>See an example:</b> ${esc(E)}</p>`:''}`;
 aTxt=`${nm}\n\nPurpose. ${P}\n\nTask.\n${T.map((x,i)=>`${i+1}. ${x}`).join('\n')}\n\nCriteria for success.\n${C.map(x=>`- ${x}`).join('\n')}${E?`\n\nSee an example: ${E}`:''}`;
 $('aOut').hidden=false;$('aCopy').hidden=false;$('aCopy').textContent='Copy the handout'});
$('aCopy').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(aTxt);$('aCopy').textContent='Copied'}catch(err){$('aCopy').textContent='Copy not available: select the text instead'}});
'''+grid('''[
 ['TILT stands for…',['Transparency in Learning and Teaching','Testing in Large Teams','Teaching Is Long Term'],0,'Started by Mary-Ann Winkelmes.'],
 ['The 2016 national study was at…',['Minority-serving institutions','Elite private colleges','High schools'],0,'Published in 2016.'],
 ['Students in more transparent courses reported…',['More confidence, belonging and awareness of skills','Lower grades','More stress'],0,'Self-reported outcomes.'],
 ['Benefits were larger for…',['First-generation, low-income and underrepresented students','Senior students','No one'],0,'Unwritten rules matter.'],
 ['Were the studies randomized trials?',['No','Yes','Some were'],0,'A reason for caution.'],
 ['Rubrics and examples are…',['Part of transparency','A replacement for teaching','Unhelpful'],0,'Show what good work looks like.']]''','The pattern: making purpose, task and criteria explicit helps, most of all for students without the unwritten rules.'))
open('e10/template.html','w').write(page(o))

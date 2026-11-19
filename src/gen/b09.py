import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='b09',n='9',label='The Learning Brain · Belonging · Topic 9',epi='The Learning Brain, Belonging, episode 9',
title='Seeing Yourself: Same-Race Teachers and Long-Run Outcomes',h1='Seeing yourself',em='Students need to see a future self. Show them many.',read='7',mins='2 minutes',vtitle='Seeing yourself',
dek='Can seeing someone like you at the front of the room change where you end up? Tennessee’s STAR experiment made a rare fair test possible.',
jumps='<span><a href="#eT">Predict the long run</a></span><span><a href="#bT">Who do your students see?</a></span>',
hero_aria='Drawing of the side of the brain with the fusiform face area, on the underside, where faces are processed, and the prefrontal cortex, at the front, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.ffa.lab=[860,770];BR.R.ffa.al='right';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['ffa','pfc'],labels:['ffa','pfc'],labelT:{ffa:0.8,pfc:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS+'''
.qq{font:600 clamp(18px,2.2vw,21px)/1.45 var(--body);color:#fff;max-width:42ch;margin:0;text-align:center}
.jb{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}
.jb[hidden]{display:none}
.gfb{font:600 17px/1.45 var(--body);color:#E9EEF6;min-height:1.5em;margin:0;text-align:center;max-width:44ch}
.gfb b.ok{color:#7DD3A8}.gfb b.no{color:#FFB38A}''',
body='''  <div class="col lede">
    <p>It is a hard question to test, because students and teachers are rarely matched at random. But Tennessee’s STAR experiment, in the 1980s, randomly assigned young students and their teachers to classrooms, from kindergarten through third grade. Years later, that made a rare fair test possible.</p>
    <p>Economists Seth Gershenson, Cassandra Hart, Joshua Hyman, Constance Lindsay and Nicholas Papageorge followed up, and published the results in 2022.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>+13%</strong><span>more likely to graduate from high school (9 points), for Black students with at least one Black teacher in K–3</span></div>
      <div role="listitem"><strong>+19%</strong><span>more likely to enroll in college (6 points)</span></div>
      <div role="listitem"><strong>None</strong><span>no significant long-run effect for white students</span></div>
      <div role="listitem"><strong>Not visible</strong><span>in short-run test scores alone</span></div>
    </div>
  </div>

  <section class="night" aria-labelledby="eT">
    <div class="col">
      <h2 class="sec" id="eT"><span class="n">Try it</span>Predict the long run</h2>
      <p>Three quick predictions about the STAR follow-up, then the results. About 1 minute.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="eScreen">
          <p class="qq" id="eQ" aria-live="polite">Press Start.</p>
          <div class="jb" id="eB" hidden role="group" aria-label="Your prediction"></div>
          <p class="gfb" id="eFb" aria-live="polite"></p>
          <p class="prog" id="eProg" aria-live="polite"></p>
        </div>
        <div>
          <p class="phase" id="ePhase">Ready</p>
          <p class="mtitle" id="eTitle">Years later</p>
          <p class="mtext" id="eText" aria-live="polite">Black students randomly assigned at least one Black teacher in kindergarten to third grade, compared with Black schoolmates who were not.</p>
          <div id="eRes"></div>
          <div class="mrow"><button class="nbtn" id="eGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Where the gains were</span>Concentrated, and long-run</h2>
    <p>The gains were concentrated among disadvantaged Black boys, and the college gains came mostly from two-year colleges. Data from North Carolina showed a similar pattern. And these long-run effects were not visible in short-run test scores alone.</p>
    <p>The researchers suggest role-model effects. A teacher who shares your background can change your beliefs about what is possible for someone like you.</p>
  </div>

'''+cls_html('bT','Who do your students see?','Eight things a college instructor might do. For each, decide: does it widen who students see in the field, or not? You’ll get feedback after each one.',[('W','Widens it',''),('N','Doesn’t','')],'Widens who students see, or not?','Who do your students see?','The question is always: can more students see a future self here?')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Earliest grades, one group</h2>
    <p>This is about the earliest grades, and one group of students. And most instructors cannot change who they are. But you can change who your students see.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">For teaching</h3>
      <p>Invite speakers and alumni from varied backgrounds. Feature a range of people in your examples and readings. And connect students with mentors and peers they can identify with. Look beyond test scores when you judge whether it is working.</p>
    </aside>
  </div>
''',
tips_h='Students need to see a future self. Show them many.',
tips='''      <li><b>Varied speakers and alumni</b><span>Invite them in.</span></li>
      <li><b>A range of people</b><span>In examples and readings.</span></li>
      <li><b>Mentors and peers</b><span>Students can identify with.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1257/pol.20190573">Gershenson, S., Hart, C. M. D., Hyman, J., Lindsay, C. A., &amp; Papageorge, N. W. (2022). The long-run impacts of same-race teachers. <i>American Economic Journal: Economic Policy, 14</i>(4), 300–342.</a></li>''',
quiz='''[
 {q:'Black students with at least one Black teacher in K–3 were more likely to graduate from high school by…',o:['9 points (13%)','1 point','30 points'],a:0,f:'And 6 points (19%) more likely to enroll in college.'},
 {q:'For white students, the long-run effect was…',o:['Not significant either way','Large and positive','Large and negative'],a:0,f:'Gershenson and colleagues, 2022.'},
 {q:'Were these long-run effects visible in short-run test scores alone?',o:['No','Yes, clearly','Only in maths'],a:0,f:'Look beyond test scores.'}]''',
js=BASE+r'''
/* ---------- predict the long run ---------- */
const EQ=[
 ['Black students with at least one Black teacher in K–3: high school graduation?',['About the same','Somewhat more likely','Much less likely'],1,'Somewhat more likely: 9 percentage points, or 13%.'],
 ['And for white students with a Black teacher?',['Large benefit','No significant long-run effect','Large harm'],1,'No significant long-run effect, either way.'],
 ['Were the effects visible in short-run test scores?',['Yes, clearly','Not on their own','Only in reading'],1,'Not on their own: the long-run pattern only showed up later.']];
let er=null;
function eChoose(opts){return new Promise(res=>{er.res=res;const b=$('eB');b.innerHTML=opts.map((t,j)=>`<button class="nbtn${j?' ghost':''}" type="button" data-v="${j}">${t}</button>`).join('');b.hidden=false;b.querySelector('button').focus()})}
$('eB').addEventListener('click',e=>{const b=e.target.closest('button');if(!b||!er||!er.res)return;const r=er.res;er.res=null;$('eB').hidden=true;r(+b.dataset.v)});
function eNext(label){return new Promise(res=>{const g=$('eGo');g.textContent=label;g.disabled=false;g.focus();g.onclick=()=>{g.onclick=null;g.disabled=true;g.textContent='In progress';res()}})}
$('eGo').addEventListener('click',async()=>{if(er||$('eGo').onclick)return;er={};const g=$('eGo');g.disabled=true;g.textContent='In progress';$('eRes').innerHTML='';
 const got=[];$('ePhase').textContent='Predict';$('eTitle').textContent='Your prediction';
 for(let i=0;i<3;i++){const [q,o,a,ex]=EQ[i];$('eProg').textContent=`Prediction ${i+1} of 3`;$('eQ').textContent=q;$('eFb').textContent='';
  const c=await eChoose(o);if(!er)return;got.push(c===a);$('eFb').innerHTML=(c===a?'<b class="ok">Right.</b> ':'<b class="no">Not quite.</b> ')+ex;
  if(i<2){await eNext('Next prediction');if(!er)return}}
 $('eQ').textContent='Done.';$('eProg').textContent='';$('ePhase').textContent='The results';
 $('eRes').innerHTML=`<div class="res wl2"><p class="gh">Black students with at least one Black teacher in K–3</p>${barRow('High school graduation',13,25,'+13% (9 points)','#7DD3A8')}${barRow('College enrollment',19,25,'+19% (6 points)','#7DD3A8')}<p class="gh">White students with a Black teacher</p>${barRow('Long-run effect',0.3,25,'not significant','#C9D3E3')}</div>`;
 const n=got.filter(Boolean).length;let title,text;
 if(n===3){title='You read it right';text='All 3. A teacher who shares your background can change beliefs about what is possible, and the effect showed up years later, not in test scores alone.'}
 else if(!got[2]){title='Look beyond test scores';text=`You got ${n} of 3. The long-run gains were not visible in short-run test scores alone. Judging only by test scores would have missed them.`}
 else if(!got[0]){title='A real long-run gain';text=`You got ${n} of 3. Black students with at least one Black teacher were 13% more likely to graduate, and 19% more likely to enroll in college.`}
 else{title='No harm for white students';text=`You got ${n} of 3. There was no significant long-run effect, either way, for white students.`}
 $('eTitle').textContent=title;$('eText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();er=null});
'''+cls_js("{W:'Widens it',N:'Doesn’t'}",'''[
 ['Inviting alumni from varied backgrounds to talk about their paths','W','Widens it: students meet future selves.'],
 ['Using only the field’s most famous historical figures as examples','N','Doesn’t: it tends to show a narrow group, from long ago.'],
 ['Pairing first-year students with peer mentors they can identify with','W','Widens it: a near-peer is a believable model.'],
 ['Assigning readings by authors from a range of backgrounds','W','Widens it: who writes the field is part of who does it.'],
 ['Telling students that background doesn’t matter, so role models don’t either','N','Doesn’t: in the study, whom students saw made a lasting difference.'],
 ['Sharing short profiles of current researchers, including how they got started','W','Widens it: especially when the paths are varied and honest.'],
 ['Judging a mentoring program only by next term’s test scores','N','Doesn’t help you see it: the long-run effects were not visible in short-run scores.'],
 ['Connecting students with professional societies for groups underrepresented in the field','W','Widens it: a community students can see themselves in.']]''','Widens who students see, or not?',r'''
 if(right>=7){title='You can widen the view';text=`${right} of 8 right. You can’t change who you are, but you can change who your students see.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Ask: does it help more students see a future self?`}
 else{title='Worth another look';text=`${right} of 8 right. Speakers, mentors, readings and profiles from varied backgrounds widen the view. Narrow examples, and judging by short-run scores alone, don’t.`}'''))
open('b09/template.html','w').write(page(o))

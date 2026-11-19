import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='h07',n='7',label='The Learning Brain · Habits of the Learner · Topic 7',epi='The Learning Brain, Habits of the Learner, episode 7',
title='Phones and Attention: What Really Costs You',h1='Phones and attention',em='Guard your attention; it is where learning happens',read='7',mins='2 minutes',vtitle='Phones and attention',
dek='Your phone may be the most powerful distraction ever built to fit in a pocket. The clearest costs come from checking, switching and alerts, not from the phone just sitting there.',
jumps='<span><a href="#sT">Press, except for 3</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, and the parietal lobe, at the top, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[60,730];BR.R.pfc.al='left';BR.R.par.lab=[560,-70];BR.R.par.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc','par'],labels:['pfc','par'],labelT:{pfc:0.8,par:1.0},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.qq{font:600 clamp(18px,2.2vw,21px)/1.45 var(--body);color:#fff;max-width:42ch;margin:0;text-align:center}
.dig{font:800 88px/1 var(--body);color:#fff;min-height:96px;margin:0;text-align:center}
.tap{min-width:200px;min-height:64px;font-size:20px}
.tap[hidden]{display:none}
.notif{position:absolute;left:50%;top:10px;transform:translateX(-50%);width:min(320px,86%);background:#F2F4F8;color:#13294B;border-radius:14px;padding:10px 14px;box-shadow:0 6px 20px rgba(0,0,0,.4);font:500 15px/1.35 var(--body);text-align:left}
.notif b{display:block;font:700 13px var(--body);color:#3A4E72}
.notif[hidden]{display:none}
#sScreen{position:relative}''',
body='''  <div class="col lede">
    <p>In a simulated lecture, reported by Faria Sana, Tina Weston and Nicholas Cepeda in 2013, students who multitasked on a laptop scored 11% lower on a comprehension test. Students who simply sat where they could see a multitasking classmate scored 17% lower, and most did not think they were distracted. Sana said that gap could turn a B+ into a B−.</p>
    <p>Notifications cost you too. At Florida State University, Cary Stothart and colleagues had 166 students do an attention task while the researchers secretly called or texted the students’ own phones. Those who got a notification made more mistakes, even without checking it.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>11%</strong><span>lower comprehension for students who multitasked on a laptop</span></div>
      <div role="listitem"><strong>17%</strong><span>lower for students who could see a multitasking classmate</span></div>
      <div role="listitem"><strong>166</strong><span>students whose own phones were called or texted mid-task</span></div>
      <div role="listitem"><strong>Not found again</strong><span>the idea that a phone just sitting on the desk drains your brain</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Alerts</span>As costly as using the phone</h2>
    <p>The cost of a notification was comparable to the cost of actually using a phone for a call or a text. You don’t have to pick it up to lose some of your attention.</p>
    <h2 class="sec"><span class="n">Mere presence</span>A finding that didn’t hold</h2>
    <p>You may have heard that just having your phone on the desk drains your brain. A 2017 study by Adrian Ward and colleagues reported that. But a pre-registered direct replication did not find the effect, and a study by Matthias Hartmann at the University of Bern and colleagues found no evidence for it either. So the clearer lesson is about use and interruptions, not mere presence: the real costs come from checking, switching between tasks, and alerts.</p>
  </div>

  <section class="night" aria-labelledby="sT">
    <div class="col">
      <h2 class="sec" id="sT"><span class="n">Try it</span>Press, except for 3</h2>
      <p>A short version of the kind of attention task used in the notification study. Digits appear one at a time. Press the button (or the space bar) for every digit except 3. Two rounds of about a minute: one quiet, one with pretend phone notifications on the screen. Ignore them. This task needs sight and quick responses.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="sScreen">
          <div class="notif" id="sN" hidden aria-hidden="true"><b id="sNa">Messages · now</b><span id="sNt"></span></div>
          <p class="qq" id="sQ" aria-live="polite">Press Start.</p>
          <p class="dig" id="sD" aria-hidden="true"></p>
          <button class="nbtn tap" id="sTap" type="button" hidden>Press</button>
          <p class="prog" id="sProg" aria-live="polite"></p>
        </div>
        <div>
          <p class="phase" id="sPhase">Ready</p>
          <p class="mtitle" id="sTitle">Quiet, then interrupted</p>
          <p class="mtext" id="sText" aria-live="polite">Press for every digit except 3. Go for accuracy.</p>
          <div id="sRes"></div>
          <div class="mrow"><button class="nbtn" id="sGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Lab tasks, but the same direction</h2>
    <p>The laptop studies used simulated lectures, and the notification study used a simple lab task. But they point the same way, and the fix costs nothing.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Try this</h3>
      <p>Turn notifications off while you study. Close extra tabs and apps. In class, sit where you can’t see other people’s screens. And check your phone in planned breaks, not whenever it buzzes.</p>
    </aside>
  </div>
''',
tips_h='Guard your attention. It is where learning happens.',
tips='''      <li><b>Notifications off</b><span>While you study.</span></li>
      <li><b>Sit away from screens</b><span>Other people’s multitasking costs you too.</span></li>
      <li><b>Planned breaks</b><span>Check your phone then, not whenever it buzzes.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1016/j.compedu.2012.10.003">Sana, F., Weston, T., &amp; Cepeda, N. J. (2013). Laptop multitasking hinders classroom learning for both users and nearby peers. <i>Computers &amp; Education, 62</i>, 24–31.</a></li>
        <li><a href="https://doi.org/10.1037/xhp0000100">Stothart, C., Mitchum, A., &amp; Yehnert, C. (2015). The attentional cost of receiving a cell phone notification. <i>Journal of Experimental Psychology: Human Perception and Performance, 41</i>(4), 893–897.</a></li>
        <li><a href="https://doi.org/10.1016/j.actpsy.2022.103717">Ruiz Pardo, A. C., &amp; Minda, J. P. (2022). Reexamining the “brain drain” effect: A replication of Ward et al. (2017). <i>Acta Psychologica, 230</i>, 103717.</a></li>
        <li><a href="https://sonar.unidistance.ch/documents/322142/files/Hartmann%202020_Smartphone_Accepted%20manuscript%20version.pdf">Hartmann, M., Martarelli, C. S., Reber, T. P., &amp; Rothen, N. (2020). Does a smartphone on the desk drain our brain? No evidence of cognitive costs due to smartphone presence in a short-term and prospective memory task. <i>Consciousness and Cognition</i>.</a></li>''',
quiz='''[
 {q:'Students who could see a classmate multitasking on a laptop scored…',o:['17% lower','About the same','Higher'],a:0,f:'And most didn’t think they were distracted.'},
 {q:'Getting a phone notification during a task, without checking it…',o:['Still led to more mistakes','Had no effect','Improved focus'],a:0,f:'Comparable to actually using the phone.'},
 {q:'A phone just sitting on the desk draining your brain…',o:['Was not found again in replications','Is firmly established','Doubles your errors'],a:0,f:'The clearer costs come from use and interruptions.'}]''',
js=BASE+r'''
/* ---------- press, except for 3 ----------
   2 blocks x 45 digits (1 s each: 250 ms digit, then blank). About 1 in 9 digits is a 3.
   Block 2 shows 3 fake notification banners (2.5 s each) at random times. Errors: pressed on 3 (commission), missed a non-3 (omission). */
const NT=['Sam: are you coming tonight??','Group chat: 12 new messages','Mum: call me when you can','Instagram: someone liked your post','Alex: did you do the reading?'];
let sr=null;
const swt=ms=>new Promise(r=>{sr.tm=setTimeout(r,ms)});
function seq(){const a=[];for(let i=0;i<45;i++)a.push(i%9===4?3:[1,2,4,5,6,7,8,9][Math.floor(Math.random()*8)]);return shuf(a)}
function press(){if(!sr||!sr.on)return;if(sr.pressed)return;sr.pressed=true;$('sTap').classList.add('ghost');setTimeout(()=>$('sTap').classList.remove('ghost'),120)}
$('sTap').addEventListener('click',press);
document.addEventListener('keydown',e=>{if(sr&&sr.on&&(e.code==='Space'||e.key===' ')){e.preventDefault();press()}});
async function block(notify){const s=seq();let com=0,om=0,n3=0;const nt=notify?shuf([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]).slice(0,3):[];const msg=shuf([...NT]);
 for(let i=0;i<45;i++){if(!sr)return null;
  if(nt.includes(i)){$('sNt').textContent=msg.pop();$('sN').hidden=false;sr.nh=setTimeout(()=>{$('sN').hidden=true},2500)}
  sr.pressed=false;sr.on=true;$('sD').textContent=s[i];await swt(250);if(!sr)return null;$('sD').textContent='';await swt(750);if(!sr)return null;sr.on=false;
  if(s[i]===3){n3++;if(sr.pressed)com++}else if(!sr.pressed)om++;
  $('sProg').textContent=`${i+1} of 45`}
 $('sN').hidden=true;return{com,om,n3}}
$('sGo').addEventListener('click',async()=>{if(sr)return;sr={};const g=$('sGo');g.disabled=true;g.textContent='In progress';$('sRes').innerHTML='';
 const R=[];
 for(let b=0;b<2;b++){
  $('sPhase').textContent=b?'Round 2: with notifications':'Round 1: quiet';$('sTitle').textContent=b?'Ignore the banners':'Just the digits';$('sText').textContent='Press for every digit except 3.';
  $('sQ').textContent=b?'Round 2 starts in 3 seconds. Ignore any notifications.':'Round 1 starts in 3 seconds.';$('sD').textContent='';$('sTap').hidden=false;$('sTap').focus();await swt(3000);if(!sr)return;$('sQ').textContent='Press for every digit except 3.';
  const r=await block(b===1);if(!r)return;R.push(r)}
 $('sTap').hidden=true;$('sD').textContent='';$('sQ').textContent='Done.';$('sProg').textContent='';$('sPhase').textContent='Your results';
 const [a,b]=R,ea=a.com+a.om,eb=b.com+b.om;
 $('sRes').innerHTML=`<div class="res wl2"><p class="gh">Mistakes (out of 45)</p>${barRow('Quiet',ea,Math.max(6,ea,eb),ea+(ea===1?' mistake':' mistakes'),'#7DD3A8')}${barRow('Notifications',eb,Math.max(6,ea,eb),eb+(eb===1?' mistake':' mistakes'),'#FFB38A')}</div><p class="mtext">Pressed on a 3: ${a.com} of ${a.n3} quiet, ${b.com} of ${b.n3} with notifications. Missed another digit: ${a.om} quiet, ${b.om} with notifications.</p>`;
 let title,text;
 if(a.om>=30&&b.om>=30){title='Did you press?';text='Almost every digit went by without a press. Press the button or the space bar for every digit except 3, then try again.'}
 else if(eb>ea){title='The banners cost you';text=`${eb} mistakes with notifications, against ${ea} without, even though you didn’t touch a phone. In the study, notifications alone caused errors comparable to using the phone.`}
 else if(eb===ea&&ea===0){title='Flawless both times';text='No mistakes in either round. In the real study, the notifications came from people’s own phones, which pull much harder than a pretend banner. Turn alerts off anyway: the cost is real, even when you don’t feel it.'}
 else if(eb===ea){title='No difference this time';text=`${ea} mistakes in each round. A pretend banner pulls less than your own phone, and two short rounds leave a lot to chance. In the study, real notifications did cost attention.`}
 else{title='Better with notifications, this time';text=`${eb} mistakes with notifications, against ${ea} without. Practice from round 1 probably helped, and pretend banners pull less than your own phone. In the study, real notifications did cost attention.`}
 $('sTitle').textContent=title;$('sText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();sr=null});
'''+grid('''[
 ['Students who multitasked on a laptop in a simulated lecture scored…',['11% lower','About the same','11% higher'],0,'Sana, Weston and Cepeda, 2013.'],
 ['Students who could only see a multitasking classmate scored…',['17% lower','About the same','A little higher'],0,'Most didn’t think they were distracted.'],
 ['Getting a call or text during a task, without checking it…',['Led to more mistakes','Made no difference','Helped focus'],0,'Stothart and colleagues, 2015.'],
 ['Did the students know the researchers were sending the notifications?',['No','Yes','Only some'],0,'The calls and texts came to their own phones, unannounced.'],
 ['The cost of a notification was…',['Comparable to actually using the phone','Tiny','Larger than using the phone'],0,'You don’t have to pick it up.'],
 ['A phone simply sitting on the desk reducing your brainpower…',['Was not found again in replications','Was confirmed many times','Has never been tested'],0,'The clearer lesson is about use and interruptions.']]''','The pattern: attention is lost to checking, switching and alerts, yours and other people’s. Mere presence matters less than once claimed.'))
import json as _j;o['vnote']=_j.load(open('gen/vnotes.json'))['h07']
open('h07/template.html','w').write(page(o))

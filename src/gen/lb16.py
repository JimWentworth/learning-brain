import sys;sys.path.insert(0,'gen')
from common import page
o=dict(id='lb16',n='16',title='Social Learning: Learning from Each Other',h1='Social learning',em='Learning from each other',read='8',mins='3 minutes',vtitle='Social learning',
dek='People learn by watching, but watching is not passive: learners must attend, remember, be able to reproduce, and have a reason to. Worked examples, observed tutoring, peer discussion and the expectation of teaching all put this to work.',
jumps='<span><a href="#bT">Why didn’t they learn it?</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with two areas glowing orange and labelled: the frontal lobe, whose premotor region holds cells that respond both to doing and to watching an action, and the parietal lobe.',
hero_js="BR.R.fro.lab=[40,-60];BR.R.fro.al='left';BR.R.par.lab=[1000,770];BR.R.par.al='right';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['fro','par'],labels:['fro','par'],labelT:{fro:0.8,par:1.0},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css='''.bscen{font:600 clamp(19px,2.4vw,22px)/1.45 var(--body);color:#fff;max-width:40ch;min-height:5.8em;margin:0}
.bopts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;width:100%;max-width:480px}
.bopts[hidden]{display:none}
.bopts button{min-height:52px;border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;font:700 17px/1.2 var(--body);cursor:pointer;padding:4px 8px}
.bopts button small{display:block;font-size:13px;color:#C9D3E3;font-weight:600}
.bopts button:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.bopts button.ok{border-color:#7DD3A8;background:#173B33}.bopts button.no{border-color:#FFB38A;background:#3B2420}
.bopts button:disabled{cursor:default}
.bfb{font-size:18px;line-height:1.45;color:#E9EEF6;margin:0;min-height:3em;max-width:44ch}
.bfb b.ok{color:#7DD3A8}.bfb b.no{color:#FFB38A}
.res.wl2 .row{grid-template-columns:150px minmax(0,1fr) 90px}
@media (max-width:520px){.res.wl2 .row{grid-template-columns:110px minmax(0,1fr) 70px}}''',
body='''  <div class="col lede">
    <p>In 1961, preschool children watched an adult attack an inflatable Bobo doll: punching it, sitting on it, striking it with a mallet. Later, alone with the doll, many of them copied those exact, unusual actions. Nobody had rewarded them. They learned just by watching.</p>
    <p>Albert Bandura argued that watching is not passive. The learner has to attend to the model, retain what they saw, be able to reproduce it, and have a reason to. If any one of these fails, the learning doesn’t show up.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>4 steps</strong><span>attend, retain, reproduce, and have a reason to</span></div>
      <div role="listitem"><strong>92 of 532</strong><span>cells recorded in monkey premotor cortex, about 17%, responded to both doing and watching</span></div>
      <div role="listitem"><strong>Pairs</strong><span>of students watching tutoring videos learned as much as the students being tutored</span></div>
      <div role="listitem"><strong>“You’ll teach this”</strong><span>was enough to improve recall, though nobody actually taught</span></div>
    </div>
  </div>

  <section class="night" aria-labelledby="bT">
    <div class="col">
      <h2 class="sec" id="bT"><span class="n">Try it</span>Why didn’t they learn it?</h2>
      <p>Eight short cases where watching didn’t lead to learning. For each, decide which of Bandura’s four steps broke down. About 3 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="bScreen">
          <p class="bscen" id="bScen" aria-live="polite">Press Start.</p>
          <div class="bopts" id="bOpts" hidden role="group" aria-label="Which step broke down?"><button type="button" data-k="A">Attention<small>didn’t take it in</small></button><button type="button" data-k="R">Retention<small>didn’t keep it</small></button><button type="button" data-k="P">Reproduction<small>can’t do it yet</small></button><button type="button" data-k="M">Motivation<small>no reason to</small></button></div>
          <p class="prog" id="bProg" aria-live="polite"></p>
        </div>
        <div>
          <p class="phase" id="bPhase">Ready</p>
          <p class="mtitle" id="bTitle">Diagnose the breakdown</p>
          <p class="bfb" id="bFb" aria-live="polite">Each case has one main breakdown. You’ll get feedback after each answer.</p>
          <div id="bRes"></div>
          <div class="mrow"><button class="nbtn" id="bGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">The brain</span>Mirror neurons, and a caution</h2>
    <p>In the 1990s, Giacomo Rizzolatti’s group, recording single cells in the premotor cortex of macaque monkeys, found neurons that fired both when the monkey grasped an object and when it watched someone else do so. They called them mirror neurons. In the most detailed early study, by Vittorio Gallese and colleagues in 1996, they were 92 of the 532 cells recorded, about 17%.</p>
    <p>Claims that mirror neurons explain empathy, language or human learning went far beyond the data. Most human evidence comes from brain imaging, not single cells, and whether these cells are needed to understand actions is contested. The behavioural finding stands on its own: people learn by watching.</p>
    <h2 class="sec"><span class="n">The classroom</span>Watching, discussing, teaching</h2>
    <p>For novices, studying worked examples beats solving the same problems unaided, as <a href="@@LB:lb06@@">the working memory page</a> explains. As skill grows, the advantage fades and practice should take over.</p>
    <p>Watching expert help can work too. In 2008, Michelene Chi, Marguerite Roy and Robert Hausmann found that students who watched videos of physics tutoring in pairs, talking it through, learned to solve problems as well as the students being tutored. Peers matter as well. In 2009, Michelle Smith and colleagues had genetics students answer a clicker question, discuss it with neighbours, then answer a new question on the same concept alone. Scores improved, even in groups where no one had known the answer at first. And in 2014, John Nestojko and colleagues found that learners told they would teach a passage recalled more of it, and organized it better, than learners expecting a test. Nobody actually taught.</p>
  </div>

  <section aria-labelledby="brT" style="margin:24px 0 40px">
    <div class="col">
      <h2 class="sec" id="brT"><span class="n">Try it</span>Predict the findings</h2>
      <p>For each comparison from the research, predict what was found. Then check.</p>
    </div>
    <div class="wide">
      <form class="pgrid" id="pGrid"></form>
      <div class="qrow"><button class="pbtn" id="pCheck" type="button">Check my predictions</button><button class="pbtn" id="pReset" type="button" hidden>Try again</button></div>
      <p class="pmsg" id="pSum" aria-live="polite"></p>
    </div>
  </section>

  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Let students see how experts think</h3>
      <p>Show worked examples early, then fade them as students gain skill. Think aloud: make your reasoning visible, including the dead ends. Use peer discussion before you reveal the answer. And give students reasons to explain to someone else.</p>
    </aside>
  </div>
''',
tips_h='We are built to learn from each other',
tips='''      <li><b>Worked examples, then fade</b><span>Examples for novices; practice as skill grows.</span></li>
      <li><b>Think aloud</b><span>Show your reasoning, dead ends included.</span></li>
      <li><b>Discuss, then reveal</b><span>And give students reasons to explain.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1037/h0045925">Bandura, A., Ross, D., &amp; Ross, S. A. (1961). Transmission of aggression through imitation of aggressive models. <i>Journal of Abnormal and Social Psychology</i>.</a></li>
        <li><a href="https://pages.ucsd.edu/~jpineda/COGS260Mirroring/readings/Gallese%20et%20al.%20-%20action%20recognition%20in%20the%20premotor%20cortex.pdf">Gallese, V., Fadiga, L., Fogassi, L., &amp; Rizzolatti, G. (1996). Action recognition in the premotor cortex. <i>Brain</i>.</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3898692">Review table of mirror-neuron proportions (Gallese et al.: 92 of 532, 17.3%).</a></li>
        <li><a href="https://api.crossref.org/works/10.1080%2F03640210701863396">Chi, M. T. H., Roy, M., &amp; Hausmann, R. G. M. (2008). Observing tutorial dialogues collaboratively. <i>Cognitive Science</i>.</a></li>
        <li><a href="https://serc.carleton.edu/resources/40584.html">Smith, M. K., et al. (2009). Why peer discussion improves student performance on in-class concept questions. <i>Science</i>.</a></li>
        <li><a href="https://profiles.wustl.edu/en/publications/expecting-to-teach-enhances-learning-and-organization-of-knowledg/">Nestojko, J. F., Bui, D. C., Kornell, N., &amp; Bjork, E. L. (2014). Expecting to teach enhances learning and organization of knowledge in free recall of text passages. <i>Memory &amp; Cognition</i>.</a></li>''',
quiz='''[
 {q:'A student watched a clear demonstration but has forgotten the steps by the time they try. Which step failed?',o:['Retention','Attention','Motivation'],a:0,f:'They took it in, but didn’t keep it.'},
 {q:'What did students learn from watching tutoring videos in pairs?',o:['As much as the students being tutored','Nothing useful','Less than students studying alone'],a:0,f:'Talking it through while watching made the difference.'},
 {q:'Why be cautious about mirror-neuron claims?',o:['Broad claims about empathy and language went far beyond the data','Mirror neurons were never found','They are found only in humans'],a:0,f:'The behavioural finding, that people learn by watching, stands on its own.'}]''',
js=r'''
const shuf=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
/* ---------- why didn't they learn it? ----------
   8 cases, 2 per step, random order. Pick one of four steps; feedback after each. Score, and which steps were confused. */
const NM={A:'Attention',R:'Retention',P:'Reproduction',M:'Motivation'};
const CASES=[
 ['A student watches the teacher solve a problem on the board while texting under the desk.','A','Attention: the demonstration never got in. The student was looking elsewhere.'],
 ['A new employee watches a software demo, but the presenter’s screen is too small to read from the back of the room.','A','Attention: the key details couldn’t be seen, so they couldn’t be learned.'],
 ['A trainee watches a 12-step lab procedure once. A week later, they can’t remember the order of the steps.','R','Retention: they saw it, but didn’t keep it. Notes, practice or a checklist would help.'],
 ['Students follow a worked example in class and understand it, but take no notes. Two weeks later, they can’t recall the method.','R','Retention: understanding at the time isn’t the same as remembering later.'],
 ['A child watches a gymnast’s back flip closely and can describe every step, but can’t do one yet.','P','Reproduction: knowing what to do isn’t the same as being able to do it. That takes practice.'],
 ['A beginner watches a pianist play a passage slowly and remembers the fingering, but their hands can’t move that fast yet.','P','Reproduction: the skill is in memory but not yet in the hands.'],
 ['A student knows exactly how a classmate asks good questions, but in this class questions are ignored, so they don’t bother.','M','Motivation: they could do it, but see no reason to.'],
 ['In a later Bandura study, children who saw the model punished copied less, until they were offered a reward for showing what they had seen.','M','Motivation: they had learned the actions all along. The reward revealed it.']];
let br=null;
function bAnswer(){return new Promise(res=>{br.res=res;const o=$('bOpts');o.hidden=false;o.querySelectorAll('button').forEach(b=>{b.disabled=false;b.classList.remove('ok','no')});o.querySelector('button').focus()})}
$('bOpts').addEventListener('click',e=>{const b=e.target.closest('button');if(!b||!br||!br.res)return;const r=br.res;br.res=null;r(b.dataset.k)});
function bWait(label){return new Promise(res=>{const g=$('bGo');g.textContent=label;g.disabled=false;g.focus();g.onclick=()=>{g.onclick=null;g.disabled=true;g.textContent='In progress';res()}})}
$('bGo').addEventListener('click',async()=>{if(br||$('bGo').onclick)return;br={};const g=$('bGo');g.disabled=true;g.textContent='In progress';$('bRes').innerHTML='';
 const order=shuf([...CASES]);let right=0;const miss={A:0,R:0,P:0,M:0};
 $('bTitle').textContent='Which step broke down?';
 for(let i=0;i<order.length;i++){const [txt,k,ex]=order[i];$('bPhase').textContent=`Case ${i+1} of ${order.length}`;$('bScen').textContent=txt;$('bProg').textContent='';$('bFb').textContent='';
  const a=await bAnswer();if(!br)return;const ok=a===k;if(ok)right++;else miss[k]++;
  $('bOpts').querySelectorAll('button').forEach(b=>{b.disabled=true;if(b.dataset.k===k)b.classList.add('ok');else if(b.dataset.k===a)b.classList.add('no')});
  $('bFb').innerHTML=(ok?'<b class="ok">Right.</b> ':`<b class="no">Not quite.</b> You chose ${NM[a]}. `)+ex;$('bProg').textContent=`${right} of ${i+1} right so far.`;
  if(i<order.length-1){await bWait('Next case');if(!br)return}}
 $('bOpts').hidden=true;$('bScen').textContent='Done.';$('bProg').textContent='';$('bPhase').textContent='Your results';
 const row=(k)=>`<div class="row"><span>${NM[k]}</span><div class="bar"><i style="width:${(2-miss[k])/2*100}%;background:#FCB316"></i></div><b>${2-miss[k]} of 2</b></div>`;
 $('bRes').innerHTML=`<div class="res wl2">${['A','R','P','M'].map(row).join('')}</div>`;
 const weak=Object.keys(miss).filter(k=>miss[k]>0).map(k=>NM[k]);
 let title,text;
 if(right>=7){title='You can diagnose the breakdown';text=`${right} of 8 right. When watching doesn’t lead to learning, ask which step failed: the fix for a student who wasn’t looking is different from the fix for one who can’t do it yet.`}
 else if(right>=4){title='Mostly there';text=`${right} of 8 right. You missed some ${weak.join(', ')} cases. A tip: if the learner could describe what they saw, attention and retention worked, so look at reproduction or motivation.`}
 else{title='Worth another look';text=`${right} of 8 right. Try asking two questions in order: did they take it in and keep it? If yes, can they physically or mentally do it, and do they have a reason to?`}
 $('bTitle').textContent=title;$('bFb').textContent=text;g.onclick=null;g.textContent='Try again';g.disabled=false;g.focus();br=null});

/* ---------- predict the findings ---------- */
const PI=[
 ['Preschoolers who had watched an adult attack a Bobo doll, later alone with it, with no reward',['Many copied the exact actions','Few did anything unusual','They avoided the doll'],0,'They learned just by watching.'],
 ['Share of recorded premotor cells that responded to both doing and watching, in the 1996 study',['About 17%','Nearly all','Under 1%'],0,'92 of 532 cells.'],
 ['Novices studying worked examples, compared with solving the same problems unaided',['Learned more','Learned less','No difference'],0,'The worked example effect. It fades as skill grows.'],
 ['Pairs of students watching tutoring videos and talking it through, compared with the students being tutored',['Learned about as much','Learned much less','Learned more'],0,'Students watching alone learned less.'],
 ['Students who discussed a clicker question, then answered a new question on the same concept alone',['Did better, even if no one in the group knew the answer at first','Did better only if someone already knew','Did no better'],0,'Discussion built understanding, not just copying.'],
 ['Learners told they would teach a passage, compared with learners expecting a test',['Recalled more, and better organized','Recalled less, from stress','No difference'],0,'Nobody actually taught; expecting to was enough.']];
const NP=PI.length;
$('pGrid').innerHTML=PI.map(([q,o],i)=>`<div class="prow"><p class="it" id="pq${i}">${i+1}. ${q}</p><fieldset aria-labelledby="pq${i}"><legend>${q}</legend>${shuf(o.map((t,j)=>[t,j])).map(([t,j])=>`<label><input type="radio" name="p${i}" value="${j}">${t}</label>`).join('')}</fieldset><p class="ex" id="px${i}" hidden></p></div>`).join('');
$('pCheck').addEventListener('click',()=>{let right=0,ans=0;PI.forEach(([q,o,a,ex],i)=>{const sel=document.querySelector(`input[name="p${i}"]:checked`);let lead;
  if(!sel)lead=`<b class="no">Not answered.</b> ${o[a]}. `;else{ans++;const ok=+sel.value===a;if(ok)right++;lead=ok?`<b>Right.</b> `:`<b class="no">Not quite.</b> ${o[a]}. `}
  const x=$('px'+i);x.innerHTML=lead+ex;x.hidden=false});
 document.querySelectorAll('#pGrid input').forEach(n=>n.disabled=true);
 $('pSum').textContent=(ans===0?'You didn’t make any predictions, so here are the answers. ':`You got ${right} of ${ans} prediction${ans>1?'s':''} right${ans<NP?` (${NP-ans} left blank)`:''}. `)+'The pattern: people learn a great deal from watching and talking with others, especially when they are active while they do it.';
 $('pCheck').hidden=true;$('pReset').hidden=false;$('pReset').focus()});
$('pReset').addEventListener('click',()=>{document.querySelectorAll('#pGrid input').forEach(n=>{n.disabled=false;n.checked=false});document.querySelectorAll('#pGrid .ex').forEach(x=>{x.hidden=true;x.innerHTML=''});$('pSum').textContent='';$('pReset').hidden=true;$('pCheck').hidden=false;document.querySelector('#pGrid input').focus()});
''')
open('lb16/template.html','w').write(page(o))

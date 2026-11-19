import sys;sys.path.insert(0,'gen')
from common import page
o=dict(id='lb18',n='18',title='Transfer: Same Idea, New Clothes',h1='Transfer',em='Same idea, new clothes',read='8',mins='2½ minutes',vtitle='Transfer',
dek='Using what you learned in a new situation is the point of learning, and it often fails. The knowledge is there; what fails is noticing that it applies. Comparing examples that differ on the surface but share a deep structure helps people notice.',
jumps='<span><a href="#tT">The tumour problem</a></span><span><a href="#dT">Spot the deep structure</a></span>',
hero_aria='Drawing of the side of the brain with two areas glowing orange and labelled: the prefrontal cortex, which helps map one situation onto another, and the hippocampus, which retrieves the earlier example.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.hip.lab=[700,740];BR.R.hip.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc','hip'],labels:['pfc','hip'],labelT:{pfc:0.8,hip:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css='''.tstory{font:500 clamp(18px,2.2vw,20px)/1.55 var(--body);color:#fff;max-width:46ch;margin:0}
.tstory b{color:#FCB316}
.topts{display:grid;gap:8px;width:100%;max-width:480px}
.topts[hidden]{display:none}
.topts button{min-height:48px;border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;font:700 17px/1.3 var(--body);cursor:pointer;text-align:left;padding:8px 14px}
.topts button:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.tin{display:flex;flex-direction:column;gap:10px;align-items:center;width:100%}
.tin[hidden]{display:none}
.tin textarea{width:100%;max-width:460px;min-height:110px;padding:10px 12px;font:600 18px/1.4 var(--body);border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;resize:vertical}
.tin textarea:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.tknew{display:flex;gap:8px;align-items:center;color:#E9EEF6;font-size:16px;min-height:36px}
.dl{display:grid;gap:12px}
.dl .prow fieldset{display:flex;gap:10px;flex-wrap:wrap}''',
body='''  <div class="col lede">
    <p>A doctor must destroy a tumour with rays. A ray strong enough to kill the tumour will also destroy the healthy tissue around it. How?</p>
    <p>In 1980, Mary Gick and Keith Holyoak gave people this classic puzzle, first posed by Karl Duncker, after they had read a story with the same solution. Most didn’t use the story. Told that it might help, about three in four solved the problem. That is transfer: using what you learned in a new situation. The knowledge was there. What failed was noticing that it applied.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>~75%</strong><span>solved the tumour problem once told the earlier story might help</span></div>
      <div role="listitem"><strong>11,430</strong><span>adults in a six-week brain-training study: no gains on untrained tasks</span></div>
      <div role="listitem"><strong>57</strong><span>experiments in a 2013 review of learning by comparing cases</span></div>
      <div role="listitem"><strong>d = 0.50</strong><span>average benefit of case comparison in that review</span></div>
    </div>
  </div>

  <section class="night" aria-labelledby="tT">
    <div class="col">
      <h2 class="sec" id="tT"><span class="n">Try it</span>The tumour problem</h2>
      <p>First, a short reading task: two brief stories, each with a quick question. Then a puzzle. About 4 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="tScreen" style="align-items:stretch">
          <p class="tstory" id="tStory" aria-live="polite">Press Start.</p>
          <div class="topts" id="tOpts" hidden role="group" aria-label="Choose an answer"></div>
          <form class="tin" id="tForm" hidden><label class="sr-only" for="tIn">Your solution</label><textarea id="tIn" placeholder="Describe your solution in a sentence or two"></textarea><button class="nbtn" type="submit">Done</button></form>
          <p class="prog" id="tProg" aria-live="polite"></p>
        </div>
        <div>
          <p class="phase" id="tPhase">Ready</p>
          <p class="mtitle" id="tTitle">Will you notice?</p>
          <p class="mtext" id="tText" aria-live="polite">Read carefully. There’s no time limit.</p>
          <label class="tknew"><input type="checkbox" id="tKnew"> I already know the tumour puzzle</label>
          <div id="tRes"></div>
          <div class="mrow"><button class="nbtn" id="tGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Near and far</span>Why brain training disappoints</h2>
    <p>Students meet the same idea in new clothing and don’t recognise it. Near transfer, to similar situations, is common. Far transfer, to very different ones, is rare and hard won. That is also why brain training disappoints. In 2010, Adrian Owen and colleagues ran a six-week online study with 11,430 adults. People improved on every task they practised, but showed no gains on untrained tasks, even closely related ones. Practice makes you better at what you practise.</p>
    <h2 class="sec"><span class="n">What helps</span>Compare, then name the principle</h2>
    <p>What helps is comparison. When people read two analogous stories and described what they had in common, they were much more likely to solve a new problem: they had built a general pattern, not just a memory of one story. In 2013, Louis Alfieri, Timothy Nokes-Malach and Christian Schunn pooled 57 experiments. Comparing cases reliably improved learning, especially when learners looked for similarities and were then given the principle.</p>
  </div>

  <section aria-labelledby="dT" style="margin:24px 0 40px">
    <div class="col">
      <h2 class="sec" id="dT"><span class="n">Try it</span>Spot the deep structure</h2>
      <p>Six short cases. Which ones share the deep structure of the fortress story, whatever they look like on the surface?</p>
    </div>
    <div class="wide">
      <form class="pgrid dl" id="dGrid"></form>
      <div class="qrow"><button class="pbtn" id="dCheck" type="button">Check my answers</button><button class="pbtn" id="dReset" type="button" hidden>Try again</button></div>
      <p class="pmsg" id="dSum" aria-live="polite"></p>
    </div>
  </section>

  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Same structure, different surfaces</h3>
      <p>Teach with two or more examples that differ on the surface but share the deep structure. Ask students what the examples have in common, and name the principle after they compare. Mix problem types, so students must recognise which idea applies. And tell them plainly: this idea will show up again, in places that look different.</p>
    </aside>
  </div>
''',
tips_h='The brain learns what it does',
tips='''      <li><b>Two examples, one principle</b><span>Different surfaces, same deep structure.</span></li>
      <li><b>Compare, then name it</b><span>Ask what they share, then give the principle.</span></li>
      <li><b>Mix problem types</b><span>So students must recognise which idea applies.</span></li>''',
sources='''        <li><a href="https://deepblue.lib.umich.edu/handle/2027.42/23210">Gick, M. L., &amp; Holyoak, K. J. (1980). Analogical problem solving. <i>Cognitive Psychology</i>.</a></li>
        <li><a href="https://link.springer.com/content/pdf/10.3758/BF03197035.pdf">Holyoak, K. J., &amp; Koh, K. (1987). Surface and structural similarity in analogical transfer. <i>Memory &amp; Cognition</i>. (About 75% with a hint.)</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC2884087">Owen, A. M., et al. (2010). Putting brain training to the test. <i>Nature</i>.</a></li>
        <li><a href="https://www.lrdc.pitt.edu/Schunn/papers/ContrastingCasesMeta-AlfieriEtAl2013.pdf">Alfieri, L., Nokes-Malach, T. J., &amp; Schunn, C. D. (2013). Learning through case comparisons: A meta-analytic review. <i>Educational Psychologist</i>.</a></li>''',
quiz='''[
 {q:'In the tumour study, what was usually missing when people failed to solve it?',o:['Noticing that the earlier story applied','Knowing the earlier story','Intelligence'],a:0,f:'Told the story might help, about three in four solved it.'},
 {q:'What did the six-week brain-training study find?',o:['Gains on practised tasks, none on untrained ones','Gains on everything','No gains at all'],a:0,f:'Practice makes you better at what you practise.'},
 {q:'What helps transfer most?',o:['Comparing examples that share a deep structure, then naming the principle','Studying one example very thoroughly','Practising the exact same problem'],a:0,f:'Comparison builds a general pattern.'}]''',
js=r'''
const shuf=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
/* ---------- the tumour problem ----------
   Reading task: a distractor story and the fortress story (random order), each with one comprehension question.
   Then the tumour problem: free answer, then the reader classifies it. Convergence = solved.
   If not solved: hint ("one of the stories may help"), second answer, classify again.
   Branches: known puzzle / solved without hint / solved after hint / not solved. */
const STORIES=[
 ['fort','A small country was ruled from a strong fortress by a dictator. Many roads led to the fortress from every side, like spokes on a wheel. A general planned to capture it, but the roads were mined so that small groups could pass safely, while any large army would set off the mines. So the general divided his army into small groups and sent one down each road. At a signal, they all arrived together, and the full force captured the fortress.','Why did the general split his army?',['Because a large group on one road would set off the mines','Because he had too few soldiers','To surprise the enemy from behind'],0],
 ['dist','A town’s only bakery was so popular that the queue every morning stretched around the block. The baker tried opening earlier, but the queue simply started earlier too. Finally, she started taking orders the night before, so customers could collect their bread at a set time. The queue disappeared, and she sold more bread than ever.','What finally made the queue disappear?',['Taking orders the night before','Opening earlier','Hiring more staff'],0]];
const PROB='A patient has a tumour deep inside the body. It is impossible to operate, but the tumour can be destroyed by a type of ray. At high strength, the ray destroys the tumour, but it also destroys the healthy tissue it passes through on the way. At low strength, the ray is harmless to healthy tissue but doesn’t affect the tumour either. How could the rays be used to destroy the tumour without destroying the healthy tissue?';
const KINDS=[['C','Several weak rays from different directions, meeting at the tumour'],['P','Send the ray along an existing path, such as a natural opening, to avoid tissue'],['O','Expose or move the tumour, or protect the healthy tissue in some way'],['N','Something else, or I didn’t find a solution']];
let tr=null;
function choose(opts){return new Promise(res=>{const box=$('tOpts');box.innerHTML=opts.map((t,i)=>`<button type="button" data-i="${i}">${t}</button>`).join('');box.hidden=false;box.querySelector('button').focus();
 box.onclick=e=>{const b=e.target.closest('button');if(!b||!tr)return;box.onclick=null;box.hidden=true;res(+b.dataset.i)}})}
function write(){return new Promise(res=>{tr.res=res;$('tForm').hidden=false;$('tIn').value='';$('tIn').focus()})}
$('tForm').addEventListener('submit',e=>{e.preventDefault();if(!tr||!tr.res)return;const r=tr.res;tr.res=null;$('tForm').hidden=true;r($('tIn').value)});
function tWait(label){return new Promise(res=>{const g=$('tGo');g.textContent=label;g.disabled=false;g.focus();g.onclick=()=>{g.onclick=null;g.disabled=true;g.textContent='In progress';res()}})}
async function attempt(label){$('tStory').textContent=PROB;$('tProg').textContent=label;$('tTitle').textContent='The puzzle';$('tText').textContent='Write your best idea. Then you’ll say which kind of solution it was.';
 const txt=await write();if(!tr)return null;
 $('tStory').innerHTML=`<b>Your answer:</b> ${(txt.trim()||'(blank)').replace(/</g,'&lt;').slice(0,400)}`;$('tTitle').textContent='Which kind was it?';$('tText').textContent='Choose the description that best matches what you wrote.';
 const k=await choose(KINDS.map(x=>x[1]));if(!tr)return null;return KINDS[k][0]}
$('tGo').addEventListener('click',async()=>{if(tr||$('tGo').onclick)return;tr={};const g=$('tGo');g.disabled=true;g.textContent='In progress';$('tRes').innerHTML='';const knew=$('tKnew').checked;$('tKnew').disabled=true;
 const st=shuf([...STORIES]);
 for(let i=0;i<2;i++){const [id,txt,q,opts,a]=st[i];$('tPhase').textContent=`Reading ${i+1} of 2`;$('tTitle').textContent='Read the story';$('tText').textContent='Then answer the question.';$('tStory').textContent=txt;$('tProg').textContent='';
  await tWait('I’ve read it');if(!tr)return;$('tStory').textContent=q;const ord=shuf([0,1,2]);const c=await choose(ord.map(k=>opts[k]));if(!tr)return;
  $('tProg').textContent=ord[c]===a?'Right.':`The answer: ${opts[a].toLowerCase()}.`}
 $('tPhase').textContent='The puzzle';let k1=await attempt('First try');if(!k1)return;let k2=null;
 if(k1!=='C'){$('tStory').textContent='A hint: one of the stories you just read may help.';$('tTitle').textContent='A hint';$('tText').textContent='Think back to the two stories, then try again.';$('tProg').textContent='';
  await tWait('Try again');if(!tr)return;k2=await attempt('Second try, after the hint');if(!k2)return}
 $('tPhase').textContent='Your result';
 $('tStory').innerHTML='<b>The convergence solution:</b> aim several weak rays at the tumour from different directions, so they meet there. Each ray is harmless on its way through healthy tissue; together, at the tumour, they are strong enough to destroy it. Just like the general’s small groups on many roads.';
 let title,text;
 if(knew){title='You knew this one';text=k1==='C'?'You solved it, but you already knew the puzzle, so it can’t show spontaneous transfer. Try it on someone else, after telling them the fortress story among others.':'You knew the puzzle but didn’t pick the convergence answer. The solution is above.'}
 else if(k1==='C'){title='You noticed the analogy';text='You solved it on the first try. In the 1980 study, most people who read the fortress story still didn’t use it until told it might help. Did you think of the story, or find the idea another way?'}
 else if(k2==='C'){title='The knowledge was there';text='You solved it once told a story might help, as about three in four people did in the classic study. The fortress story was in your memory all along. What failed was noticing that it applied, which is the usual problem with transfer.'}
 else{title='The story didn’t come to mind';text=k1==='P'||k1==='O'||k2==='P'||k2==='O'?'Your idea is a natural first thought, but it doesn’t get round the problem: surgery is ruled out, and any path to the tumour still runs through healthy tissue. The solution is above. Notice how the general’s problem and the doctor’s problem share a structure, many weak forces converging, under different surfaces.':'The solution is above. Notice how the general’s problem and the doctor’s problem share a structure, many weak forces converging, under different surfaces.'}
 $('tTitle').textContent=title;$('tText').textContent=text;$('tProg').textContent='';$('tKnew').disabled=false;g.textContent='Try again';g.disabled=false;g.focus();tr=null});

/* ---------- spot the deep structure ---------- */
const DI=[
 ['A fire is too hot to approach with one big hose, so firefighters aim many small hoses at it from all sides at once.',1,'Many small forces from different directions, combining at one point: the same structure, in a new setting.'],
 ['A general takes a fortress by surrounding it and cutting off its supplies until it surrenders.',0,'Military surface, different structure: a siege, not converging forces.'],
 ['A doctor treats an infection with one strong dose of antibiotic.',0,'Medical surface, different structure: one strong treatment, no convergence.'],
 ['A stage designer lights an actor with several dim lamps from different angles, so the bright spot doesn’t dazzle the audience.',1,'Weak sources that add up at a single spot: convergence.'],
 ['A radiosurgery machine aims many weak beams of radiation so they cross at one point in the brain.',1,'This is the tumour solution, used in real medicine.'],
 ['A cook adds salt a little at a time, tasting as she goes, so the soup isn’t too salty.',0,'Small steps over time, but nothing converging on a target: a different structure.']];
$('dGrid').innerHTML=DI.map(([q],i)=>`<div class="prow"><p class="it" id="dq${i}">${i+1}. ${q}</p><fieldset aria-labelledby="dq${i}"><legend>${q}</legend><label><input type="radio" name="d${i}" value="1">Same deep structure</label><label><input type="radio" name="d${i}" value="0">Different structure</label></fieldset><p class="ex" id="dx${i}" hidden></p></div>`).join('');
$('dCheck').addEventListener('click',()=>{let right=0,ans=0,surf=0;DI.forEach(([q,a,ex],i)=>{const sel=document.querySelector(`input[name="d${i}"]:checked`);let lead;
  if(!sel)lead=`<b class="no">Not answered.</b> ${a?'Same deep structure':'Different structure'}. `;else{ans++;const ok=+sel.value===a;if(ok)right++;else if(i===1||i===2)surf++;lead=ok?`<b>Right.</b> `:`<b class="no">Not quite.</b> ${a?'Same deep structure':'Different structure'}. `}
  const x=$('dx'+i);x.innerHTML=lead+ex;x.hidden=false});
 document.querySelectorAll('#dGrid input').forEach(n=>n.disabled=true);
 const base=ans===0?'You didn’t answer any, so here are the answers. ':`You got ${right} of ${ans} right${ans<DI.length?` (${DI.length-ans} left blank)`:''}. `;
 const tail=surf?'You were caught by surface similarity: a military or medical setting doesn’t mean the same structure.':right===DI.length?'You looked past the surface to the structure, which is exactly what transfer needs.':'Look for the structure: many weak forces converging on one target.';
 $('dSum').textContent=base+tail;
 $('dCheck').hidden=true;$('dReset').hidden=false;$('dReset').focus()});
$('dReset').addEventListener('click',()=>{document.querySelectorAll('#dGrid input').forEach(n=>{n.disabled=false;n.checked=false});document.querySelectorAll('#dGrid .ex').forEach(x=>{x.hidden=true;x.innerHTML=''});$('dSum').textContent='';$('dReset').hidden=true;$('dCheck').hidden=false;document.querySelector('#dGrid input').focus()});
''')
open('lb18/template.html','w').write(page(o))

import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='m01',n='1',label='The Learning Brain · Memory · Topic 1',epi='The Learning Brain, Memory, episode 1',
title='The Life of a Memory: Encode, Consolidate, Retrieve',h1='The life of a memory',em='Encode, consolidate, retrieve',read='8',mins='2½ minutes',vtitle='The life of a memory',
dek='A memory has to be taken in, made to last, and found again. It can fail at any of the three stages, and each failure looks different and needs a different fix.',
jumps='<span><a href="#cT">Stored but out of reach</a></span><span><a href="#bT">Which stage failed?</a></span>',
hero_aria='Drawing of the side of the brain with the hippocampus, deep inside, and the prefrontal cortex, at the front, glowing orange and labelled. The hippocampus helps bind new memories; the prefrontal cortex helps steer what is taken in and search for it later.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.hip.lab=[640,770];BR.R.hip.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['hip','pfc'],labels:['hip','pfc'],labelT:{hip:0.8,pfc:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.fw .cat{font-size:15px}
.cues{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;max-width:460px}
.cues[hidden]{display:none}
.cues span{border:1px solid #8FA3C2;border-radius:999px;padding:4px 12px;color:#fff;font:700 16px var(--body)}
.bscen{font:600 clamp(19px,2.4vw,22px)/1.45 var(--body);color:#fff;max-width:40ch;min-height:5.8em;margin:0}
.bopts{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;width:100%;max-width:520px}
@media (max-width:520px){.bopts{grid-template-columns:1fr}}
.bopts[hidden]{display:none}
.bopts button{min-height:52px;border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;font:700 17px/1.2 var(--body);cursor:pointer;padding:4px 8px}
.bopts button small{display:block;font-size:13px;color:#C9D3E3;font-weight:600}
.bopts button:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.bopts button.ok{border-color:#7DD3A8;background:#173B33}.bopts button.no{border-color:#FFB38A;background:#3B2420}
.bopts button:disabled{cursor:default}
.bfb{font-size:18px;line-height:1.45;color:#E9EEF6;margin:0;min-height:3em;max-width:44ch}
.bfb b.ok{color:#7DD3A8}.bfb b.no{color:#FFB38A}''',
body='''  <div class="col lede">
    <p>Picture a US penny. You have handled thousands. Which way does Lincoln face? What words are above his head? In a 1979 study by Raymond Nickerson and Marilyn Adams, most people could not pick the real penny out of 15 drawings.</p>
    <p>Seeing something thousands of times is not the same as storing it. This series follows the life of a single memory, and this page starts with its three stages.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>15</strong><span>penny drawings; most people couldn’t pick the real one</span></div>
      <div role="listitem"><strong>3</strong><span>stages: encode, consolidate, retrieve</span></div>
      <div role="listitem"><strong>58%</strong><span>of the learning effort Ebbinghaus saved after 20 minutes; about a fifth after a month</span></div>
      <div role="listitem"><strong>Cues</strong><span>brought back words that free recall missed: stored, but out of reach</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Three stages</span>Taken in, made to last, found again</h2>
    <p>First a memory is <b>encoded</b>: taken in and given a form. Then it is <b>consolidated</b>: stabilized so that it lasts. Finally it is <b>retrieved</b>: found again when it is needed. A memory can fail at any of the three, and each failure looks different.</p>
    <p>The penny is an encoding failure. Nobody needs those details to spend a coin, so they were never really taken in. Repetition alone didn’t do it. What gets stored depends on what the learner does with the material, not on how often it passes in front of them.</p>
    <p>In the brain, the <a href="@@LB:hippocampus@@">hippocampus</a> helps bind the parts of a new experience into a memory. The prefrontal cortex helps steer what gets processed and search for it later. In a 1998 brain-scanning study, Anthony Wagner and colleagues found that stronger activity in left prefrontal and temporal regions while people judged a word predicted whether they would remember it later.</p>
  </div>

  <section class="night" aria-labelledby="cT">
    <div class="col">
      <h2 class="sec" id="cT"><span class="n">Try it</span>Stored, but out of reach</h2>
      <p>Study 24 words from six categories, take a 30-second break, and type all the words you remember. Then you’ll see the category names and get a second chance. About 2½ minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="cScreen">
'''+recall_screen('c')+'''
          <div class="cues" id="cCues" hidden aria-label="Category names"></div>
'''+tail('c')+'''
        </div>
        <div>
          <p class="phase" id="cPhase">Ready</p>
          <p class="mtitle" id="cTitle">Can a cue find what you couldn’t?</p>
          <p class="mtext" id="cText" aria-live="polite">Each word appears for 2 seconds with its category above it. Just read each one and try to remember it.</p>
          <div id="cRes"></div>
          <div class="mrow"><button class="nbtn" id="cGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Consolidate</span>Most of the loss comes early</h2>
    <p>Consolidation failure looks different. In the 1880s, Hermann Ebbinghaus learned lists of nonsense syllables, then measured how much faster he could relearn them later. After 20 minutes, he saved 58% of the original effort. After a day, about a third. After a month, about a fifth. Most of the loss came early, while the memory was still new. A 2015 replication by Jaap Murre and Joeri Dros found a very similar curve.</p>
    <h2 class="sec"><span class="n">Retrieve</span>Stored the whole time</h2>
    <p>Retrieval failure looks different again. In a 1966 experiment by Endel Tulving and Zena Pearlstone, people studied word lists sorted into categories. Asked to recall freely, they missed many words. Given the category names as cues, they recalled far more. Most of the gain came from whole categories they had missed. The words were stored all along; they just couldn’t be reached without a way in.</p>
    <h2 class="sec"><span class="n">One caution</span>A model, not three boxes</h2>
    <p>The three stages are a model, not three separate boxes. Retrieving a memory also changes it, and encoding builds on what is already stored. The stages overlap, and later topics in this series show where.</p>
  </div>

  <section aria-labelledby="bT" class="night">
    <div class="col">
      <h2 class="sec" id="bT"><span class="n">Try it</span>Which stage failed?</h2>
      <p>Nine short cases. For each, decide which stage broke down: encoding, consolidation or retrieval. You’ll get feedback after each one.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="bScreen">
          <p class="bscen" id="bScen" aria-live="polite">Press Start.</p>
          <div class="bopts" id="bOpts" hidden role="group" aria-label="Which stage failed?"><button type="button" data-k="E">Encode<small>never really taken in</small></button><button type="button" data-k="C">Consolidate<small>faded before it set</small></button><button type="button" data-k="R">Retrieve<small>stored, but out of reach</small></button></div>
          <p class="prog" id="bProg" aria-live="polite"></p>
        </div>
        <div>
          <p class="phase" id="bPhase">Ready</p>
          <p class="mtitle" id="bTitle">Diagnose the failure</p>
          <p class="bfb" id="bFb" aria-live="polite">Each case has one main failure.</p>
          <div id="bRes"></div>
          <div class="mrow"><button class="nbtn" id="bGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">“I studied, but I couldn’t remember”</h3>
      <p>When a student says this, ask which stage failed. Did they really work with the material the first time? Did they come back to it within days, or let it fade? Or do they know it, but can’t find it without the right cue? Each problem has a different fix: deeper work at the start, <a href="@@LB:lb11@@">spaced return visits</a>, or <a href="@@LB:lb10@@">practice at retrieving</a> with fewer and fewer cues.</p>
    </aside>
  </div>
''',
tips_h='Ask which stage failed',
tips='''      <li><b>Encode</b><span>Make students do something with the material, not just see it.</span></li>
      <li><b>Consolidate</b><span>Come back to it within days, before it fades.</span></li>
      <li><b>Retrieve</b><span>Practise finding it, with fewer cues each time.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1016/0010-0285(79)90013-6">Nickerson, R. S., &amp; Adams, M. J. (1979). Long-term memory for a common object. <i>Cognitive Psychology</i>.</a></li>
        <li><a href="https://doi.org/10.1371/journal.pone.0120644">Murre, J. M. J., &amp; Dros, J. (2015). Replication and analysis of Ebbinghaus’ forgetting curve. <i>PLOS ONE</i>.</a></li>
        <li><a href="https://doi.org/10.1016/S0022-5371(66)80048-8">Tulving, E., &amp; Pearlstone, Z. (1966). Availability versus accessibility of information in memory for words. <i>Journal of Verbal Learning and Verbal Behavior</i>.</a></li>
        <li><a href="https://www.nmr.mgh.harvard.edu/publications/journal_articles/3493">Wagner, A. D., et al. (1998). Building memories: Remembering and forgetting of verbal experiences as predicted by brain activity. <i>Science</i>.</a></li>''',
quiz='''[
 {q:'Most people can’t pick the real penny from 15 drawings. Which stage failed?',o:['Encoding: the details were never really taken in','Consolidation','Retrieval'],a:0,f:'Seeing something often is not the same as storing it.'},
 {q:'When did Ebbinghaus lose most of what he had learned?',o:['Early, while the memory was new','Evenly over the month','Only after a month'],a:0,f:'He saved 58% after 20 minutes, about a third after a day, about a fifth after a month.'},
 {q:'Category names brought back words people couldn’t recall freely. What does that show?',o:['The words were stored but out of reach','The cues taught them new words','The words had been forgotten'],a:0,f:'A retrieval failure: available, but not accessible.'}]''',
js=BASE+recall_kit('c','cr')+r'''
/* ---------- stored, but out of reach ----------
   24 words, 6 categories of 4, studied by category (2 s each, category shown). 30 s break. Free recall.
   Then category names as cues, second recall. Count free, added with cues, categories reached. */
const CATS=[['Animals',['tiger','rabbit','camel','otter']],['Fruits',['mango','cherry','lemon','grape']],['Tools',['hammer','wrench','chisel','drill']],['Clothing',['scarf','jacket','glove','sandal']],['Vehicles',['tractor','canoe','scooter','wagon']],['Instruments',['violin','trumpet','banjo','flute']]];
let cr=null;
$('cGo').addEventListener('click',async()=>{if(cr)return;cr={};const g=$('cGo');g.disabled=true;g.textContent='In progress';$('cRes').innerHTML='';$('cCues').hidden=true;
 const order=shuf(CATS.map(([c,w])=>[c,shuf([...w])]));const items=[];order.forEach(([c,w])=>w.forEach(x=>items.push({w:x,c,f:false,q:false})));
 $('cPhase').textContent='Step 1 of 4 · Study';$('cTitle').textContent='Read each word';
 for(let i=0;i<items.length;i++){const it=items[i];$('cW').innerHTML=`<small>${it.c}</small>${it.w}`;$('cProg').textContent=`Word ${i+1} of 24`;if(!await cHold(2))return}
 $('cW').textContent='';$('cPhase').textContent='Step 2 of 4 · Break';$('cTitle').textContent='Step away';$('cText').textContent='An easy, 30-second task.';await cBreak();if(!cr)return;
 $('cPhase').textContent='Step 3 of 4 · Recall';$('cTitle').textContent='Recall, no help';$('cText').textContent='Type every word you remember, in any order.';$('cW').textContent='Which words?';
 let v=await cRecall();if(!cr)return;toks(v).forEach(t=>items.forEach(it=>{if(match(t,it.w))it.f=true}));
 $('cPhase').textContent='Step 4 of 4 · Recall with cues';$('cTitle').textContent='Recall, with the categories';$('cText').textContent='Here are the six categories. Type any more words you can now find. It’s fine to leave it blank.';$('cW').textContent='The categories';
 $('cCues').innerHTML=CATS.map(([c])=>`<span>${c}</span>`).join('');$('cCues').hidden=false;
 v=await cRecall('Type any more words you remember');if(!cr)return;toks(v).forEach(t=>items.forEach(it=>{if(!it.f&&match(t,it.w))it.q=true}));
 $('cCues').hidden=true;$('cW').textContent='Done';$('cPhase').textContent='Your results';
 const F=items.filter(x=>x.f).length,Q=items.filter(x=>x.q).length,T=F+Q;
 const catF=CATS.filter(([c])=>items.some(x=>x.c===c&&x.f)).length,catT=CATS.filter(([c])=>items.some(x=>x.c===c&&(x.f||x.q))).length;
 const newCat=CATS.filter(([c])=>!items.some(x=>x.c===c&&x.f)&&items.some(x=>x.c===c&&x.q)).length;
 $('cRes').innerHTML=`<div class="res wl2"><p class="gh">Words, out of 24</p>${barRow('No help',F,24,F+' of 24','#C9D3E3')}${barRow('With categories',T,24,T+' of 24','#FCB316')}<p class="gh">Categories reached, out of 6</p>${barRow('No help',catF,6,catF+' of 6','#C9D3E3')}${barRow('With categories',catT,6,catT+' of 6','#FCB316')}</div>`;
 const wd=n=>n===1?'1 word':n+' words';let title,text;
 if(T<3){title='Too few words to compare';text=`You recalled ${wd(T)} in all, too few to see what the cues did. The break may have pushed them out. Try again, and say each word to yourself as it appears.`}
 else if(F>=21){title='You found nearly everything without help';text=`You recalled ${F} of 24 with no help, so the cues had little left to find${Q?` (they added ${wd(Q)})`:''}. With longer lists or a longer wait, people miss more, and cues make a bigger difference.`}
 else if(Q>=2){title='Stored, but out of reach';text=`With no help you recalled ${wd(F)}. Given the category names, you found ${Q} more. They were stored all along; you just couldn’t reach them. That is a retrieval failure, and the fix is a better cue, not more study.`+(newCat?` ${newCat===1?'One category':newCat+' categories'} came back only with the cue: once you had the category, its words followed. Tulving and Pearlstone found the same.`:'')}
 else{title='The cues added little';text=`With no help you recalled ${wd(F)}; the category names added ${Q===0?'none':'just 1'}. The words you missed may never have been encoded well in 2 seconds each, or you had already searched each category on your own${catF===6?' (you reached all six)':''}. In the 1966 study, cues helped most when lists were long.`}
 $('cTitle').textContent=title;$('cText').textContent=text;$('cProg').textContent='';g.textContent='Try again';g.disabled=false;g.focus();cr=null});

/* ---------- which stage failed? ---------- */
const NM={E:'Encode',C:'Consolidate',R:'Retrieve'};
const CASES=[
 ['Asked to draw the logo of an app she opens every day, a student gets the colours wrong and leaves out half of it.','E','Encode: seeing it every day didn’t store the details. She never needed them, so she never really took them in.'],
 ['A student “reads” a chapter while chatting with friends. Ten minutes later, he can’t say what it was about.','E','Encode: his attention was elsewhere, so the chapter barely got in.'],
 ['In a lecture, a student copies every slide word for word. As soon as class ends, she can’t answer a simple question about them.','E','Encode: copying kept her attention on the words, not the meaning.'],
 ['A student understands a method well at the end of Monday’s class and can do the problems. She doesn’t look at it again, and by next week it’s gone.','C','Consolidate: it got in, but faded before it set. A return visit within days would help.'],
 ['After cramming all night, a student does well on the morning exam. A month later he remembers almost nothing.','C','Consolidate: one late-night session got it in for the morning, but it wasn’t made to last.'],
 ['A new employee learns 20 colleagues’ names on her first day and can use them all by evening. After a week away, most are gone.','C','Consolidate: the names were taken in, then faded without use.'],
 ['On a test, a student blanks on a term. Walking out of the room, it comes to her.','R','Retrieve: it was stored the whole time, but she couldn’t reach it under pressure.'],
 ['A student can’t name the three long bones of the arm, but when shown a list of bones, picks out all three.','R','Retrieve: he knew them; recognizing them was easier than recalling them.'],
 ['A student uses the right formula when a problem says “find the area”, but not when the problem only describes a field to be fenced.','R','Retrieve: she knows it, but the problem didn’t give her the cue she learned it with.']];
let br=null;
function bAnswer(){return new Promise(res=>{br.res=res;const o=$('bOpts');o.hidden=false;o.querySelectorAll('button').forEach(b=>{b.disabled=false;b.classList.remove('ok','no')});o.querySelector('button').focus()})}
$('bOpts').addEventListener('click',e=>{const b=e.target.closest('button');if(!b||!br||!br.res)return;const r=br.res;br.res=null;r(b.dataset.k)});
function bWait(label){return new Promise(res=>{const g=$('bGo');g.textContent=label;g.disabled=false;g.focus();g.onclick=()=>{g.onclick=null;g.disabled=true;g.textContent='In progress';res()}})}
$('bGo').addEventListener('click',async()=>{if(br||$('bGo').onclick)return;br={};const g=$('bGo');g.disabled=true;g.textContent='In progress';$('bRes').innerHTML='';
 const order=shuf([...CASES]);let right=0;const miss={E:0,C:0,R:0};
 $('bTitle').textContent='Which stage failed?';
 for(let i=0;i<order.length;i++){const [txt,k,ex]=order[i];$('bPhase').textContent=`Case ${i+1} of ${order.length}`;$('bScen').textContent=txt;$('bProg').textContent='';$('bFb').textContent='';
  const a=await bAnswer();if(!br)return;const ok=a===k;if(ok)right++;else miss[k]++;
  $('bOpts').querySelectorAll('button').forEach(b=>{b.disabled=true;if(b.dataset.k===k)b.classList.add('ok');else if(b.dataset.k===a)b.classList.add('no')});
  $('bFb').innerHTML=(ok?'<b class="ok">Right.</b> ':`<b class="no">Not quite.</b> You chose ${NM[a]}. `)+ex;$('bProg').textContent=`${right} of ${i+1} right so far.`;
  if(i<order.length-1){await bWait('Next case');if(!br)return}}
 $('bOpts').hidden=true;$('bScen').textContent='Done.';$('bProg').textContent='';$('bPhase').textContent='Your results';
 $('bRes').innerHTML=`<div class="res wl2">${['E','C','R'].map(k=>barRow(NM[k],3-miss[k],3,(3-miss[k])+' of 3','#FCB316')).join('')}</div>`;
 const weak=Object.keys(miss).filter(k=>miss[k]>0).map(k=>NM[k].toLowerCase());
 let title,text;
 if(right>=8){title='You can diagnose the failure';text=`${right} of 9 right. When a student can’t remember, the fix depends on which stage failed, so asking is the first step.`}
 else if(right>=5){title='Mostly there';text=`${right} of 9 right. You missed ${weak.length===3?'cases at every stage':'some '+weak.join(' and ')+' cases'}. A tip: ask in order. Could they use it right after learning? If not, encoding. If they could then but not later, consolidation. If a cue or hint brings it back, retrieval.`}
 else{title='Worth another look';text=`${right} of 9 right. Ask in order. Could they use it right after learning? If not, it was never encoded. If they could then but not later, it faded before it set. If a cue or hint brings it back, it was stored but out of reach.`}
 $('bTitle').textContent=title;$('bFb').textContent=text;g.onclick=null;g.textContent='Try again';g.disabled=false;g.focus();br=null});
''')
open('m01/template.html','w').write(page(o))

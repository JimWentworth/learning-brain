import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='a02',n='2',label='The Learning Brain · Generative AI · Topic 2',epi='The Learning Brain, Generative AI, episode 2',
title='Offloading: What to Keep in Your Own Head',h1='Offloading',em='What were you meant to learn?',read='7',mins='2 minutes',vtitle='Offloading',
dek='Using notes, devices or AI to lower the load on your mind is old and often smart. But what you offload, you may not learn, unless you mean to.',
jumps='<span><a href="#sT">Save it or keep it</a></span><span><a href="#bT">Offload or hold?</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, and the hippocampus, deep inside, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.hip.lab=[640,770];BR.R.hip.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc','hip'],labels:['pfc','hip'],labelT:{pfc:0.8,hip:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS+'''
.flist{font:700 24px/1.4 var(--body);color:#fff;text-align:center;margin:0;display:grid;grid-template-columns:repeat(4,auto);gap:6px 22px;justify-content:center}
@media (max-width:520px){.flist{grid-template-columns:repeat(2,auto)}}
.flist small{grid-column:1/-1;display:block;font:800 14px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#C9D3E3}
.savebar{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
.savebar[hidden]{display:none}''',
body='''  <div class="col lede">
    <p>Students studied a list of words in one computer file, then a second list in another. When they saved the first file before moving on, they remembered more of the second list. Benjamin Storm and Sean Stone reported this in 2015. Offloading the first list freed room for the next.</p>
    <p>Psychologists call this cognitive offloading: using the world, a note, a device, or now an AI, to lower the demand on your own head. It’s as old as writing, and often smart.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>Saving</strong><span>the first file helped people remember the second</span></div>
      <div role="listitem"><strong>3 × 172</strong><span>people in experiments showing that more offloading meant better performance but weaker memory</span></div>
      <div role="listitem"><strong>Almost all</strong><span>of that cost was made up when people knew a test was coming</span></div>
      <div role="listitem"><strong>Failed</strong><span>replication: the claim that hard questions make us think of searching the internet</span></div>
    </div>
  </div>

'''+'''  <section class="night" aria-labelledby="sT">
    <div class="col">
      <h2 class="sec" id="sT"><span class="n">Try it</span>Save it or keep it</h2>
      <p>Two rounds. In each, you’ll study two short word lists, one after the other. In one round you’ll save the first list before moving on; in the other you’ll just close it. Then you’ll recall the second list. About 2 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="sScreen">
          <div class="flist" id="sL" aria-live="polite"></div>
          <div class="savebar" id="sBar" hidden><button class="nbtn" id="sAct" type="button">Save file A</button></div>
'''+recall_screen('s')+'''
'''+tail('s')+'''
        </div>
        <div>
          <p class="phase" id="sPhase">Ready</p>
          <p class="mtitle" id="sTitle">Does saving free your memory?</p>
          <p class="mtext" id="sText" aria-live="polite">Each list has 8 words, shown for 15 seconds. Which round you save in is chosen at random.</p>
          <div id="sRes"></div>
          <div class="mrow"><button class="nbtn" id="sGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">The cost</span>Better now, less later</h2>
    <p>Offloading has a cost. In 2021, Sandra Grinschgl, Frank Papenmeier and Hauke Meyerhoff had people copy colour patterns, choosing how often to look back at the model instead of holding it in mind. People who offloaded more performed better in the moment and remembered less afterwards, across three experiments of 172 people each.</p>
    <p>The cost wasn’t fixed. When people who offloaded as much as possible knew a memory test was coming, they almost entirely made up for it. Intending to learn changed what stayed. And Storm and Stone’s saving benefit vanished when people were told the saved file might not be there: offloading only frees the mind when the store is trusted.</p>
    <h2 class="sec"><span class="n">Headlines</span>Separate the pattern from the hype</h2>
    <p>One famous 2011 claim, that hard questions make us think of searching the internet, failed to replicate in a large 2018 project led by Colin Camerer. The broad pattern of offloading is solid; some striking headlines aren’t. These are lab tasks with lists and patterns, and generative AI can offload more than memory: it can offload the reasoning itself.</p>
  </div>

'''+cls_html('bT','Offload it or hold it?','Ten things a learner might hand to a note, a device or an AI. For each, decide: fine to offload, or something they should hold in their own head? You’ll get feedback after each one.',[('O','Offload it','look it up when needed'),('H','Hold it','learn it yourself')],'Offload it or hold it?','Offload or hold?','The question is always: what were you meant to learn?')+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Say what must stay in their heads</h3>
      <p>Decide what students must hold in their own heads, and say so. Let them offload the rest, and tell them when a test is coming, so they learn on purpose. And when AI does a step, have them restate it in their own words.</p>
    </aside>
  </div>
''',
tips_h='Offloading what you were meant to learn is the problem',
tips='''      <li><b>Name what must be held</b><span>And let the rest be offloaded.</span></li>
      <li><b>Announce the test</b><span>So students learn on purpose.</span></li>
      <li><b>Restate what AI did</b><span>In their own words.</span></li>''',
sources='''        <li><a href="https://www.psychologicalscience.org/news/releases/saving-old-information-can-boost-memory-for-new-information.html">Storm, B. C., &amp; Stone, S. M. (2015). Saving-enhanced memory: The benefits of saving on the learning and remembering of new information. <i>Psychological Science</i>.</a></li>
        <li><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8358584/">Grinschgl, S., Papenmeier, F., &amp; Meyerhoff, H. S. (2021). Consequences of cognitive offloading: Boosting performance but diminishing memory. <i>Quarterly Journal of Experimental Psychology</i>.</a></li>
        <li><a href="https://neurosciencenews.com/metacognition-technology-4857/">Risko, E. F., &amp; Gilbert, S. J. (2016). Cognitive offloading. <i>Trends in Cognitive Sciences</i>. (Summary.)</a></li>
        <li><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7651475/">Hesselmann, G. (2020). No conclusive evidence that difficult general knowledge questions cause a “Google Stroop effect”. <i>PeerJ</i>. (On the failed replication of Sparrow, Liu &amp; Wegner, 2011.)</a></li>''',
quiz='''[
 {q:'Saving the first file before studying a second list did what?',o:['Improved memory for the second list','Hurt memory for both','Nothing'],a:0,f:'Offloading the first list freed room for the next.'},
 {q:'When did the saving benefit disappear?',o:['When people were told the saved file might not be there','When the lists were short','Never'],a:0,f:'Offloading only frees the mind when the store is trusted.'},
 {q:'People forced to offload a lot, but who knew a test was coming…',o:['Almost entirely made up for the memory cost','Remembered nothing','Did worse than everyone'],a:0,f:'Intending to learn changed what stayed.'}]''',
js=BASE+recall_kit('s','sr')+r'''
/* ---------- save it or keep it ----------
   Two rounds, each: file A (8 words, 15 s) → Save or Close → file B (8 words, 15 s) → recall B → recall A.
   Save in one round, close in the other (random order). Compare recall of B. */
const POOL=['anchor','barrel','candle','donkey','engine','feather','garden','hammer','island','jacket','kettle','ladder','magnet','napkin','orchid','pencil','quiver','rocket','saddle','tablet','violin','walnut','yogurt','zipper','button','cactus','dagger','falcon','glider','helmet','iguana','jigsaw'];
let sr=null;
function act(label){return new Promise(res=>{$('sAct').textContent=label;$('sBar').hidden=false;$('sAct').focus();$('sAct').onclick=()=>{$('sAct').onclick=null;$('sBar').hidden=true;res()}})}
async function show(name,L){$('sL').innerHTML=`<small>${name}</small>${L.map(x=>`<span>${x}</span>`).join('')}`;$('sProg').textContent='Study the list';return await sHold(15)}
$('sGo').addEventListener('click',async()=>{if(sr)return;sr={};const g=$('sGo');g.disabled=true;g.textContent='In progress';$('sRes').innerHTML='';
 const w=shuf([...POOL]);const saveFirst=Math.random()<0.5;const res={save:0,close:0,saveA:0,closeA:0};
 for(let r=0;r<2;r++){const save=(r===0)===saveFirst;const A=w.slice(r*16,r*16+8),B=w.slice(r*16+8,r*16+16);
  $('sPhase').textContent=`Round ${r+1} of 2`;$('sTitle').textContent='File A';$('sText').textContent='Study these 8 words.';
  if(!await show('File A',A))return;$('sL').textContent='';
  $('sTitle').textContent=save?'Save file A':'Close file A';$('sText').textContent=save?'File A will be saved to the page.':'File A will be closed without saving.';$('sProg').textContent='';
  await act(save?'Save file A':'Close file A');if(!sr)return;
  $('sTitle').textContent='File B';$('sText').textContent='Study these 8 words.';if(!await show('File B',B))return;$('sL').textContent='';
  $('sTitle').textContent='Recall file B';$('sText').textContent='Type the words from file B.';$('sW').textContent='File B?';$('sProg').textContent='';
  let v=await sRecall();if(!sr)return;let t=toks(v);const nb=B.filter(x=>t.some(y=>match(y,x))).length;
  $('sTitle').textContent='Recall file A';$('sText').textContent=save?'Now type the words from file A, the one you saved.':'Now type the words from file A, the one you closed.';$('sW').textContent='File A?';
  v=await sRecall();if(!sr)return;t=toks(v);const na=A.filter(x=>t.some(y=>match(y,x))).length;
  if(save){res.save=nb;res.saveA=na}else{res.close=nb;res.closeA=na}$('sW').textContent=''}
 $('sL').textContent='';$('sW').textContent='Done';$('sProg').textContent='';$('sPhase').textContent='Your results';
 $('sRes').innerHTML=`<div class="res wl2"><p class="gh">File B recalled, out of 8</p>${barRow('After saving A',res.save,8,res.save+' of 8','#FCB316')}${barRow('After closing A',res.close,8,res.close+' of 8','#C9D3E3')}<p class="gh">File A recalled, out of 8</p>${barRow('Saved',res.saveA,8,res.saveA+' of 8','#FCB316')}${barRow('Closed',res.closeA,8,res.closeA+' of 8','#C9D3E3')}</div>`;
 const d=res.save-res.close,tot=res.save+res.close;let title,text;
 if(tot<3){title='Too few to compare';text=`You recalled ${tot} word${tot===1?'':'s'} from the two B files. Try again, and say each word to yourself as you study.`}
 else if(d>=2){title='Saving freed some room';text=`You recalled ${res.save} of 8 from file B after saving file A, and ${res.close} after just closing it. Trusting the file to hold the first list seems to have left more room for the second, as in Storm and Stone’s study.`+(res.saveA<res.closeA?` And you remembered less of the saved list itself (${res.saveA} against ${res.closeA}): what you offload, you may not keep.`:'')}
 else if(d>=-1){title='About the same this time';text=`You recalled ${res.save} of 8 after saving and ${res.close} after closing. With 8 words a list, chance plays a big part, and you may not have trusted the save, which in the original study removed the benefit.`}
 else{title='Closing did better this time';text=`You recalled ${res.close} of 8 after closing file A and ${res.save} after saving it, the reverse of the usual result. With 8 words a list, chance plays a big part. Try again; the order changes at random.`}
 $('sTitle').textContent=title;$('sText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();sr=null});
'''+cls_js("{O:'Offload it',H:'Hold it'}",'''[
 ['A nursing student who will need drug dosage rules in emergencies','H','Hold it: in an emergency there may be no time to look it up, and judgment depends on knowing it.'],
 ['A citation format the student uses twice a year','O','Offload it: a reference guide does this well, and memorizing it uses effort better spent elsewhere.'],
 ['Vocabulary in a language the student is learning to speak','H','Hold it: you can’t hold a conversation through a lookup.'],
 ['The dates of next term’s meetings','O','Offload it: a calendar is the right place for this.'],
 ['The core concepts of the student’s own field','H','Hold it: they are what new learning builds on, and what lets you check an AI’s answer.'],
 ['The exact syntax of a function the student rarely uses','O','Offload it: look it up when needed, as long as you know what the function is for.'],
 ['The steps of a proof the student will be examined on, and needs to understand','H','Hold it: this is what the course is meant to teach.'],
 ['A friend’s phone number','O','Offload it: the phone keeps it well, as long as the phone is trusted.'],
 ['The times tables, for a student starting algebra','H','Hold it: fluent recall frees working memory for the new ideas.'],
 ['A first draft of an essay meant to show the student’s own reasoning','H','Hold it: if AI writes the reasoning, the thinking the task was set for may never happen.']]''','Offload it or hold it?',r'''
 if(right>=9){title='You know what to keep';text=`${right} of 10 right. The test is always: what was the learner meant to learn? Offload the rest, and trust the store.`}
 else if(right>=6){title='Mostly there';text=`${right} of 10 right. You missed ${missed}. Ask: would they need it fast, without a lookup? Does new learning build on it? Is it what the task is meant to teach? If so, hold it.`}
 else{title='Worth another look';text=`${right} of 10 right. Hold what must be fast, what later learning builds on, and what the task is meant to teach. Offload lookups, dates and formats.`}'''))
open('a02/template.html','w').write(page(o))

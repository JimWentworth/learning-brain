import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='m06',n='6',label='The Learning Brain · Memory · Topic 6',epi='The Learning Brain, Memory, episode 6',
title='From Fragile to Stable: How Memories Consolidate',h1='From fragile to stable',em='A memory is still being built',read='8',mins='2½ minutes',vtitle='From fragile to stable',
dek='New memories start fragile and settle with time: over minutes, over hours as synapses change, and over years as storage shifts from the hippocampus to the cortex.',
jumps='<span><a href="#bT">On what timescale?</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the hippocampus, deep inside, and the temporal lobe glowing orange and labelled. The hippocampus helps bind a new memory; over time, the cortex takes on more of the storage.',
hero_js="BR.R.tem.lab=[600,770];BR.R.tem.al='left';BR.R.hip.lab=[560,-70];BR.R.hip.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['hip','tem'],labels:['hip','tem'],labelT:{hip:0.8,tem:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.bscen{font:600 clamp(19px,2.4vw,22px)/1.45 var(--body);color:#fff;max-width:40ch;min-height:5.8em;margin:0}
.bopts{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;width:100%;max-width:560px}
@media (max-width:520px){.bopts{grid-template-columns:repeat(2,minmax(0,1fr))}}
.bopts[hidden]{display:none}
.bopts button{min-height:52px;border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;font:700 17px/1.2 var(--body);cursor:pointer;padding:4px 8px}
.bopts button:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.bopts button.ok{border-color:#7DD3A8;background:#173B33}.bopts button.no{border-color:#FFB38A;background:#3B2420}
.bopts button:disabled{cursor:default}
.bfb{font-size:18px;line-height:1.45;color:#E9EEF6;margin:0;min-height:3em;max-width:44ch}
.bfb b.ok{color:#7DD3A8}.bfb b.no{color:#FFB38A}''',
body='''  <div class="col lede">
    <p>In 1900, two German psychologists, Georg Elias Müller and Alfons Pilzecker, had people learn a list of nonsense-syllable pairs, then a second list. When the second list came right away, memory for the first suffered. When it came six minutes later, the first list held up better.</p>
    <p>New memories, they concluded, need time to set. They called the process consolidation.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>6 minutes</strong><span>of rest before a second list protected the first</span></div>
      <div role="listitem"><strong>Up to 10 hours</strong><span>a hippocampal connection stayed stronger after a brief burst of stimulation, in 1973</span></div>
      <div role="listitem"><strong>A sparse set</strong><span>of hippocampal cells, switched on with light, brought back a mouse’s fear memory</span></div>
      <div role="listitem"><strong>About 15 years</strong><span>of memories lost before brain damage, in one study of amnesic patients; older ones were spared</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">In the synapse</span>Making a change last</h2>
    <p>In 1973, Tim Bliss and Terje Lømo gave a pathway into the <a href="@@LB:hippocampus@@">hippocampus</a> of anaesthetized rabbits a brief burst of stimulation. Afterwards, the connection responded more strongly for periods of 30 minutes to 10 hours; in later work with awake rabbits, for up to 3 days. This is long-term potentiation.</p>
    <p>Making changes like this last requires new proteins. Reviewing the evidence in 1984, Hasker Davis and Larry Squire concluded that blocking protein synthesis in animals around the time of learning left short-term memory intact, but long-term memory failed. The window is hours, not weeks.</p>
    <h2 class="sec"><span class="n">The engram</span>Where is the memory?</h2>
    <p>In 2012, Xu Liu, Steve Ramirez, Susumu Tonegawa and colleagues tagged the small set of hippocampal cells that were active while a mouse learned to fear a place. Later, in a completely different box, they switched those cells on with light. The mice froze, as if remembering. A sparse set of cells was enough to bring the memory back: a physical trace of an experience, called an engram.</p>
  </div>

  <section class="night" aria-labelledby="bT">
    <div class="col">
      <h2 class="sec" id="bT"><span class="n">Try it</span>On what timescale?</h2>
      <p>Eight findings about how memories settle. For each, choose the timescale: minutes, hours, days to weeks, or years. You’ll get feedback after each one.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="bScreen">
          <p class="bscen" id="bScen" aria-live="polite">Press Start.</p>
          <div class="bopts" id="bOpts" hidden role="group" aria-label="Choose the timescale"><button type="button" data-k="M">Minutes</button><button type="button" data-k="H">Hours</button><button type="button" data-k="D">Days to weeks</button><button type="button" data-k="Y">Years</button></div>
          <p class="prog" id="bProg" aria-live="polite"></p>
        </div>
        <div>
          <p class="phase" id="bPhase">Ready</p>
          <p class="mtitle" id="bTitle">How long does it take to set?</p>
          <p class="bfb" id="bFb" aria-live="polite">Consolidation happens on several timescales at once.</p>
          <div id="bRes"></div>
          <div class="mrow"><button class="nbtn" id="bGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Over years</span>From hippocampus to cortex</h2>
    <p>Over longer spans, memories reorganize. The hippocampus helps bind an experience together, and gradually the cortex takes on more of the storage. That is why damage to the hippocampus tends to spare old memories and hit recent ones hardest. In people, this loss can reach back years; in rats and mice, days to a month or two. And as <a href="#" id="m05link">the last topic</a> showed, a strong schema can make the hand-off happen much faster.</p>
    <h2 class="sec"><span class="n">Two cautions</span>Mice, fear, and live debates</h2>
    <p>The engram work is in mice, mostly with fear memories, a long way from a lecture hall. And the protein story has exceptions and live debates; for example, some drugs used to block protein synthesis also suppress nerve activity. What is solid is the shape: new memories start fragile and stabilize with time.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Treat new learning as fragile</h3>
      <p>Avoid piling a second demanding topic straight on top of the first. Give a short pause, a summary or a low-stakes question before moving on. Come back within a day or two, while the trace is still settling; the <a href="@@LB:lb11@@">spacing and sleep page</a> shows why. And connect new material to what students already know, so it settles into an existing frame.</p>
    </aside>
  </div>
''',
tips_h='A memory isn’t finished when the lesson ends',
tips='''      <li><b>Pause before the next topic</b><span>A summary or a low-stakes question.</span></li>
      <li><b>Come back within a day or two</b><span>While the trace is still settling.</span></li>
      <li><b>Connect it to what they know</b><span>So it settles into an existing frame.</span></li>''',
sources='''        <li><a href="https://www.encyclopedia.com/psychology/encyclopedias-almanacs-transcripts-and-maps/memory-consolidation-prolonged-process-reorganization">Memory consolidation: Prolonged process of reorganization, on Müller &amp; Pilzecker (1900). <i>Learning and Memory</i> encyclopedia, via Encyclopedia.com.</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC1350458/">Bliss, T. V. P., &amp; Lømo, T. (1973). Long-lasting potentiation of synaptic transmission in the dentate area of the anaesthetized rabbit following stimulation of the perforant path. <i>Journal of Physiology</i>.</a></li>
        <li><a href="https://www.ucl.ac.uk/~ucgbarg/res/GM73_JP232_357.pdf">Bliss, T. V. P., &amp; Gardner-Medwin, A. R. (1973). Long-lasting potentiation of synaptic transmission in the dentate area of the unanaesthetized rabbit following stimulation of the perforant path. <i>Journal of Physiology</i>.</a></li>
        <li><a href="https://doi.org/10.1037/0033-2909.96.3.518">Davis, H. P., &amp; Squire, L. R. (1984). Protein synthesis and memory: A review. <i>Psychological Bulletin</i>.</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/3331914">Liu, X., Ramirez, S., Pang, P. T., et al. (2012). Optogenetic stimulation of a hippocampal engram activates fear memory recall. <i>Nature</i>.</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6569980">Squire, L. R., Haist, F., &amp; Shimamura, A. P. (1989). The neurology of memory: Quantitative assessment of retrograde amnesia in two groups of amnesic patients. <i>Journal of Neuroscience</i>.</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6605282">Sharma, A. V., Nargang, F. E., &amp; Dickson, C. T. (2012). Neurosilence: Profound suppression of neural activity following intracerebral administration of the protein synthesis inhibitor anisomycin. <i>Journal of Neuroscience</i>.</a></li>''',
quiz='''[
 {q:'A second list came right after the first, or six minutes later. When did the first list hold up better?',o:['Six minutes later','Right away','No difference'],a:0,f:'New memories need time to set.'},
 {q:'Blocking protein synthesis around learning, in animals, affected which memory?',o:['Long-term memory','Short-term memory','Both equally'],a:0,f:'Short-term memory stayed intact.'},
 {q:'Damage to the hippocampus tends to hit which memories hardest?',o:['Recent ones','Old ones','All equally'],a:0,f:'Over time, the cortex takes on more of the storage.'}]''',
js=BASE+r'''
/* ---------- on what timescale? ---------- */
const NM={M:'Minutes',H:'Hours',D:'Days to weeks',Y:'Years'};
const CASES=[
 ['Müller and Pilzecker: a second list did less harm to the first if it came this much later.','M','Minutes: six minutes of rest was enough to protect the first list.'],
 ['Müller and Pilzecker: the most damaging second list came this soon after the first.','M','Minutes, or less: about 17 seconds later.'],
 ['Bliss and Lømo, 1973: after a brief burst of stimulation, a hippocampal connection stayed stronger for this long, in anaesthetized rabbits.','H','Hours: from 30 minutes to 10 hours.'],
 ['In animals, blocking protein synthesis stops long-term memory only if it happens within this window of learning.','H','Hours: during or shortly after learning. Later, it has no effect.'],
 ['In later work with awake rabbits, that stronger connection lasted up to this long.','D','Days: up to 3 days.'],
 ['Rats with a well-learned map of flavour locations: a new location stopped needing the hippocampus within this time.','D','Days: about two, with a schema in place.'],
 ['In rats and mice, damage to the hippocampus wipes out memories formed within this span before it.','D','Days to weeks: from several days to a month or two, depending on the study.'],
 ['In people, damage to the hippocampus and nearby areas can wipe out memories formed within this span before it.','Y','Years: in one study, about 15. Older memories were spared.']];
let br=null;
function bAnswer(){return new Promise(res=>{br.res=res;const o=$('bOpts');o.hidden=false;o.querySelectorAll('button').forEach(b=>{b.disabled=false;b.classList.remove('ok','no')});o.querySelector('button').focus()})}
$('bOpts').addEventListener('click',e=>{const b=e.target.closest('button');if(!b||!br||!br.res)return;const r=br.res;br.res=null;r(b.dataset.k)});
function bWait(label){return new Promise(res=>{const g=$('bGo');g.textContent=label;g.disabled=false;g.focus();g.onclick=()=>{g.onclick=null;g.disabled=true;g.textContent='In progress';res()}})}
$('bGo').addEventListener('click',async()=>{if(br||$('bGo').onclick)return;br={};const g=$('bGo');g.disabled=true;g.textContent='In progress';$('bRes').innerHTML='';
 const order=shuf([...CASES]);let right=0;const tot={M:0,H:0,D:0,Y:0},got={M:0,H:0,D:0,Y:0};let early=0,late=0;const rank={M:0,H:1,D:2,Y:3};
 $('bTitle').textContent='What timescale?';
 for(let i=0;i<order.length;i++){const [txt,k,ex]=order[i];tot[k]++;$('bPhase').textContent=`Finding ${i+1} of ${order.length}`;$('bScen').textContent=txt;$('bProg').textContent='';$('bFb').textContent='';
  const a=await bAnswer();if(!br)return;const ok=a===k;if(ok){right++;got[k]++}else if(rank[a]<rank[k])early++;else late++;
  $('bOpts').querySelectorAll('button').forEach(b=>{b.disabled=true;if(b.dataset.k===k)b.classList.add('ok');else if(b.dataset.k===a)b.classList.add('no')});
  $('bFb').innerHTML=(ok?'<b class="ok">Right.</b> ':`<b class="no">Not quite.</b> You chose ${NM[a].toLowerCase()}. `)+ex;$('bProg').textContent=`${right} of ${i+1} right so far.`;
  if(i<order.length-1){await bWait('Next finding');if(!br)return}}
 $('bOpts').hidden=true;$('bScen').textContent='Done.';$('bProg').textContent='';$('bPhase').textContent='Your results';
 $('bRes').innerHTML=`<div class="res wl2">${['M','H','D','Y'].map(k=>barRow(NM[k],got[k],tot[k],got[k]+' of '+tot[k],'#FCB316')).join('')}</div>`;
 const lean=early>=2&&early>late?' You tended to pick shorter timescales than the real ones: consolidation keeps going long after a lesson.':late>=2&&late>early?' You tended to pick longer timescales than the real ones: the first steps happen within minutes and hours.':'';
 let title,text;
 if(right>=7){title='You know the shape';text=`${right} of 8 right. Consolidation runs on several clocks at once: minutes for the first protection, hours for synapses and proteins, days to years for the shift to the cortex.`+lean}
 else if(right>=4){title='Mostly there';text=`${right} of 8 right.`+lean+' The shape: minutes for the first protection, hours for synapses and proteins, days to years for the shift to the cortex.'}
 else{title='Worth another look';text=`${right} of 8 right.`+lean+' Think of three clocks: minutes for the first protection, hours for synapses and new proteins, and days in animals or years in people for the shift from hippocampus to cortex.'}
 $('bTitle').textContent=title;$('bFb').textContent=text;g.onclick=null;g.textContent='Try again';g.disabled=false;g.focus();br=null});
'''+grid('''[
 ['A second list right after the first, compared with six minutes later: the first list was remembered',['Better after the six-minute gap','Better right away','The same'],0,'New memories need time to set.'],
 ['A brief burst of stimulation to a hippocampal pathway: the connection then',['Stayed stronger for hours','Weakened','Returned to normal within seconds'],0,'Long-term potentiation, 1973.'],
 ['Blocking protein synthesis around learning, in animals',['Long-term memory failed; short-term was intact','Short-term memory failed','Nothing changed'],0,'Making a change last requires new proteins.'],
 ['Mice in a different box, when light switched on the cells active during fear learning',['Froze, as if remembering','Ignored it','Explored more'],0,'A sparse set of cells was enough to bring the memory back.'],
 ['Damage to the hippocampus: which memories are hit hardest?',['Recent ones','Old ones','All equally'],0,'Older memories rely more on the cortex.'],
 ['Rats with a well-learned schema: how soon did a new memory stop needing the hippocampus?',['About two days','About a year','Never'],0,'A schema speeds up the hand-off.']]''','The pattern: new memories start fragile and stabilize with time, on several timescales at once.'))
s=page(o).replace('href="#" id="m05link"','href="@@LB:m05@@"')
open('m06/template.html','w').write(s)

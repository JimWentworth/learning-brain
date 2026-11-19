import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='m04',n='4',label='The Learning Brain · Memory · Topic 4',epi='The Learning Brain, Memory, episode 4',
title='Make It, Don’t Take It: The Generation Effect',h1='Make it, don’t take it',em='What students make, they keep',read='7',mins='2 minutes',vtitle='Make it, don’t take it',
dek='Producing an answer, even an easy one, leaves a stronger memory than reading it. The same idea scales up to explaining, and even to guessing before you learn, as long as the right answer follows.',
jumps='<span><a href="#gT">Read it or make it</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, and the hippocampus, deep inside, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.hip.lab=[640,770];BR.R.hip.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc','hip'],labels:['pfc','hip'],labelT:{pfc:0.8,hip:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.pair{font:700 34px/1.2 var(--body);color:#fff;text-align:center;min-height:48px}
.pair small{display:block;font:800 15px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#C9D3E3;margin-bottom:6px}
.pair .gap{color:#FCB316;letter-spacing:.12em}
.gin{display:flex;gap:10px;align-items:center;justify-content:center;flex-wrap:wrap}
.gin[hidden]{display:none}
.gin input{width:200px;min-height:50px;font:700 22px var(--body);text-align:center;border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff}
.gin input:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.gfb{font:600 17px var(--body);color:#E9EEF6;min-height:1.5em;margin:0;text-align:center}
.gfb b.ok{color:#7DD3A8}.gfb b.no{color:#FFB38A}''',
body='''  <div class="col lede">
    <p>Two ways to meet the same word. Read it: <i>rapid – fast</i>. Or make it: <i>rapid – f _ _ _</i>. The second takes a moment of effort, and in study after study, words people generated were remembered better than words they simply read.</p>
    <p>This is the generation effect. Producing an answer, even an easy one, leaves a stronger trace than receiving it.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>86</strong><span>studies in a 2007 review of the generation effect</span></div>
      <div role="listitem"><strong>0.40</strong><span>its average size: almost half a standard deviation, generating over reading</span></div>
      <div role="listitem"><strong>64</strong><span>reports, with nearly 6,000 learners, in a 2018 review of prompted self-explanation</span></div>
      <div role="listitem"><strong>Wrong guesses</strong><span>made before reading still helped, once the right answer followed</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The generation effect</span>Producing beats receiving</h2>
    <p>Sharon Bertsch and colleagues combined 86 studies in 2007. Generating beat reading by 0.40 of a standard deviation, almost half. It held for synonyms, opposites, categories and rhymes, and on both recognition and recall tests.</p>
    <p>Generating is a kind of <a href="@@LB:m03@@">deep processing</a>: to produce the word, you have to search what you know and check that the answer fits.</p>
  </div>

  <section class="night" aria-labelledby="gT">
    <div class="col">
      <h2 class="sec" id="gT"><span class="n">Try it</span>Read it or make it</h2>
      <p>20 pairs, each a category and one of its members. You’ll read half of them and complete the other half from the first letters. After a 30-second break, you’ll see each category and try to recall its member. About 3 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="gScreen">
          <div class="pair" id="gP" aria-live="polite"></div>
          <form class="gin" id="gGen" hidden><label class="sr-only" for="gGi">Your answer</label><input id="gGi" autocomplete="off" autocapitalize="off" spellcheck="false"><button class="nbtn" type="submit">OK</button></form>
          <p class="gfb" id="gFb" aria-live="polite"></p>
'''+recall_screen('g')+'''
'''+tail('g')+'''
        </div>
        <div>
          <p class="phase" id="gPhase">Ready</p>
          <p class="mtitle" id="gTitle">Does making it make it stick?</p>
          <p class="mtext" id="gText" aria-live="polite">Read pairs stay on screen for 4 seconds. For the others, type the whole word and press OK; you’ll see the answer either way.</p>
          <div id="gRes"></div>
          <div class="mrow"><button class="nbtn" id="gGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Self-explanation</span>The same idea, scaled up</h2>
    <p>Self-explanation means pausing to explain why a step works, or how one idea connects to another. A 2018 review by Kiran Bisra and colleagues combined 64 research reports with nearly 6,000 learners. Prompting students to explain to themselves improved learning by about half a standard deviation, across many subjects.</p>
    <h2 class="sec"><span class="n">Before learning</span>A wrong guess can prepare the mind</h2>
    <p>Generation even helps before learning. In 2009, Lindsey Richland, Nate Kornell and Liche Kao had students answer questions about an essay before reading it. Most guesses were wrong. Yet those items were learned better than items given the same extra time to study, even counting only the questions students had got wrong.</p>
    <h2 class="sec"><span class="n">One caution</span>Close the loop</h2>
    <p>In these studies, the correct answer always followed. A wrong guess left uncorrected is just a wrong guess. Generation works when students can make something meaningful and get the right answer soon after, which is also the lesson of <a href="@@LB:lb12@@">the errors and feedback page</a>.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Let them make it first</h3>
      <p>Before a lecture, pose two or three questions students can’t yet answer, then teach. Leave gaps in notes for students to fill. Pause after a worked step and ask: why does this follow? Have students predict a result before you show it. And always close the loop with the correct answer.</p>
    </aside>
  </div>
''',
tips_h='What students make, they keep',
tips='''      <li><b>Questions before teaching</b><span>Two or three they can’t yet answer.</span></li>
      <li><b>Gaps to fill, steps to explain</b><span>“Why does this follow?”</span></li>
      <li><b>Always close the loop</b><span>Give the right answer soon after.</span></li>''',
sources='''        <li><a href="https://pubmed.ncbi.nlm.nih.gov/17645161/">Bertsch, S., Pesta, B. J., Wiscott, R., &amp; McDaniel, M. A. (2007). The generation effect: A meta-analytic review. <i>Memory &amp; Cognition</i>.</a></li>
        <li><a href="https://doi.org/10.1007/s10648-018-9434-x">Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., &amp; Winne, P. H. (2018). Inducing self-explanation: A meta-analysis. <i>Educational Psychology Review</i>.</a></li>
        <li><a href="https://pubmed.ncbi.nlm.nih.gov/19751074/">Richland, L. E., Kornell, N., &amp; Kao, L. S. (2009). The pretesting effect: Do unsuccessful retrieval attempts enhance learning? <i>Journal of Experimental Psychology: Applied</i>.</a></li>''',
quiz='''[
 {q:'Across 86 studies, how did generating a word compare with reading it?',o:['Generating was remembered better, by almost half a standard deviation','No difference','Reading was better'],a:0,f:'The 2007 review found an average effect of 0.40.'},
 {q:'Students guessed answers about an essay before reading it, mostly wrongly. What happened?',o:['Those items were learned better than with extra study time','The wrong guesses stuck','No effect'],a:0,f:'A failed attempt prepared them for the answer.'},
 {q:'What must follow a guess for generation to help?',o:['The correct answer, soon after','Nothing','A second guess'],a:0,f:'An uncorrected wrong guess is just a wrong guess.'}]''',
js=BASE+recall_kit('g','gr')+r'''
/* ---------- read it or make it ----------
   20 category: member pairs; 10 read (4 s), 10 generated from the first two letters (self-paced, answer shown 1.5 s).
   Random order. 30 s break. Cued recall: category shown, type member, one at a time. Compare read vs generated. */
const PAIRS=[['fruit','plum'],['bird','crow'],['tree','maple'],['metal','copper'],['flower','tulip'],['fish','trout'],['tool','chisel'],['dance','tango'],['vegetable','radish'],['insect','beetle'],['colour','violet'],['drink','cider'],['weather','sleet'],['boat','kayak'],['fabric','denim'],['spice','ginger'],['dog breed','poodle'],['board game','chess'],['sport','rugby'],['bread','bagel']];
const frag=w=>w.slice(0,2)+' _'.repeat(w.length-2);
let gr=null;
function gen(){return new Promise(res=>{gr.gres=res;$('gGen').hidden=false;$('gGi').value='';$('gGi').focus()})}
$('gGen').addEventListener('submit',e=>{e.preventDefault();if(!gr||!gr.gres)return;const r=gr.gres;gr.gres=null;$('gGen').hidden=true;r($('gGi').value.trim().toLowerCase())});
$('gGo').addEventListener('click',async()=>{if(gr)return;gr={};const g=$('gGo');g.disabled=true;g.textContent='In progress';$('gRes').innerHTML='';$('gFb').textContent='';
 const kinds=shuf([...Array(10).fill('r'),...Array(10).fill('g')]);const items=shuf(PAIRS.map(([c,w],i)=>({c,w,k:kinds[i],made:null,got:false})));
 $('gPhase').textContent='Step 1 of 3 · Study';
 for(let i=0;i<items.length;i++){const it=items[i];$('gProg').textContent=`Pair ${i+1} of 20`;
  if(it.k==='r'){$('gTitle').textContent='Read it';$('gP').innerHTML=`<small>${it.c}</small>${it.w}`;if(!await gHold(4))return}
  else{$('gTitle').textContent='Make it';$('gP').innerHTML=`<small>${it.c}</small><span class="gap">${frag(it.w)}</span>`;const v=await gen();if(!gr)return;it.made=match(v,it.w);
   $('gFb').innerHTML=(it.made?'<b class="ok">Yes:</b> ':'<b class="no">The answer:</b> ')+it.w;$('gP').innerHTML=`<small>${it.c}</small>${it.w}`;if(!await gHold(1.5))return;$('gFb').textContent=''}
  $('gP').textContent=''}
 $('gPhase').textContent='Step 2 of 3 · Break';$('gTitle').textContent='Step away';$('gText').textContent='An easy, 30-second task.';await gBreak();if(!gr)return;
 $('gPhase').textContent='Step 3 of 3 · Recall';$('gTitle').textContent='Recall each member';$('gText').textContent='For each category, type the member you saw. Leave it blank if you can’t remember.';
 const test=shuf([...items]);
 for(let i=0;i<test.length;i++){const it=test[i];$('gProg').textContent=`Category ${i+1} of 20`;$('gP').innerHTML=`<small>${it.c}</small>?`;const v=await gen();if(!gr)return;it.got=!!v&&match(v,it.w)}
 $('gP').textContent='Done';$('gProg').textContent='';$('gPhase').textContent='Your results';
 const R=items.filter(x=>x.k==='r'&&x.got).length,G=items.filter(x=>x.k==='g'&&x.got).length,tot=R+G,d=G-R,miss=items.filter(x=>x.k==='g'&&!x.made).length;
 $('gRes').innerHTML=`<div class="res wl2"><p class="gh">Recalled, out of 10</p>${barRow('Read',R,10,R+' of 10','#C9D3E3')}${barRow('Made',G,10,G+' of 10','#FCB316')}</div>`;
 const mt=miss?` You couldn’t complete ${miss} of the 10 yourself; you saw the answer right after, which is what makes a miss useful.`:'';
 let title,text;
 if(tot<3){title='Too few to compare';text=`You recalled ${tot} of 20, too few to compare reading with making. Try again; the pairs will be split differently.`}
 else if(d>=2){title='Making it made it stick';text=`You recalled ${G} of the 10 pairs you completed, and ${R} of the 10 you read. A few seconds of effort left a stronger trace.`+mt}
 else if(d>=-1){title='About the same this time';text=`You recalled ${G} pairs you completed and ${R} you read. With 10 of each, chance plays a big part. Reading pairs for 4 seconds also leaves time to think about them, which is a form of making. Across 86 studies, the generation advantage was reliable but moderate.`+mt}
 else{title='Reading did better this time';text=`You recalled ${R} pairs you read and ${G} you completed, the reverse of the usual result. With 10 of each, chance plays a big part, and 4 seconds to read is long enough to rehearse.`+mt+' Try again; the pairs will be split differently.'}
 $('gTitle').textContent=title;$('gText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();gr=null});
'''+grid('''[
 ['Across 86 studies, words people generated compared with words they read',['Remembered better','Remembered the same','Remembered worse'],0,'By about 0.40 of a standard deviation.'],
 ['Did the generation effect hold on both recognition and recall tests?',['Yes, both','Only recognition','Only recall'],0,'It also held for synonyms, opposites, categories and rhymes.'],
 ['Students prompted to explain steps to themselves, in 64 research reports',['Learned more, by about half a standard deviation','Learned the same','Learned less, from the extra effort'],0,'Across many subjects.'],
 ['Before reading an essay, students guessed answers to questions about it. How many guesses were right?',['Most were wrong','Most were right','About half'],0,'They didn’t know the material yet.'],
 ['Those wrongly guessed items, compared with items given the same extra study time',['Learned better','Learned worse','No difference'],0,'A failed attempt prepared the mind for the answer.'],
 ['What did these studies always include?',['The correct answer, soon after','No feedback','A reward for guessing right'],0,'An uncorrected wrong guess is just a wrong guess.']]''','The pattern: producing an answer beats receiving it, as long as the right answer follows.'))
open('m04/template.html','w').write(page(o))

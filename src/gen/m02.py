import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='m02',n='2',label='The Learning Brain · Memory · Topic 2',epi='The Learning Brain, Memory, episode 2',
title='Attention Is the Gate: What Gets Into Memory',h1='Attention is the gate',em='Nothing is remembered that never got in',read='8',mins='2½ minutes',vtitle='Attention is the gate',
dek='What you attend to can be encoded; what you don’t barely gets in. Splitting attention while learning costs far more than splitting it while remembering.',
jumps='<span><a href="#gT">Learn with a second task</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the frontal lobe and the intraparietal sulcus, in the parietal lobe, glowing orange and labelled. Together they form a network that steers attention on purpose.',
hero_js="BR.R.fro.lab=[60,730];BR.R.fro.al='left';BR.R.ips.lab=[560,-70];BR.R.ips.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.44,s:fitS(W,H,1.32),t,active:['fro','ips'],labels:['fro','ips'],labelT:{fro:0.8,ips:1.0},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.dig{font:800 30px var(--body);color:#FCB316;min-height:40px;text-align:center}
.dig[hidden]{display:none}
.oddb{min-height:52px;min-width:180px;border-radius:12px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;font:800 18px var(--body);cursor:pointer}
.oddb small{display:block;font:600 13px var(--body);color:#C9D3E3}
.oddb[hidden]{display:none}
.oddb:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.oddb.hit{border-color:#7DD3A8}.oddb.miss{border-color:#FFB38A}''',
body='''  <div class="col lede">
    <p>Watch a video of people passing a basketball, and count the passes. Partway through, a person in a gorilla suit walks through the middle of the scene. In Daniel Simons and Christopher Chabris’s 1999 study, about half of viewers never saw it. Their eyes were on the screen; their attention was on the ball.</p>
    <p>Attention is the gate to memory. The brain can’t take in everything, so it selects, and what isn’t selected is mostly gone before memory can work on it.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>About half</strong><span>of viewers missed the gorilla</span></div>
      <div role="listitem"><strong>11%</strong><span>lower test scores for students who multitasked on laptops in a lecture</span></div>
      <div role="listitem"><strong>17%</strong><span>lower for students who could simply see a classmate’s multitasking screen</span></div>
      <div role="listitem"><strong>About ⅓</strong><span>of live lecture time spent mind wandering, in one study; more than half of it by choice</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Where the gate sits</span>Learning needs attention far more than remembering</h2>
    <p>In 1996, Fergus Craik and colleagues had people learn word lists while doing a second task, reacting to lights. Splitting attention while learning sharply reduced what they remembered later. Splitting attention while recalling barely touched memory, though it slowed the second task. Learning needs attention far more than remembering does.</p>
    <p>In the brain, a network linking the frontal lobe and the intraparietal sulcus, in the parietal lobe, steers attention on purpose: toward the ball, away from the gorilla. The <a href="@@LB:lb02@@">attention page</a> shows how what you select wins out over what you don’t.</p>
  </div>

  <section class="night" aria-labelledby="gT">
    <div class="col">
      <h2 class="sec" id="gT"><span class="n">Try it</span>Learn with a second task</h2>
      <p>Study two lists of 12 words. During one list, you’ll also watch a stream of digits and press a button for every odd one. After a 30-second break, type all the words you remember from both lists. About 2½ minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="gScreen">
'''+recall_screen('g')+'''
          <div class="dig" id="gDig" hidden aria-live="off"></div>
          <button class="oddb" id="gOdd" type="button" hidden>Odd!<small>or press Space</small></button>
'''+tail('g')+'''
        </div>
        <div>
          <p class="phase" id="gPhase">Ready</p>
          <p class="mtitle" id="gTitle">What does a second task cost?</p>
          <p class="mtext" id="gText" aria-live="polite">Each word appears for 2½ seconds. Try to remember them all. The order of the two lists is chosen at random.</p>
          <div id="gRes"></div>
          <div class="mrow"><button class="nbtn" id="gGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">In class</span>Divided attention, all day long</h2>
    <p>Classrooms divide attention constantly. In a simulated lecture, Faria Sana, Tina Weston and Nicholas Cepeda found in 2013 that students who multitasked on laptops scored 11% lower on a test. Students who merely had a view of a classmate’s multitasking screen scored 17% lower, in a separate experiment.</p>
    <h2 class="sec"><span class="n">From the inside</span>Minds wander, sometimes on purpose</h2>
    <p>Attention also drifts from the inside. In recorded lectures, mind wandering tends to rise as the lecture goes on, and memory for later material falls. In live classes the picture is less clear. Across a semester of real lectures, Jeffrey Wammes and colleagues found in 2016 that students were mind wandering about a third of the time, with no steady rise within a lecture, and that more than half of it was by choice.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Guard the gate</h3>
      <p>Make the first exposure count: one demanding thing at a time. Set a device policy, and explain why, including the cost to neighbours. Tell students what to look for before you show it. Break long explanations with questions that need a response. Attention lets material in; what students do next, the subject of <a href="#" id="m03link">the next topic</a>, decides what stays.</p>
    </aside>
  </div>
''',
tips_h='Nothing is remembered that never got in',
tips='''      <li><b>One thing at a time</b><span>Don’t ask students to learn something new while doing something else.</span></li>
      <li><b>A device policy, with the reason</b><span>Including the cost to the people nearby.</span></li>
      <li><b>Say what to look for</b><span>Then break long talks with questions.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1068/p281059">Simons, D. J., &amp; Chabris, C. F. (1999). Gorillas in our midst: Sustained inattentional blindness for dynamic events. <i>Perception</i>.</a></li>
        <li><a href="https://pubmed.ncbi.nlm.nih.gov/8683192/">Craik, F. I. M., Govoni, R., Naveh-Benjamin, M., &amp; Anderson, N. D. (1996). The effects of divided attention on encoding and retrieval processes in human memory. <i>Journal of Experimental Psychology: General</i>.</a></li>
        <li><a href="https://doi.org/10.1016/j.compedu.2012.10.003">Sana, F., Weston, T., &amp; Cepeda, N. J. (2013). Laptop multitasking hinders classroom learning for both users and nearby peers. <i>Computers &amp; Education</i>.</a></li>
        <li><a href="https://www.noba.to/blog/2016-07-25-are-your-students-paying-attention">Wammes, J. D. (2016). Are your students paying attention? <i>Noba blog</i>, on Wammes, Boucher, Seli, Cheyne, &amp; Smilek (2016).</a></li>
        <li><a href="https://doi.org/10.1038/nrn755">Corbetta, M., &amp; Shulman, G. L. (2002). Control of goal-directed and stimulus-driven attention in the brain. <i>Nature Reviews Neuroscience</i>.</a></li>''',
quiz='''[
 {q:'When does dividing attention hurt memory most?',o:['While learning','While recalling','Equally at both'],a:0,f:'Divided attention while recalling barely touched memory, though it slowed the other task.'},
 {q:'Students with a view of a classmate’s multitasking screen…',o:['scored lower too','scored the same','scored higher'],a:0,f:'17% lower, in a simulated lecture.'},
 {q:'In one study of live lectures, how much of students’ mind wandering was by choice?',o:['More than half','Almost none','All of it'],a:0,f:'They wandered about a third of the time, and more than half of that was intentional.'}]''',
js=BASE+recall_kit('g','gr')+r'''
/* ---------- learn with a second task ----------
   Two lists of 12 words, 2.5 s each. During one list (random which comes first) a digit changes every 0.8 s;
   press Odd for odd digits. 30 s break, then free recall of both lists. Compare recall by list; report digit task. */
const POOL=['pilot','marble','pepper','cabin','parrot','engine','pillow','kitten','ribbon','tower','lizard','napkin','sailor','bottle','turkey','helmet','circus','meadow','oyster','blanket','muffin','spider','lantern','island','pocket','dentist','camera','hornet','walrus','tablet','puzzle','saucer'];
let gr=null;
async function digits(sec){const st={odd:0,hit:0,fa:0};const t0=performance.now();$('gDig').hidden=false;$('gOdd').hidden=false;let last=0;
 while(performance.now()-t0<sec*1000){let d;do{d=1+Math.floor(Math.random()*9)}while(d===last);last=d;const odd=d%2===1;if(odd)st.odd++;gr.cur={odd,pressed:false};$('gDig').textContent=d;$('gOdd').className='oddb';
  await sw(800);if(!gr)return st;const c=gr.cur;if(c.pressed){if(c.odd)st.hit++;else st.fa++}}
 gr.cur=null;$('gDig').hidden=true;$('gOdd').hidden=true;return st}
const press=()=>{if(!gr||!gr.cur||gr.cur.pressed)return;gr.cur.pressed=true;$('gOdd').className='oddb '+(gr.cur.odd?'hit':'miss')};
$('gOdd').addEventListener('click',press);
addEventListener('keydown',e=>{if(gr&&gr.cur&&e.key===' '&&document.activeElement!==$('gBrk')){e.preventDefault();press()}});
async function study(list,dual){const run=dual?digits(list.length*2.5):null;
 for(let i=0;i<list.length;i++){$('gW').textContent=list[i];$('gProg').textContent=`Word ${i+1} of 12`;if(!await gHold(2.5))return null}
 $('gW').textContent='';return dual?await run:true}
$('gGo').addEventListener('click',async()=>{if(gr)return;gr={};const g=$('gGo');g.disabled=true;g.textContent='In progress';$('gRes').innerHTML='';
 const w=shuf([...POOL]).slice(0,24);const A=w.slice(0,12),B=w.slice(12);const dualFirst=Math.random()<0.5;
 const lists=dualFirst?[[A,true],[B,false]]:[[B,false],[A,true]];let st=null;
 for(let k=0;k<2;k++){const [L,dual]=lists[k];
  $('gPhase').textContent=`Step ${k+1} of 4 · List ${k+1}`;$('gTitle').textContent=dual?'Words, plus odd digits':'Words only';
  $('gText').textContent=dual?'Remember the words, and press Odd (or Space) whenever the orange digit is odd.':'Just remember the words.';
  $('gW').textContent='Get ready';await sw(1500);if(!gr)return;const r=await study(L,dual);if(!gr||r===null)return;if(dual)st=r}
 $('gPhase').textContent='Step 3 of 4 · Break';$('gTitle').textContent='Step away';$('gText').textContent='An easy, 30-second task.';await gBreak();if(!gr)return;
 $('gPhase').textContent='Step 4 of 4 · Recall';$('gTitle').textContent='Recall';$('gText').textContent='Type every word you remember from both lists, in any order.';$('gW').textContent='Which words?';
 const v=await gRecall();if(!gr)return;const t=toks(v);const n=L=>L.filter(x=>t.some(y=>match(y,x))).length;
 const nA=n(A),nB=n(B),tot=nA+nB,d=nB-nA,hr=st.odd?st.hit/st.odd:1;
 $('gW').textContent='Done';$('gPhase').textContent='Your results';$('gProg').textContent='';
 $('gRes').innerHTML=`<div class="res wl2"><p class="gh">Words recalled, out of 12</p>${barRow('Full attention',nB,12,nB+' of 12','#FCB316')}${barRow('With digits',nA,12,nA+' of 12','#C9D3E3')}<p class="gh">Digit task</p>${barRow('Odd digits caught',st.hit,st.odd,st.hit+' of '+st.odd,'#C9D3E3')}</div>`;
 const fa=st.fa?` (and ${st.fa} press${st.fa>1?'es':''} on even digits)`:'';
 const ord=dualFirst?'the digit list came first, so it had longer to fade before the test':'the digit list came second, so it was fresher at the test';
 let title,text;
 if(tot<3){title='Too few words to compare';text=`You recalled ${tot} word${tot===1?'':'s'} in all, too few to compare the lists. Try again, and say each word to yourself as it appears.`}
 else if(d>=2){title='The gate narrowed';text=`You recalled ${nB} of 12 words learned with full attention, and ${nA} of 12 learned with the digits. You caught ${st.hit} of ${st.odd} odd digits${fa}. Splitting attention while learning cost you words, as it did in Craik’s studies.`+(hr<0.5?' And you let many digits go, so the second task got even less than it seemed to.':'')}
 else if(d>=-1){title=hr<0.5?'You may have let the digits go':'About the same this time';
  text=`You recalled ${nB} words with full attention and ${nA} with the digits. `+(hr<0.5?`But you caught only ${st.hit} of ${st.odd} odd digits${fa}. Protecting the words by neglecting the second task is a real strategy: in Craik’s studies, people could trade one task off against the other.`:`You also caught ${st.hit} of ${st.odd} odd digits${fa}. With only 12 words per list, chance plays a big part; here, ${ord}. In studies with many people and lists, the cost of splitting attention while learning is large and reliable.`)}
 else{title='The digit list did better';text=`You recalled ${nA} words learned with the digits and ${nB} with full attention, the reverse of the usual result. With 12 words per list, chance plays a big part, and ${ord}. You caught ${st.hit} of ${st.odd} odd digits${fa}. Try again: the order changes at random.`}
 $('gTitle').textContent=title;$('gText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();gr=null});
'''+grid('''[
 ['People counting basketball passes: how many missed the person in a gorilla suit?',['About half','Almost no one','Almost everyone'],0,'About half, in the 1999 study. Their attention was on the ball.'],
 ['Learning a word list while doing a second task',['Memory sharply reduced','Memory barely changed','Memory improved'],0,'The gate narrowed: less got in.'],
 ['Recalling a word list while doing a second task',['Memory barely changed','Memory sharply reduced','Memory improved'],0,'Recall barely suffered, though the second task slowed.'],
 ['Students who multitasked on laptops during a lecture, on a test',['11% lower','About the same','11% higher'],0,'In a simulated lecture, 2013.'],
 ['Students who could see a classmate’s multitasking screen',['17% lower','About the same','Higher, from the contrast'],0,'Most didn’t feel distracted.'],
 ['In live lectures over a semester, how much of students’ mind wandering was by choice?',['More than half','Almost none','All of it'],0,'They wandered about a third of the time; more than half of it was intentional.']]''','The pattern: attention matters most while learning, and the classroom divides it in many ways.'))
s=page(o).replace('href="#" id="m03link"','href="@@LB:m03@@"')
open('m02/template.html','w').write(s)

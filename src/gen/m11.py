import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='m11',n='11',label='The Learning Brain · Memory · Topic 11',epi='The Learning Brain, Memory, episode 11',
title='Retrieval Rewrites Memory: Every Recall Writes It Again',h1='Retrieval rewrites memory',em='Every recall writes it again',read='8',mins='2 minutes',vtitle='Retrieval rewrites memory',
dek='Recalling a memory rebuilds it, strengthening the path that was used. That makes practice tests powerful, and it means recall can also hide what was not practised, or absorb a leading question.',
jumps='<span><a href="#rT">Practise some, lose others</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the hippocampus, deep inside, and the prefrontal cortex, at the front, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.hip.lab=[640,770];BR.R.hip.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['hip','pfc'],labels:['hip','pfc'],labelT:{hip:0.8,pfc:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.pair{font:700 34px/1.2 var(--body);color:#fff;text-align:center;min-height:48px}
.pair small{display:block;font:800 15px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#C9D3E3;margin-bottom:6px}
.pair .gap{color:#FCB316;letter-spacing:.12em}
.gin{display:flex;gap:10px;align-items:center;justify-content:center;flex-wrap:wrap}
.gin[hidden]{display:none}
.gin input{width:200px;min-height:50px;font:700 22px var(--body);text-align:center;border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff}
.gin input:focus-visible{outline:3px solid #FCB316;outline-offset:2px}''',
body='''  <div class="col lede">
    <p>Students read a short science passage. Some then read it again; others tried to recall it, with no feedback. Five minutes later, rereading looked better. But two days and a week later, the students who had recalled it remembered more. Henry Roediger and Jeffrey Karpicke reported this in 2006.</p>
    <p>Retrieval isn’t a simple readout. Each time a memory is pulled up, it is rebuilt and stored again, strengthened along the path that was used. Rereading lets the page do the work; recall makes the brain do it.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>272</strong><span>effects, from about 15,000 people, in a 2017 review of practice tests</span></div>
      <div role="listitem"><strong>Without feedback</strong><span>practice tests still helped</span></div>
      <div role="listitem"><strong>Unpractised items</strong><span>from practised categories were recalled worse later</span></div>
      <div role="listitem"><strong>32% vs 14%</strong><span>“remembered” broken glass that wasn’t there, after “smashed” vs “hit”</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Practice tests</span>Beat restudying, in labs and classrooms</h2>
    <p>A 2017 review by Olusola Adesope, Dominic Trevisan and Narayankripa Sundararajan combined 272 effects from about 15,000 people. Practice tests beat restudying, in labs and in classrooms, and helped even without feedback. The <a href="@@LB:lb10@@">retrieval practice page</a> has more.</p>
  </div>

  <section class="night" aria-labelledby="rT">
    <div class="col">
      <h2 class="sec" id="rT"><span class="n">Try it</span>Practise some, lose others</h2>
      <p>Study 24 words in six categories. Then practise recalling a few of them from their first letters. After a 30-second break, recall every word, category by category. About 3 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="rScreen">
          <div class="pair" id="rP" aria-live="polite"></div>
          <form class="gin" id="rGen" hidden><label class="sr-only" for="rGi">Your answer</label><input id="rGi" autocomplete="off" autocapitalize="off" spellcheck="false"><button class="nbtn" type="submit">OK</button></form>
'''+recall_screen('r')+'''
'''+tail('r')+'''
        </div>
        <div>
          <p class="phase" id="rPhase">Ready</p>
          <p class="mtitle" id="rTitle">What does practising some words do to the others?</p>
          <p class="mtext" id="rText" aria-live="polite">Each word appears for 2 seconds with its category. Try to remember them all.</p>
          <div id="rRes"></div>
          <div class="mrow"><button class="nbtn" id="rGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Hidden by practice</span>Retrieval reshapes what isn’t retrieved</h2>
    <p>In 1994, Michael Anderson, Robert Bjork and Elizabeth Bjork had people study categories of words, then practise recalling half the items from half the categories. Later, the unpractised items from practised categories were recalled worse than items from categories that hadn’t been practised at all. This is retrieval-induced forgetting.</p>
    <h2 class="sec"><span class="n">Steered from outside</span>A word can plant a memory</h2>
    <p>In 1974, Elizabeth Loftus and John Palmer showed people films of car crashes. Asked how fast the cars were going when they <i>smashed</i>, rather than <i>hit</i>, people gave higher estimates. A week later, 32% of the “smashed” group reported seeing broken glass, against 14% of the “hit” group. There was no broken glass.</p>
    <h2 class="sec"><span class="n">A caution</span>Retrieval needs a foothold</h2>
    <p>Testing helps most when students can retrieve at least some of the answer, and when errors are corrected. And a leading question can plant a mistake as easily as it checks knowledge.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Quiz often, quiz widely, word it neutrally</h3>
      <p>Use frequent, low-stakes quizzes instead of extra review. Ask students to recall before showing the answer, then give feedback. Quiz across the whole topic, not just a few favourite points, so practice doesn’t push the rest out of reach. And word questions neutrally.</p>
    </aside>
  </div>
''',
tips_h='Every time we recall, we write the memory again',
tips='''      <li><b>Low-stakes quizzes</b><span>Instead of extra review.</span></li>
      <li><b>Recall, then feedback</b><span>Not the answer first.</span></li>
      <li><b>Quiz the whole topic, neutrally</b><span>Not just favourite points, and no leading questions.</span></li>''',
sources='''        <li><a href="https://www.psychologicalscience.org/journals/psychological-science/j.1467-9280.2006.01693.x/">Roediger, H. L., &amp; Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. <i>Psychological Science</i>.</a></li>
        <li><a href="https://doi.org/10.3102/0034654316689306">Adesope, O. O., Trevisan, D. A., &amp; Sundararajan, N. (2017). Rethinking the use of tests: A meta-analysis of practice testing. <i>Review of Educational Research</i>.</a></li>
        <li><a href="https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/07/Anderson_RBjork_EBjork_1994.pdf">Anderson, M. C., Bjork, R. A., &amp; Bjork, E. L. (1994). Remembering can cause forgetting: Retrieval dynamics in long-term memory. <i>Journal of Experimental Psychology: Learning, Memory, and Cognition</i>.</a></li>
        <li><a href="https://doi.org/10.1016/S0022-5371(74)80011-3">Loftus, E. F., &amp; Palmer, J. C. (1974). Reconstruction of automobile destruction. <i>Journal of Verbal Learning and Verbal Behavior</i>.</a></li>''',
quiz='''[
 {q:'Rereading vs recalling a passage: who remembered more a week later?',o:['Those who recalled it','Those who reread it','No difference'],a:0,f:'Rereading looked better only at five minutes.'},
 {q:'Practising some items from a category does what to the rest of that category?',o:['Makes them harder to recall later','Makes them easier','Nothing'],a:0,f:'Retrieval-induced forgetting.'},
 {q:'After “smashed” rather than “hit”, what did more people report a week later?',o:['Broken glass that wasn’t there','A slower speed','Nothing different'],a:0,f:'The question became part of the memory.'}]''',
js=BASE+recall_kit('r','rr')+r'''
/* ---------- practise some, lose others ----------
   6 categories x 4 words, studied 2 s each (category shown). Practice: 2 words from each of 3 random categories,
   completed from category + first two letters, 3 rounds (feedback). 30 s break. Category-cued recall of all.
   Compare practised (Rp+), unpractised from practised categories (Rp-), and words from unpractised categories (Nrp). */
const CATS=[['Drinks',['coffee','juice','milk','soda']],['Trees',['oak','pine','birch','maple']],['Sports',['tennis','hockey','golf','rugby']],
 ['Metals',['iron','copper','silver','nickel']],['Birds',['robin','eagle','crow','owl']],['Vegetables',['carrot','onion','potato','celery']]];
let rr=null;
function rAsk(){return new Promise(res=>{rr.gres=res;$('rGen').hidden=false;$('rGi').value='';$('rGi').focus()})}
$('rGen').addEventListener('submit',e=>{e.preventDefault();if(!rr||!rr.gres)return;const r=rr.gres;rr.gres=null;$('rGen').hidden=true;r($('rGi').value.trim().toLowerCase())});
const pct=(a,n)=>Math.round(a/n*100);
$('rGo').addEventListener('click',async()=>{if(rr)return;rr={};const g=$('rGo');g.disabled=true;g.textContent='In progress';$('rRes').innerHTML='';
 const pc=new Set(shuf([0,1,2,3,4,5]).slice(0,3));const items=[];
 CATS.forEach(([c,ws],ci)=>{const prac=new Set(pc.has(ci)?shuf([...ws]).slice(0,2):[]);ws.forEach(w=>items.push({c,w,t:pc.has(ci)?(prac.has(w)?'P':'R'):'N',got:false}))});
 $('rPhase').textContent='Step 1 of 4 · Study';$('rTitle').textContent='Remember these';
 const study=shuf([...items]);
 for(let i=0;i<study.length;i++){$('rP').innerHTML=`<small>${study[i].c}</small>${study[i].w}`;$('rProg').textContent=`Word ${i+1} of 24`;if(!await rHold(2))return}
 $('rPhase').textContent='Step 2 of 4 · Practise';$('rTitle').textContent='Practise recalling';$('rText').textContent='Complete each word from its category and first letters. You’ll see the answer after each one.';
 const P=items.filter(x=>x.t==='P');
 for(let r=0;r<3;r++){const ord=shuf([...P]);for(let i=0;i<ord.length;i++){const it=ord[i];$('rProg').textContent=`Round ${r+1} of 3 · ${i+1} of ${ord.length}`;
  $('rP').innerHTML=`<small>${it.c}</small><span class="gap">${it.w.slice(0,2)}${' _'.repeat(it.w.length-2)}</span>`;const v=await rAsk();if(!rr)return;
  $('rP').innerHTML=`<small>${it.c}</small>${it.w}`;if(!await rHold(1))return}}
 $('rP').textContent='';$('rPhase').textContent='Step 3 of 4 · Break';$('rTitle').textContent='Step away';$('rText').textContent='An easy, 30-second task.';await rBreak();if(!rr)return;
 $('rPhase').textContent='Step 4 of 4 · Recall';$('rTitle').textContent='Recall each category';$('rText').textContent='Type every word you studied in this category, practised or not.';
 for(const [c] of shuf([...CATS])){$('rW').innerHTML=`<small>Category</small>${c}`;const v=await rRecall(`All the ${c.toLowerCase()} you studied`);if(!rr)return;const t=toks(v);items.filter(x=>x.c===c).forEach(x=>{x.got=t.some(y=>match(y,x.w))})}
 $('rW').textContent='Done';$('rProg').textContent='';$('rPhase').textContent='Your results';
 const n=k=>items.filter(x=>x.t===k).length,gt=k=>items.filter(x=>x.t===k&&x.got).length;
 const p=pct(gt('P'),n('P')),rm=pct(gt('R'),n('R')),nr=pct(gt('N'),n('N'));
 $('rRes').innerHTML=`<div class="res wl2"><p class="gh">Recalled</p>${barRow('Practised',p,100,gt('P')+' of 6','#FCB316')}${barRow('Not practised, same category',rm,100,gt('R')+' of 6','#FFB38A')}${barRow('Categories not practised',nr,100,gt('N')+' of 12','#C9D3E3')}</div>`;
 const tot=gt('P')+gt('R')+gt('N');let title,text;
 if(tot<4){title='Too few to compare';text=`You recalled ${tot} of 24 words. Try again, and picture each word as it appears.`}
 else if(nr-rm>=15&&p>=rm){title='Practice hid its neighbours';text=`You recalled ${p}% of the words you practised, ${nr}% of words from categories you never practised, and only ${rm}% of the unpractised words in practised categories. Recalling some words seems to have pushed their neighbours out of reach.`}
 else if(p>=nr+15&&rm>=nr-14){title='Practice helped, with no hidden cost';text=`You recalled ${p}% of the words you practised, against ${nr}% from unpractised categories. Their unpractised neighbours, at ${rm}%, didn’t suffer much this time. In studies with many people the cost is real but modest, so a single run often won’t show it.`}
 else if(p<nr){title='Practice didn’t show up this time';text=`You recalled ${p}% of the practised words and ${nr}% from unpractised categories${rm<nr?`, and ${rm}% of the practised categories’ other words`:''}. With 6 to 12 words per group, chance plays a big part.`}
 else{title='About even this time';text=`Practised words: ${p}%. Their unpractised neighbours: ${rm}%. Words from unpractised categories: ${nr}%. The cost to neighbours is real but modest in studies with many people, so a single run often won’t show it.`}
 $('rTitle').textContent=title;$('rText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();rr=null});
'''+grid('''[
 ['Students who recalled a passage instead of rereading it, tested five minutes later',['Did worse than rereaders','Did better','Did the same'],0,'Rereading looked better at first.'],
 ['The same students, tested a week later',['Remembered more than rereaders','Remembered less','The same'],0,'Recall made the brain do the work.'],
 ['Across 272 effects, practice tests without feedback',['Still helped','Didn’t help','Made things worse'],0,'Though feedback helps more.'],
 ['Unpractised items from practised categories, recalled later',['Worse than items from unpractised categories','Better','The same'],0,'Retrieval-induced forgetting.'],
 ['A week after being asked how fast cars “smashed” into each other',['More people “remembered” broken glass','Fewer did','No difference from “hit”'],0,'32% against 14%. There was no broken glass.'],
 ['When does testing help most?',['When students can retrieve some of the answer, and errors are corrected','When the questions are far too hard','When there are no answers'],0,'Retrieval needs a foothold.']]''','The pattern: every recall rewrites a memory, so recall often, widely and with neutral questions.'))
open('m11/template.html','w').write(page(o))

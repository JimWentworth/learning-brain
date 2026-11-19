import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='h08',n='8',label='The Learning Brain · Habits of the Learner · Topic 8',epi='The Learning Brain, Habits of the Learner, episode 8',
title='Illusions of Learning: Why Familiar Feels Like Learned',h1='Illusions of learning',em='Feeling fluent is not the same as knowing',read='7',mins='2 minutes',vtitle='Illusions of learning',
dek='Rereading your notes feels productive. The words look familiar, and familiar feels like learned. But recognizing something is not the same as being able to recall it in an exam.',
jumps='<span><a href="#wT">Reread or recall?</a></span><span><a href="#bT">Fluency trap or real test?</a></span>',
hero_aria='Drawing of the side of the brain with the hippocampus, deep inside, and the prefrontal cortex, at the front, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.hip.lab=[640,770];BR.R.hip.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['hip','pfc'],labels:['hip','pfc'],labelT:{hip:0.8,pfc:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS+'''
.qq{font:600 clamp(18px,2.2vw,21px)/1.45 var(--body);color:#fff;max-width:42ch;margin:0;text-align:center}
.pair{font:800 clamp(30px,5vw,42px)/1.2 var(--body);color:#fff;margin:0;text-align:center;min-height:52px}
.pair span{color:#FCB316}
.jb{display:flex;gap:8px;flex-wrap:wrap;justify-content:center}
.jb[hidden]{display:none}
.jb .nbtn{min-width:52px}
.wform{display:flex;gap:10px;align-items:center;justify-content:center;flex-wrap:wrap;width:100%}
.wform[hidden]{display:none}
.wform input{font:600 20px var(--body);min-height:48px;border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;padding:0 12px;width:min(260px,70vw)}
.wform input:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.wclock{font:800 40px var(--body);color:#FCB316;margin:0}
.wclock[hidden]{display:none}
.gfb{font:600 17px/1.45 var(--body);color:#E9EEF6;min-height:1.5em;margin:0;text-align:center}
.gfb b.ok{color:#7DD3A8}.gfb b.no{color:#FFB38A}''',
body='''  <div class="col lede">
    <p>In a survey of 177 college students, reported by Jeffrey Karpicke, Andrew Butler and Henry Roediger in 2009, 84% said they reread their notes or textbook, and 55% called it their top strategy. Only 11% said they tested themselves, and just 1% ranked that first.</p>
    <p>Rereading builds fluency: the material feels easy because you have just seen it. In one classic experiment, by Roediger and Karpicke, students who reread a passage did slightly better five minutes later. But after a week, students who had practised recalling it remembered 56%, against 42% for the rereaders.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>84%</strong><span>of students reread notes or textbooks</span></div>
      <div role="listitem"><strong>1%</strong><span>ranked testing themselves as their top strategy</span></div>
      <div role="listitem"><strong>56% vs 42%</strong><span>remembered after a week: recall practice against rereading</span></div>
      <div role="listitem"><strong>78%</strong><span>believed blocking had helped more, even after testing showed otherwise</span></div>
    </div>
  </div>

  <section class="night" aria-labelledby="wT">
    <div class="col">
      <h2 class="sec" id="wT"><span class="n">Try it</span>Reread or recall?</h2>
      <p>Learn ten Swahili words. You’ll see each one, then reread half of them and try to recall the other half. Predict how many of each you’ll remember, take a short break, and then test yourself. About 3 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="wScreen">
          <p class="qq" id="wQ" aria-live="polite">Press Start.</p>
          <p class="pair" id="wPair" aria-live="polite"></p>
          <form class="wform" id="wF" hidden><label class="sr-only" for="wI" id="wIL">English meaning</label><input id="wI" autocomplete="off" autocapitalize="off" spellcheck="false"><button class="nbtn" type="submit">Enter</button></form>
          <div class="jb" id="wB" hidden role="group" aria-label="Your prediction"></div>
          <p class="gfb" id="wFb" aria-live="polite"></p>
          <p class="wclock" id="wC" hidden aria-live="off"></p>
          <p class="prog" id="wProg" aria-live="polite"></p>
        </div>
        <div>
          <p class="phase" id="wPhase">Ready</p>
          <p class="mtitle" id="wTitle">See, then reread or recall</p>
          <p class="mtext" id="wText" aria-live="polite">Ten words, two ways of studying, one test.</p>
          <div id="wRes"></div>
          <div class="mrow"><button class="nbtn" id="wGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Mixing</span>The same illusion</h2>
    <p>Spacing and mixing show the same illusion. Nate Kornell and Robert Bjork had students learn painters’ styles with each artist’s paintings in a block, or with artists mixed together. Mixing worked better for most of them. Yet 78% believed blocking had helped more, even after their own test showed the opposite. A large online replication in 2014, by Peter Verkoeijen and Samantha Bouwmeester, found a similar advantage for mixing.</p>
  </div>

'''+cls_html('bT','Fluency trap or real test?','Eight ways to study or check what you know. For each, decide: does it only make the material feel familiar (a fluency trap), or does it really test whether you can recall it? You’ll get feedback after each one.',[('F','Fluency trap','feels familiar'),('R','Real test','makes you recall')],'Fluency trap or real test?','Fluency trap or real test?','The question is always: do you have to produce the answer from memory?')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Rereading isn’t useless</h2>
    <p>These are mostly lab tasks with short materials. And rereading is not useless: a first read is how you take the material in. The problem is relying on it to check what you know.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Try this</h3>
      <p>After reading, close the book and write down what you remember. Quiz yourself with questions, not highlights. Mix topics, and space sessions across days. And when something feels easy, test it before you trust it.</p>
    </aside>
  </div>
''',
tips_h='Feeling fluent is not the same as knowing. Test it.',
tips='''      <li><b>Close the book</b><span>Write down what you remember.</span></li>
      <li><b>Questions, not highlights</b><span>Make yourself produce the answer.</span></li>
      <li><b>Mix and space</b><span>Topics mixed, sessions spread across days.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1080/09658210802647009">Karpicke, J. D., Butler, A. C., &amp; Roediger, H. L. (2009). Metacognitive strategies in student learning: Do students practise retrieval when they study on their own? <i>Memory, 17</i>(4), 471–479.</a></li>
        <li><a href="https://doi.org/10.1111/j.1467-9280.2006.01693.x">Roediger, H. L., &amp; Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. <i>Psychological Science, 17</i>(3), 249–255.</a></li>
        <li><a href="https://doi.org/10.1111/j.1467-9280.2008.02127.x">Kornell, N., &amp; Bjork, R. A. (2008). Learning concepts and categories: Is spacing the “enemy of induction”? <i>Psychological Science, 19</i>(6), 585–592.</a></li>
        <li><a href="https://doi.org/10.3389/fpsyg.2014.00259">Verkoeijen, P. P. J. L., &amp; Bouwmeester, S. (2014). Is spacing really the “friend of induction”? <i>Frontiers in Psychology, 5</i>, 259.</a></li>''',
quiz='''[
 {q:'What share of students ranked self-testing as their top strategy?',o:['1%','55%','84%'],a:0,f:'55% ranked rereading first.'},
 {q:'After a week, students who practised recalling a passage remembered…',o:['56%, against 42% for rereaders','Less than rereaders','The same'],a:0,f:'Rereaders did slightly better after five minutes.'},
 {q:'After learning painters’ styles, most students believed…',o:['Blocking helped more, though mixing worked better','Mixing helped more','Both were equal'],a:0,f:'78% believed blocking helped more.'}]''',
js=BASE+r'''
/* ---------- reread or recall? ----------
   10 Swahili-English pairs; 5 assigned to reread (R), 5 to recall practice (T).
   Phase 1: each pair once (3.5 s). Phase 2 (mixed order): R pairs shown again (3.5 s); T: cue only, type the meaning, then feedback (2 s).
   Predict how many of each 5 you'll recall; 30 s break; final cued test of all 10. */
const WP=[['nyumba','house'],['kitabu','book'],['maji','water'],['chakula','food'],['rafiki','friend'],['mlima','mountain'],['ndege','bird'],['samaki','fish'],['mti','tree'],['jua','sun']];
let wr=null;
const ww=ms=>new Promise(r=>{wr.tm=setTimeout(r,ms)});
const ok=(v,e)=>toks(v).some(t=>match(t,e));
function wType(q,label){return new Promise(res=>{wr.res=res;$('wQ').textContent=q;$('wIL').textContent=label;$('wI').value='';$('wF').hidden=false;$('wI').focus()})}
$('wF').addEventListener('submit',e=>{e.preventDefault();if(!wr||!wr.res)return;const r=wr.res;wr.res=null;$('wF').hidden=true;r($('wI').value.trim())});
function wPick(q){return new Promise(res=>{wr.pres=res;$('wQ').textContent=q;const b=$('wB');b.innerHTML=[0,1,2,3,4,5].map(n=>`<button class="nbtn${n===3?'':' ghost'}" type="button" data-v="${n}">${n}</button>`).join('');b.hidden=false;b.querySelector('[data-v="3"]').focus()})}
$('wB').addEventListener('click',e=>{const b=e.target.closest('button');if(!b||!wr||!wr.pres)return;const r=wr.pres;wr.pres=null;$('wB').hidden=true;r(+b.dataset.v)});
const show=([s,e])=>{$('wPair').innerHTML=`${s} = <span>${e}</span>`};
$('wGo').addEventListener('click',async()=>{if(wr)return;wr={};const g=$('wGo');g.disabled=true;g.textContent='In progress';$('wRes').innerHTML='';$('wFb').textContent='';
 const P=shuf([...WP]).map((p,i)=>({s:p[0],e:p[1],m:i<5?'R':'T'}));
 $('wPhase').textContent='Study';$('wTitle').textContent='First look';$('wText').textContent='Each word once. Just read it.';
 for(const [i,p] of shuf([...P]).entries()){$('wProg').textContent=`Word ${i+1} of 10`;$('wQ').textContent='Swahili = English';show([p.s,p.e]);await ww(3500);if(!wr)return}
 $('wPair').textContent='';$('wPhase').textContent='Second pass';$('wTitle').textContent='Reread or recall';$('wText').textContent='Some words you’ll see again. For others, type the meaning first.';
 for(const [i,p] of shuf([...P]).entries()){$('wProg').textContent=`Word ${i+1} of 10`;
  if(p.m==='R'){$('wQ').textContent='Read it again';show([p.s,p.e]);await ww(3500);if(!wr)return}
  else{$('wPair').textContent=p.s+' = ?';const v=await wType('What does it mean?',`English meaning of ${p.s}`);if(!wr)return;show([p.s,p.e]);$('wFb').innerHTML=ok(v,p.e)?'<b class="ok">Right.</b>':`<b class="no">It means “${p.e}”.</b>`;await ww(2000);if(!wr)return;$('wFb').textContent=''}}
 $('wPair').textContent='';$('wProg').textContent='';$('wPhase').textContent='Predict';$('wTitle').textContent='How many will you remember?';$('wText').textContent='You’ll be tested in about half a minute.';
 const pr=await wPick('Of the 5 words you simply reread, how many will you remember?');if(!wr)return;
 const pt=await wPick('Of the 5 words you practised recalling, how many will you remember?');if(!wr)return;
 $('wPhase').textContent='Short break';$('wTitle').textContent='30 seconds';$('wText').textContent='A short gap before the test.';$('wQ').textContent='Count backwards from 100 in sevens, in your head.';
 const c=$('wC');c.hidden=false;for(let s=30;s>0;s--){c.textContent=s;await ww(1000);if(!wr)return}c.hidden=true;
 $('wPhase').textContent='Test';$('wTitle').textContent='All ten';$('wText').textContent='Type the English meaning. Guess if you’re not sure.';
 let ar=0,at=0;const miss=[];
 for(const [i,p] of shuf([...P]).entries()){$('wProg').textContent=`Word ${i+1} of 10`;$('wPair').textContent=p.s+' = ?';const v=await wType('What does it mean?',`English meaning of ${p.s}`);if(!wr)return;if(ok(v,p.e)){if(p.m==='R')ar++;else at++}else miss.push(`${p.s} = ${p.e}`)}
 $('wPair').textContent='';$('wProg').textContent='';$('wQ').textContent='Done.';$('wPhase').textContent='Your results';
 $('wRes').innerHTML=`<div class="res wl2"><p class="gh">Reread (out of 5)</p>${barRow('You predicted',pr,5,String(pr),'#C9D3E3')}${barRow('You got',ar,5,String(ar),'#FCB316')}<p class="gh">Recall practice (out of 5)</p>${barRow('You predicted',pt,5,String(pt),'#C9D3E3')}${barRow('You got',at,5,String(at),'#7DD3A8')}</div>`+(miss.length?`<p class="mtext">Missed: ${miss.join('; ')}.</p>`:'');
 let title,text;
 if(pr>pt&&at>=ar){title='The fluency illusion';text=`You expected rereading to work better (${pr} against ${pt}), but recall practice did at least as well (${at} against ${ar}). Seeing the answer again felt like learning; producing it actually was.`}
 else if(ar>at){title='Rereading won, for now';text=`Rereading did better today (${ar} against ${at}). That matches the classic study, where rereaders were slightly ahead after five minutes. After a week, the recall group remembered 56% against 42%. The test that matters comes later.`}
 else if(pt>pr){title='You trusted recall';text=`You predicted recall practice would win (${pt} against ${pr}), and got ${at} against ${ar}. Most students rank rereading first; only 1% rank self-testing first.`}
 else{title='Neck and neck';text=`Reread: ${ar} of 5; recall practice: ${at} of 5, after only half a minute. Over a week, the gap opens up: 56% against 42% in the classic study.`}
 if(pr-ar>=2)text+=` You expected ${pr} of the reread words and got ${ar}: familiar felt like learned.`;
 $('wTitle').textContent=title;$('wText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();wr=null});
'''+cls_js("{F:'Fluency trap',R:'Real test'}",'''[
 ['Rereading your highlighted notes the night before','F','Fluency trap: it feels familiar because you’ve just seen it.'],
 ['Closing the book and writing down everything you remember','R','Real test: you have to produce it from memory.'],
 ['Looking at a worked solution and thinking “yes, I get it”','F','Fluency trap: following a solution is not the same as producing one.'],
 ['Covering the answers on a flashcard and saying them before you flip','R','Real test: recall first, then check.'],
 ['Doing practice questions on mixed topics, without notes','R','Real test: you have to recall, and choose which method applies.'],
 ['Watching the lecture recording again at double speed','F','Fluency trap: it all looks familiar the second time.'],
 ['Explaining a concept out loud to a friend, without notes','R','Real test: explaining reveals what you can and can’t recall.'],
 ['Copying your notes out neatly','F','Fluency trap: rewriting can be done without recalling anything.']]''','Fluency trap or real test?',r'''
 if(right>=7){title='You can spot the trap';text=`${right} of 8 right. If you can see the answer while you study, it will feel easier than it is. Make yourself produce it.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Ask: do I have to produce the answer from memory, or is it in front of me?`}
 else{title='Worth another look';text=`${right} of 8 right. Rereading, reviewing and copying feel productive because the material looks familiar. Real tests make you recall it.`}'''))
open('h08/template.html','w').write(page(o))

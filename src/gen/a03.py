import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='a03',n='3',label='The Learning Brain · Generative AI · Topic 3',epi='The Learning Brain, Generative AI, episode 3',
title='The Jagged Frontier: Where AI Helps and Where It Misleads',h1='The jagged frontier',em='Real, but invisible',read='7',mins='2 minutes',vtitle='The jagged frontier',
dek='On some tasks AI makes people much faster and better; on others that look just as hard, it makes them worse, and sounds just as confident. Finding the edge is now part of learning.',
jumps='<span><a href="#jT">Accept or check?</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc'],labels:['pfc'],labelT:{pfc:0.8},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.qq{font:600 clamp(18px,2.2vw,21px)/1.45 var(--body);color:#fff;max-width:42ch;margin:0}
.ai{background:#0F2240;border:1px solid #3A4E72;border-radius:10px;padding:12px 14px;max-width:42ch;width:100%;margin:0;color:#E9EEF6;font-size:18px;line-height:1.45}
.ai b{display:block;font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#FCB316;margin-bottom:4px}
.ai[hidden]{display:none}
.jb{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}
.jb[hidden]{display:none}
.gin{display:flex;gap:10px;align-items:center;justify-content:center;flex-wrap:wrap}
.gin[hidden]{display:none}
.gin input{width:180px;min-height:50px;font:700 20px var(--body);text-align:center;border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff}
.gin input:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.gfb{font:600 17px/1.45 var(--body);color:#E9EEF6;min-height:1.5em;margin:0;text-align:center;max-width:42ch}
.gfb b.ok{color:#7DD3A8}.gfb b.no{color:#FFB38A}
.rlist{margin:8px 0 14px;padding-left:20px;color:#E9EEF6;font-size:16px;line-height:1.5}''',
body='''  <div class="col lede">
    <p>In 2023, Fabrizio Dell’Acqua, Ethan Mollick, Karim Lakhani and colleagues gave 758 consultants at a global firm realistic tasks, some with an AI model and some without. On tasks inside the AI’s abilities, those with AI finished 12% more tasks, a quarter faster, at more than 40% higher quality.</p>
    <p>But one task was chosen to sit just outside what the AI could do. There, consultants using AI were 19 percentage points less likely to get the right answer. The tool sounded just as confident.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>758</strong><span>consultants in a pre-registered experiment</span></div>
      <div role="listitem"><strong>+40%</strong><span>quality on tasks inside the frontier</span></div>
      <div role="listitem"><strong>−19 points</strong><span>in correct answers on a task just outside it</span></div>
      <div role="listitem"><strong>+34%</strong><span>productivity for novice support agents, with little effect for experts</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">A jagged frontier</span>The line is invisible from the inside</h2>
    <p>The researchers called this a jagged frontier. Tasks that look equally hard can fall on either side, and the line is invisible from the inside.</p>
  </div>

  <section class="night" aria-labelledby="jT">
    <div class="col">
      <h2 class="sec" id="jT"><span class="n">Try it</span>Accept or check?</h2>
      <p>A simulated assistant answers eight short questions, confidently. The answers were written for this page, not produced by a real AI, and some may be wrong. For each, accept the answer or work it out yourself. About 3 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="jScreen">
          <p class="qq" id="jQ" aria-live="polite">Press Start.</p>
          <p class="ai" id="jA" hidden></p>
          <div class="jb" id="jB" hidden><button class="nbtn" type="button" data-v="a">Accept</button><button class="nbtn ghost" type="button" data-v="c">Check it myself</button></div>
          <form class="gin" id="jGen" hidden><label class="sr-only" for="jGi">Your own answer</label><input id="jGi" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="Your answer"><button class="nbtn" type="submit">OK</button></form>
          <p class="gfb" id="jFb" aria-live="polite"></p>
          <div class="mrow" style="justify-content:center"><button class="nbtn ghost" id="jNext" type="button" hidden>Next question</button></div>
          <p class="prog" id="jProg" aria-live="polite"></p>
        </div>
        <div>
          <p class="phase" id="jPhase">Ready</p>
          <p class="mtitle" id="jTitle">Where is the edge?</p>
          <p class="mtext" id="jText" aria-live="polite">Accepting is quick. Checking takes effort. You decide, question by question.</p>
          <div id="jRes"></div>
          <div class="mrow"><button class="nbtn" id="jGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Levelling</span>Novices gain most, and see least</h2>
    <p>AI also levels skill. Consultants below average improved by 43%, those above by 17%. In a study of 5,179 customer-support agents, Erik Brynjolfsson, Danielle Li and Lindsey Raymond found that AI raised productivity by 14% overall and by 34% for novices, with little effect for experts.</p>
    <p>For learning, that levelling cuts two ways. Novices gain the most performance, and they are also the least able to tell when the AI is wrong.</p>
    <h2 class="sec"><span class="n">Centaurs and cyborgs</span>Two ways that worked</h2>
    <p>Successful users worked in two ways. Centaurs split the task, deciding what to hand off. Cyborgs worked in constant back-and-forth. Both kept judging the output.</p>
    <h2 class="sec"><span class="n">A caution</span>Performance, not learning</h2>
    <p>These are workplace studies of performance, not learning, using models from 2023. The frontier has moved since, and it is still jagged.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Teach students to find the edge</h3>
      <p>Map your own assignments against the frontier: where does AI help, and where does it mislead? Give students one task deliberately outside it, so they learn to spot the edge. And require a check step before any AI answer is accepted.</p>
    </aside>
  </div>
''',
tips_h='The frontier is real, but invisible',
tips='''      <li><b>Map your assignments</b><span>Where does AI help, and where does it mislead?</span></li>
      <li><b>One task outside the frontier</b><span>So students learn to spot the edge.</span></li>
      <li><b>A check step, always</b><span>Before any AI answer is accepted.</span></li>''',
sources='''        <li><a href="https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf">Dell’Acqua, F., McFowland, E., Mollick, E., et al. (2023). Navigating the jagged technological frontier: Field experimental evidence of the effects of AI on knowledge worker productivity and quality. <i>Harvard Business School Working Paper 24-013</i>.</a></li>
        <li><a href="https://www.nber.org/papers/w31161">Brynjolfsson, E., Li, D., &amp; Raymond, L. R. (2023). Generative AI at work. <i>NBER Working Paper 31161</i>.</a></li>''',
quiz='''[
 {q:'On the task chosen to sit just outside the AI’s abilities, consultants using AI…',o:['Were 19 percentage points less likely to be right','Did better','Did the same'],a:0,f:'The tool sounded just as confident.'},
 {q:'Who gained most from AI help?',o:['Novices and below-average workers','Experts','Everyone equally'],a:0,f:'And novices are least able to tell when the AI is wrong.'},
 {q:'What did successful users, centaurs and cyborgs alike, keep doing?',o:['Judging the output','Accepting every answer','Avoiding AI'],a:0,f:'Require a check step before any AI answer is accepted.'}]''',
js=BASE+r'''
/* ---------- accept or check? ----------
   8 questions with simulated, confident answers (written for this page). Two are wrong (classic trick questions).
   Accept, or check by entering your own answer. Then the correct answer is shown (after checking) or at the end (if accepted). */
const QS=[
 ['What is 15% of 80?','15% of 80 is 12.',1,['12'],'12. 10% is 8, and 5% is 4.'],
 ['A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost?','The ball costs 10 cents.',0,['5','0.05','.05','$0.05','5c','5 cents','five cents','five'],'5 cents. If the ball were 10 cents, the bat would be $1.10 and the total $1.20.'],
 ['How many days are there in a leap year?','A leap year has 366 days.',1,['366'],'366.'],
 ['If 5 machines take 5 minutes to make 5 widgets, how long would 100 machines take to make 100 widgets?','100 machines would take 100 minutes.',0,['5','5 minutes','five','five minutes'],'5 minutes. Each machine makes one widget in 5 minutes, however many machines there are.'],
 ['How many minutes are there in 3 hours and 15 minutes?','That is 195 minutes.',1,['195'],'195.'],
 ['What comes next: 2, 4, 8, 16, …?','The next number is 32.',1,['32'],'32. Each number doubles.'],
 ['Rearrange the letters of LISTEN to make another word.','SILENT.',1,['silent','enlist','tinsel','inlets'],'SILENT works; so do ENLIST and TINSEL.'],
 ['A patch of lily pads doubles in size every day. It takes 48 days to cover the lake. How long to cover half the lake?','It takes 47 days.',1,['47','47 days'],'47 days. It doubles to cover the whole lake on the last day.']];
const norm=v=>v.toLowerCase().replace(/\s+/g,' ').replace(/[^a-z0-9.$ ]/g,'').trim();
let jr=null;
function choose(){return new Promise(res=>{jr.res=res;const b=$('jB');b.hidden=false;b.querySelector('button').focus()})}
$('jB').addEventListener('click',e=>{const b=e.target.closest('button');if(!b||!jr||!jr.res)return;const r=jr.res;jr.res=null;$('jB').hidden=true;r(b.dataset.v)});
function ask(){return new Promise(res=>{jr.gres=res;$('jGen').hidden=false;$('jGi').value='';$('jGi').focus()})}
$('jGen').addEventListener('submit',e=>{e.preventDefault();if(!jr||!jr.gres)return;const r=jr.gres;jr.gres=null;$('jGen').hidden=true;r(norm($('jGi').value))});
function next(label){return new Promise(res=>{const b=$('jNext');b.textContent=label;b.hidden=false;b.focus();b.onclick=()=>{b.onclick=null;b.hidden=true;res()}})}
$('jGo').addEventListener('click',async()=>{if(jr)return;jr={};const g=$('jGo');g.disabled=true;g.textContent='In progress';$('jRes').innerHTML='';
 const order=shuf([...QS]);let acc=0,chk=0,accWrong=[],caught=0,fooled=0,right=0;
 $('jPhase').textContent='Accept or check';$('jTitle').textContent='Your call';
 for(let i=0;i<order.length;i++){const [q,a,ok,good,ex]=order[i];$('jProg').textContent=`Question ${i+1} of 8`;$('jQ').textContent=q;$('jA').innerHTML=`<b>Assistant</b>${a}`;$('jA').hidden=false;$('jFb').textContent='';
  const c=await choose();if(!jr)return;
  if(c==='a'){acc++;if(ok)right++;else accWrong.push([q,ex]);$('jFb').textContent='Accepted.'}
  else{chk++;const v=await ask();if(!jr)return;const mine=good.some(x=>norm(x)===v);if(mine)right++;
   if(!ok&&mine)caught++;if(!ok&&!mine)fooled++;
   $('jFb').innerHTML=(mine?'<b class="ok">Your answer is right.</b> ':'<b class="no">Not quite.</b> ')+(ok?'The assistant was right too. ':'<b class="no">The assistant was wrong.</b> ')+'The answer: '+ex}
  if(i<7){await next('Next question');if(!jr)return}}
 $('jQ').textContent='Done.';$('jA').hidden=true;$('jFb').textContent='';$('jProg').textContent='';$('jPhase').textContent='Your results';
 const W=accWrong.length;
 $('jRes').innerHTML=`<div class="res wl2"><p class="gh">Out of 8</p>${barRow('Accepted',acc,8,acc+' of 8','#C9D3E3')}${barRow('Checked',chk,8,chk+' of 8','#FCB316')}${barRow('Right in the end',right,8,right+' of 8','#7DD3A8')}</div>`+(W?`<p class="gh" style="color:#FFB38A">Wrong answers you accepted</p><ul class="rlist">${accWrong.map(([q,ex])=>`<li>${q} <b>${ex}</b></li>`).join('')}</ul>`:'');
 let title,text;
 if(W===2){title='Both wrong answers got through';text=`You accepted ${acc} answers, including both wrong ones. They sounded as confident as the right ones, and the questions looked no harder. That is the jagged frontier: the edge is invisible from the inside.`}
 else if(W===1){title='One wrong answer got through';text=`You accepted ${acc} answers, and one of them was wrong. You checked ${chk}.`+(caught?` Checking caught ${caught===1?'one wrong answer':'the other'}.`:'')+' Nothing in the tone told the right answers from the wrong ones.'}
 else if(fooled>0){title='You checked, but the trick got you';text=`You didn’t accept any wrong answers, but when you checked, ${fooled===1?'one of the trick questions':'the trick questions'} led you to the same wrong answer as the assistant. Checking only helps when you know enough to check. Two of the questions are classic traps.`}
 else if(chk===8){title='Careful, and slow';text=`You checked all 8 and caught both wrong answers. That works, but checking everything costs time. The skill is knowing where the edge is likely to be, and checking there.`}
 else{title='You found the edge';text=`You accepted ${acc}, checked ${chk}, and let no wrong answers through. Two of the eight were wrong, written as confidently as the rest.`}
 $('jTitle').textContent=title;$('jText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();jr=null});
'''+grid('''[
 ['Consultants with AI, on tasks inside its abilities',['Finished 12% more tasks, faster, at over 40% higher quality','Did about the same','Did worse'],0,'Dell’Acqua and colleagues, 2023.'],
 ['On a task just outside the AI’s abilities',['19 percentage points less likely to be right','Slightly better','The same'],0,'The tool sounded just as confident.'],
 ['Consultants below average, with AI',['Improved by 43%','Improved by 17%','Didn’t improve'],0,'Those above average improved by 17%.'],
 ['Novice customer-support agents with AI',['34% more productive','Less productive','No change'],0,'With little effect for experts.'],
 ['Who is least able to tell when the AI is wrong?',['Novices','Experts','Everyone equally'],0,'Levelling cuts two ways for learners.'],
 ['These studies measured…',['Workplace performance, with 2023 models','Long-term learning','Children’s learning'],0,'The frontier has moved since, and it is still jagged.']]''','The pattern: AI helps a lot inside the frontier and misleads just outside it, so checking is part of the job.'))
open('a03/template.html','w').write(page(o))

import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='h02',n='2',label='The Learning Brain · Habits of the Learner · Topic 2',epi='The Learning Brain, Habits of the Learner, episode 2',
title='Sleep on a Schedule: Why Timing Matters, Not Just Hours',h1='Sleep on a schedule',em='Your body clock likes routine',read='7',mins='2 minutes',vtitle='Sleep on a schedule',
dek='Two students each sleep about seven hours a night. One keeps a steady schedule; the other doesn’t. The research says timing matters, not just hours.',
jumps='<span><a href="#sT">Score your sleep week</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the hippocampus, deep inside, and the brainstem, at the base, glowing orange and labelled.',
hero_js="BR.R.hip.lab=[560,-70];BR.R.hip.al='left';BR.R.stem.lab=[520,735];BR.R.stem.al='right';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['hip','stem'],labels:['hip','stem'],labelT:{hip:0.8,stem:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.wk{width:100%;max-width:560px;border-collapse:collapse;color:#E9EEF6;font-size:16px}
.wk th{font:800 12px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#C9D3E3;text-align:left;padding:4px 6px}
.wk td{padding:3px 6px}
.wk select{min-height:40px;font:600 16px var(--body);border-radius:8px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;padding:0 4px;width:100%}
@media (max-width:520px){.wk select{font-size:14px;padding:0 1px}.wk th,.wk td{padding:3px 2px}.wk td.hrs{font-size:14px}}
.wk select:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.wk td.hrs{font-weight:700;color:#FCB316;white-space:nowrap}
.jb{display:flex;gap:8px;flex-wrap:wrap;justify-content:center}
.sbar{width:100%;max-width:560px;display:block;height:auto}''',
body='''  <div class="col lede">
    <p>Two students each sleep about seven hours a night. One goes to bed at a different time every night. The other keeps a steady schedule. Who does better? The research says timing matters, not just hours.</p>
    <p>At Harvard, Andrew Phillips and colleagues followed 61 undergraduates for 30 days with sleep diaries, and scored how regular each person’s sleep was from one day to the next. More regular sleepers tended to earn higher grades.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>61</strong><span>Harvard undergraduates, 30 days of sleep diaries</span></div>
      <div role="listitem"><strong>~2.5 hours</strong><span>later melatonin release in the most irregular sleepers</span></div>
      <div role="listitem"><strong>88</strong><span>MIT chemistry students wearing activity trackers for a semester</span></div>
      <div role="listitem"><strong>~25%</strong><span>of the variation in their scores went with sleep measures</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The body clock</span>A 9 a.m. class at 6 a.m.</h2>
    <p>The surprise was the body clock. In the most irregular sleepers, the sleep hormone melatonin was released about two and a half hours later. So a 9 a.m. class could feel more like 6 a.m. And their average sleep length was not significantly different.</p>
    <p>The likely driver was light. Regular sleepers got brighter light during the day and less light at night, which keeps the body clock anchored.</p>
  </div>

  <section class="night" aria-labelledby="sT">
    <div class="col">
      <h2 class="sec" id="sT"><span class="n">Try it</span>Score your sleep week</h2>
      <p>Compare two example students who both sleep seven hours a night, then enter a typical week of your own. The page scores how regular the week is, from 0 to 100, using a simplified version of the study’s sleep regularity index. Nothing you enter leaves this page.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="sScreen">
          <div class="jb" role="group" aria-label="Load a week"><button class="nbtn" type="button" id="sA">Steady student</button><button class="nbtn ghost" type="button" id="sB">Irregular student</button><button class="nbtn ghost" type="button" id="sMine">My week</button></div>
          <table class="wk"><caption class="sr-only">Bedtime and wake time for each night</caption><thead><tr><th scope="col">Night</th><th scope="col">Bed</th><th scope="col">Wake</th><th scope="col">Sleep</th></tr></thead><tbody id="sRows"></tbody></table>
        </div>
        <div>
          <p class="phase" id="sPhase">Your week</p>
          <p class="mtitle" id="sTitle">Pick a week to score</p>
          <p class="mtext" id="sText" aria-live="polite">Start with the two example students, then try your own.</p>
          <div id="sRes"></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">MIT</span>The week, not the night before</h2>
    <p>At MIT, Kana Okano and colleagues gave activity trackers to 88 chemistry students for a semester. Better quality, longer and more consistent sleep all went with better grades. Together, sleep measures accounted for nearly a quarter of the variation in scores.</p>
    <p>And the night before a test? It showed no relation to that test’s score. Sleep across the week and the month before is what tracked with grades. Going to bed after about 2 a.m. also went with lower scores, even with the same hours.</p>
    <h2 class="sec"><span class="n">A caution</span>Correlations at two universities</h2>
    <p>Both studies are correlations, each at a single university. Students who sleep regularly may differ in other ways too. But regular timing is cheap, safe, and in your control.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Try this</h3>
      <p>Pick a wake time you can keep seven days a week, weekends included. Get daylight soon after you wake. Dim screens and lights in the last hour before bed. And protect your sleep across the whole week before an exam, not just the night before.</p>
    </aside>
  </div>
''',
tips_h='Your body clock likes routine. Give it one.',
tips='''      <li><b>One wake time, seven days</b><span>Weekends included.</span></li>
      <li><b>Light by day, dim by night</b><span>Daylight soon after waking; dim screens before bed.</span></li>
      <li><b>Protect the whole week</b><span>Not just the night before an exam.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1038/s41598-017-03171-4">Phillips, A. J. K., Clerx, W. M., O’Brien, C. S., et al. (2017). Irregular sleep/wake patterns are associated with poorer academic performance and delayed circadian and sleep/wake timing. <i>Scientific Reports, 7</i>, 3216.</a></li>
        <li><a href="https://doi.org/10.1038/s41539-019-0055-z">Okano, K., Kaczmarzyk, J. R., Dave, N., Gabrieli, J. D. E., &amp; Grossman, J. C. (2019). Sleep quality, duration, and consistency are associated with better academic performance in college students. <i>npj Science of Learning, 4</i>, 16.</a></li>''',
quiz='''[
 {q:'In the most irregular sleepers, melatonin was released…',o:['About two and a half hours later','At the same time','Earlier'],a:0,f:'So a 9 a.m. class could feel like 6 a.m.'},
 {q:'Sleep on the night before a test…',o:['Showed no relation to that test’s score','Was the best predictor','Mattered more than the month before'],a:0,f:'Sleep across the week and month before tracked with grades.'},
 {q:'What likely keeps the body clock anchored?',o:['Bright light by day, less light at night','Sleeping in on weekends','Caffeine'],a:0,f:'Regular sleepers got more daytime light and less at night.'}]''',
js=BASE+r'''
/* ---------- score your sleep week ----------
   7 nights, bed and wake in 30-minute steps. Times stored as minutes after noon.
   Simplified SRI: each night is a 24 h window from noon (48 slots); compare slot by slot with the next night
   (6 pairs); SRI = 200*agreement - 100, clamped to 0..100. Also average hours, and weekend shift of mid-sleep. */
const NIGHTS=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
const NN=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
const fmt=m=>{const t=(m+720)%1440,h=Math.floor(t/60),mi=t%60;return `${h===0?12:h>12?h-12:h}:${mi?'30':'00'} ${t<720?'am':'pm'}`};
const BEDS=[];for(let m=480;m<=960;m+=30)BEDS.push(m);   /* 8 p.m. to 4 a.m. */
const WAKES=[];for(let m=960;m<=1500;m+=30)WAKES.push(m);/* 4 a.m. to 1 p.m. */
const PRE={A:Array(7).fill([690,1110]),B:[[750,1170],[660,1080],[840,1260],[690,1110],[810,1230],[900,1320],[870,1290]]};
let mine=Array(7).fill([690,1170]);
$('sRows').innerHTML=NIGHTS.map((d,i)=>`<tr><th scope="row">${d}</th><td><label class="sr-only" for="b${i}">${NN[i]} night, bedtime</label><select id="b${i}">${BEDS.map(m=>`<option value="${m}">${fmt(m)}</option>`).join('')}</select></td><td><label class="sr-only" for="w${i}">${NN[i]} night, wake time</label><select id="w${i}">${WAKES.map(m=>`<option value="${m}">${fmt(m)}</option>`).join('')}</select></td><td class="hrs" id="h${i}"></td></tr>`).join('');
let cur='A';
function load(W){W.forEach(([b,w],i)=>{$('b'+i).value=b;$('w'+i).value=w});score()}
function read(){return NIGHTS.map((_,i)=>[+$('b'+i).value,+$('w'+i).value])}
function score(){const W=read();
 W.forEach(([b,w],i)=>{const h=(w-b)/60;$('h'+i).textContent=h>0?(h%1?h.toFixed(1):h)+' h':'—'});
 if(W.some(([b,w])=>w<=b)){$('sTitle').textContent='Check the times';$('sText').textContent='Each wake time needs to be after the bedtime.';$('sRes').innerHTML='';return}
 const slots=W.map(([b,w])=>Array.from({length:48},(_,k)=>{const t=k*30+15;return t>b&&t<w}));
 let agree=0,tot=0;for(let d=0;d<6;d++)for(let k=0;k<48;k++){tot++;if(slots[d][k]===slots[d+1][k])agree++}
 const sri=Math.max(0,Math.min(100,Math.round(200*agree/tot-100)));
 const avg=W.reduce((s,[b,w])=>s+(w-b),0)/7/60;
 const mid=([b,w])=>(b+w)/2;const wkday=[0,1,2,3,4].map(i=>mid(W[i])).reduce((a,c)=>a+c,0)/5,wkend=[5,6].map(i=>mid(W[i])).reduce((a,c)=>a+c,0)/2;
 const shift=(wkend-wkday)/60;const late=W.filter(([b])=>b>840).length;
 const who=cur==='A'?'The steady student':cur==='B'?'The irregular student':'Your week';
 $('sRes').innerHTML=`<div class="res wl2"><p class="gh">${who}</p>${barRow('Regularity',sri,100,sri+' of 100','#7DD3A8')}${barRow('Average sleep',avg,10,(Math.round(avg*10)/10)+' h','#FCB316')}${barRow('Weekend shift',Math.max(0,Math.abs(shift)),4,(Math.round(Math.abs(shift)*10)/10)+' h','#FFB38A')}</div>`;
 let title,text;
 if(sri>=80){title='Steady';text=`A regularity score of ${sri}. Going to bed and waking at about the same time keeps the body clock anchored.`}
 else if(sri>=50){title='Somewhat irregular';text=`A regularity score of ${sri}. Some nights start or end at quite different times. In the Harvard study, more irregular sleepers had later body clocks, which makes morning classes harder.`}
 else{title='Irregular';text=`A regularity score of ${sri}. In the Harvard study, the most irregular sleepers released melatonin about two and a half hours later, so morning classes fell in their biological night.`}
 if(cur==='B')text+=' The same seven hours a night as the steady student: only the timing differs.';
 if(avg<7)text+=` The average is ${Math.round(avg*10)/10} hours, which is on the short side for most young adults.`;
 if(Math.abs(shift)>=1.5)text+=` Your sleep shifts by about ${Math.round(Math.abs(shift)*10)/10} hours at the weekend, like flying across time zones every Friday.`;
 if(late)text+=` ${late===1?'One night starts':late+' nights start'} after 2 a.m.; in the MIT study, bedtimes after about 2 a.m. went with lower scores, even with the same hours.`;
 $('sTitle').textContent=title;$('sText').textContent=text}
$('sRows').addEventListener('change',()=>{if(cur!=='M'){cur='M';mine=read();setBtn()}else mine=read();score()});
function setBtn(){[['sA','A'],['sB','B'],['sMine','M']].forEach(([id,k])=>{const b=$(id);b.classList.toggle('ghost',cur!==k);b.setAttribute('aria-pressed',cur===k)});$('sPhase').textContent=cur==='M'?'Your week':cur==='A'?'Example: steady':'Example: irregular'}
$('sA').addEventListener('click',()=>{cur='A';setBtn();load(PRE.A)});
$('sB').addEventListener('click',()=>{cur='B';setBtn();load(PRE.B)});
$('sMine').addEventListener('click',()=>{cur='M';setBtn();load(mine);$('b0').focus()});
cur='A';setBtn();load(PRE.A);
'''+grid('''[
 ['Regular sleepers at Harvard, compared with irregular ones, tended to…',['Earn higher grades','Earn lower grades','Do the same'],0,'Phillips and colleagues, 2017.'],
 ['In the most irregular sleepers, melatonin was released…',['About two and a half hours later','About the same time','Earlier'],0,'A 9 a.m. class could feel like 6 a.m.'],
 ['Did irregular sleepers sleep fewer hours on average?',['Not significantly','Yes, about two hours fewer','Yes, about one hour fewer'],0,'Timing differed, not total sleep.'],
 ['At MIT, sleep measures accounted for about what share of the variation in scores?',['Nearly a quarter','Almost none','About three quarters'],0,'Okano and colleagues, 2019.'],
 ['Sleep on the night before a test…',['Showed no relation to that test’s score','Mattered most','Mattered only for maths'],0,'The week and month before tracked with grades.'],
 ['Going to bed after about 2 a.m.…',['Went with lower scores, even with the same hours','Made no difference','Went with higher scores'],0,'Timing again.']]''','The pattern: when you sleep, and how regularly, matters alongside how long, across the whole week.'))
open('h02/template.html','w').write(page(o))

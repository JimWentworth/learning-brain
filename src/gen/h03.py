import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='h03',n='3',label='The Learning Brain · Habits of the Learner · Topic 3',epi='The Learning Brain, Habits of the Learner, episode 3',
title='Larks, Owls and 8 a.m.: Chronotype and Learning',h1='Larks, owls and 8 a.m.',em='Know your clock, then work with it',read='7',mins='2 minutes',vtitle='Larks, owls and 8 a.m.',
dek='Some people wake up sharp; others hit their stride late at night. Among university students, owls are common, and early classes hit them hardest.',
jumps='<span><a href="#kT">Lark or owl?</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, and the brainstem, at the base, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.stem.lab=[520,735];BR.R.stem.al='right';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc','stem'],labels:['pfc','stem'],labelT:{pfc:0.8,stem:1.0},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.kform{display:grid;gap:12px;width:100%;max-width:560px}
.kform fieldset{border:1px solid #3A4E72;border-radius:10px;padding:8px 12px 12px;margin:0;display:grid;grid-template-columns:1fr 1fr;gap:8px 12px}
.kform legend{font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#FCB316;padding:0 6px}
.kform label{display:block;font:600 14px var(--body);color:#C9D3E3}
.kform select{display:block;width:100%;margin-top:4px;min-height:42px;font:600 16px var(--body);border-radius:8px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;padding:0 6px}
.kform select:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.kscale{width:100%;max-width:560px;height:auto;display:block}
.kscale[hidden]{display:none}''',
body='''  <div class="col lede">
    <p>Some people wake up sharp. Others hit their stride late at night. Researchers call this your chronotype: lark, owl, or somewhere in between. Among university students, owls are common, and evening types usually outnumber morning types.</p>
    <p>At the National University of Singapore, Sing Chen Yeo, Joshua Gooley and colleagues used Wi-Fi logs to estimate lecture attendance for more than 23,000 students. Attendance at 8 a.m. classes was about 10 percentage points lower than at later times.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>23,391</strong><span>students whose Wi-Fi logs showed class attendance</span></div>
      <div role="listitem"><strong>~10 points</strong><span>lower attendance at 8 a.m. than at later times</span></div>
      <div role="listitem"><strong>~1 hour</strong><span>less sleep before an early class</span></div>
      <div role="listitem"><strong>33,818</strong><span>students: more days with morning classes went with lower grades</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Early classes</span>Less sleep, lower grades</h2>
    <p>Watch data from 181 students showed about an hour less sleep before an early class, because they woke earlier than usual. And across nearly 34,000 students, the more days a week they had morning classes, the lower their grade point average tended to be.</p>
    <h2 class="sec"><span class="n">Owls</span>Timing hits owls hardest</h2>
    <p>In Dutch high schools, Vincent van der Vinne, Giulia Zerbini and colleagues found that late chronotypes did worse on early-morning exams, but the gap shrank later in the day. Lab studies call this the synchrony effect: demanding tasks tend to go best at your own peak time.</p>
  </div>

  <section class="night" aria-labelledby="kT">
    <div class="col">
      <h2 class="sec" id="kT"><span class="n">Try it</span>Lark or owl?</h2>
      <p>Enter when you usually fall asleep and wake up, on days with and without an alarm. The page estimates your chronotype from the middle of your sleep on free days, the measure researchers often use. It’s a rough guide, not a diagnosis. Nothing you enter leaves this page.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="kScreen">
          <form class="kform" id="kF">
            <fieldset><legend>Days with an alarm (classes, work)</legend>
              <label for="kWs">Fall asleep<select id="kWs"></select></label>
              <label for="kWw">Wake up<select id="kWw"></select></label>
            </fieldset>
            <fieldset><legend>Free days (no alarm)</legend>
              <label for="kFs">Fall asleep<select id="kFs"></select></label>
              <label for="kFw">Wake up<select id="kFw"></select></label>
            </fieldset>
            <div class="mrow" style="justify-content:center"><button class="nbtn" type="submit">Find my chronotype</button></div>
          </form>
          <svg class="kscale" id="kSvg" viewBox="0 0 560 90" hidden role="img" aria-labelledby="kSvgT"><title id="kSvgT">Where your mid-sleep falls</title></svg>
        </div>
        <div>
          <p class="phase" id="kPhase">Your clock</p>
          <p class="mtitle" id="kTitle">Free days tell the truth</p>
          <p class="mtext" id="kText" aria-live="polite">On days without an alarm, your sleep shows your body clock most clearly.</p>
          <div id="kRes"></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Mostly correlations</h2>
    <p>These are mostly correlations. At one American university, morning types still had slightly better grades even after class times were taken into account. And chronotype can shift, even within a semester.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Try this</h3>
      <p>Notice when you feel sharpest, and put your hardest study there. If you can choose, avoid stacking early classes. If you can’t, keep your wake time steady so the early start hurts less. And save routine tasks for your low hours.</p>
    </aside>
  </div>
''',
tips_h='Know your clock. Then work with it.',
tips='''      <li><b>Hardest work at your peak</b><span>Notice when you feel sharpest.</span></li>
      <li><b>Avoid stacking early classes</b><span>If you can choose.</span></li>
      <li><b>Routine tasks for low hours</b><span>And keep your wake time steady.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1038/s41562-023-01531-x">Yeo, S. C., Lai, C. K. Y., Tan, J., Lim, S., Chandramoghan, Y., Tan, T. K., &amp; Gooley, J. J. (2023). Early morning university classes are associated with impaired sleep and academic performance. <i>Nature Human Behaviour, 7</i>(4), 502–514.</a></li>
        <li><a href="https://doi.org/10.1177/0748730414564786">van der Vinne, V., Zerbini, G., Siersema, A., et al. (2015). Timing of examinations affects school performance differently in early and late chronotypes. <i>Journal of Biological Rhythms, 30</i>(1), 53–60.</a></li>
        <li><a href="https://doi.org/10.1080/07420528.2017.1281287">Enright, T., &amp; Refinetti, R. (2017). Chronotype, class times, and academic achievement of university students. <i>Chronobiology International, 34</i>(4), 445–450.</a></li>''',
quiz='''[
 {q:'Attendance at 8 a.m. classes at NUS was…',o:['About 10 percentage points lower','About the same','Higher'],a:0,f:'From Wi-Fi logs of more than 23,000 students.'},
 {q:'Before an early class, students slept…',o:['About an hour less','About the same','More'],a:0,f:'Because they woke earlier than usual.'},
 {q:'The synchrony effect says demanding tasks go best…',o:['At your own peak time','Always in the morning','Always at night'],a:0,f:'Late chronotypes did worse on early-morning exams.'}]''',
js=BASE+r'''
/* ---------- lark or owl? ----------
   MCTQ-style estimate: mid-sleep on free days (MSF), corrected for catch-up sleep when free-day sleep is longer:
   MSFsc = MSF - (SDf - SDweek)/2, SDweek = (5*SDw + 2*SDf)/7. Times in minutes after noon.
   Bands (rough): before 3:30 a.m. lark-leaning; 3:30-5:00 in between; after 5:00 owl-leaning. Social jet lag = MSF - MSW. */
const fmt=m=>{const t=((m+720)%1440+1440)%1440,h=Math.floor(t/60),mi=Math.round(t%60);return `${h===0?12:h>12?h-12:h}:${String(mi).padStart(2,'0')} ${t<720?'a.m.':'p.m.'}`};
const SL=[];for(let m=480;m<=1020;m+=30)SL.push(m);  /* 8 p.m. - 5 a.m. */
const WK=[];for(let m=960;m<=1560;m+=30)WK.push(m);  /* 4 a.m. - 2 p.m. */
const fill=(id,arr,v)=>{$(id).innerHTML=arr.map(m=>`<option value="${m}">${fmt(m)}</option>`).join('');$(id).value=v};
fill('kWs',SL,720);fill('kWw',WK,1140);fill('kFs',SL,780);fill('kFw',WK,1260);
$('kF').addEventListener('submit',e=>{e.preventDefault();
 const ws=+$('kWs').value,ww=+$('kWw').value,fs=+$('kFs').value,fw=+$('kFw').value;
 if(ww<=ws||fw<=fs){$('kTitle').textContent='Check the times';$('kText').textContent='Each wake time needs to be after the time you fall asleep.';$('kRes').innerHTML='';$('kSvg').hidden=true;return}
 const SDw=ww-ws,SDf=fw-fs,MSW=ws+SDw/2,MSF=fs+SDf/2,SDweek=(5*SDw+2*SDf)/7;
 const MSFsc=SDf>SDw?MSF-(SDf-SDweek)/2:MSF;const sjl=(MSF-MSW)/60;
 const am=MSFsc-720; /* minutes after midnight */
 const X=m=>40+(m-60)/(480-60)*480; /* scale 1 a.m. .. 8 a.m. */
 const x=Math.max(40,Math.min(520,X(am)));
 $('kSvg').innerHTML=`<title id="kSvgT">Your mid-sleep on free days: ${fmt(MSFsc)}</title><rect x="40" y="30" width="${X(210)-40}" height="18" fill="#7DD3A8" opacity=".55"/><rect x="${X(210)}" y="30" width="${X(300)-X(210)}" height="18" fill="#C9D3E3" opacity=".55"/><rect x="${X(300)}" y="30" width="${520-X(300)}" height="18" fill="#FCB316" opacity=".55"/>`+
  `<text x="${(40+X(210))/2}" y="22" text-anchor="middle" font-size="12" fill="#E9EEF6">lark-leaning</text><text x="${(X(210)+X(300))/2}" y="22" text-anchor="middle" font-size="12" fill="#E9EEF6">in between</text><text x="${(X(300)+520)/2}" y="22" text-anchor="middle" font-size="12" fill="#E9EEF6">owl-leaning</text>`+
  [60,180,300,420].map(m=>`<text x="${X(m)}" y="68" text-anchor="middle" font-size="12" fill="#C9D3E3">${fmt(m+720)}</text>`).join('')+`<path d="M${x} 52 l-7 12 h14z" fill="#fff"/><text x="${x}" y="86" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">you</text>`;
 $('kSvg').hidden=false;
 const band=am<210?'L':am<=300?'M':'O';
 $('kRes').innerHTML=`<div class="res wl2"><p class="gh">Your numbers</p>${barRow('Sleep, alarm days',SDw/60,11,(Math.round(SDw/6)/10)+' h','#C9D3E3')}${barRow('Sleep, free days',SDf/60,11,(Math.round(SDf/6)/10)+' h','#FCB316')}${barRow('Social jet lag',Math.max(0,sjl),5,(Math.round(Math.max(0,sjl)*10)/10)+' h','#FFB38A')}</div>`;
 let title,text;
 if(band==='L'){title='Lark-leaning';text=`On free days, the middle of your sleep falls around ${fmt(MSFsc)}, earlier than most students. Mornings are likely your stronger time for hard work.`}
 else if(band==='M'){title='In between';text=`On free days, the middle of your sleep falls around ${fmt(MSFsc)}, in between, like most people. Notice when you feel sharpest, and put your hardest study there.`}
 else{title='Owl-leaning';text=`On free days, the middle of your sleep falls around ${fmt(MSFsc)}, which is late, as is common in students. Early classes and exams are likely to hit you hardest; hard study may go better later in the day.`}
 if(sjl>=2)text+=` Your sleep shifts by about ${Math.round(sjl*10)/10} hours between alarm days and free days. Researchers call that social jet lag: like crossing time zones every weekend.`;
 else if(sjl>=1)text+=` Your sleep shifts by about ${Math.round(sjl*10)/10} hours on free days, a moderate social jet lag.`;
 if(SDf-SDw>=90)text+=' You sleep much longer on free days, a sign you are catching up on lost sleep during the week.';
 $('kTitle').textContent=title;$('kText').textContent=text});
'''+grid('''[
 ['At NUS, attendance at 8 a.m. classes was…',['About 10 percentage points lower','About the same','Higher'],0,'Yeo, Gooley and colleagues, 2023.'],
 ['Before an early class, students slept…',['About an hour less','About the same','An hour more'],0,'They woke earlier than usual.'],
 ['More days a week with morning classes went with…',['A lower grade point average','A higher one','No difference'],0,'Across nearly 34,000 students.'],
 ['In Dutch high schools, late chronotypes did worst on…',['Early-morning exams','Afternoon exams','No particular exams'],0,'The gap shrank later in the day.'],
 ['The synchrony effect: demanding tasks tend to go best…',['At your own peak time','First thing in the morning','Late at night for everyone'],0,'Larks peak earlier; owls later.'],
 ['At one American university, after class times were taken into account, morning types…',['Still had slightly better grades','Did worse','Did the same'],0,'Enright and Refinetti, 2017. Chronotype isn’t the whole story.']]''','The pattern: early starts cost owls the most, in attendance, sleep and grades. Put your hardest work at your own peak.'))
import json as _j;o['vnote']=_j.load(open('gen/vnotes.json'))['h03']
open('h03/template.html','w').write(page(o))

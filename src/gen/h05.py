import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='h05',n='5',label='The Learning Brain · Habits of the Learner · Topic 5',epi='The Learning Brain, Habits of the Learner, episode 5',
title='Food, Caffeine and the Glucose Myth',h1='Food, caffeine and the glucose myth',em='Feed your routine, not the myths',read='7',mins='2 minutes',vtitle='Food, caffeine and the glucose myth',
dek='Exam week often brings sugary snacks, energy drinks and skipped meals. Your brain isn’t running out of fuel mid-problem set, but regular meals help, and caffeine has a catch.',
jumps='<span><a href="#kT">Plan your caffeine</a></span><span><a href="#bT">Myth or fact?</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, and the brainstem, at the base, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.stem.lab=[520,735];BR.R.stem.al='right';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc','stem'],labels:['pfc','stem'],labelT:{pfc:0.8,stem:1.0},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS+'''
.kp{display:grid;gap:10px;width:100%;max-width:560px}
.kp .row2{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.kp label{display:block;font:600 14px var(--body);color:#C9D3E3}
.kp select{display:block;width:100%;margin-top:4px;min-height:42px;font:600 16px var(--body);border-radius:8px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;padding:0 6px}
.kp select:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.kp fieldset{border:1px solid #3A4E72;border-radius:10px;padding:8px 12px 12px;margin:0}
.kp legend{font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#FCB316;padding:0 6px}
.kchart{width:100%;max-width:560px;height:auto;display:block}''',
body='''  <div class="col lede">
    <p>Your brain is about 2% of your body weight, but uses roughly 20% of your energy at rest. Hard thinking adds only a little on top, perhaps around 5%. Your brain is not running out of fuel halfway through a problem set.</p>
    <p>A popular idea held that self-control burns blood sugar, and a sugary drink tops it back up. But a 2016 analysis by Miguel Vadillo and colleagues found signs of publication bias in that research, and weak evidence overall. Experiments that measured people’s blood glucose directly found no link with self-control either.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>~2% / ~20%</strong><span>of body weight, and of energy used at rest</span></div>
      <div role="listitem"><strong>45</strong><span>studies of breakfast in children and teenagers</span></div>
      <div role="listitem"><strong>40–300 mg</strong><span>of caffeine: better alertness, attention and reaction time</span></div>
      <div role="listitem"><strong>&gt;1 hour</strong><span>less sleep after 400 mg of caffeine, six hours before bed</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Meals</span>Breakfast helps that morning</h2>
    <p>Meals still matter. A review of 45 studies in children and teenagers, by Katie Adolphus and colleagues, found that breakfast, compared with fasting, gave a short-term boost that same morning, especially on tasks of attention and memory. It could not say which breakfast works best.</p>
    <h2 class="sec"><span class="n">Caffeine</span>Alertness, not memory</h2>
    <p>Caffeine is the most common study aid. Low to moderate doses, roughly 40 to 300 milligrams, improve alertness, attention and reaction time. Effects on memory and complex reasoning are less consistent.</p>
    <p>The catch is sleep. In a study by Christopher Drake and colleagues, 400 mg of caffeine taken six hours before bed cut sleep by more than an hour, and people did not notice.</p>
  </div>

  <section class="night" aria-labelledby="kT">
    <div class="col">
      <h2 class="sec" id="kT"><span class="n">Try it</span>Plan your caffeine</h2>
      <p>Pick a bedtime and up to three drinks. The chart shows roughly how much caffeine is still in your body over the day, assuming it halves about every five hours. That is a typical figure; in real people it varies widely. Drink amounts are typical values, and brands differ.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="kScreen">
          <form class="kp" id="kF">
            <label for="kBed">Bedtime<select id="kBed"></select></label>
            <fieldset><legend>Drink 1</legend><div class="row2"><label for="kD0">Drink<select id="kD0"></select></label><label for="kT0">Time<select id="kT0"></select></label></div></fieldset>
            <fieldset><legend>Drink 2</legend><div class="row2"><label for="kD1">Drink<select id="kD1"></select></label><label for="kT1">Time<select id="kT1"></select></label></div></fieldset>
            <fieldset><legend>Drink 3</legend><div class="row2"><label for="kD2">Drink<select id="kD2"></select></label><label for="kT2">Time<select id="kT2"></select></label></div></fieldset>
          </form>
          <svg class="kchart" id="kSvg" viewBox="0 0 560 196" role="img" aria-labelledby="kSvgT"><title id="kSvgT">Caffeine in your body over the day</title></svg>
        </div>
        <div>
          <p class="phase" id="kPhase">Your day</p>
          <p class="mtitle" id="kTitle">Caffeine and bedtime</p>
          <p class="mtext" id="kText" aria-live="polite"></p>
          <div id="kRes"></div>
        </div>
      </div>
    </div>
  </section>

'''+cls_html('bT','Myth or fact?','Eight claims about food, sugar and caffeine for studying. For each, decide: myth or fact? You’ll get feedback after each one.',[('M','Myth',''),('F','Fact','')],'Myth or fact?','Myth or fact?','The question is always: what does the evidence actually show?')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Small studies, big differences</h2>
    <p>The breakfast studies are mostly in children. The caffeine and sleep study had just 12 people. And responses to caffeine vary a lot from person to person.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Try this</h3>
      <p>Eat at regular times, especially before morning exams. Don’t count on sugar for a willpower boost. Use caffeine early in the day, for alertness, not memory. And stop caffeine at least six hours before bed.</p>
    </aside>
  </div>
''',
tips_h='Feed your routine, not the myths.',
tips='''      <li><b>Regular meals</b><span>Especially before morning exams.</span></li>
      <li><b>Caffeine early</b><span>For alertness, not memory.</span></li>
      <li><b>Six hours before bed</b><span>Stop caffeine by then, at least.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1177/0956797616654911">Vadillo, M. A., Gold, N., &amp; Osman, M. (2016). The bitter truth about sugar and willpower: The limited evidential value of the glucose model of ego depletion. <i>Psychological Science, 27</i>(9), 1207–1214.</a></li>
        <li><a href="https://doi.org/10.3945/an.115.010256">Adolphus, K., Lawton, C. L., Champ, C. L., &amp; Dye, L. (2016). The effects of breakfast and breakfast composition on cognition in children and adolescents: A systematic review. <i>Advances in Nutrition, 7</i>(3), 590S–612S.</a></li>
        <li><a href="https://doi.org/10.1016/j.neubiorev.2016.09.001">McLellan, T. M., Caldwell, J. A., &amp; Lieberman, H. R. (2016). A review of caffeine’s effects on cognitive, physical and occupational performance. <i>Neuroscience &amp; Biobehavioral Reviews, 71</i>, 294–312.</a></li>
        <li><a href="https://doi.org/10.5664/jcsm.3170">Drake, C., Roehrs, T., Shambroom, J., &amp; Roth, T. (2013). Caffeine effects on sleep taken 0, 3, or 6 hours before going to bed. <i>Journal of Clinical Sleep Medicine, 9</i>(11), 1195–1200.</a></li>''',
quiz='''[
 {q:'Hard thinking raises the brain’s energy use by about…',o:['A little, perhaps around 5%','Double','Ten times'],a:0,f:'The brain already uses about 20% of your energy at rest.'},
 {q:'Low to moderate caffeine most reliably improves…',o:['Alertness, attention and reaction time','Long-term memory','Complex reasoning'],a:0,f:'Effects on memory and reasoning are less consistent.'},
 {q:'400 mg of caffeine six hours before bed…',o:['Cut sleep by more than an hour, unnoticed','Had no effect','Improved sleep'],a:0,f:'Stop caffeine at least six hours before bed.'}]''',
js=BASE+r'''
/* ---------- plan your caffeine ----------
   Up to 3 drinks; each adds its dose at its time; total decays with a 5-hour half-life. Times in minutes after midnight.
   Typical amounts: brewed coffee 8 oz ~95 mg, espresso shot ~65 mg, energy drink 16 oz ~160 mg, black tea 8 oz ~47 mg, cola 12 oz ~34 mg. */
const DR=[['none','No drink',0],['cof','Coffee, 8 oz (~95 mg)',95],['big','Large coffee, 16 oz (~190 mg)',190],['esp','Espresso shot (~65 mg)',65],['nrg','Energy drink, 16 oz (~160 mg)',160],['tea','Black tea, 8 oz (~47 mg)',47],['cola','Cola, 12 oz (~34 mg)',34]];
const hm=m=>{const h=Math.floor(m/60)%24,mi=m%60;return `${h%12===0?12:h%12}:${String(mi).padStart(2,'0')} ${h<12?'a.m.':'p.m.'}`};
const TIMES=[];for(let m=360;m<=1380;m+=60)TIMES.push(m);
const BEDS=[];for(let m=1260;m<=1560;m+=30)BEDS.push(m);
$('kBed').innerHTML=BEDS.map(m=>`<option value="${m}">${hm(m%1440)}</option>`).join('');$('kBed').value='1410';
[0,1,2].forEach(i=>{$('kD'+i).innerHTML=DR.map(([k,t])=>`<option value="${k}">${t}</option>`).join('');$('kT'+i).innerHTML=TIMES.map(m=>`<option value="${m}">${hm(m)}</option>`).join('')});
$('kD0').value='cof';$('kT0').value='480';$('kD1').value='nrg';$('kT1').value='1020';$('kD2').value='none';$('kT2').value='840';
const HL=300;
function plan(){const bed=+$('kBed').value;const ds=[0,1,2].map(i=>{const d=DR.find(x=>x[0]===$('kD'+i).value);return{mg:d[2],name:d[1].split(' (')[0],t:+$('kT'+i).value}}).filter(d=>d.mg>0);
 const at=m=>ds.reduce((s,d)=>s+(m>=d.t?d.mg*Math.pow(.5,(m-d.t)/HL):0),0);
 const X=m=>40+(m-360)/(bed+60-360)*500;const top=Math.max(100,...Array.from({length:120},(_,k)=>at(360+k*(bed+60-360)/120)));const Y=v=>170-v/top*140;
 let p='';for(let k=0;k<=120;k++){const m=360+k*(bed+60-360)/120;p+=(k?'L':'M')+X(m).toFixed(1)+' '+Y(at(m)).toFixed(1)}
 const cut=bed-360;
 $('kSvg').innerHTML=`<title id="kSvgT">Caffeine in your body over the day</title><rect x="${X(Math.max(360,cut))}" y="30" width="${X(bed)-X(Math.max(360,cut))}" height="140" fill="#22375C"/><text x="${X(bed)}" y="22" text-anchor="end" font-size="18" fill="#C9D3E3">shaded: last 6 hours before bed</text><line x1="40" y1="170" x2="540" y2="170" stroke="#8FA3C2"/><line x1="${X(bed)}" y1="30" x2="${X(bed)}" y2="170" stroke="#FCB316" stroke-dasharray="4 4"/><text x="${X(bed)-4}" y="186" text-anchor="end" font-size="18" fill="#FCB316">bed</text>`+
  [360,720,1080].filter(m=>m<bed-60).map(m=>`<text x="${X(m)}" y="186" text-anchor="${m===360?'start':'middle'}" font-size="18" fill="#C9D3E3">${hm(m)}</text>`).join('')+`<path d="${p}" fill="none" stroke="#7DD3A8" stroke-width="3"/>`;
 const atBed=Math.round(at(bed)),total=ds.reduce((s,d)=>s+d.mg,0),late=ds.filter(d=>d.t>cut);
 $('kRes').innerHTML=`<div class="res wl2"><p class="gh">Your day</p>${barRow('Total caffeine',total,600,total+' mg','#FCB316')}${barRow('Still in you at bedtime',atBed,600,atBed+' mg','#FFB38A')}</div>`;
 let title,text;
 if(!ds.length){title='No caffeine';text='No drinks chosen. Add one to see how long caffeine lingers.'}
 else if(late.length){title='Too close to bed';const lst=late.map(d=>`the ${d.name.split(',')[0].toLowerCase()} at ${hm(d.t)}`).join(' and ');text=`${lst[0].toUpperCase()+lst.slice(1)} ${late.length>1?'fall':'falls'} within six hours of bedtime. About ${atBed} mg would still be in your body when you lie down. In the sleep study, 400 mg taken six hours before bed cut sleep by more than an hour, and people didn’t notice.`}
 else if(atBed>=50){title='Lingering at bedtime';text=`Every drink is more than six hours before bed, but about ${atBed} mg would still be in your body at bedtime, because caffeine halves only about every five hours. Consider an earlier last drink, or a smaller one.`}
 else{title='Well timed';text=`Your last caffeine is more than six hours before bed, and only about ${atBed} mg would be left at bedtime. Early caffeine, for alertness, is the way to use it.`}
 if(total>400)text+=` Your total, ${total} mg, is above the 400 mg a day that health agencies generally treat as the upper limit for healthy adults.`;
 $('kTitle').textContent=title;$('kText').textContent=text}
$('kF').addEventListener('change',plan);plan();
'''+cls_js("{M:'Myth',F:'Fact'}",'''[
 ['Hard studying burns through your brain’s fuel, so you need sugar to keep going.','M','Myth: thinking hard adds only a little to the brain’s energy use, perhaps around 5%.'],
 ['A sugary drink restores your willpower when it’s running low.','M','Myth: that research showed signs of publication bias, and later experiments found no link.'],
 ['For children and teenagers, eating breakfast can help attention and memory that morning.','F','Fact: a review of 45 studies found a short-term boost, compared with fasting.'],
 ['Caffeine reliably improves alertness and reaction time.','F','Fact: low to moderate doses, roughly 40 to 300 mg.'],
 ['Caffeine is a reliable way to remember more of what you study.','M','Myth: effects on memory and complex reasoning are less consistent than on alertness.'],
 ['Coffee at 5 p.m. won’t affect sleep if you feel fine at bedtime.','M','Myth: in one study, caffeine six hours before bed cut sleep by more than an hour, and people didn’t notice.'],
 ['People differ a lot in how they respond to caffeine.','F','Fact: responses vary a lot from person to person.'],
 ['The brain uses about a fifth of your energy at rest, though it is only about 2% of your weight.','F','Fact: it is always running, whether or not you are thinking hard.']]''','Myth or fact?',r'''
 if(right>=7){title='Myth-proof';text=`${right} of 8 right. Your brain isn’t running out of fuel; regular meals help; caffeine is for alertness, and it lingers.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. The sugar-and-willpower idea has weak evidence; caffeine helps alertness more than memory.`}
 else{title='Worth another look';text=`${right} of 8 right. The brain uses a steady fifth of your energy, sugar doesn’t restore willpower, and caffeine’s catch is sleep.`}'''))
import json as _j;o['vnote']=_j.load(open('gen/vnotes.json'))['h05']
open('h05/template.html','w').write(page(o))

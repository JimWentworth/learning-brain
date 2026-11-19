import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='h11',n='11',label='The Learning Brain · Habits of the Learner · Topic 11',epi='The Learning Brain, Habits of the Learner, episode 11',
title='Mindset, with Realistic Effects',h1='Mindset, with realistic effects',em='Abilities can grow; strategies make it happen',read='7',mins='2 minutes',vtitle='Mindset, with realistic effects',
dek='Growth mindset is on posters in many schools. The best evidence says its effects are real for some students in some settings, small on average, and depend on strategy, not effort alone.',
jumps='<span><a href="#eT">How big is “small”?</a></span><span><a href="#bT">Respond to a bad mark</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc'],labels:['pfc'],labelT:{pfc:0.8},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS+'''
.jb{display:flex;gap:8px;flex-wrap:wrap;justify-content:center}
.echart{width:100%;max-width:560px;height:auto;display:block}''',
body='''  <div class="col lede">
    <p>Growth mindset is the belief that your abilities can develop through effort, good strategies and help from others. How much does teaching it actually change results?</p>
    <p>The biggest test, led by David Yeager and published in 2019, involved more than 12,000 ninth graders across the United States. They did either a growth mindset program or a control activity: two short online sessions of about 25 minutes each. Among lower-achieving students, grades rose by about a tenth of a grade point, and the share with a D or F average fell by more than five percentage points.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>12,000+</strong><span>ninth graders in a national experiment</span></div>
      <div role="listitem"><strong>+0.10</strong><span>grade points for lower achievers, after under an hour online</span></div>
      <div role="listitem"><strong>0.08</strong><span>the average effect on achievement in a 2018 meta-analysis: tiny</span></div>
      <div role="listitem"><strong>2.5×</strong><span>as likely to report benefits: authors with a financial stake, in a 2023 review</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Context</span>A seed that needs fertile soil</h2>
    <p>Both higher and lower achievers were also a little more likely to take advanced maths the next year. The effect on grades was larger in schools where classmates valued taking on hard work. Yeager compared the program to a seed that grows in fertile soil.</p>
    <h2 class="sec"><span class="n">Meta-analyses</span>A more modest story</h2>
    <p>In 2018, Victoria Sisk, Brooke Macnamara and colleagues found the average effect of mindset programs on achievement was tiny, about 0.08. In 2023, Macnamara and Alexander Burgoyne found that the highest-quality studies showed little or no benefit, and that authors with a financial stake were about two and a half times as likely to report positive results. Another 2023 meta-analysis, by Jeni Burnette and colleagues, found meaningful effects for students at academic risk. The debate continues.</p>
  </div>

  <section class="night" aria-labelledby="eT">
    <div class="col">
      <h2 class="sec" id="eT"><span class="n">Try it</span>How big is “small”?</h2>
      <p>Researchers report effects as standardized differences, like 0.08. Pick a size and see what it means: two groups of students, one with the program and one without, and how much they overlap.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="eScreen">
          <div class="jb" role="group" aria-label="Effect size"><button class="nbtn" type="button" data-d="0.08">0.08: average mindset effect</button><button class="nbtn ghost" type="button" data-d="0.2">0.2: small</button><button class="nbtn ghost" type="button" data-d="0.5">0.5: medium</button><button class="nbtn ghost" type="button" data-d="0.8">0.8: large</button></div>
          <svg class="echart" id="eSvg" viewBox="0 0 560 230" role="img" aria-labelledby="eSvgT"><title id="eSvgT">Two overlapping groups</title></svg>
        </div>
        <div>
          <p class="phase" id="ePhase">Effect size</p>
          <p class="mtitle" id="eTitle"></p>
          <p class="mtext" id="eText" aria-live="polite"></p>
          <div id="eRes"></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>One ingredient, not a fix</h2>
    <p>Effects are small on average, and depend on context. A mindset is one ingredient, not a fix. And growth comes from effort plus better strategies, not effort alone.</p>
  </div>

'''+cls_html('bT','Respond to a bad mark','You get a disappointing mark. Here are eight things a student might think or do next. For each, decide: is it a growth response with a strategy, effort alone, or a fixed response? You’ll get feedback after each one.',[('G','Growth + strategy','effort and a new approach'),('E','Effort alone','try harder, same way'),('F','Fixed','ability can’t change')],'Growth with strategy, effort alone, or fixed?','Respond to a bad mark','The question is always: is anything going to change about how you study?')+'''
  <div class="col">
'''+'''    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Try this</h3>
      <p>When you get a bad mark, ask what it tells you, and what you will change. Pair effort with a new strategy, like self-testing instead of rereading. Ask for help early. And now and then, choose a challenge you might fail.</p>
    </aside>
  </div>
''',
tips_h='Abilities can grow. Strategies make it happen.',
tips='''      <li><b>What does this mark tell me?</b><span>And what will I change?</span></li>
      <li><b>Effort plus a new strategy</b><span>Self-testing instead of rereading.</span></li>
      <li><b>Ask for help early</b><span>And sometimes pick a challenge you might fail.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1038/s41586-019-1466-y">Yeager, D. S., Hanselman, P., Walton, G. M., et al. (2019). A national experiment reveals where a growth mindset improves achievement. <i>Nature, 573</i>, 364–369.</a></li>
        <li><a href="https://doi.org/10.1177/0956797617739704">Sisk, V. F., Burgoyne, A. P., Sun, J., Butler, J. L., &amp; Macnamara, B. N. (2018). To what extent and under which circumstances are growth mind-sets important to academic achievement? Two meta-analyses. <i>Psychological Science, 29</i>(4), 549–571.</a></li>
        <li><a href="https://doi.org/10.1037/bul0000352">Macnamara, B. N., &amp; Burgoyne, A. P. (2023). Do growth mindset interventions impact students’ academic achievement? A systematic review and meta-analysis with recommendations for best practices. <i>Psychological Bulletin, 149</i>(3–4), 133–173.</a></li>
        <li><a href="https://doi.org/10.1037/bul0000368">Burnette, J. L., Billingsley, J., Banks, G. C., et al. (2023). A systematic review and meta-analysis of growth mindset interventions: For whom, how, and why might such interventions work? <i>Psychological Bulletin, 149</i>(3–4), 174–205.</a></li>''',
quiz='''[
 {q:'In the national experiment, lower achievers’ grades rose by about…',o:['A tenth of a grade point','A full grade point','Nothing'],a:0,f:'After two short online sessions.'},
 {q:'The average effect of mindset programs in the 2018 meta-analysis was…',o:['Tiny, about 0.08','Large, about 0.8','Negative'],a:0,f:'Larger for some students at academic risk.'},
 {q:'Growth comes from…',o:['Effort plus better strategies','Effort alone','Believing alone'],a:0,f:'A mindset is one ingredient, not a fix.'}]''',
js=BASE+r'''
/* ---------- how big is "small"? ----------
   Two normal curves shifted by d. Report Cohen's U3 (share of program group above the control average = Phi(d))
   and the chance that a random program student beats a random control student (Phi(d/sqrt2)). */
const Phi=x=>{const t=1/(1+0.2316419*Math.abs(x)),y=0.3989423*Math.exp(-x*x/2)*t*(0.3193815+t*(-0.3565638+t*(1.781478+t*(-1.821256+t*1.330274))));return x>=0?1-y:y};
function show(d){
 const X=z=>280+z*80,Y=v=>200-v*380,pdf=(z,m)=>Math.exp(-((z-m)**2)/2)/Math.sqrt(2*Math.PI);
 const path=m=>{let p='';for(let z=-3.4;z<=4.2;z+=0.05)p+=(p?'L':'M')+X(z).toFixed(1)+' '+Y(pdf(z,m)).toFixed(1);return p};
 $('eSvg').innerHTML=`<title id="eSvgT">Two overlapping groups, effect size ${d}</title><line x1="10" y1="200" x2="550" y2="200" stroke="#8FA3C2"/><path d="${path(0)}" fill="#C9D3E3" fill-opacity=".25" stroke="#C9D3E3" stroke-width="2"/><path d="${path(d)}" fill="#FCB316" fill-opacity=".25" stroke="#FCB316" stroke-width="3"/><line x1="${X(0)}" y1="40" x2="${X(0)}" y2="200" stroke="#C9D3E3" stroke-dasharray="4 4"/><text x="${X(0)-6}" y="30" text-anchor="end" font-size="18" fill="#C9D3E3">without</text><text x="${X(d)+6}" y="30" font-size="18" fill="#FCB316">with the program</text>`;
 const u3=Phi(d),ps=Phi(d/Math.SQRT2);
 $('eRes').innerHTML=`<div class="res wl2">${barRow('Above the other group’s average',u3,1,Math.round(u3*100)+'%','#FCB316')}${barRow('Random pair: program student scores higher',ps,1,Math.round(ps*100)+'%','#7DD3A8')}</div>`;
 const T={0.08:['Tiny','At 0.08, the two groups almost completely overlap. Only about 53% of students with the program score above the average student without it, against 50% by chance. That was the average effect of mindset programs in the 2018 meta-analysis.'],
  0.2:['Small','At 0.2, about 58% of the program group is above the other group’s average. Noticeable across thousands of students, hard to see in one classroom.'],
  0.5:['Medium','At 0.5, about 69% of the program group is above the other group’s average. A difference a teacher would notice.'],
  0.8:['Large','At 0.8, about 79% of the program group is above the other group’s average. Large, by the usual conventions.']}[d];
 $('eTitle').textContent=T[0];$('eText').textContent=T[1];
 document.querySelectorAll('#eScreen .jb button').forEach(b=>{const on=+b.dataset.d===d;b.classList.toggle('ghost',!on);b.setAttribute('aria-pressed',on)})}
document.querySelector('#eScreen .jb').addEventListener('click',e=>{const b=e.target.closest('button');if(b)show(+b.dataset.d)});
show(0.08);
'''+cls_js("{G:'Growth + strategy',E:'Effort alone',F:'Fixed'}",'''[
 ['“I’ll find out which questions I got wrong and why, then switch from rereading to self-testing.”','G','Growth with a strategy: effort aimed at a new approach.'],
 ['“I’ll just study twice as long next time, the same way.”','E','Effort alone: more of the same rarely fixes the problem.'],
 ['“I’m just not a maths person.”','F','Fixed: it treats ability as something that can’t change.'],
 ['“I’ll go to office hours this week and ask how to approach these problems.”','G','Growth with a strategy: asking for help early is a strategy.'],
 ['“I need to want it more.”','E','Effort alone: wanting it more isn’t a plan.'],
 ['“Some people are naturally good at this, and I’m not one of them.”','F','Fixed: a belief that closes the door on getting better.'],
 ['“I’ll do practice questions under exam conditions, and check my errors each time.”','G','Growth with a strategy: practice that gives feedback.'],
 ['“I’ll stay up all night before the next test.”','E','Effort alone, and it costs sleep, which matters for memory.']]''','Growth with strategy, effort alone, or fixed?',r'''
 if(right>=7){title='Effort plus strategy';text=`${right} of 8 right. A growth mindset only helps if something changes in how you study. Effort alone, more of the same, rarely does it.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. The key difference: growth responses change the strategy, not just the amount of effort.`}
 else{title='Worth another look';text=`${right} of 8 right. Fixed responses say ability can’t change; effort-alone responses try harder the same way; growth responses change the approach.`}'''))
open('h11/template.html','w').write(page(o))

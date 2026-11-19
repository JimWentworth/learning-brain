import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='h09',n='9',label='The Learning Brain · Habits of the Learner · Topic 9',epi='The Learning Brain, Habits of the Learner, episode 9',
title='Dunning–Kruger, Carefully: What the Evidence Really Shows',h1='Dunning–Kruger, carefully',em='Use it as a mirror, not an insult',read='7',mins='2 minutes',vtitle='Dunning–Kruger, carefully',
dek='“The less you know, the more confident you are” is a great story. The evidence is more interesting: random numbers can draw the famous graph, and everyone’s confidence is imperfect.',
jumps='<span><a href="#dT">Draw it from random numbers</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc'],labels:['pfc'],labelT:{pfc:0.8},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.dctl{display:grid;gap:10px;width:100%;max-width:560px}
.dctl fieldset{border:1px solid #3A4E72;border-radius:10px;padding:8px 12px;margin:0}
.dctl legend{font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#FCB316;padding:0 6px}
.dctl label{display:flex;gap:8px;align-items:flex-start;padding:4px 0;color:#E9EEF6;font-size:16px;line-height:1.35;cursor:pointer}
.dctl input{margin-top:3px;width:18px;height:18px;accent-color:#FCB316;flex:none}
.dchart{width:100%;max-width:560px;height:auto;display:block}''',
body='''  <div class="col lede">
    <p>You have probably heard of the Dunning–Kruger effect: the idea that the less you know, the more confident you are. In 1999, Justin Kruger and David Dunning gave Cornell students tests of logic, grammar and humour. Those in the bottom quarter scored around the 12th percentile, but estimated they were around the 62nd.</p>
    <p>But random numbers can draw the same picture. When Edward Nuhfer and colleagues fed computer-generated numbers into the classic graph, the famous pattern appeared anyway. Regression to the mean, plus most people rating themselves above average, is enough to produce it.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>12th vs 62nd</strong><span>percentile: actual and estimated, for the bottom quarter in 1999</span></div>
      <div role="listitem"><strong>Random numbers</strong><span>can draw the same famous graph</span></div>
      <div role="listitem"><strong>929</strong><span>adults: self-rated and measured intelligence on a straight line</span></div>
      <div role="listitem"><strong>Brief training</strong><span>made low scorers far more accurate about themselves</span></div>
    </div>
  </div>

  <section class="night" aria-labelledby="dT">
    <div class="col">
      <h2 class="sec" id="dT"><span class="n">Try it</span>Draw it from random numbers</h2>
      <p>Simulate 400 people. Each gets a test score with some luck in it, and a self-estimate. Then group them into quarters by score, as the classic graph does, and compare their real and estimated percentiles. Change the settings and redraw. No real people are involved.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="dScreen">
          <form class="dctl" id="dF">
            <fieldset><legend>Self-estimates</legend>
              <label><input type="radio" name="dk" value="0" checked>Pure guesses: no link at all to real skill</label>
              <label><input type="radio" name="dk" value="0.5">Somewhat accurate</label>
              <label><input type="radio" name="dk" value="0.9">Very accurate</label>
            </fieldset>
            <fieldset><legend>Above-average effect</legend>
              <label><input type="radio" name="db" value="12" checked>Most people rate themselves a bit above average</label>
              <label><input type="radio" name="db" value="0">No one does</label>
            </fieldset>
            <div class="mrow" style="justify-content:center"><button class="nbtn" type="submit">Draw the graph</button></div>
          </form>
          <svg class="dchart" id="dSvg" viewBox="0 0 560 254" role="img" aria-labelledby="dSvgT"><title id="dSvgT">Actual and estimated percentile by quarter</title></svg>
        </div>
        <div>
          <p class="phase" id="dPhase">Simulation</p>
          <p class="mtitle" id="dTitle">Start with pure guesses</p>
          <p class="mtext" id="dText" aria-live="polite">Draw the graph with no link between skill and self-estimate.</p>
          <div id="dRes"></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Better methods</span>No special blind spot at the bottom</h2>
    <p>With better methods, Nuhfer’s team found that most of more than a thousand students and faculty judged their own performance fairly accurately. And in a study of 929 adults, by Gilles Gignac and Marcin Zajenkowski, self-rated and measured intelligence lined up along a straight line, with no special blind spot at the bottom.</p>
    <p>So the safer lesson is not that some people are clueless. Everyone’s confidence is imperfect, especially in a skill you are just starting to learn. Dunning himself has stressed that the effect is about all of us, not other people.</p>
    <h2 class="sec"><span class="n">The hopeful part</span>Training improved self-judgement</h2>
    <p>The original paper also found something hopeful. After brief training in logic, low scorers became far more accurate about their own performance.</p>
    <h2 class="sec"><span class="n">A caution</span>Still debated</h2>
    <p>Researchers still debate how much of the effect is real, and some critics of the critiques argue the statistics cut both ways. But one fix works either way: compare your confidence with real results.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Try this</h3>
      <p>Before each quiz, predict your score, then compare. Mark the questions you felt sure about, and check them. Get feedback early, well before the exam. And never use Dunning–Kruger as an insult. Use it as a mirror.</p>
    </aside>
  </div>
''',
tips_h='Check your confidence against your results.',
tips='''      <li><b>Predict, then compare</b><span>Before each quiz.</span></li>
      <li><b>Check your sure answers</b><span>Mark them, then see.</span></li>
      <li><b>A mirror, not an insult</b><span>It’s about all of us.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1037/0022-3514.77.6.1121">Kruger, J., &amp; Dunning, D. (1999). Unskilled and unaware of it: How difficulties in recognizing one’s own incompetence lead to inflated self-assessments. <i>Journal of Personality and Social Psychology, 77</i>(6), 1121–1134.</a></li>
        <li><a href="https://doi.org/10.5038/1936-4660.10.1.4">Nuhfer, E., Fleisher, S., Cogan, C., Wirth, K., &amp; Gaze, E. (2017). How random noise and a graphical convention subverted behavioral scientists’ explanations of self-assessment data: Numeracy underlies better alternatives. <i>Numeracy, 10</i>(1), 4.</a></li>
        <li><a href="https://doi.org/10.1016/j.intell.2020.101449">Gignac, G. E., &amp; Zajenkowski, M. (2020). The Dunning-Kruger effect is (mostly) a statistical artefact: Valid approaches to testing the hypothesis with individual differences data. <i>Intelligence, 80</i>, 101449.</a></li>''',
quiz='''[
 {q:'In 1999, the bottom quarter scored around the 12th percentile and estimated…',o:['Around the 62nd','Around the 12th','Around the 95th'],a:0,f:'The famous graph.'},
 {q:'What can also produce the famous graph?',o:['Random numbers, plus an above-average bias','Only real overconfidence','Nothing else'],a:0,f:'Regression to the mean does much of the work.'},
 {q:'After brief training in logic, low scorers…',o:['Became far more accurate about themselves','Became more overconfident','Didn’t change'],a:0,f:'Feedback and training help calibration.'}]''',
js=BASE+r'''
/* ---------- draw it from random numbers ----------
   400 simulated people: skill ~ N(0,1); test score = skill + luck (N(0,1)); self-estimate = r*skill + sqrt(1-r^2)*noise.
   Convert score and estimate to percentiles; shift estimates up by the above-average bias (clamped 1-99).
   Group by score quartile; plot mean actual percentile and mean estimated percentile. */
const rn=()=>{let u=0,v=0;while(!u)u=Math.random();while(!v)v=Math.random();return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v)};
const pct=a=>{const s=a.map((v,i)=>[v,i]).sort((x,y)=>x[0]-y[0]);const p=Array(a.length);s.forEach(([v,i],k)=>p[i]=(k+0.5)/a.length*100);return p};
let draws=0;
function draw(){const r=+document.querySelector('input[name=dk]:checked').value,bias=+document.querySelector('input[name=db]:checked').value;
 const N=400,sk=[],sc=[],es=[];for(let i=0;i<N;i++){const s=rn();sk.push(s);sc.push(s+rn());es.push(r*s+Math.sqrt(1-r*r)*rn())}
 const ps=pct(sc),pe=pct(es).map(v=>Math.max(1,Math.min(99,v+bias)));
 const q=[0,1,2,3].map(k=>{const idx=ps.map((v,i)=>[v,i]).filter(([v])=>v>=k*25&&v<(k+1)*25).map(([,i])=>i);return{act:idx.reduce((s,i)=>s+ps[i],0)/idx.length,est:idx.reduce((s,i)=>s+pe[i],0)/idx.length}});
 const X=k=>90+k*130,Y=v=>215-v*1.85;
 const line=(key,col,dash)=>`<path d="${q.map((d,k)=>(k?'L':'M')+X(k)+' '+Y(d[key]).toFixed(1)).join('')}" fill="none" stroke="${col}" stroke-width="3"${dash?' stroke-dasharray="6 5"':''}/>`+q.map((d,k)=>`<circle cx="${X(k)}" cy="${Y(d[key]).toFixed(1)}" r="5" fill="${col}"/>`).join('');
 $('dSvg').innerHTML=`<title id="dSvgT">Actual and estimated percentile by quarter</title>`+[0,25,50,75,100].map(v=>`<line x1="50" y1="${Y(v)}" x2="540" y2="${Y(v)}" stroke="#3A4E72"/><text x="44" y="${Y(v)+4}" text-anchor="end" font-size="18" fill="#C9D3E3">${v}</text>`).join('')+
  ['Bottom','Second','Third','Top'].map((t,k)=>`<text x="${X(k)}" y="240" text-anchor="middle" font-size="18" fill="#C9D3E3">${t}</text>`).join('')+line('act','#7DD3A8')+line('est','#FCB316',true)+
  `<text x="${X(3)}" y="${Y(q[3].act)-12}" text-anchor="end" font-size="18" fill="#7DD3A8">actual</text><text x="${X(0)+8}" y="${Y(q[0].est)-12}" font-size="18" fill="#FCB316">estimated</text>`;
 const b=q[0],t=q[3];draws++;const ord=x=>{const n=Math.round(x),m=n%100;return n+((m>10&&m<14)?'th':({1:'st',2:'nd',3:'rd'}[n%10]||'th'))};
 $('dRes').innerHTML=`<div class="res wl2"><p class="gh">Bottom quarter</p>${barRow('Actual',b.act,100,ord(b.act),'#7DD3A8')}${barRow('Estimated',b.est,100,ord(b.est),'#FCB316')}<p class="gh">Top quarter</p>${barRow('Actual',t.act,100,ord(t.act),'#7DD3A8')}${barRow('Estimated',t.est,100,ord(t.est),'#FCB316')}</div>`;
 let title,text;
 const gap=b.est-b.act;
 if(r===0&&bias>0){title='The famous graph, from nothing';text=`These estimates are pure guesses, yet the bottom quarter “overestimates” by about ${Math.round(gap)} points and the top quarter “underestimates”. With no link to skill, every group’s estimate sits near the middle, nudged up by the above-average effect. That alone draws the classic picture.`}
 else if(r===0){title='Still a slope, from pure chance';text=`Even with no above-average effect, guesses with no link to skill sit near the middle for every group, so the bottom looks overconfident and the top underconfident. That is regression to the mean.`}
 else if(r>=0.9){title='Accurate people, smaller gap';text=`When self-estimates track real skill closely, the lines nearly meet${bias?', apart from the above-average nudge':''}. Some gap remains because test scores include luck.`}
 else{title='Somewhat accurate, still the pattern';text=`With somewhat accurate self-estimates, the classic shape still appears: the bottom quarter overestimates by about ${Math.round(gap)} points. Part of that is regression to the mean, not a special blind spot.`}
 $('dTitle').textContent=title;$('dText').textContent=text}
$('dF').addEventListener('submit',e=>{e.preventDefault();draw()});
draw();
'''+grid('''[
 ['In 1999, the bottom quarter scored around the 12th percentile and estimated…',['Around the 62nd','Around the 12th','Around the 90th'],0,'Kruger and Dunning, 1999.'],
 ['When random numbers were fed into the classic graph…',['The famous pattern appeared anyway','Nothing appeared','The pattern reversed'],0,'Nuhfer and colleagues.'],
 ['With better methods, most of more than a thousand students and faculty…',['Judged their own performance fairly accurately','Wildly overestimated','Wildly underestimated'],0,'Most people are roughly calibrated.'],
 ['In 929 adults, self-rated and measured intelligence…',['Lined up along a straight line','Diverged sharply at the bottom','Were unrelated'],0,'Gignac and Zajenkowski, 2020.'],
 ['After brief training in logic, low scorers…',['Became far more accurate about themselves','Got more overconfident','Didn’t change'],0,'The hopeful finding in the original paper.'],
 ['The safer lesson is…',['Everyone’s confidence is imperfect','Some people are clueless','Confidence is always right'],0,'Use it as a mirror, not an insult.']]''','The pattern: much of the famous graph is statistics, not a special blind spot. Everyone benefits from checking confidence against results.'))
import json as _j;o['vnote']=_j.load(open('gen/vnotes.json'))['h09']
open('h09/template.html','w').write(page(o))

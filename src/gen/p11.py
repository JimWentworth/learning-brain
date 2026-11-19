import sys;sys.path.insert(0,'gen')
from pkit import *
from memjs import grid
o=pbase(11,'Graphs That Fool the Eye','Graphs that','fool the eye',
'Graphs are read by the visual system, and it judges some things far better than others. Positions along a scale are easy; areas and angles are hard; a cut-off axis can make a small difference look huge.',
'<span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['ips','v1'],{'ips':([460,-70],'left'),'v1':([960,770],'right')},'Drawing of the side of the brain with the intraparietal sulcus, at the top, involved in judging quantities, and the visual cortex, at the back, glowing orange and labelled.')

screen='''            <svg id="grSvg" viewBox="0 0 520 260" width="100%" style="max-width:540px;display:block;background:#fff;border-radius:6px" role="img" aria-labelledby="grD">
              <desc id="grD">A simple chart comparing two values, A and B. The panel beside it asks you to estimate how they compare.</desc>
              <g id="grG" font-family="Source Sans 3, sans-serif"></g>
            </svg>
            <div id="grSl" hidden style="width:100%;max-width:440px;color:#E9EEF6"><label for="grIn" style="font-weight:700;display:block;margin-bottom:6px" id="grLab">B is how many times A?</label><input id="grIn" type="range" min="1" max="10" step="0.5" value="1" style="width:100%;accent-color:#FF5F05" aria-describedby="grVal"><p id="grVal" style="margin:4px 0 0;font:800 24px var(--body);color:#fff;text-align:center">1×</p></div>'''
student=lab(screen,'Ready','How much bigger?','Part 1: estimate how many times bigger B is than A, in three kinds of chart. Part 2: judge two bar charts of test scores.','Start')

o.update(body=tabs('How much bigger?','Bars, circles and slices: estimate the ratio. Then look at two charts of the same numbers.',student,
 'About 10 minutes',
 ['Show each chart in part 1 and ask everyone to write down their estimate of “B is how many times A?” before revealing.',
  'Compare the spread of answers for bars, circles and pie slices. Which were people most accurate on?',
  'In part 2, show the cut-off axis chart first and take a vote on how big the difference is. Then show the full axis.',
  'Look at a chart from your own slides or a textbook. Which comparison does it ask the eye to make? Could position do it better?'],
 ['Which chart type gave the most accurate estimates? Why?',
  'Did knowing the axis was cut off change your impression?',
  'When is a cut-off axis honest, and when is it misleading?'],
 'Put the comparison that matters on a common scale, as position or length, and label the values. Start bar charts at zero. Use pies and bubbles only when rough proportions are enough.',
 'There is no single right answer to “how big does it look”; the point is to compare your impression of the two charts.')+'''
  <div class="col lede">
    <p>In 1984, the statisticians William Cleveland and Robert McGill asked a simple question: when a chart encodes a number as a position, a length, an angle or an area, how accurately can people read it? Their experiments produced a ranking that still shapes chart design.</p>
    <p>Judgements of position along a common scale were the most accurate, then length, then angle and slope, with area judgements last.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>Position</strong><span>along a common scale: the most accurate judgement</span></div>
      <div role="listitem"><strong>Area</strong><span>the least accurate of the judgements tested</span></div>
      <div role="listitem"><strong>Exaggerated</strong><span>differences when a bar chart’s axis doesn’t start at zero</span></div>
      <div role="listitem"><strong>Persistent</strong><span>even when the chart shows the axis is cut off</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Why bars beat pies</span>Different judgements</h2>
    <p>A bar chart asks the eye to compare the ends of bars against a shared axis. A pie chart asks it to compare angles or areas, which the visual system judges less accurately. That doesn’t make pies useless for showing rough shares of a whole, but it makes them a poor choice when the size of a difference matters.</p>
    <h2 class="sec"><span class="n">The cut-off axis</span>A small gap made large</h2>
    <p>Michael Correll, Enrico Bertini and Steven Franconeri tested how people judge differences when a chart’s y-axis doesn’t start at zero. Truncated axes made differences look bigger, across chart types, and the effect persisted even with designs that explicitly marked the truncation. They suggest choosing an axis that matches the size of difference that actually matters, rather than following a single rule.</p>
    <h2 class="sec"><span class="n">For learning</span>Charts are read by perception first</h2>
    <p>Students form an impression of a chart before they read its numbers, and that impression is hard to undo. Design for the comparison you want them to make, and teach them to check the axis before they trust the picture.</p>
  </div>

'''+pgrid_html(),
tips_h='Design for the comparison you want students to make.',
tips='''      <li><b>Use position and length</b><span>For comparisons that matter, use bars or dots on a shared axis.</span></li>
      <li><b>Start bars at zero</b><span>Or choose the axis for the size of difference that matters, and say so.</span></li>
      <li><b>Teach the axis check</b><span>Students should read the scale before trusting the shape.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1080/01621459.1984.10478080">Cleveland, W. S., &amp; McGill, R. (1984). Graphical perception: Theory, experimentation, and application to the development of graphical methods. <i>Journal of the American Statistical Association, 79</i>(387), 531–554.</a></li>
        <li>Cleveland, W. S., &amp; McGill, R. (1986). An experiment in graphical perception. <i>International Journal of Man-Machine Studies, 25</i>(5), 491–500.</li>
        <li><a href="https://arxiv.org/abs/1907.02035">Correll, M., Bertini, E., &amp; Franconeri, S. (2020). Truncating the y-axis: Threat or menace? <i>Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems</i>.</a></li>''',
foot='The charts are drawn for this page; the test-score numbers are made up. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'Which judgement did Cleveland and McGill find most accurate?',o:['Position along a common scale','Area','Angle'],a:0,f:'Area was least accurate.'},
 {q:'A bar chart whose y-axis starts at 80 instead of 0 tends to make differences look…',o:['Bigger','Smaller','The same'],a:0,f:'Even when the cut is marked.'},
 {q:'For an important comparison, the best choice is usually…',o:['Bars or dots on a shared axis','A pie chart','Bubbles'],a:0,f:'Position and length are read most accurately.'}]''',
js=PANEL_JS+r'''
/* ---------- ratio estimates + truncated axis ---------- */
const N='#13294B',O='#FF5F05';const lbl=(x,y,t)=>`<text x="${x}" y="${y}" text-anchor="middle" font-size="22" font-weight="800" fill="${N}">${t}</text>`;
const BARS=()=>`<line x1="60" y1="220" x2="460" y2="220" stroke="${N}" stroke-width="2"/><rect x="140" y="${220-45}" width="80" height="45" fill="${O}"/><rect x="300" y="${220-180}" width="80" height="180" fill="${O}"/>${lbl(180,248,'A')}${lbl(340,248,'B')}`;
const CIRC=()=>`<circle cx="160" cy="140" r="40" fill="${O}"/><circle cx="350" cy="130" r="80" fill="${O}"/>${lbl(160,248,'A')}${lbl(350,248,'B')}`;
const PIE=()=>{const cx=260,cy=125,r=100;const seg=(a0,a1,c)=>{const p=a=>[cx+r*Math.cos(a),cy+r*Math.sin(a)];const [x0,y0]=p(a0),[x1,y1]=p(a1);return `<path d="M${cx} ${cy} L${x0} ${y0} A${r} ${r} 0 ${a1-a0>Math.PI?1:0} 1 ${x1} ${y1} Z" fill="${c}" stroke="#fff" stroke-width="3"/>`};
 const t=2*Math.PI,s=-Math.PI/2,a=t*0.1,b=t*0.3;return seg(s,s+a,'#3E6B9E')+seg(s+a,s+a+b,O)+seg(s+a+b,s+t,'#C9D1DC')+`<text x="${cx+19}" y="${cy-50}" text-anchor="middle" font-size="18" font-weight="800" fill="#fff">A</text><text x="${cx+70}" y="${cy+30}" font-size="20" font-weight="800" fill="${N}">B</text>`};
const ITEMS=[['Bars',BARS,4],['Circles (by area)',CIRC,4],['Pie slices',PIE,3]];
function score(axis0){const lo=axis0?0:80,hi=axis0?100:88,y=v=>220-(v-lo)/(hi-lo)*190;const tick=[];for(let v=lo;v<=hi;v+=axis0?20:2)tick.push(`<line x1="70" y1="${y(v)}" x2="460" y2="${y(v)}" stroke="#E3E8EF"/><text x="62" y="${y(v)+5}" text-anchor="end" font-size="15" fill="${N}">${v}%</text>`);
 return tick.join('')+`<rect x="150" y="${y(84)}" width="90" height="${220-y(84)}" fill="#3E6B9E"/><rect x="300" y="${y(87)}" width="90" height="${220-y(87)}" fill="${O}"/><text x="195" y="245" text-anchor="middle" font-size="16" font-weight="700" fill="${N}">Section 1</text><text x="345" y="245" text-anchor="middle" font-size="16" font-weight="700" fill="${N}">Section 2</text>`}
const upd=()=>{$('grVal').textContent=$('grIn').value+'×'};$('grIn').addEventListener('input',upd);
startRun(async()=>{const est=[];
 for(let i=0;i<ITEMS.length;i++){const [nm,fn,tr]=ITEMS[i];$('grG').innerHTML=fn();$('grSl').hidden=false;$('grIn').value=1;upd();$('grIn').disabled=false;
  say(`Part 1 · ${i+1} of 3`,nm,'Use the slider: B is how many times A? Go with your impression; no measuring. Then press Done.');
  $('grIn').focus();await nextBtn('Done');if(!RUN)return;const v=+$('grIn').value;est.push([nm,v,tr]);$('grIn').disabled=true;
  say(null,`Actual: ${tr}×`,`You said ${v}×. `+(i===0?'Bars on a shared baseline are compared by length and position, which people judge well.':i===1?'Circle B has twice the radius, so four times the area. Many people underestimate area differences.':'Slice B is three times slice A. Angles and areas are harder to judge than lengths.'));
  if(i<2){await nextBtn('Next chart');if(!RUN)return}}
 $('grSl').hidden=true;
 $('sRes').innerHTML='<div class="res">'+est.map(([n,v,t])=>barRow(n.split(' ')[0],Math.abs(v-t),4,`off by ${Math.abs(v-t)}`,'#FCB316')).join('')+'</div>';
 await nextBtn('Part 2: test scores');if(!RUN)return;$('sRes').innerHTML='';
 $('grG').innerHTML=score(false);
 say('Part 2 · chart 1','Average test score by section','How big does the difference between the sections look?');
 const a=await ask(['Tiny','Small','Moderate','Large','Huge'],'How big does the difference look?');if(!RUN)return;hideCh();
 $('grG').innerHTML=score(true);
 say('Part 2 · chart 2','The same two scores','Same data: 84% and 87%. Now how big does it look?');
 const b=await ask(['Tiny','Small','Moderate','Large','Huge'],'How big does the difference look now?');if(!RUN)return;hideCh();
 say('What happened',b<a?'Same numbers, smaller impression':'Same numbers, two charts',
  'Both charts show 84% and 87%. The first axis started at 80%, which stretched a 3-point gap across most of the chart. Studies of truncated axes find that this exaggerates the perceived difference, even when viewers can see the axis is cut off. '+(b<a?'Your own ratings showed it.':''))});
'''+grid('''[
 ['In Cleveland and McGill’s experiments, which judgements were most accurate?',['Position along a common scale','Area','Angle'],0,'Then length, then angle and slope.'],
 ['Which were least accurate?',['Area','Length','Position'],0,'So bubbles and area-based charts are hard to read precisely.'],
 ['Did truncated y-axes make differences look bigger?',['Yes','No','Only in pie charts'],0,'Correll, Bertini and Franconeri, 2020.'],
 ['Did marking the truncation on the chart remove the effect?',['No, it persisted','Yes, completely','It reversed it'],0,'The impression was hard to undo.'],
 ['What did Correll and colleagues recommend?',['Choose the axis for the size of difference that matters','Never truncate any chart','Always truncate line charts'],0,'Not a single blanket rule.']]''','The pattern: the eye reads charts before the mind reads numbers.'))
write(o)

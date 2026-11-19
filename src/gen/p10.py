import sys;sys.path.insert(0,'gen')
from pkit import *
from memjs import grid
o=pbase(10,'Where Experts Look: Eye Tracking and Pointing the Way','Where experts look,','and pointing the way',
'Experts look at different places than beginners, and they get there faster. Students can’t see where your eyes go, but you can show them: point, highlight, and say where to look.',
'<span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['par','pfc'],{'par':([560,-70],'left'),'pfc':([60,730],'left')},'Drawing of the side of the brain with the parietal lobe, at the top, and the prefrontal cortex, at the front, which guide attention and eye movements, glowing orange and labelled.')

screen='''            <div id="vsGrid" role="group" aria-label="Search grid: find the letter T among the letter L" style="display:grid;grid-template-columns:repeat(6,1fr);gap:4px;width:100%;max-width:420px;background:#fff;border-radius:6px;padding:10px;position:relative"></div>
            <p class="prog" id="vsCap" aria-live="polite">&nbsp;</p>'''
student=lab(screen,'Ready','Find the T','Find the one T among the Ls and click it (or tab to it and press Enter). Some rounds give you a pointer first; some don’t. Eight rounds, timed.','Start')

o.update(body=tabs('Find the T','A grid of rotated Ls with one T hidden among them. Find it, with and without someone pointing the way.',student,
 'About 10 minutes',
 ['Students do the eight rounds on their own devices and note their two average times: with a pointer and without.',
  'Collect a few pairs of times. Was the pointer faster for nearly everyone?',
  'Project a diagram from your course. Ask students to mark where they would look first. Then show where an expert looks, and why.',
  'Discuss: what is the “T” in our diagrams, and how do I point to it?'],
 ['How did you search when there was no pointer?',
  'How much did the pointer save you?',
  'Where do you look first in this kind of diagram, and how did you learn that?'],
 'When you show a complex image, point to the part that matters, highlight it, or build it up step by step, and say what you are looking at and why. Recording a short video with your cursor or pen showing where you look is a simple version of an expert’s eye-movement model.',
 'Search time depends on the screen and the person. The comparison that matters is each person’s own time with and without the pointer.')+'''
  <div class="col lede">
    <p>Andreas Gegenfurtner, Erno Lehtinen and Roger Säljö pooled 296 effect sizes from eye-tracking studies comparing experts and non-experts looking at visualisations in fields such as medicine, sport and aviation. Experts had shorter fixations, looked more at the task-relevant areas and less at irrelevant ones, and got their eyes to the relevant information sooner.</p>
    <p>In other words, part of expertise is knowing where to look, and that is invisible to a learner sitting next to the expert.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>296</strong><span>effect sizes in the meta-analysis of expert and novice eye movements</span></div>
      <div role="listitem"><strong>Sooner</strong><span>experts’ eyes reached the relevant information faster</span></div>
      <div role="listitem"><strong>g = 0.53</strong><span>average benefit of signalling for retention across 139 comparisons</span></div>
      <div role="listitem"><strong>g = 0.33</strong><span>average benefit of signalling for transfer</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Signalling</span>Point to what matters</h2>
    <p>Highlighting, arrows, colour cues and spoken pointers are called signalling in multimedia research. A 2018 meta-analysis by Sascha Schneider and colleagues, covering more than 12,000 learners, found that signals improved retention (g = 0.53) and transfer (g = 0.33). A 2020 meta-analysis by David Alpizar and colleagues also found a positive average effect (d = 0.38), with effects varying from small to large.</p>
    <h2 class="sec"><span class="n">Showing the gaze</span>Eye-movement modelling examples</h2>
    <p>Researchers have tried showing learners an expert’s eye movements directly: a video in which a dot or spotlight marks where the expert is looking while they explain. In one study, Halszka Jarodzka and colleagues used this approach to teach medical students to recognise seizures in infants from patient videos. Results across studies are mixed, and some find no benefit, so this is a promising idea rather than a settled one. Simple signalling has the stronger evidence.</p>
    <h2 class="sec"><span class="n">For learning</span>Your eyes know; say where they go</h2>
    <p>When you look at a graph, a slide or a specimen, you go straight to what matters. Students can’t see that. Narrate it: “First I look at the axes. Then the gap between these two lines.” Point while you say it.</p>
  </div>

'''+pgrid_html(),
tips_h='Students can’t see where your eyes go. Show them.',
tips='''      <li><b>Point while you talk</b><span>A cursor, laser or finger on the part you are describing.</span></li>
      <li><b>Highlight or build up</b><span>Reveal a complex diagram in steps, or dim what doesn’t matter yet.</span></li>
      <li><b>Narrate your looking</b><span>“First I check the axes…” makes the expert’s search visible.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1007/s10648-011-9174-7">Gegenfurtner, A., Lehtinen, E., &amp; Säljö, R. (2011). Expertise differences in the comprehension of visualizations: A meta-analysis of eye-tracking research in professional domains. <i>Educational Psychology Review, 23</i>(4), 523–552.</a></li>
        <li>Schneider, S., Beege, M., Nebel, S., &amp; Rey, G. D. (2018). A meta-analysis of how signaling affects learning with media. <i>Educational Research Review, 23</i>, 1–24.</li>
        <li><a href="https://doi.org/10.1007/s11423-020-09748-7">Alpizar, D., Adesope, O. O., &amp; Wong, R. M. (2020). A meta-analysis of signaling principle in multimedia learning environments. <i>Educational Technology Research and Development, 68</i>, 2095–2119.</a></li>
        <li><a href="https://doi.org/10.1007/s11251-012-9218-5">Jarodzka, H., Balslev, T., Holmqvist, K., Nyström, M., Scheiter, K., Gerjets, P., &amp; Eika, B. (2012). Conveying clinical reasoning based on visual observation via eye-movement modelling examples. <i>Instructional Science, 40</i>(5), 813–827.</a></li>''',
foot='The search task is a classic T-among-Ls display drawn for this page. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'Compared with novices, experts’ eyes…',o:['Reach the relevant information sooner','Move more slowly','Look at everything equally'],a:0,f:'And dwell less on irrelevant areas.'},
 {q:'Signalling means…',o:['Highlighting or pointing to what matters','Adding sound effects','Using more slides'],a:0,f:'Arrows, colour, spoken cues.'},
 {q:'Showing learners an expert’s eye movements has…',o:['Mixed results so far','Always worked','Always failed'],a:0,f:'Promising, not settled.'}]''',
js=PANEL_JS+r'''
/* ---------- T among Ls ---------- */
const G=$('vsGrid');let tgt=-1,resolve=null,t0=0;
function build(cuedIdx){const n=36;tgt=Math.floor(Math.random()*n);let h='';
 for(let i=0;i<n;i++){const isT=i===tgt,rot=[0,90,180,270][Math.floor(Math.random()*4)];
  h+=`<button type="button" data-i="${i}" aria-label="${isT?'T':'L'}" style="appearance:none;border:2px solid transparent;background:#fff;border-radius:6px;aspect-ratio:1;display:flex;align-items:center;justify-content:center;cursor:pointer;padding:0"><span style="display:block;transform:rotate(${rot}deg);font:800 30px/1 var(--body);color:#13294B">${isT?'T':'L'}</span></button>`}
 G.innerHTML=h}
G.addEventListener('click',e=>{const b=e.target.closest('button');if(!b||!resolve)return;const i=+b.dataset.i;if(i===tgt){const r=resolve;resolve=null;b.style.borderColor='#2E7D32';r((performance.now()-t0)/1000)}else{b.style.borderColor='#FFB38A';$('vsCap').textContent='That’s an L. Keep looking.'}});
function ring(on){const b=G.querySelector(`[data-i="${tgt}"]`);if(b)b.style.boxShadow=on?'0 0 0 5px #FF5F05':'none'}
startRun(async()=>{const plan=shuf([0,0,0,0,1,1,1,1]);const res={0:[],1:[]};G.innerHTML='';
 for(let k=0;k<plan.length;k++){const cued=plan[k];
  say(`Round ${k+1} of 8`,cued?'With a pointer':'No pointer',cued?'An orange ring will show you where to look. Then find the T.':'Find the T as fast as you can.');
  await sw(700);if(!RUN)return;build();$('vsCap').textContent=' ';
  if(cued){ring(true);await sw(500);if(!RUN)return;ring(false)}
  t0=performance.now();const t=await new Promise(r=>{resolve=r});if(!RUN)return;res[cued].push(t);
  $('vsCap').textContent=`Found in ${t.toFixed(1)} s`;await sw(600);if(!RUN)return}
 G.innerHTML='';$('vsCap').textContent=' ';
 const m=a=>a.reduce((x,y)=>x+y,0)/a.length,a0=m(res[0]),a1=m(res[1]),mx=Math.max(a0,a1);
 $('sRes').innerHTML='<div class="res">'+barRow('No pointer',a0,mx,a0.toFixed(1)+' s','#FCB316')+barRow('With pointer',a1,mx,a1.toFixed(1)+' s','#7DD3A8')+'</div>';
 say('What happened',a1<a0?`The pointer saved you ${(a0-a1).toFixed(1)} seconds a round`:'The pointer usually helps',
  'Without a pointer, you searched letter by letter, because a T among rotated Ls doesn’t pop out. With one, your eyes went straight there. An expert’s knowledge of where to look works like that pointer; students don’t have it yet unless you share it.')});
'''+grid('''[
 ['How many effect sizes did Gegenfurtner and colleagues pool from eye-tracking studies of expertise?',['296','29','2,960'],0,'From professional domains such as medicine and sport.'],
 ['Compared with non-experts, experts’ fixations were…',['Shorter','Longer','The same'],0,'And more of them landed on task-relevant areas.'],
 ['In Schneider and colleagues’ 2018 meta-analysis, did signalling improve retention?',['Yes, g = 0.53','No','It hurt retention'],0,'Across more than 12,000 learners.'],
 ['And transfer?',['Yes, g = 0.33','No','It hurt transfer'],0,'Smaller, but positive.'],
 ['Do eye-movement modelling examples reliably help?',['Results are mixed','Yes, always','No, never'],0,'Some studies find benefits, some don’t.']]''','The pattern: experts know where to look; pointing passes that on.'))
write(o)

import sys;sys.path.insert(0,'gen')
from pkit import *
from memjs import grid
o=pbase(4,'Only the Centre Is Sharp: Eye Movements and Reading','Only the centre','is sharp',
'You feel you see a whole page at once. In fact only a tiny patch is sharp at any moment, and your eyes jump several times a second to build the picture. That has consequences for every slide you show.',
'<span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['v1','ips'],{'v1':([960,770],'right'),'ips':([520,-70],'left')},'Drawing of the side of the brain with the visual cortex, at the back, and the intraparietal sulcus, at the top, which helps guide where the eyes go next, glowing orange and labelled.')

screen='''            <div id="fvBox" tabindex="0" role="application" aria-label="Reading window. Move the pointer over the text, or use the arrow keys, to move the sharp window." style="position:relative;width:100%;max-width:520px;min-height:260px;background:#fff;border-radius:6px;color:#13294B;font:17px/1.55 var(--body);cursor:crosshair;touch-action:none;overflow:hidden">
              <div id="fvBlur" aria-hidden="true" style="padding:18px 20px;filter:blur(4.5px);user-select:none"></div>
              <div id="fvSharp" aria-hidden="true" style="position:absolute;inset:0;padding:18px 20px;user-select:none;clip-path:circle(0px at 0 0)"></div>
              <div id="fvCover" style="position:absolute;inset:0;background:#fff;display:flex;align-items:center;justify-content:center;color:#3D4A5C;font-weight:600;padding:20px;text-align:center">The text appears when you press Start.</div>
            </div>
            <p class="prog" id="fvT" aria-live="off">&nbsp;</p>'''
student=lab(screen,'Ready','See like your fovea','Only a small circle of the text will be sharp, roughly the size of the sharp centre of your vision. Move it with the pointer (or arrow keys) to find the answer. Two rounds, timed.','Start',
 '<button class="nbtn ghost" id="fvGot" type="button" hidden>I found it</button>')

o.update(body=tabs('See like your fovea','A page of text, sharp only where you point. Find one fact in a dense paragraph, then in a laid-out notice.',student,
 'About 10 minutes',
 ['Students use their own devices; this one needs a pointer, finger or arrow keys for each person.',
  'Run round 1 (dense paragraph) and round 2 (labelled layout). Students note both times.',
  'Collect a few times on the board. Ask why round 2 was quicker.',
  'Show one of your own slides. Ask: where would your eyes land first? How many jumps to find the key point?'],
 ['What did you have to do to find the answer in round 1?',
  'What about the layout in round 2 let you jump straight to it?',
  'If students are reading this slide, can they also listen to me?'],
 'Every word on a slide costs eye movements, a few per line. Put the key point where the eye lands, use labels and short lines, and avoid making students read dense text while you talk.',
 'Round 2 is easier partly because it is laid out with labels, which is the point. The two rounds aren’t a controlled experiment.')+'''
  <div class="col lede">
    <p>The fovea, the small pit at the centre of the retina, covers only about the central 2 degrees of what you see. Outside it, detail falls away fast. To read, the eyes must keep moving the fovea onto the next few letters.</p>
    <p>Reading is a series of brief stops, called fixations, usually 200 to 250 milliseconds each, separated by fast jumps called saccades that last 20 to 50 milliseconds. Keith Rayner, who spent decades measuring this, compared reading to a slide show of short segments of text.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>~2°</strong><span>of the visual field falls on the fovea, the sharp centre</span></div>
      <div role="listitem"><strong>200–250 ms</strong><span>a typical fixation when reading</span></div>
      <div role="listitem"><strong>20–50 ms</strong><span>a typical saccade, the jump between fixations</span></div>
      <div role="listitem"><strong>3–4 / 14–15</strong><span>letters to the left and right that a skilled reader takes in per fixation</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The perceptual span</span>A small window that moves</h2>
    <p>Using displays that change with each eye movement, researchers measured how much text a reader actually uses during one fixation. For skilled readers of English, it is about three or four letters to the left of where they are looking and 14 or 15 letters to the right. The rest of the line is a blur of shapes and spaces that helps plan the next jump.</p>
    <h2 class="sec"><span class="n">Why it feels whole</span>The brain stitches it together</h2>
    <p>We don’t experience a page as a small sharp spot jumping about, because the brain combines what it took in across fixations, and because we seldom notice what we didn’t look at. The activity above makes the hidden process visible, in simplified form: real readers also get some information from just outside the fovea.</p>
    <h2 class="sec"><span class="n">For learning</span>Every word on a slide costs a jump</h2>
    <p>A slide full of sentences takes many fixations to read, and while students read they are not looking at you or the diagram. A slide with short labelled lines lets the eye go straight to what matters. The Digital Learning series looks at the evidence on reading slides aloud and on extra text.</p>
  </div>

'''+pgrid_html(),
tips_h='Every word costs a jump. Spend them on what matters.',
tips='''      <li><b>Put the point where the eye lands</b><span>Top left, large, and short.</span></li>
      <li><b>Use labels and short lines</b><span>Structure lets the eye jump straight to the answer.</span></li>
      <li><b>Don’t compete with your own slide</b><span>If students must read, pause talking.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1037/0033-2909.124.3.372">Rayner, K. (1998). Eye movements in reading and information processing: 20 years of research. <i>Psychological Bulletin, 124</i>(3), 372–422.</a></li>
        <li><a href="https://doi.org/10.3758/PBR.17.6.834">Rayner, K., Slattery, T. J., &amp; Bélanger, N. N. (2010). Eye movements, the perceptual span, and reading speed. <i>Psychonomic Bulletin &amp; Review, 17</i>(6), 834–839.</a></li>
        <li><a href="https://doi.org/10.3758/s13414-011-0219-2">Schotter, E. R., Angele, B., &amp; Rayner, K. (2012). Parafoveal processing in reading. <i>Attention, Perception, &amp; Psychophysics, 74</i>, 5–35.</a></li>''',
foot='The reading window is a simplified illustration of foveal vision, not a gaze-contingent experiment. The two notices are made up for this activity. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'The sharp centre of vision covers about…',o:['2 degrees','20 degrees','Everything in view'],a:0,f:'The fovea.'},
 {q:'A typical fixation in reading lasts about…',o:['200–250 milliseconds','2 seconds','10 milliseconds'],a:0,f:'Then a quick saccade to the next spot.'},
 {q:'Skilled readers take in more letters…',o:['To the right of where they look','To the left','Equally on both sides'],a:0,f:'14–15 to the right, 3–4 to the left, in English.'}]''',
js=PANEL_JS+r'''
/* ---------- fovea window ---------- */
const TXT=[`<p style="margin:0"><b>Notice for the field trip.</b> The bus leaves from the north entrance of the science building, not the main entrance as stated in last week’s email, and students should arrive fifteen minutes early so attendance can be taken before departure. Lunch is provided by the museum, but bring water. The trip has moved from the original date of March 3 because of a planned maintenance closure; the new date is March 17, a Tuesday, and the return time is unchanged.</p>`,
`<p style="margin:0 0 10px"><b>Lab safety session</b></p><p style="margin:0"><b>Where:</b> Room 210, chemistry building<br><b>When:</b> Thursday, 2 p.m.<br><b>Bring:</b> goggles and your lab notebook<br><b>Note:</b> counts toward your lab grade</p>`];
const QS=[['What is the new date of the trip?',['March 3','March 17','March 15'],1],['Which room is the session in?',['Room 120','Room 201','Room 210'],2]];
const R=36;let fx=40,fy=40,live=false;
function place(){$('fvSharp').style.clipPath=live?`circle(${R}px at ${fx}px ${fy}px)`:'circle(0px at 0 0)'}
const fvB=$('fvBox');
function mv(e){if(!live)return;const r=fvB.getBoundingClientRect();fx=e.clientX-r.left;fy=e.clientY-r.top;place()}
fvB.addEventListener('pointermove',mv);fvB.addEventListener('pointerdown',mv);
fvB.addEventListener('keydown',e=>{if(!live)return;const d={ArrowLeft:[-20,0],ArrowRight:[20,0],ArrowUp:[0,-20],ArrowDown:[0,20]}[e.key];if(!d)return;e.preventDefault();fx=Math.max(0,Math.min(fvB.clientWidth,fx+d[0]));fy=Math.max(0,Math.min(fvB.clientHeight,fy+d[1]));place()});
function setText(i){$('fvBlur').innerHTML=TXT[i];$('fvSharp').innerHTML=TXT[i];$('fvCover').style.display='none';live=true;fx=40;fy=34;place()}
function cover(){live=false;place();$('fvCover').style.display='flex'}
function waitGot(t0){return new Promise(res=>{const b=$('fvGot');b.hidden=false;const iv=setInterval(()=>{$('fvT').textContent=`${Math.floor((performance.now()-t0)/1000)} s`},250);b.onclick=()=>{clearInterval(iv);b.onclick=null;b.hidden=true;res((performance.now()-t0)/1000)}})}
startRun(async()=>{const times=[];cover();
 for(let i=0;i<2;i++){
  say(`Round ${i+1} of 2`,QS[i][0],(i===0?'A dense paragraph. ':'The same kind of notice, laid out with labels. ')+'Move the sharp window to find the answer, then press “I found it”.');
  setText(i);fvB.focus();const t=await waitGot(performance.now());if(!RUN)return;cover();
  const a=await ask(QS[i][1],QS[i][0]);if(!RUN)return;mark(QS[i][2],a);times.push(t);
  say(null,null,(a===QS[i][2]?'<b class="ok">Right.</b> ':`<b class="no">Not quite.</b> It was ${QS[i][1][QS[i][2]]}. `)+`You took ${t.toFixed(1)} seconds.`);
  if(i===0){await nextBtn('Start round 2');if(!RUN)return;hideCh()}}
 $('fvT').textContent=' ';
 const mx=Math.max(...times);$('sRes').innerHTML='<div class="res">'+times.map((t,i)=>barRow(i?'Laid out':'Dense',t,mx,t.toFixed(1)+' s','#FCB316')).join('')+'</div>';
 say('What happened',times[1]<times[0]?'The layout let your eyes jump':'Layout usually helps',
  'With only a small sharp window, you had to search the dense paragraph a few letters at a time. Your eyes do the same on any page: they move the fovea from spot to spot several times a second. Labels and short lines tell the eye where to jump.')});
'''+grid('''[
 ['How much of the visual field does the fovea, the sharp centre, cover?',['About 2 degrees','About 20 degrees','About 90 degrees'],0,'Detail falls away quickly outside it.'],
 ['How long does a typical fixation in reading last?',['200–250 milliseconds','About 1 second','About 20 milliseconds'],0,'With a lot of variation between readers.'],
 ['How long does a typical saccade, the jump between fixations, last?',['20–50 milliseconds','About half a second','About 2 seconds'],0,'Depending on how far the eyes move.'],
 ['For skilled readers of English, the perceptual span reaches how far to the right of fixation?',['About 14–15 letters','About 3–4 letters','A whole line'],0,'And only 3–4 letters to the left.'],
 ['Rayner compared reading to…',['A slide show of short segments','A continuous film','A photograph'],0,'Information is taken in during fixations only.']]''','The pattern: we read through a small moving window, a few letters at a time.'))
write(o)

import sys;sys.path.insert(0,'gen')
from pkit import *
from memjs import grid
o=pbase(5,'The Brain Corrects the Light: Colour, Contrast and the Dress','The brain','corrects the light',
'The colour and lightness you see depend on what surrounds them and on what the brain assumes about the light. That is why one photo of a dress split the internet, and why a colour that works on your laptop can vanish on the projector.',
'<span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['occ','tem'],{'occ':([960,-60],'right'),'tem':([300,770],'left')},'Drawing of the side of the brain with the occipital lobe, at the back, and the temporal lobe, at the side, where colour and objects are processed, glowing orange and labelled.')

screen='''            <svg id="ccSvg" viewBox="0 0 520 260" width="100%" style="max-width:540px;display:block;border-radius:6px" role="img" aria-labelledby="ccD">
              <desc id="ccD">Two panels side by side. Left: a grey square on a dark navy background. Right: an adjustable grey square on a very light background. The task is to make the right square look the same as the left one.</desc>
              <rect x="0" y="0" width="260" height="260" fill="#13294B"/><rect x="260" y="0" width="260" height="260" fill="#F2F2F2"/>
              <rect id="ccL" x="85" y="85" width="90" height="90" fill="rgb(128,128,128)"/>
              <rect id="ccR" x="345" y="85" width="90" height="90" fill="rgb(128,128,128)"/>
              <rect id="ccBridge" x="130" y="118" width="260" height="24" fill="rgb(128,128,128)" display="none"/>
            </svg>
            <div id="ccSl" style="width:100%;max-width:440px" hidden><label for="ccIn" style="color:#E9EEF6;font-weight:700;display:block;margin-bottom:6px">Right square: darker ← → lighter</label><input id="ccIn" type="range" min="40" max="220" step="1" value="90" style="width:100%;accent-color:#FF5F05"></div>
            <div id="ccPair" hidden style="width:100%;max-width:440px;border-radius:8px;padding:26px 18px;text-align:center;font:700 22px/1.3 var(--body)">Sample text</div>'''
student=lab(screen,'Ready','Match the grey','Part 1: make two greys look the same. Part 2: predict which text colours pass the accessibility standard for contrast.','Start')

o.update(body=tabs('Match the grey','Two grey squares, one on dark and one on light. Make them look the same, then see what you actually set.',student,
 'About 10 minutes',
 ['Project part 1. Ask a volunteer to drag the slider until the two squares look the same, while the class calls out “lighter” or “darker”.',
  'Press “Done”. The page shows the value they chose and joins the squares with a bar of the original grey.',
  'In part 2, the class votes on each colour pair: does it pass the 4.5 to 1 contrast standard? Reveal the ratio each time.',
  'Bring one of your own slides and check its colours the same way.'],
 ['Why did the square on the dark background look lighter?',
  'Which pairs surprised you?',
  'How might a colour-coded chart look to someone with red–green colour vision deficiency?'],
 'Lightness and colour are judged relative to their surroundings, and projectors wash colours out. Check text contrast with a contrast checker rather than by eye, and never use colour as the only way to show a difference.',
 'Results vary with the screen, the room’s light and the viewer. That variation is part of the lesson.')+'''
  <div class="col lede">
    <p>In 2015, a photo of a striped dress divided the internet. Rosa Lafer-Sousa, Katherine Hermann and Bevil Conway surveyed 1,401 people: 57% saw it as blue and black, 30% as white and gold, and 11% as blue and brown.</p>
    <p>Their explanation: the photo gives few clues about the lighting. People who assume a cool, bluish light, like daylight from a blue sky, discount the blue and see white and gold. People who assume warm, artificial light discount the yellow and see blue and black.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>57% / 30%</strong><span>saw the dress as blue and black, or white and gold</span></div>
      <div role="listitem"><strong>1,401</strong><span>people surveyed, 313 of whom had never seen the photo</span></div>
      <div role="listitem"><strong>4.5 : 1</strong><span>the minimum contrast for normal-size text in the web accessibility standard</span></div>
      <div role="listitem"><strong>1 in 12</strong><span>men of Northern European ancestry have red–green colour vision deficiency</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Constancy</span>Seeing the surface, not the light</h2>
    <p>The light reaching your eye from a sheet of paper changes enormously between candlelight and noon. The paper still looks white. The brain estimates the lighting and discounts it, so that we see the surface, not the light. Usually that’s what we want. When the lighting is ambiguous, as in the dress photo, different brains can make different assumptions, and see different colours.</p>
    <h2 class="sec"><span class="n">Context</span>A grey is lighter on dark</h2>
    <p>The same grey looks lighter on a dark background than on a light one, which is what you measured in part 1. In a chart, the same colour can look different depending on what sits next to it.</p>
    <h2 class="sec"><span class="n">Not everyone sees it the same</span>Colour vision differs</h2>
    <p>Red–green colour vision deficiency affects about 1 in 12 men and 1 in 200 women among people of Northern European ancestry, and is less common in most other populations. A chart that relies on red versus green alone may carry no information for some of your students.</p>
    <h2 class="sec"><span class="n">For learning</span>Check contrast, don’t eyeball it</h2>
    <p>The web accessibility guidelines (WCAG) ask for a contrast ratio of at least 4.5 to 1 for normal text, and 3 to 1 for large text. Our judgement of contrast is relative, so a colour that looks fine on your bright laptop can fade on a projector. Use a contrast checker, and pair colour with labels, patterns or position.</p>
  </div>

'''+pgrid_html(),
tips_h='Lightness is relative. Measure contrast; don’t rely on colour alone.',
tips='''      <li><b>Check contrast</b><span>At least 4.5 to 1 for normal text. Use a checker.</span></li>
      <li><b>Never colour alone</b><span>Add labels, patterns or position to colour coding.</span></li>
      <li><b>Test on the projector</b><span>Colours fade; check slides in the room you’ll use.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1016/j.cub.2015.04.053">Lafer-Sousa, R., Hermann, K. L., &amp; Conway, B. R. (2015). Striking individual differences in color perception uncovered by ‘the dress’ photograph. <i>Current Biology, 25</i>(13), R545–R546.</a></li>
        <li><a href="https://medlineplus.gov/genetics/condition/color-vision-deficiency/">MedlinePlus Genetics. Color vision deficiency. U.S. National Library of Medicine.</a></li>
        <li><a href="https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html">W3C. Understanding Success Criterion 1.4.3: Contrast (Minimum). Web Content Accessibility Guidelines 2.2.</a></li>''',
foot='Contrast ratios in part 2 are calculated with the WCAG formula. The grey squares are drawn for this page. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'People who saw the dress as white and gold probably assumed the light was…',o:['Cool and bluish, like daylight','Warm and yellowish','Perfectly white'],a:0,f:'So their brains discounted the blue.'},
 {q:'The same grey looks lighter on…',o:['A dark background','A light background','Any background'],a:0,f:'Lightness is judged relative to surroundings.'},
 {q:'The minimum contrast for normal text in WCAG is…',o:['4.5 to 1','2 to 1','10 to 1'],a:0,f:'3 to 1 for large text.'}]''',
js=PANEL_JS+r'''
/* ---------- grey match + contrast ---------- */
const lum=h=>{const c=[0,2,4].map(i=>parseInt(h.slice(i+1,i+3),16)/255).map(x=>x<=0.03928?x/12.92:Math.pow((x+0.055)/1.055,2.4));return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2]};
const ratio=(a,b)=>{const x=lum(a),y=lum(b);return (Math.max(x,y)+0.05)/(Math.min(x,y)+0.05)};
const PAIRS=[['#13294B','#FFFFFF','Navy text on white'],['#FF5F05','#FFFFFF','Orange text on white'],['#767676','#FFFFFF','Mid-grey text on white'],['#999999','#FFFFFF','Light grey text on white'],['#13294B','#FF5F05','Navy text on orange'],['#FCB316','#FFFFFF','Gold text on white'],['#2E7D32','#D32F2F','Green text on red']];
const setR=v=>$('ccR').setAttribute('fill',`rgb(${v},${v},${v})`);
$('ccIn').addEventListener('input',e=>setR(+e.target.value));
startRun(async()=>{$('ccSvg').style.display='block';$('ccBridge').setAttribute('display','none');$('ccPair').hidden=true;$('ccIn').value=90;setR(90);$('ccIn').disabled=false;
 say('Part 1 of 2','Make them look the same','Drag the slider (or use the arrow keys) until the right square looks the same grey as the left one. Then press Done.');
 $('ccSl').hidden=false;$('ccIn').focus();await nextBtn('Done');if(!RUN)return;
 const v=+$('ccIn').value;$('ccIn').disabled=true;$('ccBridge').setAttribute('display','inline');$('ccL').setAttribute('y',85);
 const d=v-128;
 say('Part 1 of 2',Math.abs(d)<6?'Close to identical':`You set it ${Math.abs(d)} steps ${d>0?'lighter':'darker'}`,
  `The left square is 128 on a 0–255 scale. You chose ${v}. `+(d>4?'Like most people, you made the right square lighter than the left one, because the grey on the dark background looked lighter.':d<-4?'Most people go the other way: the grey on dark looks lighter, so they make the right one lighter.':'You matched it closely, but notice how different they looked at first.')+' The bar joining them is the original grey.');
 await nextBtn('Part 2: contrast');if(!RUN)return;$('ccSl').hidden=true;$('ccSvg').style.display='none';
 let right=0;const order=shuf([...PAIRS]);
 for(let i=0;i<order.length;i++){const [fg,bg,name]=order[i];const r=ratio(fg,bg),pass=r>=4.5;
  const p=$('ccPair');p.hidden=false;p.style.color=fg;p.style.background=bg;p.textContent='Read this sample text';
  say(`Part 2 · ${i+1} of ${order.length}`,name,'Does this pass the 4.5 to 1 minimum for normal text?');
  const a=await ask(['Passes','Fails'],'Does it pass?');if(!RUN)return;const ok=(a===0)===pass;if(ok)right++;mark(pass?0:1,a);
  say(null,null,(ok?'<b class="ok">Right.</b> ':'<b class="no">Not quite.</b> ')+`Contrast ratio ${r.toFixed(2)} to 1. `+(name.startsWith('Green')?'Hue alone gives almost no contrast, and red–green is the most common colour vision deficiency.':name.startsWith('Mid')?'This grey just passes; a shade lighter would not.':name.startsWith('Navy text on o')?'It passes, narrowly. White on the same orange would not.':''));
  if(i<order.length-1){await nextBtn('Next pair');if(!RUN)return;hideCh()}}
 say('What happened',`${right} of ${PAIRS.length} contrast calls right`,'Lightness is judged relative to its surroundings, so our eyes are poor contrast meters. A grey you set by eye in part 1 drifted from the true value; the same thing happens when we judge text colours. Measure contrast instead.')});
'''+grid('''[
 ['In a survey of 1,401 people, what share saw the dress as blue and black?',['57%','30%','90%'],0,'30% saw white and gold, 11% blue and brown.'],
 ['People who saw white and gold probably assumed the lighting was…',['Cool and bluish','Warm and yellowish','Dim'],0,'So they discounted the blue in the photo.'],
 ['Red–green colour vision deficiency affects about how many men of Northern European ancestry?',['1 in 12','1 in 200','1 in 1,000'],0,'And about 1 in 200 women.'],
 ['WCAG’s minimum contrast for normal-size text is…',['4.5 to 1','3 to 1','7 to 1'],0,'3 to 1 is the minimum for large text.'],
 ['Does orange #FF5F05 text on white pass that minimum?',['No, about 3 to 1','Yes, easily','Exactly 4.5 to 1'],0,'Bright colours often have surprisingly low contrast with white.']]''','The pattern: colour and lightness are judged in context, so measure what matters.'))
write(o)

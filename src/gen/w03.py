from wkit import *
o=wbase(3,'Reading Is Learned, Not Natural','Reading is learned,','not natural',
'Speech comes naturally to children; reading does not. Writing is a recent invention, so the brain has to repurpose visual areas to read. Watching that happen, even in adults, says a lot about what fluency is.')
o['hero_aria'],o['hero_js']=hero(['occ','tem'],{'occ':([960,-60],'right'),'tem':([300,770],'left')},'Drawing of the side of the brain with the occipital lobe, at the back, where reading begins, and the temporal lobe, where written words connect to spoken language, glowing orange and labelled.')
screen='''            <svg id="rdKey" viewBox="0 0 520 84" width="100%" style="max-width:520px;display:block;background:#fff;border-radius:6px" role="img" aria-label="Key: each symbol and the letter it stands for."></svg>
            <svg id="rdWord" viewBox="0 0 520 120" width="100%" style="max-width:520px;display:block;background:#F4F6FA;border-radius:6px" role="img" aria-label="A word written in the new script."></svg>
            <p class="prog" id="rdP" aria-live="polite">&nbsp;</p>'''
student=lab(screen,'Ready','Read a new script','Eight letters, eight new symbols. Read 12 words, as fast as you can while staying accurate. For the last six, the key disappears.')
GLY={'a':'<circle cx="20" cy="20" r="13" fill="none" stroke="#13294B" stroke-width="5"/>',
'e':'<path d="M20 5 L35 34 L5 34 Z" fill="none" stroke="#13294B" stroke-width="5" stroke-linejoin="round"/>',
'n':'<path d="M10 5 V35 M30 5 V35" stroke="#13294B" stroke-width="5"/>',
'o':'<rect x="7" y="7" width="26" height="26" fill="none" stroke="#13294B" stroke-width="5"/>',
'p':'<path d="M20 5 V35 M20 5 A9 9 0 1 1 20 23" fill="none" stroke="#13294B" stroke-width="5"/>',
'r':'<path d="M6 32 L20 8 L34 32" fill="none" stroke="#13294B" stroke-width="5" stroke-linejoin="round"/>',
's':'<path d="M6 10 L16 30 L24 10 L34 30" fill="none" stroke="#13294B" stroke-width="5" stroke-linejoin="round"/>',
't':'<path d="M20 5 V35 M8 14 H32" stroke="#13294B" stroke-width="5"/>'}
import json
o.update(body=tabs('Read a new script','A made-up alphabet for familiar English words. Watch your reading speed change in a few minutes.',student,
 'About 10 minutes',
 ['Students do the 12 words on their own devices and note how their time per word changed.',
  'Ask: how did it feel at the start? What were you paying attention to?',
  'Ask: in the last six words, without the key, what were you relying on?',
  'Connect to your subject: which notations, symbols or diagrams are a “new script” for your students?'],
 ['What happened to your attention as decoding got faster?',
  'What would it take to read this script as easily as English?',
  'Which symbols in our field do beginners still have to decode letter by letter?'],
 'New notation (chemical formulas, mathematical symbols, musical scores, code) is read slowly and effortfully at first, leaving little attention for meaning. Give short, frequent practice reading it until it becomes fluent.',
 'Some letters are also flipped or turned versions of each other, which is part of what makes early reading hard.')+'''
  <div class="col lede">
    <p>Reading is too recent an invention for evolution to have built a dedicated reading area. Instead, learning to read changes how existing visual and language areas work.</p>
    <p>Stanislas Dehaene and colleagues scanned the brains of 63 adults: 10 who were illiterate, 22 who had learned to read as adults, and 31 who had learned as children. Literacy increased the response to written words in a region of the left fusiform gyrus, often called the visual word form area, and strengthened the response to speech in an area of the temporal lobe.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>63</strong><span>adults scanned: illiterate, literate as adults, and literate as children</span></div>
      <div role="listitem"><strong>Left fusiform</strong><span>the region that learns to respond to written words</span></div>
      <div role="listitem"><strong>Faces</strong><span>lost a little ground there as reading gained it</span></div>
      <div role="listitem"><strong>Adults too</strong><span>most changes also appeared when people learned to read in adulthood</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Recycling</span>A new job for visual cortex</h2>
    <p>As literacy increased the response to writing in the left fusiform region, it produced a small competition with faces at the same location. Literacy also broadly enhanced visual responses in fusiform and occipital cortex, and gave spoken words a route to activate their spelling.</p>
    <h2 class="sec"><span class="n">Never too late</span>Adult learners change too</h2>
    <p>Most of these changes appeared even in people who learned to read as adults. The authors emphasise that both childhood and adult education can profoundly refine how the cortex is organised.</p>
    <h2 class="sec"><span class="n">Fluency</span>Why decoding speed matters</h2>
    <p>In the activity, the first words took effort: finding each symbol, holding letters in mind, then guessing the word. As the mapping became automatic, attention was freed for the word itself. That freed attention is what comprehension needs.</p>
    <h2 class="sec"><span class="n">For learning</span>Every discipline has a script</h2>
    <p>Students meeting chemical structures, equations, musical notation or code for the first time are decoding a new script. Until reading it is fluent, little attention is left for meaning. Short, frequent practice reading the notation itself can pay off.</p>
  </div>

'''+pgrid_html(),
tips_h='Make the notation fluent, so attention can go to meaning.',
tips='''      <li><b>Spot the new scripts</b><span>Which symbols in your course are still decoded letter by letter?</span></li>
      <li><b>Short, frequent reading practice</b><span>A few minutes reading notation aloud or translating it.</span></li>
      <li><b>Expect adult learners to change</b><span>The brain reorganises for reading at any age.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1126/science.1194140">Dehaene, S., Pegado, F., Braga, L. W., Ventura, P., Nunes Filho, G., Jobert, A., Dehaene-Lambertz, G., Kolinsky, R., Morais, J., &amp; Cohen, L. (2010). How learning to read changes the cortical networks for vision and language. <i>Science, 330</i>(6009), 1359–1364.</a></li>''',
foot='The script is made up for this activity. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'Learning to read increases the response to written words in…',o:['A region of the left fusiform gyrus','The cerebellum','The right ear'],a:0,f:'Often called the visual word form area.'},
 {q:'Did brain changes appear in people who learned to read as adults?',o:['Yes, most of them','No, only in children','Only in reading speed'],a:0,f:'Dehaene and colleagues, 2010.'},
 {q:'Why does decoding speed matter for comprehension?',o:['Fluent decoding frees attention for meaning','Fast readers skip words','It doesn’t'],a:0,f:'Effortful decoding uses up attention.'}]''',
js=PANEL_JS+r'''
/* ---------- new script ---------- */
const GLY='''+json.dumps(GLY)+r''';
const KEYS=Object.keys(GLY);
$('rdKey').innerHTML=KEYS.map((k,i)=>`<g transform="translate(${10+i*64},6) scale(.9)">${GLY[k]}</g><text x="${28+i*64}" y="76" text-anchor="middle" font-family="Source Sans 3,sans-serif" font-size="24" font-weight="700" fill="#13294B">${k}</text>`).join('');
const WL=[['stop',['pots','post','spot']],['rest',['tears','sent','rose']],['near',['earn','rate','pear']],['tone',['note','tore','nose']],['snap',['pans','span','naps']],['rope',['pore','repo','tops']],['seat',['east','teas','sate']],['star',['rats','arts','tars']],['poet',['tope','pots','port']],['nose',['ones','tone','sore']],['parent',['patron','person','prates']],['toast',['stoat','oats','taps']]];
function draw(w){const n=w.length,x0=260-n*30;$('rdWord').innerHTML=[...w].map((c,i)=>`<g transform="translate(${x0+i*60+6},26) scale(1.25)">${GLY[c]}</g>`).join('')}
startRun(async()=>{$('rdKey').style.visibility='visible';const list=shuf(WL.slice());const times=[];let right=0,right2=0;
 for(let i=0;i<12;i++){const [w,ds]=list[i];if(i===6){$('rdKey').style.visibility='hidden';say('Without the key',null,'The key is gone. Read from memory.');await nextBtn('Continue');if(!RUN)return}
  draw(w);$('rdP').textContent=`Word ${i+1} of 12`+(i>=6?' · no key':'');say(i<6?'With the key':'Without the key','Which word is this?','');
  const opts=shuf([w,...ds]);const t0=performance.now();const a=await ask(opts,'Which word is this?');if(!RUN)return;const t=(performance.now()-t0)/1000;times.push(t);
  const ok=opts[a]===w;if(ok){if(i<6)right++;else right2++}mark(opts.indexOf(w),a);
  say(null,null,(ok?'<b class="ok">Right.</b> ':`<b class="no">Not quite.</b> It was “${w}”. `)+`${t.toFixed(1)} seconds.`);await sw(ok?700:1400);if(!RUN)return;hideCh()}
 $('rdWord').innerHTML='';$('rdKey').style.visibility='visible';$('rdP').textContent=' ';
 const m=a=>a.reduce((x,y)=>x+y,0)/a.length,f=m(times.slice(0,3)),l=m(times.slice(3,6)),nk=m(times.slice(6)),mx=Math.max(f,l,nk);
 $('sRes').innerHTML='<div class="res">'+barRow('First 3',f,mx,f.toFixed(1)+' s','#FCB316')+barRow('Next 3',l,mx,l.toFixed(1)+' s','#FCB316')+barRow('No key',nk,mx,nk.toFixed(1)+' s','#7DD3A8')+'</div>';
 say('What happened',l<f?'You got faster in minutes':'Decoding takes practice',`With the key: ${right} of 6 right. Without it: ${right2} of 6. At first, each word meant finding symbols one by one. As the mapping becomes automatic, reading speeds up and attention can move to meaning. That is the early stage of what every reader goes through, and what the brain reorganises itself to support.`)});
'''+grid('''[
 ['How many adults did Dehaene and colleagues scan?',['63','6','630'],0,'10 illiterate, 22 literate as adults, 31 literate as children.'],
 ['Literacy increased the response to written words in…',['A region of the left fusiform gyrus','The right frontal lobe','The brainstem'],0,'The visual word form area.'],
 ['What lost a little ground in that region as reading gained it?',['Faces','Music','Colour'],0,'A small competition with faces.'],
 ['Did most changes appear in people who learned to read as adults?',['Yes','No','Only half'],0,'Adult education can refine cortical organisation.'],
 ['Literacy also strengthened the brain’s response to…',['Speech','Smell','Touch'],0,'In the planum temporale, part of the temporal lobe.']]''','The pattern: reading rewires the brain at any age, and fluency frees attention for meaning.'))
write(o)

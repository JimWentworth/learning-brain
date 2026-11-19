import sys;sys.path.insert(0,'gen')
from pkit import *
from memjs import grid
o=pbase(9,'Learning to See Like an Expert: Perceptual Learning','Learning to see','like an expert',
'Experts don’t just know more; they see differently. A radiologist sees the shadow, a chemist sees the functional group, a musician hears the chord. That kind of seeing can be trained, with many quick examples and feedback.',
'<span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['ffa','v1'],{'ffa':([520,770],'left'),'v1':([960,-60],'right')},'Drawing of the side of the brain with the visual cortex, at the back, and the fusiform area, underneath, where expert recognition of faces, words and objects develops, glowing orange and labelled.')

screen='''            <svg id="plSvg" viewBox="0 0 300 220" width="100%" style="max-width:420px;display:block;background:#fff;border-radius:6px" role="img" aria-labelledby="plD">
              <desc id="plD">A made-up creature drawn as an outline with two bumps, a dot, and some stripes. Each one belongs to the family Kel or the family Rin.</desc>
              <g id="plG"></g>
            </svg>
            <p class="prog" id="plCap" aria-live="polite"></p>'''
student=lab(screen,'Ready','Kel or Rin?','You’ll see 24 made-up creatures from two families, Kel and Rin. Nobody will tell you the rule. Guess, use the feedback, and see how fast your eye learns.','Start')

o.update(body=tabs('Kel or Rin?','Two families of made-up creatures. No rule given, just quick examples and feedback. Watch your accuracy change.',student,
 'About 10 minutes',
 ['Students do the 24 trials on their own devices. Ask them not to discuss the rule yet.',
  'Ask for a show of hands: who got better from the first block to the last? Who can state the rule?',
  'Reveal the rule. Discuss: some people improved before they could say what they were seeing.',
  'Ask what the “Kel or Rin” of your subject is: the distinction experts see at a glance and beginners must learn.'],
 ['When did you start to get it right? Could you say why?',
  'What did you have to learn to ignore?',
  'What do experts in our field see instantly that you still have to work out?'],
 'Build short classification drills from your subject: twenty quick examples, each with immediate feedback, mixing categories and varying the irrelevant features. Is this graph linear or exponential? Which reaction type is this? Which artist painted this?',
 'The creatures are random, so a few people find the rule in the first block and others not at all. Both are useful to discuss.')+'''
  <div class="col lede">
    <p>Perceptual learning is the improvement in picking up information that comes from practice. Philip Kellman and colleagues argue it is one of the most important parts of expertise in almost any field, including mathematics, and one of the most neglected in teaching.</p>
    <p>Most teaching explains facts and procedures. Perceptual learning works differently: it gives many short examples and asks learners to recognise, classify or match them, with feedback, until the key structure jumps out.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>Many, fast</strong><span>short classification trials with feedback: the core of a perceptual learning module</span></div>
      <div role="listitem"><strong>Lasting</strong><span>gains in algebra and fractions from perceptual learning modules</span></div>
      <div role="listitem"><strong>Mixed</strong><span>examples of different painters taught their styles better than blocked ones</span></div>
      <div role="listitem"><strong>Fooled</strong><span>learners still rated blocked study as better, after doing worse with it</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">In mathematics</span>Seeing structure</h2>
    <p>Kellman, Christine Massey and colleagues built perceptual learning modules for algebra and fractions. Instead of solving full problems, students made many quick judgements, for example matching an equation to its transformation or a fraction to its picture. The modules focus learning on recognising and discriminating key structures, and students using them showed significant and lasting gains.</p>
    <h2 class="sec"><span class="n">Mix the examples</span>Painters, interleaved</h2>
    <p>Nate Kornell and Robert Bjork had people learn the styles of 12 little-known painters from six paintings each. Paintings shown interleaved with other artists’ work led to better recognition of new paintings than paintings shown in blocks by artist. Yet participants rated blocking as more effective, even after their own test results showed the opposite. A high-powered replication in 2014 found the same advantage for interleaving.</p>
    <h2 class="sec"><span class="n">Why mixing helps</span>Differences, not just similarities</h2>
    <p>Learning a category means learning what separates it from its neighbours. Seeing examples from different categories side by side draws attention to the differences that matter, and away from features that vary but don’t count, like the colour and angle of the creatures above.</p>
    <h2 class="sec"><span class="n">For learning</span>Train the eye, not only the rule</h2>
    <p>Telling students the rule helps, but it doesn’t make them see quickly. Experts got there through thousands of examples. Short, mixed, feedback-rich drills compress some of that experience into minutes.</p>
  </div>

'''+pgrid_html(),
tips_h='Experts see. Give students the examples that train seeing.',
tips='''      <li><b>Many short examples</b><span>Twenty quick classifications beat two long explanations for this.</span></li>
      <li><b>Mix the categories</b><span>Interleave so the differences stand out.</span></li>
      <li><b>Vary what doesn’t matter</b><span>So students learn to ignore it.</span></li>''',
sources='''        <li>Kellman, P. J., Massey, C., Roth, Z., Burke, T., Zucker, J., Sawa, A., Aguero, K. E., &amp; Wise, J. A. (2008). Perceptual learning and the technology of expertise: Studies in fraction learning and algebra. <i>Pragmatics &amp; Cognition, 16</i>(2), 356–405.</li>
        <li><a href="https://doi.org/10.1111/j.1756-8765.2009.01053.x">Kellman, P. J., Massey, C. M., &amp; Son, J. Y. (2010). Perceptual learning modules in mathematics: Enhancing students’ pattern recognition, structure extraction, and fluency. <i>Topics in Cognitive Science, 2</i>(2), 285–305.</a></li>
        <li><a href="https://doi.org/10.1111/j.1467-9280.2008.02127.x">Kornell, N., &amp; Bjork, R. A. (2008). Learning concepts and categories: Is spacing the “enemy of induction”? <i>Psychological Science, 19</i>(6), 585–592.</a></li>
        <li><a href="https://doi.org/10.3389/fpsyg.2014.00259">Verkoeijen, P. P. J. L., &amp; Bouwmeester, S. (2014). Is spacing really the “friend of induction”? <i>Frontiers in Psychology, 5</i>, 259.</a></li>''',
foot='Kel and Rin are made-up creatures generated for this activity. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'Perceptual learning means…',o:['Getting better at picking up information through practice','Memorising definitions','Learning only with pictures'],a:0,f:'Experts see structure beginners miss.'},
 {q:'Kornell and Bjork found painters’ styles were learned better when paintings were…',o:['Interleaved with other artists','Blocked by artist','Shown once'],a:0,f:'Yet learners preferred blocking.'},
 {q:'A perceptual learning module mostly consists of…',o:['Many quick classifications with feedback','A long lecture','One worked example'],a:0,f:'Recognise, discriminate, match.'}]''',
js=PANEL_JS+r'''
/* ---------- Kel or Rin ---------- */
const COLS=['#13294B','#3E6B9E','#B8430A','#2E6B4F'];
function creature(kel){const rot=Math.random()*360,sc=0.8+Math.random()*0.4,col=COLS[Math.floor(Math.random()*4)],st=Math.floor(Math.random()*4),flip=Math.random()<.5;
 const big=[0,0,44],small=[52,0,27];const tgt=kel?small:big;const jitter=()=>(Math.random()-.5)*8;
 let s=`<g transform="translate(130,110) rotate(${rot}) scale(${sc}${flip?',-'+sc:''})"><circle cx="${big[0]}" cy="${big[1]}" r="${big[2]}" fill="#F1F4F9" stroke="${col}" stroke-width="5"/><circle cx="${small[0]}" cy="${small[1]}" r="${small[2]}" fill="#F1F4F9" stroke="${col}" stroke-width="5"/><circle cx="${big[0]}" cy="${big[1]}" r="${big[2]-2.5}" fill="#F1F4F9"/>`;
 for(let i=0;i<st;i++)s+=`<line x1="${-30+i*14}" y1="${-30}" x2="${-30+i*14}" y2="${-12}" stroke="${col}" stroke-width="4"/>`;
 s+=`<circle cx="${tgt[0]+(kel?6:-10)+jitter()}" cy="${tgt[1]+12+jitter()}" r="7" fill="${col}"/></g>`;return s}
startRun(async()=>{const N=24;const seq=shuf([...Array(N/2).fill(true),...Array(N/2).fill(false)]);const hit=[];
 say('Practice','Kel or Rin?','Make your best guess. You’ll get feedback straight away.');
 for(let i=0;i<N;i++){$('plG').innerHTML=creature(seq[i]);$('plCap').textContent=`${i+1} of ${N}`;
  const a=await ask(['Kel','Rin'],'Kel or Rin?');if(!RUN)return;const ok=(a===0)===seq[i];hit.push(ok);mark(seq[i]?0:1,a);
  say(`Block ${Math.floor(i/6)+1} of 4`,ok?'Right':'Not quite',(ok?'<b class="ok">Right.</b> ':'<b class="no">Not quite.</b> ')+`That one was ${seq[i]?'Kel':'Rin'}.`);
  await sw(ok?550:1100);if(!RUN)return;hideCh()}
 $('plCap').textContent='';$('plG').innerHTML='';
 const blocks=[0,1,2,3].map(b=>hit.slice(b*6,b*6+6).filter(Boolean).length);
 $('sRes').innerHTML='<div class="res">'+blocks.map((v,b)=>barRow(`Block ${b+1}`,v,6,`${v} of 6`,'#FCB316')).join('')+'</div>';
 say('Your learning curve','What was the rule?','Before the answer: which feature decides the family?');
 const r=await ask(['Where the dot sits','The colour','The number of stripes','I couldn’t tell'],'What decides the family?');if(!RUN)return;mark(0,r);
 const gain=blocks[3]-blocks[0];
 say('The rule','Kel: the dot is in the small bump',`Rin has the dot in the big bump. Colour, size, angle and stripes were random. `+(gain>0?`You went from ${blocks[0]} to ${blocks[3]} of 6. `:'')+'Many people improve before they can state the rule. That is perceptual learning: the eye picks up the feature that matters, with examples and feedback rather than explanation.')});
'''+grid('''[
 ['Did students using perceptual learning modules for algebra and fractions show lasting gains?',['Yes, significant and persisting','No difference','Only short-term'],0,'Kellman and colleagues.'],
 ['When learning painters’ styles, which worked better?',['Interleaving different artists','Blocking each artist','No difference'],0,'Kornell and Bjork, 2008.'],
 ['Which did those learners rate as more effective?',['Blocking','Interleaving','Neither'],0,'Even after their own test results showed the opposite.'],
 ['Did a high-powered 2014 replication find the interleaving advantage?',['Yes, a medium-sized one','No','It reversed'],0,'With a web-based sample.'],
 ['What does a perceptual learning module ask learners to do?',['Recognise, classify or match many quick examples','Read a long explanation','Memorise a list'],0,'With feedback on each one.']]''','The pattern: seeing like an expert is learned from many varied examples with feedback.'))
write(o)

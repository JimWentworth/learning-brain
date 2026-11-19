import sys;sys.path.insert(0,'gen')
from pkit import *
from memjs import grid
o=pbase(8,'Expectation Shapes What You See and Hear','Expectation','shapes what you see',
'The same shape can be a letter or a number. The same noisy sound can be a word you never heard. What you expect fills in what the senses leave open, for you and for every student in the room.',
'<span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['tem','pfc'],{'tem':([300,770],'left'),'pfc':([40,-60],'left')},'Drawing of the side of the brain with the temporal lobe, at the side, and the prefrontal cortex, at the front, glowing orange and labelled.')

screen='''            <svg id="exSvg" viewBox="0 0 520 220" width="100%" style="max-width:540px;display:block;background:#fff;border-radius:6px" role="img" aria-labelledby="exD">
              <desc id="exD">Characters flash one at a time in the centre of a white panel. The last one is an ambiguous shape that can be read as the letter B or the number 13.</desc>
              <g id="exG" font-family="Source Sans 3, sans-serif" font-weight="700" fill="#13294B"></g>
            </svg>
            <p class="prog" id="exCap" aria-live="polite"></p>'''
student=lab(screen,'Ready','Letter or number?','A short series of characters will flash in the centre. Watch them all. Then say what the last one was.','Start')

AMB='''<rect x="0" y="0" width="16" height="88"/><path d="M27 7 h11 a18.5 18.5 0 0 1 0 37 h-6 h6 a18.5 18.5 0 0 1 0 37 h-11" fill="none" stroke="#13294B" stroke-width="15"/>'''
HA='''<path d="M4 80 L14 2 M48 80 L38 2 M9 44 L43 44" stroke="#13294B" stroke-width="14" fill="none" stroke-linecap="square"/>'''

o.update(body=tabs('Letter or number?','A few characters flash by. The last one is the same shape every time. What it looks like depends on what came before.',student,
 'About 10 minutes',
 ['Split the class into two halves. Have one half close their eyes while you show the other half round 1 (letters). Swap for round 2 (numbers).',
  'Each half writes down what the last character was, then compare. The two halves usually disagree.',
  'Show both side by side: the shape is identical.',
  'Finish with “THE CAT” and ask how the same shape became two different letters.'],
 ['How can the same shape be two different things?',
  'What did the earlier characters do to your brain?',
  'In this course, where might students “see” what they expect rather than what is there?'],
 'Expectations are set by what comes first. Tell students what kind of thing they are about to see (“this graph shows a decline”, “the next term is a technical one”), and watch for students reading their misconceptions into new data.',
 'The original experiments flashed the shape very briefly. On a slow projector the effect may be weaker; the side-by-side reveal still works.')+'''
  <div class="col lede">
    <p>In a classic 1955 study, Jerome Bruner and Leigh Minturn briefly showed students a broken capital B, with the curved part set slightly apart from the upright stroke, so it could also be read as 13. Students who had just seen letters tended to report a B; those who had just seen numbers tended to report 13.</p>
    <p>A 2020 study confirmed the effect: the same shape was judged 13 between 12 and 14, and B between A and C. Context still biased judgements even when people did not consciously see it, though the effect was smaller.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>B or 13</strong><span>the same shape, read differently after letters or numbers</span></div>
      <div role="listitem"><strong>19 of 20</strong><span>listeners didn’t notice that a speech sound had been replaced by a cough</span></div>
      <div role="listitem"><strong>Can’t say where</strong><span>listeners couldn’t place the cough in the sentence</span></div>
      <div role="listitem"><strong>Smaller</strong><span>but still present when the context wasn’t consciously seen</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">In hearing</span>The sound that wasn’t there</h2>
    <p>In 1970, Richard Warren played students a recording of the sentence “The state governors met with their respective legislatures convening in the capital city.” One sound, the first “s” in “legislatures”, had been cut out and replaced with a cough. In a group of 20, 19 did not notice anything was missing, and listeners could not say where in the sentence the cough had occurred. The brain restored the sound from what the word had to be.</p>
    <h2 class="sec"><span class="n">Why</span>Prediction fills the gaps</h2>
    <p>Signals from the senses are often incomplete or ambiguous: a smudged letter, a word lost in noise. The brain resolves them with what is likely in context. Usually that makes perception faster and more robust. It also means we can perceive what we expect, not what is there.</p>
    <h2 class="sec"><span class="n">For learning</span>Set the right expectation</h2>
    <p>Students also perceive through their expectations. A student who expects a graph to show growth may read growth into it; a student who has never heard a technical term may hear a familiar word instead. Saying what is coming, and naming new terms before using them, gives the brain the right context to fill in from.</p>
  </div>

'''+pgrid_html(),
tips_h='Tell students what they’re about to see.',
tips='''      <li><b>Frame before you show</b><span>Say what a graph or example is meant to show.</span></li>
      <li><b>Name new terms first</b><span>Write and say a technical word before using it in speech.</span></li>
      <li><b>Check what they saw</b><span>Ask students to describe it before you interpret it.</span></li>''',
sources='''        <li>Bruner, J. S., &amp; Minturn, A. L. (1955). Perceptual identification and perceptual organization. <i>Journal of General Psychology, 53</i>(1), 21–28.</li>
        <li><a href="https://doi.org/10.1177/0956797620915887">Biderman, D., Shir, Y., &amp; Mudrik, L. (2020). B or 13? Unconscious top-down contextual effects at the categorical but not the lexical level. <i>Psychological Science, 31</i>(6), 663–677.</a></li>
        <li><a href="https://doi.org/10.1126/science.167.3917.392">Warren, R. M. (1970). Perceptual restoration of missing speech sounds. <i>Science, 167</i>(3917), 392–393.</a></li>''',
foot='The ambiguous characters are drawn for this page in the style of the classic B/13 and THE CAT figures. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'After seeing a series of numbers, the ambiguous B/13 shape tends to look like…',o:['13','B','Nothing in particular'],a:0,f:'Context sets the expectation.'},
 {q:'When a sound in “legislatures” was replaced by a cough, most listeners…',o:['Heard the missing sound anyway','Noticed it was missing','Heard only the cough'],a:0,f:'Phonemic restoration.'},
 {q:'Why does expectation shape perception?',o:['The brain uses context to resolve ambiguous signals','The eyes are faulty','Only in illusions'],a:0,f:'Usually it helps; sometimes it misleads.'}]''',
js=PANEL_JS+r'''
/* ---------- B or 13 ---------- */
const AMBp='''+repr(AMB)+''',HAp='''+repr(HA)+r''';
const amb=(h)=>{const k=h/88;return `<g transform="translate(${-23*k},${32-h}) scale(${k})">${AMBp}</g>`};const ha=(h)=>{const k=h/80;return `<g transform="translate(${-26*k},${32-h}) scale(${k})">${HAp}</g>`};
const txt=t=>`<text x="0" y="32" font-size="96" text-anchor="middle">${t}</text>`;
const at=(x,s)=>`<g transform="translate(${x},110)">${s}</g>`;
async function flash(items){for(const it of items){$('exG').innerHTML=at(260,it.startsWith('<')?it:txt(it));await sw(650);if(!RUN)return;$('exG').innerHTML='';await sw(180);if(!RUN)return}
 $('exG').innerHTML=at(260,amb(70));await sw(500);$('exG').innerHTML=at(260,'<g transform="translate(-40,-40)" fill="#13294B"><rect width="80" height="80" opacity=".9"/></g>')+at(200,'<rect x="-14" y="-40" width="28" height="80" fill="#3E6B9E"/>')+at(320,'<rect x="-14" y="-40" width="28" height="80" fill="#3E6B9E"/>');await sw(400);$('exG').innerHTML=''}
startRun(async()=>{const ans=[];const rounds=shuf([['L','K','M','A','Y'],['16','10','12','17','14']]);
 for(let r=0;r<2;r++){say(`Round ${r+1} of 2`,'Watch the centre','Five characters, then one more. Name the last one.');
  if(r>0){await nextBtn('Start round 2');if(!RUN)return}
  await sw(500);await flash(rounds[r]);if(!RUN)return;
  const a=await ask(['B','13','Not sure'],'What was the last character?');if(!RUN)return;ans.push([rounds[r][0]==='L'?'letters':'numbers',a]);hideCh();
  say(null,'Noted','');}
 const row=(y,l,r,dx)=>`<g transform="translate(260,${y})"><text x="${-dx}" y="32" font-size="64" text-anchor="middle">${l}</text>${amb(46)}<text x="${dx}" y="32" font-size="64" text-anchor="middle">${r}</text></g>`;$('exG').innerHTML=row(40,'A','C',70)+row(140,'12','14',95);
 $('exCap').textContent='The middle shape is identical in both rows.';
 const L=ans.find(x=>x[0]==='letters')[1],Nn=ans.find(x=>x[0]==='numbers')[1],nm=['B','13','not sure'];
 say('The reveal','It was the same shape both times',`After letters you said ${nm[L]}; after numbers you said ${nm[Nn]}. `+(L===0&&Nn===1?'Exactly the pattern Bruner and Minturn found.':'In the original study, most people saw B after letters and 13 after numbers. A brief flash makes the effect stronger.')+' Side by side, it reads as B between A and C, and 13 between 12 and 14.');
 await nextBtn('One more');if(!RUN)return;$('exCap').textContent='';
 const T=(x,c)=>`<text x="${x}" y="32" font-size="80" text-anchor="middle">${c}</text>`;
 $('exG').innerHTML=at(0,`<g transform="translate(70,0)">${T(0,'T')}<g transform="translate(62,0)">${ha(57)}</g>${T(124,'E')}</g><g transform="translate(320,0)">${T(0,'C')}<g transform="translate(64,0)">${ha(57)}</g>${T(128,'T')}</g>`);
 say('Two words','What do these words say?','');
 const b=await ask(['THE CAT','TAE CHT','THE CHT'],'What do the words say?');if(!RUN)return;mark(0,b);
 $('exCap').textContent='The second letter of each word is the same shape.';
 say('What happened','The word decided the letter','The middle letters are identical. In “THE” you read an H, in “CAT” an A, because the word around it tells your brain what to expect. Perception uses context to settle what the senses leave open.')});
'''+grid('''[
 ['In Bruner and Minturn’s 1955 study, students who had just seen numbers tended to read the ambiguous shape as…',['13','B','A smudge'],0,'Those who had seen letters tended to read B.'],
 ['In a 2020 study, did the context still bias judgements when people didn’t consciously see it?',['Yes, but less','No','Yes, more strongly'],0,'Unconscious context had a smaller effect.'],
 ['When Warren replaced one sound in a sentence with a cough, how many of 20 listeners noticed the missing sound?',['Hardly any: 19 did not','About half','All of them'],0,'And they couldn’t say where the cough was.'],
 ['Which sound did Warren remove?',['The first “s” in “legislatures”','The “th” in “the”','A whole word'],0,'Replaced by a cough of the same length.'],
 ['Could listeners say where in the sentence the cough occurred?',['No','Yes, exactly','Only on a second listen'],0,'The restored sound felt fully present.']]''','The pattern: the brain fills gaps with what it expects.'))
write(o)

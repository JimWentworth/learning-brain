import sys;sys.path.insert(0,'gen')
from pkit import *
from memjs import grid
o=pbase(7,'Hearing With Your Eyes: Lips, the McGurk Effect and Captions','Hearing','with your eyes',
'Speech perception isn’t just hearing. The brain combines the sound with what it sees on the speaker’s face, so strongly that a mismatched face can change the sound you hear. That matters in every lecture hall.',
'<span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['tem','v1'],{'tem':([300,770],'left'),'v1':([960,-60],'right')},'Drawing of the side of the brain with the temporal lobe, at the side, which processes speech sounds, and the visual cortex, at the back, glowing orange and labelled.')

screen='''            <svg id="lpSvg" viewBox="0 0 520 200" width="100%" style="max-width:540px;display:block;background:#F4E3D3;border-radius:6px" role="img" aria-labelledby="lpD">
              <desc id="lpD">Three drawings of a mouth, in order, showing the lip shapes for one word. The panel beside it names each shape.</desc>
              <g id="lpG"></g>
            </svg>
            <p class="prog" id="lpCap" aria-live="polite"></p>'''
student=lab(screen,'Ready','Read my lips','Each word is shown as three mouth shapes, one per sound, with no audio. Which word is it? Sometimes the honest answer is that you can’t tell.','Start')

o.update(body=tabs('Read my lips','Six silent words, drawn as mouth shapes. Some you can read from the lips. Some you can’t.',student,
 'About 10 minutes, plus an optional live demo',
 ['Run the student version with the class voting on each word.',
  'Live demo: silently mouth “bat”, “pat” and “mat” in random order and ask the class to call out which. Then mouth “fan” and “pan”.',
  'Discuss which sounds the lips show (where the mouth closes) and which they hide (whether the voice is on).',
  'Connect to your room: where do you stand when you speak? What happens when you talk while writing on the board?'],
 ['Why could you tell “fan” from “pan”, but not “bat” from “pat”?',
  'What does hearing add that the lips can’t?',
  'Who in this room depends most on seeing your face, or on captions?'],
 'Face the room when you speak, don’t talk while writing on the board, use a microphone when you have one, and turn on captions for video. Seeing the speaker helps everyone, and it helps most when the room is noisy.',
 'The McGurk effect is easiest to experience in a dubbed video, and many demonstration videos exist online. Watch with your eyes closed, then open.')+'''
  <div class="col lede">
    <p>In 1976, Harry McGurk and John MacDonald dubbed the sound of someone saying “ba” onto a film of a woman’s face saying “ga”. Adults watching it reported hearing “da”: neither the sound nor the lips, but a blend. With their eyes closed, they heard “ba” correctly.</p>
    <p>The McGurk effect shows that speech perception combines what we hear and what we see. The brain doesn’t keep them separate; it makes one best guess from both.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>“da”</strong><span>heard when a “ba” sound is dubbed onto lips saying “ga”</span></div>
      <div role="listitem"><strong>1954</strong><span>first experiments showing that seeing the face helps people understand speech in noise</span></div>
      <div role="listitem"><strong>Noise</strong><span>is where seeing the speaker adds the most</span></div>
      <div role="listitem"><strong>100+</strong><span>studies on same-language captions, in one 2015 review</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">In noise</span>The face fills in what the ear misses</h2>
    <p>William Sumby and Irwin Pollack tested how well people understood spoken words in noise, with and without seeing the speaker’s face. Seeing the face helped across noise levels, and because there is so much more to recover when the sound is poor, the face added the most in the noisiest conditions.</p>
    <h2 class="sec"><span class="n">What lips show</span>Where, not whether</h2>
    <p>The lips show where in the mouth a sound is made: “p”, “b” and “m” all close the lips; “f” and “v” put the teeth on the lip. They can’t show whether the voice is on, which is the difference between “p” and “b”. Hearing supplies that. That is why the activity above has words you can read and words you can’t.</p>
    <h2 class="sec"><span class="n">Captions</span>A large literature, with caveats</h2>
    <p>In a 2015 review, Morton Ann Gernsbacher listed more than 100 studies reporting that same-language captions improve comprehension of, attention to and memory for videos. Captions are especially helpful for people watching in a second language, people learning to read, and people who are deaf or hard of hearing. Critics note that much of this evidence comes from those groups, and that well-controlled studies with typical hearing students are fewer. For many students, though, captions are essential, and they are required for accessibility in most educational settings.</p>
  </div>

'''+pgrid_html(),
tips_h='Let students see you speak.',
tips='''      <li><b>Face the room</b><span>Don’t talk to the board or the screen.</span></li>
      <li><b>Captions on</b><span>For every video. Essential for some students, useful for many.</span></li>
      <li><b>Cut the noise</b><span>Use the microphone; the noisier the room, the more the face matters.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1038/264746a0">McGurk, H., &amp; MacDonald, J. (1976). Hearing lips and seeing voices. <i>Nature, 264</i>, 746–748.</a></li>
        <li><a href="https://doi.org/10.1121/1.1907309">Sumby, W. H., &amp; Pollack, I. (1954). Visual contribution to speech intelligibility in noise. <i>Journal of the Acoustical Society of America, 26</i>(2), 212–215.</a></li>
        <li><a href="https://doi.org/10.1177/2372732215602130">Gernsbacher, M. A. (2015). Video captions benefit everyone. <i>Policy Insights from the Behavioral and Brain Sciences, 2</i>(1), 195–202.</a></li>''',
foot='The mouth shapes are simplified drawings for this page, not recordings of a speaker. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'In the McGurk effect, a “ba” sound on lips saying “ga” is usually heard as…',o:['“da”','“ba”','“ga”'],a:0,f:'A blend of sound and sight.'},
 {q:'Seeing the speaker’s face helps understanding most when…',o:['The room is noisy','The room is silent','The speaker is far away'],a:0,f:'Sumby and Pollack, 1954.'},
 {q:'Why can’t you tell “bat” from “pat” by lips alone?',o:['Both close the lips; the difference is the voice','They’re spelled differently','You can, easily'],a:0,f:'Lips show where, not whether the voice is on.'}]''',
js=PANEL_JS+r'''
/* ---------- lip reading ---------- */
const NV='#13294B',LIP='#B5473A',IN='#3B1C1C',TEETH='#FFFFFF';
const SH={
 closed:{n:'lips closed',d:`<path d="M10 45 Q60 30 110 45 Q60 60 10 45Z" fill="${LIP}"/><line x1="12" y1="45" x2="108" y2="45" stroke="${IN}" stroke-width="3"/>`},
 open:{n:'mouth open',d:`<path d="M10 40 Q60 0 110 40 Q60 95 10 40Z" fill="${LIP}"/><path d="M22 40 Q60 14 98 40 Q60 80 22 40Z" fill="${IN}"/>`},
 teethlip:{n:'top teeth on lower lip',d:`<path d="M10 38 Q60 12 110 38 Q60 70 10 38Z" fill="${LIP}"/><path d="M24 36 Q60 26 96 36 L96 44 Q60 40 24 44Z" fill="${TEETH}"/>`},
 round:{n:'lips rounded',d:`<ellipse cx="60" cy="42" rx="26" ry="24" fill="${LIP}"/><ellipse cx="60" cy="42" rx="11" ry="10" fill="${IN}"/>`},
 wide:{n:'lips spread wide',d:`<path d="M2 42 Q60 20 118 42 Q60 66 2 42Z" fill="${LIP}"/><path d="M14 42 Q60 30 106 42 Q60 54 14 42Z" fill="${IN}"/><path d="M20 39 Q60 30 100 39 L100 42 L20 42Z" fill="${TEETH}"/>`},
 teeth:{n:'teeth together, lips apart',d:`<path d="M10 42 Q60 18 110 42 Q60 68 10 42Z" fill="${LIP}"/><path d="M22 42 Q60 28 98 42 Q60 56 22 42Z" fill="${IN}"/><rect x="26" y="36" width="68" height="12" fill="${TEETH}"/>`}};
const W=[
 {s:['teethlip','open','teeth'],o:['fan','pan','man'],a:0,f:'The teeth on the lower lip give away the “f”. “p” and “m” would close the lips instead.'},
 {s:['closed','open','teeth'],o:['bat','pat','mat'],a:3,f:'“b”, “p” and “m” all close the lips. The difference, whether the voice is on and whether air goes through the nose, can’t be seen. Only the sound tells them apart.'},
 {s:['round','wide','teeth'],o:['wheat','feet','beat'],a:0,f:'Rounded lips at the start mean “w”. “f” would show teeth on the lip, and “b” closed lips.'},
 {s:['closed','wide','teeth'],o:['beat','peat','meet'],a:3,f:'All three start with closed lips. Seeing tells you it is one of these; hearing must do the rest.'},
 {s:['teethlip','wide','teeth'],o:['feet','beet','heat'],a:0,f:'Teeth on the lip: “f” (or “v”). “b” closes the lips; “h” shows nothing special.'},
 {s:['teeth','open','teeth'],o:['tan','Dan','nan'],a:3,f:'“t”, “d” and “n” are made behind the teeth with the tongue, so they look the same from outside.'}];
startRun(async()=>{let right=0;const order=shuf([...W]);
 for(let i=0;i<order.length;i++){const w=order[i];
  $('lpG').innerHTML=w.s.map((k,j)=>`<g transform="translate(${30+j*165},50)"><rect x="-10" y="-30" width="140" height="130" rx="14" fill="#E9CBB0"/>${SH[k].d}<text x="60" y="92" text-anchor="middle" font-family="Source Sans 3,sans-serif" font-size="18" font-weight="700" fill="${NV}">${j+1}</text></g>`).join('');
  $('lpCap').textContent=w.s.map((k,j)=>`${j+1}: ${SH[k].n}`).join(' · ');
  say(`Word ${i+1} of ${order.length}`,'Which word is it?','Each picture is one sound, left to right.');
  const opts=[...w.o,'Can’t tell from the lips'];const a=await ask(opts,'Which word is it?');if(!RUN)return;mark(w.a,a);if(a===w.a)right++;
  say(null,w.a===3?'It could be any of them':`It’s “${w.o[w.a]}”`,(a===w.a?'<b class="ok">Right.</b> ':'<b class="no">Not quite.</b> ')+w.f);
  if(i<order.length-1){await nextBtn('Next word');if(!RUN)return;hideCh()}}
 say('What happened',`${right} of ${W.length} right`,'The lips show where a sound is made, but not whether the voice is on. Hearing and seeing each carry part of the message, and the brain combines them. In a noisy room, or with a hard-to-hear speaker, the face carries more of the load.')});
'''+grid('''[
 ['A “ba” sound dubbed onto a face saying “ga” was usually heard as…',['“da”','“ba”','“ga”'],0,'McGurk and MacDonald, 1976.'],
 ['With their eyes closed, the same listeners heard…',['“ba”, correctly','“da”','Nothing clear'],0,'So the lips changed what they heard.'],
 ['In Sumby and Pollack’s experiments, seeing the speaker helped most when…',['The noise was loudest','There was no noise','The words were familiar'],0,'There was most to recover.'],
 ['How many studies on captions did Gernsbacher’s 2015 review list?',['More than 100','About 10','About 1,000'],0,'Reporting benefits for comprehension, attention and memory.'],
 ['Critics of “captions benefit everyone” point out that much of the evidence comes from…',['Second-language learners, deaf viewers and self-report','Only children','Brain scans'],0,'Studies with typical-hearing college students are fewer.']]''','The pattern: we hear with our eyes too, and the face matters most when the sound is poor.'))
write(o)

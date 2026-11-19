import sys;sys.path.insert(0,'gen')
from pkit import *
from memjs import grid
o=pbase(1,'Perception Is a Best Guess','Perception is','a best guess',
'Your eyes send the brain patchy, ambiguous signals. What you see is the brain’s best interpretation of them, built from context and past experience. Usually it’s right. It’s also why a student and an expert can look at the same diagram and see different things.',
'<span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['v1','pfc'],{'v1':([960,770],'right'),'pfc':([40,-60],'left')},'Drawing of the side of the brain with the visual cortex, at the back, and the prefrontal cortex, at the front, glowing orange and labelled.')

screen='''            <svg id="cbSvg" viewBox="0 0 520 380" width="100%" style="max-width:520px;display:block" role="img" aria-labelledby="cbDesc">
              <desc id="cbDesc">A checkerboard seen at an angle, with an orange cylinder standing on it. The cylinder casts a soft shadow over part of the board. Square A is a dark square in full light. Square B is a light square inside the shadow. Both are exactly the same grey, but B looks much lighter.</desc>
              <defs>
                <radialGradient id="cbSh" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#000" stop-opacity=".47"/><stop offset=".6" stop-color="#000" stop-opacity=".47"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
                <linearGradient id="cbCyl" x1="0" x2="1"><stop offset="0" stop-color="#B8430A"/><stop offset=".45" stop-color="#FF7A2E"/><stop offset="1" stop-color="#9C3606"/></linearGradient>
                <mask id="cbMask"><rect width="520" height="380" fill="#fff"/><g id="cbHoles" fill="#000"></g></mask>
              </defs>
              <rect width="520" height="380" fill="#9AA6B8"/>
              <g id="cbBoard"></g>
              <ellipse id="cbShadow" fill="url(#cbSh)"/>
              <g id="cbCylinder"></g>
              <g id="cbLabels" font-family="Source Sans 3, sans-serif" font-weight="800" font-size="26" text-anchor="middle"></g>
              <g id="cbBars" display="none"></g>
              <rect id="cbCover" width="520" height="380" fill="#9AA6B8" mask="url(#cbMask)" display="none"/>
            </svg>
            <p class="prog" id="cbNote" aria-live="polite"></p>'''

student=lab(screen,'Ready','Which square is lighter?','Look at the squares marked A and B. You’ll answer three quick questions.','Start',
 '<button class="nbtn ghost" id="cbHide" type="button" hidden aria-pressed="false">Hide the scene</button><button class="nbtn ghost" id="cbBar" type="button" hidden aria-pressed="false">Show the bars</button>')

o.update(css='',
body=tabs('Which square is lighter?','Two squares on a checkerboard, one in shadow. Decide which is lighter, then test your answer.',student,
 'About 10 minutes',
 ['Project the student version full screen. Ask everyone to decide privately which square, A or B, is lighter. Then take a show of hands.',
  'Press “Cover the scene” and vote again. With the board and shadow covered, the two squares look the same.',
  'Show the bars that join A and B. Ask: now that you know, does B still look lighter in the full picture?',
  'In pairs, students explain what their brain assumed about the light and the shadow.',
  'Bridge to your subject: where might a beginner “see” something different from what you see?'],
 ['Why might a visual system that gets this “wrong” still be a good design?',
  'What did your brain assume about the shadow?',
  'Where in this course might a beginner see something different from what an expert sees?'],
 'Before you show a diagram, graph, specimen or text, say what to look at and what to ignore. Your eye already knows what matters. Your students’ eyes are still guessing.',
 'Projectors change contrast. Check the effect on your room’s projector beforehand; if it washes out, have students use their own screens.')+'''
  <div class="col lede">
    <p>More than 150 years ago, Hermann von Helmholtz described what we see as “unconscious inferences”: conclusions the brain draws from sensory data and past knowledge. The psychologist Richard Gregory later compared perceptions to the hypotheses of science: predictions about what is out there.</p>
    <p>The checker-shadow picture, published by Edward Adelson at MIT in 1995, shows this at work. Squares A and B are the same grey. Your brain takes the shadow into account and reports what the surfaces are probably like, not how much light reaches your eye.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>Same grey</strong><span>squares A and B, in Adelson’s 1995 picture and in the version above</span></div>
      <div role="listitem"><strong>1860s</strong><span>Helmholtz describes perception as unconscious inference</span></div>
      <div role="listitem"><strong>Hollow</strong><span>a hollow mask still looks like a face that bulges out</span></div>
      <div role="listitem"><strong>Upside down</strong><span>is when the hollow-face illusion is weakest</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Why guess?</span>The signal is ambiguous</h2>
    <p>The same pattern on the retina could come from many different scenes: a dark square in bright light, or a light square in shadow. The brain can’t measure which. It settles the question with context and with what usually happens in the world.</p>
    <h2 class="sec"><span class="n">Knowledge wins</span>The hollow face</h2>
    <p>Look at the inside of a hollow mask and you will usually see a normal face bulging toward you. Gregory called this evidence for the power of top-down knowledge in vision: we have seen so many faces that bulge out that this expectation overrides shading and even the depth cues from two eyes. The illusion is strongest right side up and weakest upside down, where our experience of faces helps least.</p>
    <h2 class="sec"><span class="n">A caution</span>Illusions are not failures</h2>
    <p>The same machinery that makes square B look lighter is what lets you recognise a white page in candlelight and in sunshine. Illusions are cases where a usually good guess goes wrong. They let us see the guessing.</p>
    <h2 class="sec"><span class="n">For learning</span>Experts and beginners guess differently</h2>
    <p>If perception depends on what you already know, then a beginner and an expert don’t see the same diagram. The expert’s brain fills in structure the beginner can’t yet see. Later topics in this series look at how that changes with practice, and at how to point students to what matters.</p>
  </div>

'''+pgrid_html(),
tips_h='Say what to look at. The beginner’s brain is still guessing.',
tips='''      <li><b>Name what matters</b><span>Before showing an image, say what to look for and what to ignore.</span></li>
      <li><b>Show the context</b><span>The surrounding information is what makes the right reading obvious.</span></li>
      <li><b>Expect other readings</b><span>Ask students what they see before you tell them.</span></li>''',
sources='''        <li><a href="https://persci.mit.edu/gallery/checkershadow">Adelson, E. H. (1995). Checkershadow illusion. MIT Perceptual Science Group.</a></li>
        <li><a href="https://doi.org/10.1098/rstb.1997.0095">Gregory, R. L. (1997). Knowledge in perception and illusion. <i>Philosophical Transactions of the Royal Society B, 352</i>, 1121–1127.</a></li>
        <li>Gregory, R. L. (1970). <i>The intelligent eye</i>. Weidenfeld and Nicolson.</li>''',
foot='The checkerboard above is our own drawing in the style of Adelson’s illusion; squares A and B are set to exactly the same grey. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'In the checker-shadow picture, squares A and B are…',o:['The same grey','Slightly different','Very different'],a:0,f:'The brain discounts the shadow.'},
 {q:'Helmholtz described perceptions as…',o:['Unconscious inferences','Exact copies of the world','Memories'],a:0,f:'Conclusions from data plus knowledge.'},
 {q:'A hollow mask usually looks…',o:['Like a normal face, bulging out','Hollow','Flat'],a:0,f:'Knowledge of faces overrides depth cues.'}]''',
js=PANEL_JS+r'''
/* ---------- checker shadow ---------- */
const NS='http://www.w3.org/2000/svg';const LIGHT='rgb(217,217,217)',DARK='rgb(115,115,115)';
const P={tl:[120,70],tr:[400,70],bl:[30,330],br:[490,330]},N=5;
const lerp2=(a,b,t)=>[a[0]+(b[0]-a[0])*t,a[1]+(b[1]-a[1])*t];
function pt(u,v){const vv=v*v*0.35+v*0.65;const L=lerp2(P.tl,P.bl,vv),R=lerp2(P.tr,P.br,vv);return lerp2(L,R,u)}
function cell(i,j){return[pt(j/N,i/N),pt((j+1)/N,i/N),pt((j+1)/N,(i+1)/N),pt(j/N,(i+1)/N)]}
const ctr=q=>[(q[0][0]+q[1][0]+q[2][0]+q[3][0])/4,(q[0][1]+q[1][1]+q[2][1]+q[3][1])/4];
const A=[1,2],B=[3,1];
(function draw(){const g=$('cbBoard');let s='';for(let i=0;i<N;i++)for(let j=0;j<N;j++){const q=cell(i,j);s+=`<polygon points="${q.map(p=>p.join(',')).join(' ')}" fill="${(i+j)%2?DARK:LIGHT}"/>`}g.innerHTML=s;
 const cb=ctr(cell(...B));const sh=$('cbShadow');sh.setAttribute('cx',cb[0]+28);sh.setAttribute('cy',cb[1]-4);sh.setAttribute('rx',150);sh.setAttribute('ry',86);
 const cx=cb[0]+150,cy=cb[1]+40;$('cbCylinder').innerHTML=`<rect x="${cx-34}" y="${cy-150}" width="68" height="150" fill="url(#cbCyl)"/><ellipse cx="${cx}" cy="${cy}" rx="34" ry="11" fill="#9C3606"/><ellipse cx="${cx}" cy="${cy-150}" rx="34" ry="11" fill="#FF9A5C"/>`;
 const ca=ctr(cell(...A));$('cbLabels').innerHTML=`<text x="${ca[0]}" y="${ca[1]+9}" fill="#fff">A</text><text x="${cb[0]}" y="${cb[1]+9}" fill="#13294B">B</text>`;
 const qa=cell(...A),qb=cell(...B);$('cbHoles').innerHTML=[qa,qb].map(q=>`<polygon points="${q.map(p=>p.join(',')).join(' ')}"/>`).join('');
 const w=16,x1=ca[0]-w/2,y1=ca[1]+16,y2=cb[1]+w/2,xL=cb[0]+16;$('cbBars').innerHTML=`<rect x="${x1}" y="${y1}" width="${w}" height="${y2-y1}" fill="${DARK}"/><rect x="${xL}" y="${cb[1]-w/2}" width="${x1+w-xL}" height="${w}" fill="${DARK}"/>`;
 // labels stay readable when the scene is hidden
})();
function setHide(on){$('cbCover').setAttribute('display',on?'inline':'none');$('cbHide').setAttribute('aria-pressed',on);$('cbHide').textContent=on?'Show the scene':'Hide the scene';$('cbNote').textContent=on?'Everything except A and B is covered.':''}
function setBars(on){$('cbBars').setAttribute('display',on?'inline':'none');$('cbBar').setAttribute('aria-pressed',on);$('cbBar').textContent=on?'Hide the bars':'Show the bars'}
$('cbHide').addEventListener('click',()=>setHide($('cbCover').getAttribute('display')==='none'));
$('cbBar').addEventListener('click',()=>setBars($('cbBars').getAttribute('display')==='none'));
startRun(async()=>{setHide(false);setBars(false);$('cbHide').hidden=true;$('cbBar').hidden=true;
 say('Question 1 of 3','Which square looks lighter?','Trust your eyes. Don’t reason it out.');
 const a1=await ask(['A','B','They look the same'],'Which square looks lighter?');if(!RUN)return;
 const first=a1===1?'You said B, like most people.':a1===0?'You said A. Most people see B as lighter.':'You said they look the same. Most people see B as clearly lighter.';
 say(null,null,first+' Next, the board and the shadow will be covered.');hideCh();
 await nextBtn('Cover the scene');setHide(true);
 say('Question 2 of 3','Now which looks lighter?','Only squares A and B are showing.');
 const a2=await ask(['A','B','They look the same'],'Now which looks lighter?');if(!RUN)return;mark(2,a2);
 say(null,null,(a2===2?'<b class="ok">Right.</b> ':'<b class="no">Look again.</b> ')+'They are exactly the same grey. On screen, both are set to the same colour value.');
 await nextBtn('Show the whole picture');hideCh();setHide(false);setBars(true);
 say('Question 3 of 3','Now that you know, does B still look lighter?','The grey bars join A and B. They are the same colour as both squares.');
 const a3=await ask(['Yes, still lighter','No, they look the same now'],'Does B still look lighter?');if(!RUN)return;
 say('What happened',a3===0?'Knowing doesn’t switch it off':'Most people still see a difference',
  'Your brain worked out that B sits in shadow, so it reported B as a light surface in dim light. That inference runs automatically: knowing the answer rarely changes what you see. A student looking at a new diagram is making inferences like this too, using whatever they already know.');
 $('cbHide').hidden=false;$('cbBar').hidden=false});
'''+grid('''[
 ['In Adelson’s checker-shadow picture, squares A and B are…',['The same grey','Different by a little','Different by a lot'],0,'Exactly the same. The shadow changes how the brain interprets them.'],
 ['A hollow mask, seen from the front, usually looks…',['Like a normal face, bulging out','Hollow','Flat'],0,'Gregory took this as evidence for the power of top-down knowledge.'],
 ['The hollow-face illusion is weakest when the face is…',['Upside down','Lit from below','Right side up'],0,'Our experience with faces helps least upside down.'],
 ['Lighting a hollow mask from below makes the illusion…',['Stronger','Weaker','Disappear'],0,'It reverses the shading, so it looks like a normal face lit from above.'],
 ['Who first described perceptions as unconscious inferences?',['Hermann von Helmholtz','Max Wertheimer','Richard Gregory'],0,'In the 19th century. Gregory built on the idea.']]''','The pattern: what you see is an inference, and what you already know shapes it.'))
write(o)

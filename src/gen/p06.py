import sys;sys.path.insert(0,'gen')
from pkit import *
from memjs import grid
o=pbase(6,'Gestalt: How the Brain Groups a Page','Gestalt:','how the brain groups a page',
'Before you read a single word, your brain has already decided what goes with what: things that are close, alike, boxed together or connected. Every slide and handout is grouped this way, whether you planned it or not.',
'<span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['occ','par'],{'occ':([960,770],'right'),'par':([560,-70],'left')},'Drawing of the side of the brain with the occipital lobe, at the back, and the parietal lobe, at the top, glowing orange and labelled.')

screen='''            <svg id="gsSvg" viewBox="0 0 520 280" width="100%" style="max-width:540px;display:block;background:#fff;border-radius:6px" role="img" aria-labelledby="gsD">
              <desc id="gsD">A small arrangement of shapes. The text beside it describes each arrangement.</desc>
              <g id="gsG"></g>
            </svg>
            <p class="prog" id="gsCap" aria-live="polite"></p>'''
student=lab(screen,'Ready','What goes together?','Seven quick layouts. For each, answer with your first impression: what does your eye group together?','Start')

o.update(body=tabs('What goes together?','Dots, boxes and lines. For each layout, say what you see as a group, before you think about it.',student,
 'About 10 minutes',
 ['Project the student version. For each layout, count “one, two, three” and have everyone call out what they see as grouped.',
  'After each one, name the principle shown: proximity, similarity, common region, connection or closure.',
  'At the last layout, ask which version of the labelled diagram is easier to read, and why.',
  'Then show one of your own slides and ask: what will students group together here? Is that what you meant?'],
 ['Which layouts did everyone agree on immediately?',
  'Where did spacing and colour pull in different directions?',
  'On your last handout, what would a reader group together?'],
 'Use grouping deliberately: put labels next to what they label, leave space between unrelated items, and use boxes or shading to show what belongs together.',
 'There is no single right answer for every layout; the “most people” answers come from long-standing demonstrations, and individuals vary.')+'''
  <div class="col lede">
    <p>In 1912, Max Wertheimer published a paper on apparent motion that is widely seen as the start of Gestalt psychology. He and his colleagues went on to describe how the visual system organises a scene into groups and figures before we think about it: things that are close together, alike, enclosed together, or connected tend to be seen as belonging together.</p>
    <p>A century later, a major review by Johan Wagemans and colleagues concluded that the questions the Gestalt psychologists raised, about how structure emerges in perception, still drive research today.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>1912</strong><span>Wertheimer’s paper that launched Gestalt psychology</span></div>
      <div role="listitem"><strong>5 cues</strong><span>shown above: proximity, similarity, common region, connection and closure</span></div>
      <div role="listitem"><strong>d = 0.85</strong><span>average benefit of integrating related words and pictures, in Ginns’s 2006 meta-analysis</span></div>
      <div role="listitem"><strong>Near</strong><span>labels next to the parts beat labels in a separate legend</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Automatic</span>Grouping happens first</h2>
    <p>You don’t choose to see the dots in the first layout as columns. Grouping is part of how the visual system builds a scene, and it shapes what we notice and compare. When two cues conflict, such as spacing and colour, the stronger one tends to win.</p>
    <h2 class="sec"><span class="n">On the page</span>Layout makes a claim</h2>
    <p>Whatever is close together on a slide will be read as related. A caption that sits nearer to the wrong picture, or a label floating between two parts, sends a message you didn’t mean to send.</p>
    <h2 class="sec"><span class="n">The evidence</span>Keep related things together</h2>
    <p>Research on multimedia learning tests this directly. When a diagram’s labels are placed next to the parts, rather than in a separate key, learners don’t have to search back and forth. Paul Ginns’s 2006 meta-analysis of this split-attention effect found a large average benefit for integrated designs (d = 0.85), and a 2018 meta-analysis by Noah Schroeder and Ada Cenkci also supported placing related words and pictures close together.</p>
  </div>

'''+pgrid_html(),
tips_h='Layout says what goes with what. Make it say what you mean.',
tips='''      <li><b>Labels on the parts</b><span>Not in a legend the eye must hunt for.</span></li>
      <li><b>Space separates</b><span>Leave a clear gap between things that don’t belong together.</span></li>
      <li><b>Box what belongs</b><span>A shaded panel groups more strongly than spacing.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1037/a0029333">Wagemans, J., Elder, J. H., Kubovy, M., Palmer, S. E., Peterson, M. A., Singh, M., &amp; von der Heydt, R. (2012). A century of Gestalt psychology in visual perception: I. Perceptual grouping and figure–ground organization. <i>Psychological Bulletin, 138</i>(6), 1172–1217.</a></li>
        <li><a href="https://doi.org/10.1016/j.learninstruc.2006.10.001">Ginns, P. (2006). Integrating information: A meta-analysis of the spatial contiguity and temporal contiguity effects. <i>Learning and Instruction, 16</i>(6), 511–525.</a></li>
        <li><a href="https://doi.org/10.1007/s10648-018-9435-9">Schroeder, N. L., &amp; Cenkci, A. T. (2018). Spatial contiguity and spatial split-attention effects in multimedia learning environments: A meta-analysis. <i>Educational Psychology Review, 30</i>(3), 679–701.</a></li>''',
foot='The layouts are classic grouping demonstrations, drawn for this page. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'Dots close together are seen as a group. This is…',o:['Proximity','Similarity','Closure'],a:0,f:'Spacing creates groups.'},
 {q:'Where should a diagram’s labels go?',o:['Next to the parts they name','In a key below','On the next slide'],a:0,f:'The spatial contiguity principle.'},
 {q:'Gestalt psychology began with a paper by…',o:['Max Wertheimer, 1912','Hermann von Helmholtz, 1866','Richard Mayer, 2001'],a:0,f:'On apparent motion.'}]''',
js=PANEL_JS+r'''
/* ---------- grouping ---------- */
const N='#13294B',O='#FF5F05';
const dot=(x,y,c,r)=>`<circle cx="${x}" cy="${y}" r="${r||13}" fill="${c||N}"/>`;
function grid(fx,fy,nx,ny,col){let s='';for(let i=0;i<nx;i++)for(let j=0;j<ny;j++)s+=dot(fx(i),fy(j),col?col(i,j):N);return s}
const L=[
 {svg:grid(i=>90+i*110,j=>50+j*36,4,6),q:'What do you see?',o:['Four columns','Six rows','One block of dots'],a:0,p:'Proximity',f:'The dots are closer vertically than horizontally, so most people see columns. Spacing alone creates groups.'},
 {svg:grid(i=>80+i*60,j=>50+j*40,7,5,(i,j)=>j%2?O:N),q:'What do you see?',o:['Rows','Columns','One block of dots'],a:0,p:'Similarity',f:'The spacing is even, but colour alternates by row, so most people see rows. Alike things group together.'},
 {svg:`<rect x="110" y="95" width="140" height="90" rx="14" fill="#FFE3D1"/><rect x="290" y="95" width="140" height="90" rx="14" fill="#FFE3D1"/>`+[60,130,230,300,400,470].map(x=>dot(x,140)).join(''),q:'Which dots go together?',o:['The pairs inside the shaded boxes','The pairs that are closest together','None: it is just a row'],a:0,p:'Common region',f:'The closest dots are actually split by the box edges. In demonstrations like this, most people group by the boxes: a shared region is a strong cue, which is why shaded panels work on slides.'},
 {svg:`<g stroke="${N}" stroke-width="6"><line x1="60" y1="140" x2="185" y2="140"/><line x1="335" y1="140" x2="460" y2="140"/></g>`+[60,135,185,335,385,460].map(x=>dot(x,140)).join('')+dot(260,140),q:'What goes together?',o:['The dots joined by lines','The dots closest together','Every dot is separate'],a:0,p:'Connection',f:'A connecting line groups things even across a gap. Arrows and lines on a diagram are strong claims about what goes together.'},
 {svg:(()=>{const pts=[[260,62],[165,226],[355,226]],cx=260,cy=171,r=36;return pts.map(([x,y])=>{const c=Math.atan2(cy-y,cx-x),h=Math.PI/6,p=t=>[x+r*Math.cos(t),y+r*Math.sin(t)];const p1=p(c+h),p2=p(c-h);return `<path d="M${x} ${y} L${p1[0].toFixed(1)} ${p1[1].toFixed(1)} A${r} ${r} 0 1 1 ${p2[0].toFixed(1)} ${p2[1].toFixed(1)} Z" fill="${N}"/>`}).join('')})(),q:'What do you see in the middle?',o:['A white triangle','Nothing: three cut circles','A white circle'],a:0,p:'Closure',f:'No triangle is drawn: the brain completes the edges from the gaps. We fill in shapes that aren’t fully there, the same way we fill gaps in the blind spot.'},
 {svg:grid(i=>70+i*54,j=>60+j*80,8,3,(i,j)=>i<4?N:O).replace(/cx="(\d+)"/g,(m,x)=>`cx="${+x+(+x>250?40:0)}"`),q:'What do you see?',o:['Two groups: left and right','Eight columns','Three rows'],a:0,p:'Proximity and similarity together',f:'Here spacing and colour agree, so the two groups are unmistakable. When cues agree, grouping is fast and certain. Design slides so they agree.'},
 {svg:`<text x="110" y="34" font-family="Source Sans 3,sans-serif" font-size="18" font-weight="800" text-anchor="middle" fill="${N}">A</text><text x="330" y="34" font-family="Source Sans 3,sans-serif" font-size="18" font-weight="800" text-anchor="middle" fill="${N}">B</text>`+
  `<g transform="translate(50,60)"><circle cx="60" cy="70" r="46" fill="#FFE3D1" stroke="${N}" stroke-width="3"/><circle cx="60" cy="70" r="14" fill="${O}"/><text x="68" y="40" font-family="Source Sans 3,sans-serif" font-size="18" fill="${N}">1</text><text x="78" y="76" font-family="Source Sans 3,sans-serif" font-size="18" fill="${N}">2</text><text x="-10" y="170" font-family="Source Sans 3,sans-serif" font-size="18" fill="${N}">1 Membrane</text><text x="-10" y="194" font-family="Source Sans 3,sans-serif" font-size="18" fill="${N}">2 Nucleus</text></g>`+
  `<g transform="translate(270,60)"><circle cx="60" cy="70" r="46" fill="#FFE3D1" stroke="${N}" stroke-width="3"/><circle cx="60" cy="70" r="14" fill="${O}"/><line x1="102" y1="52" x2="124" y2="36" stroke="${N}" stroke-width="2"/><text x="128" y="40" font-family="Source Sans 3,sans-serif" font-size="18" fill="${N}">Membrane</text><line x1="74" y1="74" x2="124" y2="112" stroke="${N}" stroke-width="2"/><text x="128" y="118" font-family="Source Sans 3,sans-serif" font-size="18" fill="${N}">Nucleus</text></g>`,
  q:'Which diagram is easier to read?',o:['B: labels on the parts','A: numbered key below','No difference'],a:0,p:'Spatial contiguity',f:'In B the eye doesn’t have to jump between number and key. Meta-analyses of the split-attention effect find that placing words next to the parts they describe helps learning.'}];
startRun(async()=>{let right=0;const caps=[];
 for(let i=0;i<L.length;i++){const it=L[i];$('gsG').innerHTML=it.svg;$('gsCap').textContent='';
  say(`Layout ${i+1} of ${L.length}`,it.q,'Answer with your first impression.');
  const a=await ask(it.o,it.q);if(!RUN)return;mark(it.a,a);if(a===it.a)right++;
  $('gsCap').textContent=it.p;
  say(null,it.p,(a===it.a?'<b class="ok">Most people agree.</b> ':'<b class="no">Most people see it differently.</b> ')+it.f);
  if(i<L.length-1){await nextBtn('Next layout');if(!RUN)return;hideCh()}}
 say('What happened',`${right} of ${L.length} matched most people`,'Grouping happens before you think about it, and it happens to your students when they look at your slides. Use it on purpose: closeness, shared colour, a shaded box or a line all say “these belong together”.')});
'''+grid('''[
 ['Gestalt psychology is usually dated from a 1912 paper on…',['Apparent motion','Colour vision','Memory'],0,'By Max Wertheimer.'],
 ['In Ginns’s 2006 meta-analysis, how big was the average benefit of integrating related words and pictures?',['Large (d = 0.85)','Tiny (d = 0.05)','Negative'],0,'The split-attention or spatial contiguity effect.'],
 ['Did the 2018 meta-analysis by Schroeder and Cenkci support placing related words and pictures close together?',['Yes','No','It found harm'],0,'Integrated designs helped learning.'],
 ['A century after Gestalt began, Wagemans and colleagues concluded its questions were…',['Still driving research','Settled long ago','Abandoned'],0,'Grouping and figure–ground remain active topics.'],
 ['When spacing and colour suggest different groups, what tends to happen?',['The stronger cue wins','Both are ignored','Colour always wins'],0,'So make cues agree when you design a page.']]''','The pattern: the brain groups before it reads, so layout teaches too.'))
write(o)

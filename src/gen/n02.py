import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('n','Neuromyths',2,'Learning Styles: What the Evidence Shows','Learning styles','Students are different. The strategies that help them learn are mostly the same.','Learning styles',
'Visual learner. Auditory learner. Kinesthetic learner. It may be the most widely believed idea in education. Is it true?',
'<span><a href="#mT">See the crossover test</a></span><span><a href="#bT">Content or style?</a></span>')
o['hero_aria'],o['hero_js']=hero(['occ','tem'],{'occ':([900,-60],'right'),'tem':([600,770],'left')},'Drawing of the side of the brain with the occipital lobe, at the back, where vision starts, and the temporal lobe, at the side, where hearing is processed, glowing orange and labelled.')
o.update(css=RECALL_CSS+CLS_CSS+'''
.mx{width:100%;max-width:560px}
.mleg{font:700 16px var(--body);margin:8px 0 0;text-align:center;display:flex;gap:16px;justify-content:center;flex-wrap:wrap}
.mnote{color:#C9D3E3;font-size:14px;margin:6px 0 0;text-align:center}
.mx svg{width:100%;height:auto;display:block}
.mtog{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin-top:10px}
.mtog button[aria-pressed="true"]{background:#FCB316;color:#13294B;border-color:#FCB316}''',
body='''  <div class="col lede">
    <p>The claim is specific. Students learn better when teaching matches their preferred style. Researchers call this the meshing hypothesis.</p>
    <p>To test it, you need a particular experiment. Sort students by style. Teach each group in both formats. Then give everyone the same test.</p>
  </div>

  <section class="night" aria-labelledby="mT">
    <div class="col">
      <h2 class="sec" id="mT"><span class="n">See it</span>The crossover test</h2>
      <p>Meshing predicts a crossover: visual learners do best with visual teaching, and auditory learners with auditory teaching. Switch between what meshing predicts and what the well-designed studies mostly found.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="mScreen">
          <div class="mx"><svg id="mSvg" viewBox="0 0 600 300" role="img" aria-labelledby="mDesc"><title id="mDesc"></title>
            <line x1="80" y1="250" x2="540" y2="250" stroke="#8FA3C2"/><line x1="80" y1="30" x2="80" y2="250" stroke="#8FA3C2"/>
            <text x="30" y="140" fill="#C9D3E3" font-size="22" transform="rotate(-90 30 140)" text-anchor="middle">Test score</text>
            <text x="160" y="282" fill="#E9EEF6" font-size="22" text-anchor="middle">Taught visually</text><text x="400" y="282" fill="#E9EEF6" font-size="22" text-anchor="middle">Taught by listening</text>
            <g id="mLines"></g>
          </svg><p class="mleg"><span style="color:#7DD3A8">● “Visual learners”</span> <span style="color:#FCB316">● “Auditory learners”</span></p><p class="mnote">Illustrative patterns, not data from one study.</p></div>
          <div class="mtog" role="group" aria-label="Which pattern"><button class="nbtn ghost" type="button" id="mP" aria-pressed="true">What meshing predicts</button><button class="nbtn ghost" type="button" id="mF" aria-pressed="false">What studies mostly found</button></div>
        </div>
        <div>
          <p class="phase">The pattern</p>
          <p class="mtitle" id="mTitle"></p>
          <p class="mtext" id="mText" aria-live="polite"></p>
        </div>
      </div>
    </div>
  </section>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>2008</strong><span>review by Harold Pashler and colleagues</span></div>
      <div role="listitem"><strong>Very few</strong><span>studies used the crossover design</span></div>
      <div role="listitem"><strong>Virtually no</strong><span>evidence for meshing in those that did</span></div>
      <div role="listitem"><strong>76%</strong><span>of UK schoolteachers said they used learning styles, in a 2014 survey</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The evidence</span>A specific test, rarely passed</h2>
    <p>In 2008, Harold Pashler and colleagues reviewed the research. Very few studies used the crossover design. Those that did found virtually no evidence for meshing, and several contradicted it. Later reviews have reached the same conclusion.</p>
    <p>Yet the idea is everywhere. In a 2014 survey, 76% of UK schoolteachers said they used learning styles. And there is a thriving industry of style tests, guidebooks and workshops.</p>
    <h2 class="sec"><span class="n">The grain of truth</span>Preferences are real</h2>
    <p>People really do have preferences, and differ in abilities. But the best format depends mostly on the content. A map is visual for everyone. A melody is auditory for everyone. And a format that feels easier is not always the one that teaches more, as Habits of the Learner showed.</p>
  </div>

'''+cls_html('bT','Content or style?','Eight teaching choices. For each, decide: is the format chosen because the content needs it, or to match a student’s supposed style? You’ll get feedback after each one.',[('C','Fits the content',''),('S','Matches a style','')],'Fits the content or matches a style?','Content or style?','The question is always: would this format help nearly everyone with this content?')+GRID_HTML+box('Choose the format that fits the content, and combine words with pictures where it helps. Use methods that work for nearly everyone, like retrieval practice and spacing. And drop style inventories from your course. Share this tip with students: pick study methods by what works, not by your style.'),
tips_h='Students are different. But the strategies that help them learn are mostly the same.',
tips='''      <li><b>Format fits the content</b><span>A map is visual for everyone.</span></li>
      <li><b>Methods that work for nearly all</b><span>Retrieval practice, spacing.</span></li>
      <li><b>Drop style inventories</b><span>They sort without helping.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1111/j.1539-6053.2009.01038.x">Pashler, H., McDaniel, M., Rohrer, D., &amp; Bjork, R. (2008). Learning styles: Concepts and evidence. <i>Psychological Science in the Public Interest, 9</i>(3), 105–119.</a></li>
        <li><a href="https://doi.org/10.3389/fpsyg.2017.00444">Newton, P. M., &amp; Miah, M. (2017). Evidence-based higher education: Is the learning styles ‘myth’ important? <i>Frontiers in Psychology, 8</i>, 444.</a> (Reports the 2014 survey of UK schoolteachers.)</li>''',
quiz='''[
 {q:'The meshing hypothesis predicts…',o:['A crossover: each style does best with matched teaching','Everyone does best with pictures','No differences at all'],a:0,f:'That’s the specific claim to test.'},
 {q:'Studies that used the crossover design found…',o:['Virtually no evidence for meshing','Strong support','A small but reliable effect'],a:0,f:'Pashler and colleagues, 2008.'},
 {q:'The best format depends mostly on…',o:['The content','The student’s style','The time of day'],a:0,f:'A map is visual for everyone.'}]''',
js=BASE+r'''
/* ---------- crossover ---------- */
const MX={P:{t:'What meshing predicts',x:'If meshing were true, the lines would cross: “visual learners” score highest with visual teaching, and “auditory learners” with teaching by listening. That crossover is the pattern a test must find.',
 a:'Line chart. Visual learners score high when taught visually and low when taught by listening. Auditory learners show the opposite. The lines cross.',v:[200,90],u:[90,200]},
 F:{t:'What studies mostly found',x:'In the few well-designed studies, the lines didn’t cross. Both groups did better with whichever format suited the material, or there was no difference. That’s no support for matching.',
 a:'Line chart. Both groups score about the same in each format, and both do a little better in the same format. The lines do not cross.',v:[185,165],u:[175,155]}};
function mDraw(k){const m=MX[k];const y=s=>250-s;const L=(p,c,lab,dy)=>`<line x1="160" y1="${y(p[0])}" x2="400" y2="${y(p[1])}" stroke="${c}" stroke-width="4"/><circle cx="160" cy="${y(p[0])}" r="7" fill="${c}"/><circle cx="400" cy="${y(p[1])}" r="7" fill="${c}"/>`;
 $('mLines').innerHTML=L(m.v,'#7DD3A8','“Visual learners”',k==='P'?20:-8)+L(m.u,'#FCB316','“Auditory learners”',k==='P'?-8:22);
 $('mDesc').textContent=m.a;$('mTitle').textContent=m.t;$('mText').textContent=m.x;$('mP').setAttribute('aria-pressed',k==='P');$('mF').setAttribute('aria-pressed',k==='F')}
$('mP').addEventListener('click',()=>mDraw('P'));$('mF').addEventListener('click',()=>mDraw('F'));mDraw('P');
'''+cls_js("{C:'Fits the content',S:'Matches a style'}",'''[
 ['Using a map to teach where rivers and cities are','C','Fits the content: geography is visual for everyone.'],
 ['Giving “auditory learners” a podcast instead of the diagram everyone else gets','S','Matches a style: and the diagram is what shows how the parts connect.'],
 ['Playing the melody when teaching a piece of music','C','Fits the content: music is auditory for everyone.'],
 ['Having students take a style inventory in week one, then sorting groups by result','S','Matches a style: sorting without evidence that matching helps.'],
 ['Pairing a spoken explanation with a labelled diagram of a cell','C','Fits the content: words with pictures help nearly everyone.'],
 ['Letting “kinesthetic learners” skip the reading and build a model instead','S','Matches a style: and they miss content the reading carries.'],
 ['Having students practise a lab technique with their hands','C','Fits the content: a physical skill is learned by doing, for everyone.'],
 ['Telling a student they struggle with text because they’re a “visual learner”','S','Matches a style: and the label can discourage practice with text.']]''','Fits the content or matches a style?',r'''
 if(right>=7){title='You can tell them apart';text=`${right} of 8 right. Choose formats for the content, not the student type.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Ask: would this format help nearly everyone with this content?`}
 else{title='Worth another look';text=`${right} of 8 right. A map, a melody or a lab skill fits its content. Sorting students by style and changing the format for each has little support.`}''')+grid('''[
 ['The specific claim is called the…',['Meshing hypothesis','Mozart effect','Spacing effect'],0,'Teaching matched to style improves learning.'],
 ['Testing it needs students taught in…',['Both formats, then the same test','One format each','No format'],0,'So you can look for a crossover.'],
 ['In 2008, Pashler and colleagues found that studies with that design were…',['Very few','Very many','Impossible'],0,'And they found virtually no support.'],
 ['In a 2014 survey, the share of UK schoolteachers who said they used learning styles was…',['76%','7%','26%'],0,'Reported by Newton and Miah.'],
 ['Do people have learning preferences?',['Yes, but matching them doesn’t improve learning','No','Yes, and matching them helps a lot'],0,'Preferences are real.'],
 ['A format that feels easier…',['Is not always the one that teaches more','Always teaches more','Never teaches anything'],0,'Fluency can mislead.']]''','The pattern: preferences are real, but matching teaching to them isn’t supported. Fit the format to the content.'))
open('n02/template.html','w').write(page(o))

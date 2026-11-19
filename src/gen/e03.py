import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('e','Assessment That Teaches',3,'Do Quizzes Cause Anxiety?','Do quizzes cause anxiety?','Practice makes tests familiar. Familiar is less frightening.','Do quizzes cause anxiety?',
'Many instructors avoid frequent quizzes for a kind reason. They worry that more tests mean more stress. What does the evidence say?',
'<span><a href="#qT">Find the sweet spot</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['amy','pfc'],{'pfc':([40,-60],'left'),'amy':([330,740],'left')},'Drawing of the side of the brain with the amygdala, deep inside, involved in fear and anxiety, and the prefrontal cortex, at the front, which helps regulate it, glowing orange and labelled.')
o.update(css=RECALL_CSS+'''
.sform{display:grid;gap:10px;width:100%;max-width:560px}
.sform fieldset{border:1px solid #3A4E72;border-radius:10px;padding:8px 12px 10px;margin:0}
.sform legend{font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#FCB316;padding:0 6px}
.sform label{display:flex;gap:10px;align-items:flex-start;padding:4px 0;color:#E9EEF6;font-size:16px;line-height:1.35;cursor:pointer}
.sform input{margin-top:3px;width:18px;height:18px;accent-color:#FCB316;flex:none}
#qRes{width:100%;max-width:560px}
.qnote{color:#C9D3E3;font-size:14px;margin:4px 0 0}''',
body='''  <div class="col lede">
    <p>In 2023, Chunliang Yang, David Shanks and colleagues pooled 24 studies with more than 3,000 students, in classrooms and labs, that measured test anxiety before and after a period of regular quizzing.</p>
    <p>On average, practice tests reduced test anxiety, by a medium amount.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>24</strong><span>studies, with 3,374 participants</span></div>
      <div role="listitem"><strong>Reduced</strong><span>test anxiety, by a medium amount on average</span></div>
      <div role="listitem"><strong>Larger</strong><span>when quizzes were easier and lower stakes</span></div>
      <div role="listitem"><strong>Young</strong><span>research, in the authors’ own words</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The details</span>Easier, lower stakes</h2>
    <p>There was little sign of publication bias, and the result held when the authors removed the one study that measured anxiety during the quizzes themselves. The benefit was larger when quizzes were easier and lower stakes. Retakes and ungraded quizzes are good examples.</p>
    <h2 class="sec"><span class="n">Why</span>Familiar, and known</h2>
    <p>One idea is familiarity: the exam format stops being a surprise. Another is that students simply know the material better, and know that they know it.</p>
    <h2 class="sec"><span class="n">A caution</span>Young research</h2>
    <p>The authors call this research young. Many studies were small, anxiety was measured with surveys, and a minority of very anxious students might respond differently.</p>
  </div>

  <section class="night" aria-labelledby="qT">
    <div class="col">
      <h2 class="sec" id="qT"><span class="n">Try it</span>Find the sweet spot</h2>
      <p>There is a trade-off. Harder quizzes help learning more, while easier, lower-stakes quizzes calm anxiety more. Design a quiz, and see where it lands.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="qScreen">
          <form class="sform" id="qF">
            <fieldset><legend>Difficulty</legend>
              <label><input type="radio" name="qd" value="0">Easy: most students get most right</label>
              <label><input type="radio" name="qd" value="1" checked>Moderate: some real effort needed</label>
              <label><input type="radio" name="qd" value="2">Hard: most students miss several</label></fieldset>
            <fieldset><legend>Stakes</legend>
              <label><input type="radio" name="qs" value="0" checked>Ungraded practice</label>
              <label><input type="radio" name="qs" value="1">A small share of the grade</label>
              <label><input type="radio" name="qs" value="2">A large share of the grade</label></fieldset>
            <fieldset><legend>Second chances</legend>
              <label><input type="radio" name="qr" value="1" checked>Retakes, or drop the lowest score</label>
              <label><input type="radio" name="qr" value="0">One attempt counts</label></fieldset>
          </form>
          <div id="qRes"></div>
          <p class="qnote">A rough guide based on the pattern in the research, not a measurement.</p>
        </div>
        <div>
          <p class="phase">Your quiz</p>
          <p class="mtitle" id="qTitle"></p>
          <p class="mtext" id="qText" aria-live="polite"></p>
        </div>
      </div>
    </div>
  </section>

'''+GRID_HTML+box('Start the term with easy, ungraded quizzes, and raise the challenge gradually. Allow retakes or drop the lowest scores. Tell students the purpose: practice, not judgment. Share this tip with students: frequent small quizzes make big exams less scary.'),
tips_h='Practice makes tests familiar. Familiar is less frightening.',
tips='''      <li><b>Start easy and ungraded</b><span>Raise the challenge gradually.</span></li>
      <li><b>Retakes or drop the lowest</b><span>Lower stakes.</span></li>
      <li><b>Say the purpose</b><span>Practice, not judgment.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1007/s10648-023-09801-w">Yang, C., Li, J., Zhao, W., Luo, L., &amp; Shanks, D. R. (2023). Do practice tests (quizzes) reduce or provoke test anxiety? A meta-analytic review. <i>Educational Psychology Review, 35</i>, 87.</a></li>''',
quiz='''[
 {q:'On average, regular practice tests…',o:['Reduced test anxiety','Raised test anxiety','Had no effect'],a:0,f:'By a medium amount.'},
 {q:'The anxiety benefit was larger when quizzes were…',o:['Easier and lower stakes','Harder and higher stakes','Timed'],a:0,f:'Retakes and ungraded quizzes help.'},
 {q:'Harder quizzes…',o:['Help learning more, but calm anxiety less','Always cause anxiety','Don’t help learning'],a:0,f:'Aim for the sweet spot.'}]''',
js=BASE+r'''
/* ---------- sweet spot ---------- */
function qUpd(){const v=n=>+document.querySelector(`input[name="${n}"]:checked`).value;const d=v('qd'),s=v('qs'),r=v('qr');
 const learn=[1,2,3][d];const safe=Math.max(0,Math.min(3,3-[0,1,2][d]*0.5-[0,0.5,1.5][s]+(r?0.5:0)));const sf=Math.round(safe*2)/2;
 const lab=x=>x>=2.5?'High':x>=1.5?'Medium':x>=1?'Low':'Very low';
 $('qRes').innerHTML=`<div class="res wl2">${barRow('Challenge for learning',learn,3,lab(learn),'#7DD3A8')}${barRow('Feels safe (lower anxiety)',sf,3,lab(sf),'#FCB316')}</div>`;
 let title,text;
 if(s===2&&!r){title='High pressure';text='A large share of the grade with one attempt is where anxiety is most likely. Lower the stakes, or allow a retake, and the quiz can still challenge.'}
 else if(s===2){title='Retakes help, stakes still high';text='Retakes soften it, but a large share of the grade keeps pressure up. Consider making frequent quizzes a small share.'}
 else if(d===0&&s===0){title='Safe, a good start';text='Easy and ungraded calms anxiety most, a good way to start the term. Raise the challenge gradually as students get used to quizzing.'}
 else if(d===2&&s===0){title='Challenging, but safe';text='Hard questions help learning most. With no grade at stake'+(r?' and second chances':'')+', it can still feel safe. Explain that misses are part of practice.'}
 else if(d>=1&&s<=1){title='Near the sweet spot';text='Enough challenge to learn, low enough stakes to feel safe'+(r?', with a second chance':'')+'. That’s the balance the research points to.'}
 else{title='Low stakes, low challenge';text='Safe, but easy quizzes help learning less. Once students are comfortable, raise the difficulty.'}
 $('qTitle').textContent=title;$('qText').textContent=text}
$('qF').addEventListener('change',qUpd);qUpd();
'''+grid('''[
 ['The 2023 analysis pooled how many studies?',['24','4','240'],0,'With 3,374 participants.'],
 ['The studies measured test anxiety…',['Before and after a period of regular quizzing','Only once','During sleep'],0,'In classrooms and labs.'],
 ['Was there much sign of publication bias?',['Little','A lot','It wasn’t checked'],0,'The result also held without the one study measuring anxiety during quizzes.'],
 ['The benefit was larger when quizzes were…',['Easier and lower stakes','Harder','Longer'],0,'Retakes and ungraded quizzes.'],
 ['How was anxiety measured?',['With surveys','With heart-rate monitors','With grades'],0,'One reason for caution.'],
 ['The authors describe this research as…',['Young','Settled','Disproven'],0,'Many small studies.']]''','The pattern: regular low-stakes quizzing tends to lower test anxiety, not raise it.'))
import json as _j;o['vnote']=_j.load(open('gen/vnotes.json'))['e03']
open('e03/template.html','w').write(page(o))

import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('e','Assessment That Teaches',7,'Better Multiple Choice: Competitive Wrong Answers','Better multiple choice','A good wrong answer is a teaching tool. Write them with care.','Better multiple choice',
'Multiple choice has a reputation problem. Critics say it only tests recognition. Can a multiple-choice question make students really think?',
'<span><a href="#wT">Write the wrong answers</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['pfc','hip'],{'pfc':([40,-60],'left'),'hip':([640,770],'left')},'Drawing of the side of the brain with the prefrontal cortex, at the front, which weighs options, and the hippocampus, deep inside, which retrieves what we know, glowing orange and labelled.')
o.update(css=RECALL_CSS+'''
.wq{width:100%;max-width:560px;text-align:left}
.wq .stem{font:600 clamp(17px,2vw,20px)/1.45 var(--body);color:#fff;margin:0 0 6px}
.wq .ans{color:#7DD3A8;font-weight:700;margin:0 0 10px}
.wq label{display:flex;gap:10px;align-items:flex-start;padding:6px 0;color:#E9EEF6;font-size:17px;line-height:1.4;cursor:pointer;border-top:1px solid #3A4E72}
.wq input{margin-top:4px;width:18px;height:18px;accent-color:#FCB316;flex:none}
.wq .cnt{color:#C9D3E3;font-size:15px;margin:8px 0}
.wq ul{margin:6px 0 0;padding-left:20px;color:#E9EEF6}
.wq li{margin:0 0 6px}''',
body='''  <div class="col lede">
    <p>In 2012, Jeri Little, Elizabeth Bjork, Robert Bjork and Genna Angello tested this. Students read passages, then took practice questions in multiple-choice or short-answer format, before a final test.</p>
    <p>Both formats helped students remember the tested information. But multiple choice had an extra benefit. It also improved recall of related information that appeared only as the wrong answer options.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>Both formats</strong><span>helped memory for the tested information</span></div>
      <div role="listitem"><strong>A bonus</strong><span>multiple choice also helped with the wrong options’ content</span></div>
      <div role="listitem"><strong>Competitive</strong><span>wrong answers are the key condition</span></div>
      <div role="listitem"><strong>Large classes</strong><span>make frequent multiple-choice quizzing practical</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Why</span>Thinking through every option</h2>
    <p>When the wrong options are plausible, students have to think through why each one is wrong. That means retrieving what they know about every option, not just the right one.</p>
    <h2 class="sec"><span class="n">The key condition</span>Competitive alternatives</h2>
    <p>If the wrong answers are obviously wrong, there is nothing to think about, and the benefit disappears. So the classic weak question, with one plausible answer and three silly ones, wastes the opportunity. So does “all of the above”, which can often be spotted without much thought.</p>
  </div>

  <section class="night" aria-labelledby="wT">
    <div class="col">
      <h2 class="sec" id="wT"><span class="n">Try it</span>Write the wrong answers</h2>
      <p>Here is a question and its right answer. Pick three wrong answers from the list to finish it. Then see how much thinking your question would demand.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="wScreen">
          <form class="wq" id="wF">
            <p class="stem">Which brain structure is essential for forming new long-term memories of facts and events?</p>
            <p class="ans">Right answer: the hippocampus</p>
            <fieldset style="border:0;padding:0;margin:0"><legend class="cnt" id="wCnt">Pick three wrong answers.</legend>
            <div id="wOpts"></div></fieldset>
          </form>
        </div>
        <div>
          <p class="phase">Your question</p>
          <p class="mtitle" id="wTitle">Pick three</p>
          <div class="mtext" id="wText" aria-live="polite">Choose three wrong answers from the list.</div>
        </div>
      </div>
    </div>
  </section>

'''+GRID_HTML+box('Write wrong options from real student misconceptions. Make every option plausible to someone who has not learned the material. After the quiz, discuss why each wrong answer is wrong. Share this tip with students: ask why each wrong answer is wrong.'),
tips_h='A good wrong answer is a teaching tool. Write them with care.',
tips='''      <li><b>From real misconceptions</b><span>What students actually confuse.</span></li>
      <li><b>Every option plausible</b><span>No silly answers.</span></li>
      <li><b>Discuss the wrong answers</b><span>Why each one is wrong.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1177/0956797612443370">Little, J. L., Bjork, E. L., Bjork, R. A., &amp; Angello, G. (2012). Multiple-choice tests exonerated, at least of some charges: Fostering test-induced learning and avoiding test-induced forgetting. <i>Psychological Science, 23</i>(11), 1337–1344.</a></li>''',
quiz='''[
 {q:'Multiple choice had an extra benefit for…',o:['Information that appeared only as wrong options','Nothing','Spelling'],a:0,f:'When the wrong options were plausible.'},
 {q:'The key condition is…',o:['Competitive, plausible wrong answers','Four options exactly','“All of the above”'],a:0,f:'Obvious wrong answers give nothing to think about.'},
 {q:'Good wrong answers come from…',o:['Real student misconceptions','Jokes','Random words'],a:0,f:'And discuss them afterwards.'}]''',
js=BASE+r'''
/* ---------- write the wrong answers ---------- */
const WO=[['The amygdala',2,'Plausible: it sits right next to the hippocampus and is involved in emotional memory. Students who half-know the topic will weigh it.'],
 ['The prefrontal cortex',2,'Plausible: it’s involved in working memory and retrieval, a common confusion.'],
 ['The cerebellum',2,'Plausible: it’s involved in learning motor skills, so students must think about which kind of memory the question asks about.'],
 ['The stomach',0,'Obviously wrong: not a brain structure, so it takes no thought to rule out.'],
 ['All of the above',0,'Weak: “all of the above” can often be ruled out without much thought.'],
 ['The left ear',0,'Obviously wrong: nobody who has read anything will pick it.'],
 ['The thalamus',1,'Somewhat plausible: a deep structure students may have heard of, though less often confused with memory.']];
$('wOpts').innerHTML=WO.map(([t],i)=>`<label><input type="checkbox" value="${i}">${t}</label>`).join('');
function wUpd(){const ch=[...$('wOpts').querySelectorAll('input:checked')].map(x=>+x.value);
 $('wOpts').querySelectorAll('input').forEach(x=>{x.disabled=!x.checked&&ch.length>=3});
 $('wCnt').textContent=ch.length<3?`Pick three wrong answers (${ch.length} of 3 chosen).`:'Three chosen. Uncheck one to change.';
 if(ch.length<3){$('wTitle').textContent='Pick three';$('wText').textContent='Choose three wrong answers from the list.';return}
 const sc=ch.reduce((a,i)=>a+WO[i][1],0);let title,lead;
 if(sc>=6){title='A question that makes students think';lead='All three wrong answers are competitive. To answer, students must recall what each structure does, which is the extra benefit the 2012 study found.'}
 else if(sc>=3){title='Partly competitive';lead='At least one option will make students think, but at least one is weak or easy to rule out. Swap the weak ones for real misconceptions.'}
 else{title='Easy to spot';lead='The right answer stands out, so there is little to think about. That wastes the benefit of multiple choice.'}
 $('wTitle').textContent=title;$('wText').innerHTML=`<p>${lead}</p><ul>${ch.map(i=>`<li><b>${WO[i][0]}:</b> ${WO[i][2]}</li>`).join('')}</ul>`}
$('wOpts').addEventListener('change',wUpd);wUpd();
'''+grid('''[
 ['In the 2012 study, practice questions were…',['Multiple choice or short answer','Essays only','True or false only'],0,'Then a final test.'],
 ['Did both formats help memory for the tested information?',['Yes','Only short answer','Only multiple choice'],0,'Both helped.'],
 ['Multiple choice also improved recall of…',['Related information in the wrong options','Unrelated topics','Nothing else'],0,'The extra benefit.'],
 ['The extra benefit depends on wrong answers being…',['Plausible','Funny','Obviously wrong'],0,'Competitive alternatives.'],
 ['“All of the above” is often…',['Easy to spot without much thought','The best option','Required'],0,'It wastes the opportunity.'],
 ['Multiple choice makes frequent quizzing practical in…',['Large classes','Only small seminars','No classes'],0,'Bringing in the testing effect.']]''','The pattern: multiple choice with plausible wrong answers makes students retrieve, not just recognize.'))
open('e07/template.html','w').write(page(o))

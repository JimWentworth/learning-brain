from wkit import *
o=wbase(10,'Explaining to Learn: Self-Explanation and Talk','Explaining','to learn',
'Students who explain each step of an example to themselves, why it works and not just what it does, learn more from it. That habit can be prompted, and putting it into words is the point.')
o['hero_aria'],o['hero_js']=hero(['pfc','tem'],{'pfc':([40,-60],'left'),'tem':([300,770],'left')},'Drawing of the side of the brain with the prefrontal cortex and the temporal lobe, active when we explain an idea in words, glowing orange and labelled.')
screen='''            <div id="seE" style="background:#fff;color:#13294B;border-radius:6px;padding:16px 20px;font:17px/1.55 var(--body);max-width:540px;width:100%"></div>
            <p id="csS" style="font:600 clamp(18px,2.2vw,20px)/1.45 var(--body);color:#fff;max-width:42ch;margin:0" aria-live="polite">Press Start.</p>
            <p class="prog" id="csP">&nbsp;</p>'''
student=lab(screen,'Ready','Choose the best self-explanation','A worked example in three steps. For each step, pick the explanation a strong learner would give themselves. Then try a new problem.')
o.update(body=tabs('Choose the best self-explanation','A three-step worked example. Which explanation of each step would help you most? Then a problem that tests it.',student,
 'About 10 minutes',
 ['Show the worked example and run the three steps with the class voting on the best explanation.',
  'Before revealing the transfer problem’s answer, have pairs explain their reasoning to each other.',
  'Point out the difference between paraphrasing a step and explaining why it works.',
  'Give a worked example from your own course with a prompt after each step: “Why this step?”'],
 ['What makes an explanation “why” rather than “what”?',
  'Which explanation would have helped you on the new problem?',
  'Where in this course could you add a “why this step?” prompt?'],
 'Add short self-explanation prompts to worked examples, readings and solutions: “Why does this step work?” “What principle is used here?” Pair students to explain steps to each other, then check their explanations.',
 'Students learning in a second language may find explaining aloud harder; let them write first, or explain in pairs before sharing.')+'''
  <div class="col lede">
    <p>In a classic 1989 study, Michelene Chi and colleagues recorded students thinking aloud as they studied worked examples in a physics textbook. The students who learned more, the “good” students, generated many explanations, linking each step to the principles in the text and noticing when they didn’t understand. The weaker students mostly read and paraphrased.</p>
    <p>A follow-up in 1994 found that prompting students to explain to themselves improved their understanding.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>64</strong><span>research reports in a 2018 meta-analysis of self-explanation prompts</span></div>
      <div role="listitem"><strong>~6,000</strong><span>learners across those studies</span></div>
      <div role="listitem"><strong>g = 0.55</strong><span>average benefit of prompting students to self-explain</span></div>
      <div role="listitem"><strong>Mostly</strong><span>undergraduates in the studies so far</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The evidence</span>A reliable effect</h2>
    <p>Kiran Bisra, Qing Liu, John Nesbit, Farimah Salimi and Philip Winne analysed 64 research reports with nearly 6,000 participants that compared prompted self-explanation with other conditions. The average effect was g = 0.55, a medium effect that held across most domains and settings. Most of the studies involved undergraduate students.</p>
    <h2 class="sec"><span class="n">Why it works</span>Inferences, not paraphrases</h2>
    <p>Self-explanation means generating inferences about causal connections and conceptual relationships: why a step works, what principle it uses, how it links to what you already know. Paraphrasing a step repeats it; explaining it builds the connection that a new problem will need.</p>
    <h2 class="sec"><span class="n">Talk</span>Explaining to others</h2>
    <p>Explaining to a partner adds an audience who can ask “why?” and expose gaps. It also gives students learning in a second language practice using the discipline’s language in a low-stakes setting, where the focus is on ideas rather than polish.</p>
    <h2 class="sec"><span class="n">For learning</span>Prompt the why</h2>
    <p>Students rarely self-explain unprompted, especially when a worked example looks easy. A simple prompt after each step, “why does this work?”, turns reading into reasoning.</p>
  </div>

'''+pgrid_html(),
tips_h='Prompt the why, not just the what.',
tips='''      <li><b>Prompt after each step</b><span>“Why does this step work? What principle is it using?”</span></li>
      <li><b>Pair and explain</b><span>Partners take turns explaining steps, asking “why?”</span></li>
      <li><b>Check the explanations</b><span>Correct misconceptions before they set.</span></li>''',
sources='''        <li>Chi, M. T. H., Bassok, M., Lewis, M. W., Reimann, P., &amp; Glaser, R. (1989). Self-explanations: How students study and use examples in learning to solve problems. <i>Cognitive Science, 13</i>(2), 145–182.</li>
        <li>Chi, M. T. H., de Leeuw, N., Chiu, M.-H., &amp; LaVancher, C. (1994). Eliciting self-explanations improves understanding. <i>Cognitive Science, 18</i>, 439–477.</li>
        <li><a href="https://doi.org/10.1007/s10648-018-9434-x">Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., &amp; Winne, P. H. (2018). Inducing self-explanation: A meta-analysis. <i>Educational Psychology Review, 30</i>.</a></li>''',
foot='The worked example is written for this activity. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'In Chi’s 1989 study, students who learned more from worked examples…',o:['Explained steps by linking them to principles','Read faster','Paraphrased each step'],a:0,f:'And noticed when they didn’t understand.'},
 {q:'Prompting students to self-explain had an average effect of about…',o:['g = 0.55','g = 0.05','g = 1.5'],a:0,f:'Across 64 research reports.'},
 {q:'A good self-explanation says…',o:['Why a step works','What the step says, in other words','That it makes sense'],a:0,f:'Inferences, not paraphrases.'}]''',
js=PANEL_JS+r'''
/* ---------- self-explanation ---------- */
const EX=['<b>Problem.</b> A price rises from $40 to $50. What is the percentage increase?','<b>Step 1.</b> Change = 50 − 40 = 10.','<b>Step 2.</b> 10 ÷ 40 = 0.25.','<b>Step 3.</b> 0.25 × 100 = <b>25%</b>.'];
const ST=[
 [['We subtract 40 from 50.','A percentage change compares the size of the change with the starting value, so first we need the size of the change.','OK, that makes sense.'],1],
 [['We divide 10 by 40.','We divide by the starting value, not the new value, because the change is measured relative to where we began.','Division comes next.'],1],
 [['We multiply by 100.','Multiplying by 100 turns the proportion into a percentage: a change of 25 for every 100 of the original.','Got it.'],1]];
startRun(async()=>{let good=0;
 for(let i=0;i<3;i++){$('seE').innerHTML=EX.slice(0,i+2).join('<br>');$('csS').textContent=`Which explanation of step ${i+1} would help you most?`;$('csP').textContent=`Step ${i+1} of 3`;
  say(`Step ${i+1} of 3`,'Choose the best self-explanation','');
  const [os,k]=ST[i];const sh=shuf(os.map((x,j)=>[x,j]));const a=await ask(sh.map(x=>x[0]),'Which explanation helps most?');if(!RUN)return;const ok=sh[a][1]===k;if(ok)good++;mark(sh.findIndex(x=>x[1]===k),a);
  say(null,null,(ok?'<b class="ok">Yes.</b> ':'<b class="no">Not quite.</b> ')+'The best explanation says why the step works, by naming the principle behind it. Paraphrasing (“we subtract”) or agreeing (“makes sense”) adds nothing a new problem can use.');
  await nextBtn(i<2?'Next step':'Try a new problem');if(!RUN)return;hideCh()}
 $('seE').innerHTML='<b>New problem.</b> The price then falls from $50 back to $40. What is the percentage decrease?';$('csS').textContent='Use the principle, not the steps.';$('csP').textContent='Transfer';
 say('A new problem','What is the percentage decrease?','');
 const sh=shuf([['20%',1],['25%',0],['10%',0]]);const a=await ask(sh.map(x=>x[0]),'What is the percentage decrease?');if(!RUN)return;const ok=sh[a][1]===1;mark(sh.findIndex(x=>x[1]===1),a);
 $('csS').textContent='Done.';$('csP').textContent=' ';
 say('What happened',ok?'You transferred the principle':'The steps weren’t enough',
  (ok?'Right: 10 ÷ 50 = 20%. ':'It’s 20%: the change is 10, and the starting value is now 50. ')+'Copying the steps from the example gives 25%, the wrong answer. Knowing why you divide by the starting value gives the right one. That is what self-explanation buys: understanding that carries over to a new problem.')});
'''+grid('''[
 ['In Chi and colleagues’ 1989 study, what did weaker students mostly do with worked examples?',['Read and paraphrase them','Skip them','Explain each step'],0,'The stronger students explained.'],
 ['Did prompting self-explanation improve understanding in the 1994 follow-up?',['Yes','No','Only for weak students'],0,'Chi, de Leeuw, Chiu and LaVancher.'],
 ['How many research reports did Bisra and colleagues analyse?',['64','16','640'],0,'With nearly 6,000 participants.'],
 ['What was the average effect of self-explanation prompts?',['g = 0.55','g = 0.15','g = 1.25'],0,'A medium effect.'],
 ['Who took part in most of those studies?',['Undergraduates','Young children','Retirees'],0,'Research with younger learners is still growing.']]''','The pattern: explaining why a step works builds understanding that transfers.'))
write(o)

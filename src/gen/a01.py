import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='a01',n='1',label='The Learning Brain · Generative AI · Topic 1',epi='The Learning Brain, Generative AI, episode 1',
title='Prediction Machines: Brains, Language Models and the Next Word',h1='Prediction machines',em='Only one of them is trying to understand',read='7',mins='2 minutes',vtitle='Prediction machines',
dek='Brains and language models both predict the next word, and react when the guess is wrong. But they learn from very different amounts of language, and a model predicts what is likely, not what is true.',
jumps='<span><a href="#gT">Guess the next word</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the temporal lobe and the prefrontal cortex glowing orange and labelled. Language processing involves a network across the temporal and frontal lobes.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.tem.lab=[600,770];BR.R.tem.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['tem','pfc'],labels:['tem','pfc'],labelT:{tem:0.8,pfc:1.0},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.sframe{font:600 clamp(21px,2.6vw,27px)/1.4 var(--body);color:#fff;text-align:center;max-width:24ch;margin:0}
.sframe .blank{display:inline-block;min-width:4ch;border-bottom:3px solid #FCB316;color:#FCB316}
.gin{display:flex;gap:10px;align-items:center;justify-content:center;flex-wrap:wrap}
.gin[hidden]{display:none}
.gin input{width:200px;min-height:50px;font:700 22px var(--body);text-align:center;border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff}
.gin input:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.gfb{font:600 17px/1.45 var(--body);color:#E9EEF6;min-height:3em;margin:0;text-align:center;max-width:40ch}
.gfb b.ok{color:#7DD3A8}.gfb b.no{color:#FFB38A}''',
body='''  <div class="col lede">
    <p>Nine people listened to a 30-minute podcast while electrodes recorded from their brains. Their brains were predicting each next word before it arrived, and reacting with surprise when the guess was wrong. A language model listening to the same story did the same. Ariel Goldstein, Uri Hasson and colleagues reported this in 2022.</p>
    <p>Brains and models both predict. Only one of them is trying to understand.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>9</strong><span>people, a 30-minute podcast, and brain recordings that tracked each word</span></div>
      <div role="listitem"><strong>3</strong><span>principles shared by brains and language models</span></div>
      <div role="listitem"><strong>Nearly all</strong><span>of the explainable brain response to sentences, captured by the strongest models</span></div>
      <div role="listitem"><strong>4–5</strong><span>orders of magnitude more language for models than for children</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Shared principles</span>Predict, compare, keep the context</h2>
    <p>The 2022 study found three principles shared by brains and the model. Both predict the next word before it appears. Both compare that prediction with what actually comes. And both represent each word in its context.</p>
    <p>Across many models, Martin Schrimpf, Evelina Fedorenko and colleagues found in 2021 that the models better at predicting the next word were also better at predicting brain responses to sentences. The strongest captured nearly all of the explainable variance. Prediction also runs through human learning, as <a href="@@LB:lb04@@">the power of prediction</a> shows.</p>
  </div>

  <section class="night" aria-labelledby="gT">
    <div class="col">
      <h2 class="sec" id="gT"><span class="n">Try it</span>Guess the next word</h2>
      <p>Twelve sentences, each missing its last word. Type the word you expect, then see what comes. About 2 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="gScreen">
          <p class="sframe" id="gF" aria-live="polite"></p>
          <form class="gin" id="gGen" hidden><label class="sr-only" for="gGi">Your guess for the next word</label><input id="gGi" autocomplete="off" autocapitalize="off" spellcheck="false"><button class="nbtn" type="submit">Guess</button></form>
          <p class="gfb" id="gFb" aria-live="polite"></p>
          <div class="mrow" style="justify-content:center"><button class="nbtn ghost" id="gNext" type="button" hidden>Next sentence</button></div>
          <p class="prog" id="gProg" aria-live="polite">Press Start.</p>
        </div>
        <div>
          <p class="phase" id="gPhase">Ready</p>
          <p class="mtitle" id="gTitle">How well does your brain predict?</p>
          <p class="mtext" id="gText" aria-live="polite">Type one word for each blank. There is no time limit.</p>
          <div id="gRes"></div>
          <div class="mrow"><button class="nbtn" id="gGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Learning</span>Very different diets</h2>
    <p>The learning is very different. Children become fluent on tens of millions of words, heard in a social and physical world. As Michael Frank pointed out in 2023, large models are trained on around four or five orders of magnitude more.</p>
    <p>And prediction isn’t the whole of cognition. A model has no body, no goals of its own, and no memory of you unless one is built in. It predicts what text is likely, not what is true.</p>
    <h2 class="sec"><span class="n">A caution</span>Similar computations, different minds</h2>
    <p>Similar computations don’t mean similar minds. These studies compare language processing, mostly listening, in a handful of people and models.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Explain AI as a prediction engine</h3>
      <p>Tell students that AI predicts likely text, so they expect fluent errors. Use prediction in your own teaching: ask students to guess before they read, because a wrong guess sharpens attention. And remind them that their learning runs on effort and meaning, not volume.</p>
    </aside>
  </div>
''',
tips_h='Brains and models both predict',
tips='''      <li><b>A prediction engine</b><span>Expect fluent errors from AI.</span></li>
      <li><b>Guess before reading</b><span>A wrong guess sharpens attention.</span></li>
      <li><b>Effort and meaning, not volume</b><span>That’s what human learning runs on.</span></li>''',
sources='''        <li><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8904253/">Goldstein, A., Zada, Z., Buchnik, E., et al. (2022). Shared computational principles for language processing in humans and deep language models. <i>Nature Neuroscience</i>.</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/8694052/">Schrimpf, M., Blank, I. A., Tuckute, G., et al. (2021). The neural architecture of language: Integrative modeling converges on predictive processing. <i>PNAS</i>.</a></li>
        <li><a href="https://sites.socsci.uci.edu/~lpearl/colareadinggroup/readings/Frank2023_ChildrenLLMs.pdf">Frank, M. C. (2023). Bridging the data gap between children and large language models. <i>Trends in Cognitive Sciences</i>.</a></li>
        <li><a href="https://compneurolinglab.github.io/Lecture_Slides/LT5903/Kutas&amp;Hillyard_1980.pdf">Kutas, M., &amp; Hillyard, S. A. (1980). Reading senseless sentences: Brain potentials reflect semantic incongruity. <i>Science</i>.</a></li>''',
quiz='''[
 {q:'What did brains and a language model share, listening to the same podcast?',o:['Predicting the next word, and reacting when it was wrong','The same amount of training','The same goals'],a:0,f:'Three shared principles: predict, compare, represent in context.'},
 {q:'How much more language data do large models get than children?',o:['Around four or five orders of magnitude more','About the same','Less'],a:0,f:'Children become fluent on tens of millions of words.'},
 {q:'What does a language model predict?',o:['What text is likely','What is true','What you meant'],a:0,f:'So expect fluent errors.'}]''',
js=BASE+r'''
/* ---------- guess the next word ----------
   12 sentence frames. P = predictable ending, S = surprising ending, T = easy to predict but not true (or likely ≠ true).
   Type a guess; reveal the real ending with feedback. Count predictable endings guessed, and surprises. */
const IT=[
 ['P','Once upon a','time',['time']],
 ['P','The early bird catches the','worm',['worm']],
 ['P','It was raining, so he took his','umbrella',['umbrella','brolly']],
 ['P','Rome wasn’t built in a','day',['day']],
 ['P','He locked the door with his','key',['key','keys']],
 ['P','The cat chased the','mouse',['mouse','mice','rat']],
 ['P','She posted the letter without a','stamp',['stamp']],
 ['P','After the long run, she was very','tired',['tired','exhausted','thirsty','sweaty','hot']],
 ['S','He spread the warm bread with','socks',['socks'],'A word that doesn’t fit. In a 1980 study, endings like this one produced a larger brain response about 400 milliseconds after the word appeared.'],
 ['S','The pianist sat down and played the','toaster',['toaster'],'Your brain had a word ready, and this wasn’t it. That mismatch is the surprise signal.'],
 ['T','Lightning never strikes the same place','twice',['twice'],'Easy to predict, because the saying is so common. But it isn’t true: tall buildings and towers are struck again and again. Likely and true are different things.'],
 ['T','The capital of Australia is','Canberra',['canberra'],'Many people expect Sydney, the biggest and best-known city. The capital is Canberra. The likeliest word isn’t always the right one.']];
let gr=null;
function ask(){return new Promise(res=>{gr.res=res;$('gGen').hidden=false;$('gGi').value='';$('gGi').focus()})}
$('gGen').addEventListener('submit',e=>{e.preventDefault();if(!gr||!gr.res)return;const r=gr.res;gr.res=null;$('gGen').hidden=true;r($('gGi').value.trim().toLowerCase())});
function next(){return new Promise(res=>{const b=$('gNext');b.hidden=false;b.focus();b.onclick=()=>{b.onclick=null;b.hidden=true;res()}})}
$('gGo').addEventListener('click',async()=>{if(gr)return;gr={};const g=$('gGo');g.disabled=true;g.textContent='In progress';$('gRes').innerHTML='';
 const items=[...shuf(IT.filter(x=>x[0]==='P')).slice(0,8)];const sp=shuf(IT.filter(x=>x[0]!=='P'));
 [3,6,9,11].forEach((pos,k)=>items.splice(pos,0,sp[k]));
 const got={P:0,S:0,T:0},n={P:0,S:0,T:0};let syd=false;
 $('gPhase').textContent='Guessing';$('gTitle').textContent='What comes next?';
 for(let i=0;i<items.length;i++){const [k,fr,w,acc,note]=items[i];n[k]++;$('gProg').textContent=`Sentence ${i+1} of ${items.length}`;$('gFb').textContent='';
  $('gF').innerHTML=`${fr} <span class="blank">&nbsp;</span>`;const v=await ask();if(!gr)return;
  const hit=!!v&&acc.some(a=>v===a||v===a+'s'||(a.length>=5&&ed1(v,a)));if(hit)got[k]++;if(w==='Canberra'&&/sydney/.test(v))syd=true;
  $('gF').innerHTML=`${fr} <span class="blank">${w}</span>`;
  $('gFb').innerHTML=(hit?'<b class="ok">You predicted it.</b> ':v?`<b class="no">Surprise.</b> You guessed “${v.replace(/[<>&"]/g,'')}”. `:'<b class="no">No guess.</b> ')+(note||'');
  if(i<items.length-1){await next();if(!gr)return}}
 $('gF').textContent='Done';$('gFb').textContent='';$('gProg').textContent='';$('gPhase').textContent='Your results';
 $('gRes').innerHTML=`<div class="res wl2"><p class="gh">Endings you predicted</p>${barRow('Everyday endings',got.P,n.P,got.P+' of '+n.P,'#FCB316')}${barRow('Odd endings',got.S,n.S,got.S+' of '+n.S,'#C9D3E3')}</div>`;
 let title,text;const tail=` The last two sentences showed the catch: “lightning never strikes twice” is easy to predict and false${syd?', and like many people you expected Sydney':''}. A system that predicts likely words can be fluent and wrong.`;
 if(got.P>=6){title='Your brain was a step ahead';text=`You predicted ${got.P} of ${n.P} everyday endings, often before you’d finished reading. The odd endings caught you out: that jolt is the brain comparing its guess with what arrived.`+tail}
 else if(got.P>=3){title='Prediction, with some misses';text=`You predicted ${got.P} of ${n.P} everyday endings. Some sentences have more than one good ending, so a miss isn’t always a wrong guess. The odd endings were built to surprise.`+tail}
 else{title='Fewer matches than usual';text=`You matched ${got.P} of ${n.P} everyday endings. Perhaps you chose unusual words on purpose, or typed quickly. Most readers match most of them, because the brain predicts as it reads.`+tail}
 $('gTitle').textContent=title;$('gText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();gr=null});
'''+grid('''[
 ['Brains listening to a podcast, before each word arrived',['Were already predicting it','Waited for the word','Ignored the story'],0,'And reacted with surprise when the guess was wrong.'],
 ['A language model listening to the same story',['Did the same: predicted, then compared','Did something unrelated','Couldn’t process it'],0,'Three shared principles.'],
 ['Across many models, the ones better at predicting the next word',['Better predicted brain responses','Worse predicted brain responses','No relationship'],0,'The strongest captured nearly all of the explainable variance.'],
 ['How much language data do large models get, compared with children?',['Around four or five orders of magnitude more','About the same','Less'],0,'Children learn in a social and physical world.'],
 ['What does a language model predict?',['What text is likely','What is true','What you intend'],0,'So expect fluent errors.'],
 ['Do these studies show that models and brains are similar minds?',['No: similar computations, mostly for listening, in a handful of people','Yes, they are the same','They show models understand'],0,'Only one of them is trying to understand.']]''','The pattern: brains and models both predict, but a model predicts what is likely, not what is true.'))
open('a01/template.html','w').write(page(o))

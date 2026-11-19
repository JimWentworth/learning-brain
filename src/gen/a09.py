import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='a09',n='9',label='The Learning Brain · Generative AI · Topic 9',epi='The Learning Brain, Generative AI, episode 9',
title='Writing Is Thinking: What Happens When AI Writes the Essay',h1='Writing is thinking',em='Hand it off, and the encoding goes with it',read='7',mins='2 minutes',vtitle='Writing is thinking',
dek='Minutes after writing an essay with ChatGPT, most students couldn’t quote a sentence from it. Writing is not only a way to show thinking. It is where much of the thinking happens.',
jumps='<span><a href="#wT">Can you quote it?</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, and the temporal lobe, at the side, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.tem.lab=[600,770];BR.R.tem.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc','tem'],labels:['pfc','tem'],labelT:{pfc:0.8,tem:1.0},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.qq{font:600 clamp(18px,2.2vw,21px)/1.45 var(--body);color:#fff;max-width:42ch;margin:0;text-align:center}
.wnote{font:600 15px/1.45 var(--body);color:#C9D3E3;margin:0;text-align:center;max-width:44ch}
.wform{display:flex;flex-direction:column;gap:10px;align-items:center;width:100%;max-width:560px}
.wform[hidden]{display:none}
.wform textarea{width:100%;min-height:200px;font:500 17px/1.5 var(--body);border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;padding:10px 12px;box-sizing:border-box;resize:vertical}
.wform textarea:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.wclock{font:800 44px var(--body);color:#FCB316;margin:0}
.wclock[hidden]{display:none}
.jb{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}
.jb[hidden]{display:none}
.gfb{font:600 16px/1.45 var(--body);color:#FFB38A;min-height:1.4em;margin:0;text-align:center}''',
body='''  <div class="col lede">
    <p>Fifty-four students wrote short essays over four months, in three groups: with ChatGPT, with a search engine, or with only their own heads. Electrodes recorded their brain activity (EEG) as they wrote. Nataliya Kosmyna and colleagues at the MIT Media Lab posted the results in 2025.</p>
    <p>Brain connectivity scaled down with the amount of outside support. The unaided group showed the strongest, most widespread networks. Search users were in between. The AI group showed the weakest.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>54</strong><span>students writing essays over four months</span></div>
      <div role="listitem"><strong>~83%</strong><span>of the AI group couldn’t correctly quote their own essay, minutes after writing it</span></div>
      <div role="listitem"><strong>~11%</strong><span>in each of the other groups</span></div>
      <div role="listitem"><strong>18</strong><span>students in a fourth session, where the groups swapped</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Memory and ownership</span>Written, but not remembered</h2>
    <p>Minutes after finishing, most of the AI group could not correctly quote a sentence from the essay they had just written. In the first session the reported figure was about 83%, against about 11% in the other groups. They also felt the least ownership of their essays.</p>
  </div>

  <section class="night" aria-labelledby="wT">
    <div class="col">
      <h2 class="sec" id="wT"><span class="n">Try it</span>Can you quote it?</h2>
      <p>Write two very short essays: one in your own words, and one starting from a simulated assistant’s draft (written for this page), which you can edit. After a short break, try to type a sentence from each. About 4 minutes. Nothing you write leaves this page.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="wScreen">
          <p class="qq" id="wQ" aria-live="polite">Press Start.</p>
          <p class="wnote" id="wN"></p>
          <form class="wform" id="wF" hidden><label class="sr-only" for="wI" id="wIL">Your text</label><textarea id="wI" spellcheck="true"></textarea><button class="nbtn" type="submit" id="wSub">Submit</button></form>
          <p class="gfb" id="wFb" aria-live="polite"></p>
          <p class="wclock" id="wC" hidden aria-live="off"></p>
          <div class="jb" id="wB" hidden role="group" aria-label="Which feels more like yours?"></div>
          <p class="prog" id="wProg" aria-live="polite"></p>
        </div>
        <div>
          <p class="phase" id="wPhase">Ready</p>
          <p class="mtitle" id="wTitle">Write, break, quote</p>
          <p class="mtext" id="wText" aria-live="polite">Two essays of two or three sentences each.</p>
          <div id="wRes"></div>
          <div class="mrow"><button class="nbtn" id="wGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">The swap</span>Unaided first, then AI</h2>
    <p>In a fourth session, the groups swapped. Students who had first written unaided, and then used AI, showed higher engagement and used it more strategically. Students moving the other way showed weaker connectivity than those who had practised unaided all along.</p>
    <h2 class="sec"><span class="n">Generation</span>Where the thinking happens</h2>
    <p>This is the generation effect again. Writing is not only a way to show thinking. It is where much of the thinking happens. Hand it off, and the encoding goes with it.</p>
    <h2 class="sec"><span class="n">A caution</span>A warning sign, not a verdict</h2>
    <p>This is a preprint with a small sample: 54 people, and only 18 in the swap session. EEG connectivity is an indirect measure. Treat it as a warning sign, not a verdict.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Protect an unaided stage</h3>
      <p>Have students draft their ideas and structure before any AI use. Ask them to explain or quote their own work afterwards. And when AI comes in, use it to critique and extend a draft the student already owns.</p>
    </aside>
  </div>
''',
tips_h='If AI does the writing, the thinking may never happen',
tips='''      <li><b>Draft first, unaided</b><span>Ideas and structure before any AI.</span></li>
      <li><b>Explain or quote it back</b><span>Can students say what their own work says?</span></li>
      <li><b>AI to critique and extend</b><span>A draft the student already owns.</span></li>''',
sources='''        <li><a href="https://arxiv.org/abs/2506.08872">Kosmyna, N., Hauptmann, E., Yuan, Y. T., Situ, J., Liao, X.-H., Beresnitzky, A. V., Braunstein, I., &amp; Maes, P. (2025). Your brain on ChatGPT: Accumulation of cognitive debt when using an AI assistant for essay writing task. <i>arXiv preprint</i> 2506.08872.</a></li>''',
quiz='''[
 {q:'Brain connectivity while writing was weakest…',o:['With ChatGPT','With a search engine','With no tools'],a:0,f:'It scaled down with the amount of outside support.'},
 {q:'Minutes after writing, most of the AI group…',o:['Couldn’t correctly quote their own essay','Could quote it word for word','Had forgotten the topic'],a:0,f:'About 83% in the first session, against about 11% in the other groups.'},
 {q:'Which order worked better in the swap session?',o:['Unaided first, then AI','AI first, then unaided','No difference'],a:0,f:'Students who had written unaided first used AI more strategically.'}]''',
js=BASE+r'''
/* ---------- can you quote it? ----------
   Two prompts, randomly assigned: one written unaided, one starting from a simulated draft (editable).
   20-second break, then type one sentence from each (in writing order). Score: best overlap with any sentence of what was submitted.
   Then: which feels more like yours? */
const WP=[
 ['What makes a teacher memorable?','A memorable teacher combines deep knowledge of their subject with genuine care for students. They ask questions that spark curiosity rather than simply delivering facts. Their enthusiasm is contagious, and they make every student feel that their ideas matter.'],
 ['Why do people enjoy music?','Music engages both emotion and memory, linking sounds to moments in our lives. Its patterns of tension and release create a satisfying sense of anticipation. Sharing music with others also builds a feeling of connection and belonging.']];
const sents=t=>t.split(/(?<=[.!?])\s+/).map(s=>s.trim()).filter(s=>toks(s).length>=3);
function overlap(rec,txt){const r=toks(rec);let best=0;(sents(txt).length?sents(txt):[txt]).forEach(s=>{const w=toks(s);if(!w.length)return;const hit=w.filter(x=>r.some(y=>match(y,x))).length;best=Math.max(best,hit/Math.max(w.length,r.length))});return best}
let wr=null;
function wWrite(q,note,pre,label,minW){return new Promise(res=>{wr.res=res;wr.minW=minW;$('wQ').textContent=q;$('wN').textContent=note;$('wIL').textContent=label;$('wI').value=pre;$('wFb').textContent='';$('wF').hidden=false;$('wI').focus()})}
$('wF').addEventListener('submit',e=>{e.preventDefault();if(!wr||!wr.res)return;const v=$('wI').value.trim();const n=v.split(/\s+/).filter(Boolean).length;
 if(n<wr.minW){$('wFb').textContent=wr.minW>3?`Please write at least ${wr.minW} words (you have ${n}).`:'Type what you remember, even a few words.';$('wI').focus();return}
 const r=wr.res;wr.res=null;$('wF').hidden=true;$('wFb').textContent='';r(v)});
function wPick(){return new Promise(res=>{wr.pres=res;const b=$('wB');b.innerHTML=[['o','The one I wrote'],['a','The one the assistant drafted'],['b','Both equally']].map(([k,t],j)=>`<button class="nbtn${j?' ghost':''}" type="button" data-v="${k}">${t}</button>`).join('');b.hidden=false;b.querySelector('button').focus()})}
$('wB').addEventListener('click',e=>{const b=e.target.closest('button');if(!b||!wr||!wr.pres)return;const r=wr.pres;wr.pres=null;$('wB').hidden=true;r(b.dataset.v)});
function wBreak(sec){return new Promise(res=>{const c=$('wC');c.hidden=false;let s=sec;c.textContent=s;const tick=()=>{if(!wr)return;s--;c.textContent=s;if(s<=0){c.hidden=true;res()}else wr.tm=setTimeout(tick,1000)};wr.tm=setTimeout(tick,1000)})}
const pct=x=>Math.round(x*100);
$('wGo').addEventListener('click',async()=>{if(wr)return;wr={};const g=$('wGo');g.disabled=true;g.textContent='In progress';$('wRes').innerHTML='';
 const [P,Q]=shuf([...WP]);const ownFirst=Math.random()<.5;const own={p:P[0]},ai={p:Q[0],draft:Q[1]};const order=ownFirst?[own,ai]:[ai,own];
 $('wPhase').textContent='Write';
 for(let i=0;i<2;i++){const e=order[i];$('wProg').textContent=`Essay ${i+1} of 2`;
  if(e===own){$('wTitle').textContent='In your own words';$('wText').textContent='Two or three sentences. No need to polish.';
   e.txt=await wWrite(e.p,'Write two or three sentences of your own (at least 15 words).','','Your essay',15)}
  else{$('wTitle').textContent='With the assistant';$('wText').textContent='Edit the draft as much or as little as you like, then submit.';
   e.txt=await wWrite(e.p,'An assistant drafted this answer. Edit it as you like, then submit it as your essay.',e.draft,'Your essay, starting from the assistant’s draft',15)}
  if(!wr)return}
 $('wPhase').textContent='Short break';$('wTitle').textContent='20 seconds';$('wText').textContent='A short gap before the quiz.';$('wProg').textContent='';
 $('wQ').textContent='Count backwards from 100 in threes, in your head.';$('wN').textContent='';await wBreak(20);if(!wr)return;
 $('wPhase').textContent='Quote it';$('wTitle').textContent='From memory';$('wText').textContent='Type one sentence from each essay, as exactly as you can.';
 for(let i=0;i<2;i++){const e=order[i];$('wProg').textContent=`Quote ${i+1} of 2`;
  const rec=await wWrite(e.p,`Type one sentence from your essay on this question, as exactly as you can.`,'','One sentence from your essay',1);if(!wr)return;e.score=overlap(rec,e.txt)}
 $('wQ').textContent='Which essay feels more like yours?';$('wN').textContent='';$('wProg').textContent='';$('wPhase').textContent='Ownership';$('wTitle').textContent='One last question';$('wText').textContent='Go with your first reaction.';
 const feel=await wPick();if(!wr)return;
 $('wQ').textContent='Done.';$('wPhase').textContent='Your results';
 const sim=(a,b)=>{const A=toks(a),B=toks(b);return A.filter(x=>B.includes(x)).length/Math.max(A.length,B.length,1)};const edited=sim(ai.draft,ai.txt)<0.7;
 $('wRes').innerHTML=`<div class="res wl2"><p class="gh">Best match to a sentence you submitted</p>${barRow('Your own essay',own.score,1,pct(own.score)+'%','#7DD3A8')}${barRow('Assistant’s draft',ai.score,1,pct(ai.score)+'%','#FCB316')}</div>`;
 const Ok=own.score>=0.8,Ak=ai.score>=0.8;let title,text;
 if(Ok&&!Ak){title='Yours stuck; the draft didn’t';text=`You could quote your own essay (${pct(own.score)}% match) but not the one that started as the assistant’s (${pct(ai.score)}%). Producing the words is what lays them down.`}
 else if(Ok&&Ak){title='You could quote both';text=edited?`Both matched well. You edited the assistant’s draft a lot, which may have made it yours: the effort of rewriting is generation too.`:`Both matched well, with only a short gap and very short essays. In the study, after 20 minutes of writing, about 83% of the AI group couldn’t quote their essay.`}
 else if(Ak&&!Ok){title='The draft stuck better this time';text=`You quoted the assistant’s draft better (${pct(ai.score)}%) than your own (${pct(own.score)}%). Perhaps you read it closely, or your own essay was longer. With one try each, chance plays a big part.`}
 else if(own.score>ai.score+0.15){title='Closer for your own';text=`Neither quote was close to exact, but your own essay came closer (${pct(own.score)}% against ${pct(ai.score)}%). Writing it yourself left more behind.`}
 else{title='Neither stuck exactly';text=`Your quotes matched ${pct(own.score)}% of your own essay and ${pct(ai.score)}% of the drafted one. Exact recall is hard; the study’s gap was between groups, over many people.`}
 text+=feel==='o'?' And your own essay felt more like yours, which matches the study.':feel==='a'?' Interestingly, the drafted essay felt more like yours.':' You felt both were equally yours.';
 $('wTitle').textContent=title;$('wText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();wr=null});
'''+grid('''[
 ['Brain connectivity while writing was strongest…',['With no tools at all','With a search engine','With ChatGPT'],0,'Kosmyna and colleagues, 2025. It scaled down with outside support.'],
 ['Search engine users’ connectivity was…',['In between','The strongest','The weakest'],0,'The AI group showed the weakest.'],
 ['In the first session, the share of the AI group who couldn’t correctly quote their essay was about…',['83%','11%','50%'],0,'Against about 11% in each of the other groups.'],
 ['Which group felt the least ownership of their essays?',['The AI group','The unaided group','The search group'],0,'Ownership tracked who did the writing.'],
 ['In the swap session, students who wrote unaided first and then used AI…',['Showed higher engagement and used it more strategically','Stopped using it','Did worst of all'],0,'Students moving the other way showed weaker connectivity.'],
 ['How much weight should this study carry?',['A warning sign: a small preprint with an indirect measure','A settled verdict','None at all'],0,'54 people, and only 18 in the swap session.']]''','The pattern: the more the tool writes, the less the writer’s brain engages and remembers. Protect an unaided stage.'))
open('a09/template.html','w').write(page(o))

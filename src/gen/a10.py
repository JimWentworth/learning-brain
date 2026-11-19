import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='a10',n='10',label='The Learning Brain · Generative AI · Topic 10',epi='The Learning Brain, Generative AI, episode 10',
title='Creativity and Sameness: AI Lifts Each Writer but Narrows the Pool',h1='Creativity and sameness',em='Each writer gained; the collection lost variety',read='7',mins='2 minutes',vtitle='Creativity and sameness',
dek='With AI story ideas, people wrote stories rated more novel and better crafted, especially the least creative writers. But the stories also became more like each other.',
jumps='<span><a href="#iT">Your idea, or its idea?</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the temporal lobe, at the side, and the parietal lobe, at the top, glowing orange and labelled.',
hero_js="BR.R.par.lab=[560,-70];BR.R.par.al='left';BR.R.tem.lab=[600,770];BR.R.tem.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['tem','par'],labels:['tem','par'],labelT:{tem:0.8,par:1.0},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.qq{font:600 clamp(18px,2.2vw,21px)/1.45 var(--body);color:#fff;max-width:42ch;margin:0;text-align:center}
.ai{background:#0F2240;border:1px solid #3A4E72;border-radius:10px;padding:12px 14px;max-width:44ch;width:100%;margin:0;color:#E9EEF6;font-size:18px;line-height:1.45}
.ai b{display:block;font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#FCB316;margin-bottom:4px}
.ai[hidden]{display:none}
.wform{display:flex;flex-direction:column;gap:10px;align-items:center;width:100%;max-width:560px}
.wform[hidden]{display:none}
.wform textarea{width:100%;min-height:110px;font:500 17px/1.5 var(--body);border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;padding:10px 12px;box-sizing:border-box;resize:vertical}
.wform textarea:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.gfb{font:600 16px/1.45 var(--body);color:#FFB38A;min-height:1.4em;margin:0;text-align:center}
.shw{color:#FCB316;font-weight:700}''',
body='''  <div class="col lede">
    <p>Nearly 300 people wrote a short, eight-sentence story. A third worked alone. The others could see one AI story idea, or choose from up to five. Everyone wrote their own story, and none of them were professional writers. Six hundred evaluators judged the stories. Anil Doshi and Oliver Hauser reported the results in 2024.</p>
    <p>With access to five AI ideas, stories were rated about 8% more novel and 9% more useful, meaning better crafted and closer to publishable. The biggest gains went to the least creative writers. AI levelled the field, as it did for the consultants in topic 3.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>293</strong><span>non-professional writers, each writing an eight-sentence story</span></div>
      <div role="listitem"><strong>600</strong><span>evaluators judging the stories</span></div>
      <div role="listitem"><strong>~8% / ~9%</strong><span>more novel and more useful, with up to five AI ideas</span></div>
      <div role="listitem"><strong>More similar</strong><span>AI-assisted stories were more like each other</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Sameness</span>Each writer gained; the collection lost variety</h2>
    <p>But across the group, the AI-assisted stories were more similar to each other. The AI ideas pulled writers toward similar stories.</p>
    <p>The authors call this a social dilemma. Each person has a reason to use AI, but if everyone starts from the same suggestions, the shared pool of ideas narrows. The work drifts toward the same place.</p>
  </div>

  <section class="night" aria-labelledby="iT">
    <div class="col">
      <h2 class="sec" id="iT"><span class="n">Try it</span>Your idea, or its idea?</h2>
      <p>Write a one-sentence story idea for two prompts. For the first, you write alone. For the second, a simulated assistant offers an idea first (written for this page). Then see how much of your wording overlaps with the assistant’s idea each time. About 2 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="iScreen">
          <p class="qq" id="iQ" aria-live="polite">Press Start.</p>
          <p class="ai" id="iA" hidden></p>
          <form class="wform" id="iF" hidden><label class="sr-only" for="iI">Your story idea</label><textarea id="iI" spellcheck="true" placeholder="One sentence: who, where, and what happens"></textarea><button class="nbtn" type="submit">Submit</button></form>
          <p class="gfb" id="iFb" aria-live="polite"></p>
          <div class="mrow" style="justify-content:center"><button class="nbtn ghost" id="iNext" type="button" hidden>Next prompt</button></div>
          <p class="prog" id="iProg" aria-live="polite"></p>
        </div>
        <div>
          <p class="phase" id="iPhase">Ready</p>
          <p class="mtitle" id="iTitle">Alone, then with an idea</p>
          <p class="mtext" id="iText" aria-live="polite">Overlap is measured on the key words, ignoring small words like “the” and “a”.</p>
          <div id="iRes"></div>
          <div class="mrow"><button class="nbtn" id="iGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Short stories, non-professionals</h2>
    <p>These were short stories by non-professional writers, rated by online evaluators, with a model from 2023. Longer, expert creative work may behave differently.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Make sameness visible</h3>
      <p>Have students generate ideas alone first, then use AI to extend or challenge them. Reward difference: ask how a submission departs from what the AI suggested. In group work, compare ideas across the class, to make sameness visible. And treat the AI’s first suggestion as the obvious answer to beat, not the one to use.</p>
    </aside>
  </div>
''',
tips_h='AI can lift each person’s ideas. Keeping them different is up to us.',
tips='''      <li><b>Ideas alone first</b><span>Then use AI to extend or challenge them.</span></li>
      <li><b>Reward difference</b><span>How does the work depart from the AI’s suggestion?</span></li>
      <li><b>Beat the first suggestion</b><span>Treat it as the obvious answer, not the one to use.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1126/sciadv.adn5290">Doshi, A. R., &amp; Hauser, O. P. (2024). Generative AI enhances individual creativity but reduces the collective diversity of novel content. <i>Science Advances, 10</i>(28), eadn5290.</a></li>''',
quiz='''[
 {q:'With access to AI story ideas, individual stories were rated…',o:['More novel and more useful','Less creative','No different'],a:0,f:'About 8% more novel and 9% more useful, with up to five ideas.'},
 {q:'Who gained most?',o:['The least creative writers','The most creative writers','Everyone equally'],a:0,f:'AI levelled the field.'},
 {q:'Across the group, AI-assisted stories were…',o:['More similar to each other','More varied','Longer'],a:0,f:'Each writer gained; the collection lost variety.'}]''',
js=BASE+r'''
/* ---------- your idea, or its idea? ----------
   Two prompts (order random). Round 1: write alone, then see the assistant's idea. Round 2: see the assistant's idea, then write.
   Overlap = share of your key words (stop words removed) that also appear in the assistant's idea. */
const IP=[
 ['A story about an adventure on the open seas','A young sailor finds a map hidden in an old bottle and sets out across the stormy sea to find the treasure of a lost island.'],
 ['A story about an adventure on a different planet','An astronaut stranded on a distant planet discovers a hidden alien civilization and must find a way to send a message home.']];
const STOP=new Set('a an the and or but of to in on at for with from by as is are was were be been being it its this that these those he she they them his her their who whom which what when where while how into onto over under out up down off then than so if not no yes very can could will would should must has have had do does did i me my we our you your one some any all each every there here about after before through across'.split(' '));
const kw=t=>toks(t).filter(w=>w.length>2&&!STOP.has(w));
function ov(mine,its){const A=kw(mine),B=kw(its);const hit=A.filter(x=>B.some(y=>match(x,y)||match(y,x)));return{share:A.length?hit.length/A.length:0,hit}}
let ir=null;
function iWrite(){return new Promise(res=>{ir.res=res;$('iI').value='';$('iFb').textContent='';$('iF').hidden=false;$('iI').focus()})}
$('iF').addEventListener('submit',e=>{e.preventDefault();if(!ir||!ir.res)return;const v=$('iI').value.trim();if(kw(v).length<4){$('iFb').textContent='Please write a full sentence: who, where, and what happens.';$('iI').focus();return}const r=ir.res;ir.res=null;$('iF').hidden=true;r(v)});
function iNext(){return new Promise(res=>{const b=$('iNext');b.hidden=false;b.focus();b.onclick=()=>{b.onclick=null;b.hidden=true;res()}})}
const pct=x=>Math.round(x*100);
$('iGo').addEventListener('click',async()=>{if(ir)return;ir={};const g=$('iGo');g.disabled=true;g.textContent='In progress';$('iRes').innerHTML='';
 const [P1,P2]=shuf([...IP]);
 $('iPhase').textContent='Round 1: alone';$('iTitle').textContent='Your own idea';$('iText').textContent='One sentence. Write the first idea that appeals to you.';$('iProg').textContent='Prompt 1 of 2';
 $('iA').hidden=true;$('iQ').textContent=P1[0]+'.';const m1=await iWrite();if(!ir)return;
 $('iA').innerHTML=`<b>The assistant’s idea, for comparison</b>${P1[1]}`;$('iA').hidden=false;$('iQ').textContent='Here is what the assistant would have suggested.';
 await iNext();if(!ir)return;
 $('iPhase').textContent='Round 2: idea first';$('iTitle').textContent='With an idea in view';$('iText').textContent='Read the assistant’s idea, then write your own. Use it, change it, or ignore it.';$('iProg').textContent='Prompt 2 of 2';
 $('iQ').textContent=P2[0]+'.';$('iA').innerHTML=`<b>Assistant</b>${P2[1]}`;$('iA').hidden=false;const m2=await iWrite();if(!ir)return;
 $('iQ').textContent='Done.';$('iA').hidden=true;$('iProg').textContent='';$('iPhase').textContent='Your results';
 const o1=ov(m1,P1[1]),o2=ov(m2,P2[1]);
 const words=h=>h.length?h.map(w=>`<span class="shw">${w}</span>`).join(', '):'none';
 $('iRes').innerHTML=`<div class="res wl2"><p class="gh">Your key words that the assistant also used</p>${barRow('Alone',o1.share,1,pct(o1.share)+'%','#C9D3E3')}${barRow('Idea first',o2.share,1,pct(o2.share)+'%','#FCB316')}</div><p class="mtext">Shared alone: ${words(o1.hit)}.<br>Shared with the idea in view: ${words(o2.hit)}.</p>`;
 const d=o2.share-o1.share;const pr=pct(o1.share)===pct(o2.share)?`${pct(o1.share)}%, both times,`:`${pct(o1.share)}% and ${pct(o2.share)}%`;let title,text;
 if(d>=0.15){title='The idea pulled you in';text=`Writing alone, ${pct(o1.share)}% of your key words matched the assistant’s idea. With its idea in view, ${pct(o2.share)}% did. That is the pull the study found, and when a whole class starts from the same suggestion, the ideas converge.`}
 else if(d<=-0.15){title='You steered away from it';text=`With the assistant’s idea in view, you overlapped with it less (${pct(o2.share)}%) than when you wrote alone (${pct(o1.share)}%). Treating the suggestion as the obvious answer to beat is exactly the habit that keeps work different.`}
 else if(o1.share>=0.3&&o2.share>=0.3){title='Close to the assistant both times';text=`About ${pr} of your key words matched. The assistant’s ideas are typical ones, and typical ideas come to us easily too. That is why a class starting from AI suggestions drifts toward the same place.`}
 else{title='Your own ideas, both times';text=(o1.share+o2.share===0?'None of your key words matched the assistant’s ideas.':`Only ${pr} of your key words matched the assistant’s ideas.`)+` In the study, the pull showed up across many writers, not in every one.`}
 $('iTitle').textContent=title;$('iText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();ir=null});
'''+grid('''[
 ['With up to five AI ideas, stories were rated as more novel by about…',['8%','50%','0%'],0,'Doshi and Hauser, 2024. And about 9% more useful.'],
 ['“Useful”, in this study, meant…',['Better crafted and closer to publishable','Shorter','Funnier'],0,'Six hundred evaluators judged the stories.'],
 ['Who gained most from the AI ideas?',['The least creative writers','The most creative writers','Professional writers'],0,'AI levelled the field.'],
 ['Across the group, AI-assisted stories were…',['More similar to each other','More varied','Unchanged'],0,'The AI ideas pulled writers toward similar stories.'],
 ['The authors call this…',['A social dilemma','A placebo effect','A memory illusion'],0,'Each person has a reason to use AI, but the shared pool narrows.'],
 ['The writers in this study were…',['Non-professionals writing short stories','Published novelists','Children'],0,'Longer, expert creative work may behave differently.']]''','The pattern: AI ideas lift each writer, especially the least creative, but pull everyone toward the same stories.'))
open('a10/template.html','w').write(page(o))

import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='m09',n='9',label='The Learning Brain · Memory · Topic 9',epi='The Learning Brain, Memory, episode 9',
title='Why We Forget: Interference and Lost Paths',h1='Why we forget',em='Mostly, the way back is lost',read='8',mins='2 minutes',vtitle='Why we forget',
dek='Forgetting is not just time passing. Much of it is interference from similar material, and much of what seems forgotten is still stored, just out of reach.',
jumps='<span><a href="#iT">Watch interference build</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the hippocampus, deep inside, and the prefrontal cortex, at the front, glowing orange and labelled. In mice, switching on hippocampal engram cells with light brought back a memory that natural cues could no longer reach.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.hip.lab=[640,770];BR.R.hip.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['hip','pfc'],labels:['hip','pfc'],labelT:{hip:0.8,pfc:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.cnt{font:800 44px var(--body);color:#FCB316;text-align:center}
.wl{font:700 30px/1.35 var(--body);color:#fff;text-align:center}''',
body='''  <div class="col lede">
    <p>Ebbinghaus learned lists of nonsense syllables, then timed how long it took to relearn them. Most of the loss came fast, within the first day, and then slowed. A careful replication in 2015 found the same shape.</p>
    <p>But forgetting isn’t just time passing.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>75% → 25%</strong><span>forgetting over a day, once interference from earlier lists was removed</span></div>
      <div role="listitem"><strong>Category cues</strong><span>brought back words people couldn’t recall freely</span></div>
      <div role="listitem"><strong>Light</strong><span>brought back a mouse’s “lost” fear memory by switching on its engram cells</span></div>
      <div role="listitem"><strong>Harder to reach</strong><span>can mean more to gain from reaching it again</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Interference</span>Similar things compete</h2>
    <p>Much forgetting is interference. In 1957, Benton Underwood looked across many lab studies and found that the more lists people had learned before, the more they forgot of the next one. With that interference removed, forgetting over a day fell from about 75% to about 25%. Similar material competes, and new learning can also crowd out the old.</p>
  </div>

  <section class="night" aria-labelledby="iT">
    <div class="col">
      <h2 class="sec" id="iT"><span class="n">Try it</span>Watch interference build</h2>
      <p>Four rounds. In each, you’ll see 5 words, count backward out loud for 15 seconds, then type the words. About 2 minutes. Pay attention to the kinds of words in each round.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="iScreen">
'''+recall_screen('i')+'''
'''+tail('i')+'''
        </div>
        <div>
          <p class="phase" id="iPhase">Ready</p>
          <p class="mtitle" id="iTitle">Does each round get harder?</p>
          <p class="mtext" id="iText" aria-live="polite">Each word appears for 1½ seconds. When the number appears, count backward from it by threes, out loud, until the bar runs out.</p>
          <div id="iRes"></div>
          <div class="mrow"><button class="nbtn" id="iGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Still there</span>Available, but not accessible</h2>
    <p>Much of what seems forgotten is still stored. As <a href="@@LB:m01@@">the first topic</a> showed, people who couldn’t recall words freely recalled many more when given the category names.</p>
    <p>Mice show this at the level of cells. In 2015, Tomás Ryan, Susumu Tonegawa and colleagues gave mice a drug that blocked consolidation of a fear memory. The mice could no longer recall the fear from natural cues. But when the engram cells were switched on with light, the memory came back. The trace was stored; the path to it was lost.</p>
    <h2 class="sec"><span class="n">Forgetting helps</span>Not only failure</h2>
    <p>Losing access to outdated details, like an old address or last year’s timetable, keeps current ones easy to find. And in Robert and Elizabeth Bjork’s framework, a memory that has become harder to retrieve gains more from being retrieved again, which is one reason <a href="@@LB:lb11@@">spacing</a> works.</p>
    <h2 class="sec"><span class="n">A caution</span>Depends on the material</h2>
    <p>Much of this comes from word lists and animal studies. How fast we forget depends on the material, how well it was learned, and how it’s tested.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">When students go blank</h3>
      <p>Expect steep early loss, and revisit material within days. Separate similar topics, or teach their differences directly. And when students go blank, give a cue before giving the answer.</p>
    </aside>
  </div>
''',
tips_h='Forgetting is rarely erasing',
tips='''      <li><b>Revisit within days</b><span>The loss is steepest early.</span></li>
      <li><b>Separate similar topics</b><span>Or teach their differences directly.</span></li>
      <li><b>Cue before answering</b><span>The memory may just be out of reach.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1371/journal.pone.0120644">Murre, J. M. J., &amp; Dros, J. (2015). Replication and analysis of Ebbinghaus’ forgetting curve. <i>PLOS ONE</i>.</a></li>
        <li><a href="https://doi.org/10.1037/h0044616">Underwood, B. J. (1957). Interference and forgetting. <i>Psychological Review</i>.</a></li>
        <li><a href="https://support.pstnet.com/hc/en-us/articles/360050965574">Wickens, D. D. (1973). Some characteristics of word encoding. <i>Memory &amp; Cognition</i>. (Described by Psychology Software Tools.)</a></li>
        <li><a href="https://www.sciencedaily.com/releases/2015/05/150528142815.htm">Ryan, T. J., Roy, D. S., Pignatelli, M., Arons, A., &amp; Tonegawa, S. (2015). Engram cells retain memory under retrograde amnesia. <i>Science</i>. (Summary.)</a></li>
        <li><a href="https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2021/01/RABjorkELBjorkJARMAC2020ForPostingSingleSpaced.pdf">Bjork, R. A., &amp; Bjork, E. L. (2020). Desirable difficulties in theory and practice. <i>Journal of Applied Research in Memory and Cognition</i>.</a></li>''',
quiz='''[
 {q:'Underwood removed interference from earlier lists. What happened to forgetting over a day?',o:['It fell from about 75% to about 25%','It stayed the same','It rose'],a:0,f:'Much forgetting is competition from similar material.'},
 {q:'Mice couldn’t recall a fear after a drug blocked consolidation. What brought it back?',o:['Switching on the engram cells with light','Nothing','More training'],a:0,f:'The trace was stored; the path to it was lost.'},
 {q:'When a student goes blank, what should come first?',o:['A cue','The answer','A new topic'],a:0,f:'The memory may just be out of reach.'}]''',
js=BASE+recall_kit('i','ir')+r'''
/* ---------- watch interference build ----------
   Four Brown-Peterson rounds of 5 words: rounds 1-3 from one category, round 4 from another (random which).
   Words 1.5 s each, 15 s counting backward by threes (aloud, honour system), then typed recall. */
const CAT={fruits:['apple','banana','cherry','grape','lemon','mango','melon','peach','pear','plum','lime','kiwi','apricot','papaya','orange'],
 animals:['tiger','zebra','horse','rabbit','monkey','camel','otter','wolf','bear','deer','goat','mouse','lion','sheep','fox']};
let ir=null;
$('iGo').addEventListener('click',async()=>{if(ir)return;ir={};const g=$('iGo');g.disabled=true;g.textContent='In progress';$('iRes').innerHTML='';
 const base=Math.random()<0.5?'fruits':'animals',shift=base==='fruits'?'animals':'fruits';
 const bw=shuf([...CAT[base]]),sw5=shuf([...CAT[shift]]).slice(0,5);const rounds=[bw.slice(0,5),bw.slice(5,10),bw.slice(10,15),sw5];const got=[];
 for(let r=0;r<4;r++){const L=rounds[r];$('iPhase').textContent=`Round ${r+1} of 4`;$('iTitle').textContent='Remember these words';$('iText').textContent='Each word appears for 1½ seconds.';
  for(let i=0;i<5;i++){$('iW').innerHTML=`<span class="wl">${L[i]}</span>`;$('iProg').textContent=`Word ${i+1} of 5`;if(!await iHold(1.5))return}
  const n=300+Math.floor(Math.random()*600);$('iTitle').textContent='Count backward';$('iText').textContent='Out loud, by threes, until the bar runs out.';
  $('iW').innerHTML=`<span class="cnt">${n}</span>`;$('iProg').textContent=`${n}, ${n-3}, ${n-6}, …`;if(!await iHold(15))return;
  $('iTitle').textContent='Recall';$('iText').textContent=`Type the 5 words from round ${r+1}.`;$('iW').textContent='Which words?';$('iProg').textContent='';
  const v=await iRecall();if(!ir)return;const t=toks(v);got.push(L.filter(w=>t.some(x=>match(x,w))).length)}
 $('iW').textContent='Done';$('iPhase').textContent='Your results';
 $('iRes').innerHTML=`<div class="res wl2"><p class="gh">Words recalled, out of 5</p>${got.map((n,r)=>barRow(`Round ${r+1} · ${r<3?base:shift}`,n,5,n+' of 5',r<3?'#C9D3E3':'#FCB316')).join('')}</div>`;
 const [a,b,c,d]=got,drop=a-c,rel=d-c,tot=a+b+c+d;let title,text;
 if(tot<4){title='Too few words to see a pattern';text=`You recalled ${tot} words across four rounds. Try again, and say each word to yourself as it appears.`}
 else if(drop>=1&&rel>=1){title='Interference built up, then lifted';text=`Round 1: ${a} of 5. By round 3, after two more rounds of ${base}, ${c} of 5. When the category switched to ${shift} in round 4: ${d} of 5. The earlier ${base} crowded out the later ones; a new category escaped the competition. Delos Wickens called this release from proactive interference.`}
 else if(drop>=1){title='Interference built up';text=`You went from ${a} of 5 in round 1 to ${c} of 5 by round 3, as ${base} piled up. Switching to ${shift} in round 4 gave ${d} of 5, so the release that most people show didn’t appear this time. With 5 words a round, chance plays a big part.`}
 else if(c>=4&&a>=4){title='You held on every round';text=`You recalled ${a}, ${b}, ${c} and ${d} of 5. Five words may be too few to show interference for you, or you used a strategy, like linking each round into a story. In studies with many people, recall falls over the first few rounds of one category and rises when it switches.`}
 else{title='No build-up this time';text=`You recalled ${a}, ${b}, ${c} and ${d} of 5. Round 1 is usually the best, because nothing came before it to compete. With 5 words a round, chance plays a big part, and counting may have taken more of your attention in some rounds than others.`}
 $('iTitle').textContent=title;$('iText').textContent=text;$('iProg').textContent='';g.textContent='Try again';g.disabled=false;g.focus();ir=null});
'''+grid('''[
 ['Ebbinghaus relearning syllable lists: when did most of the loss come?',['Within the first day','Evenly over a month','Only after a week'],0,'Then it slowed. A 2015 replication found the same shape.'],
 ['People who had learned many earlier lists, recalling a new one a day later',['Forgot much more','Forgot the same','Forgot less, from practice'],0,'Underwood, 1957: about 75% against about 25%.'],
 ['Several rounds of words from one category, then a switch to a new category',['Recall jumps back up','Recall keeps falling','Recall drops to zero'],0,'Release from proactive interference.'],
 ['People who couldn’t recall words freely, given the category names',['Recalled many more','Recalled none','Recalled the same'],0,'The words were available but not accessible.'],
 ['Mice that couldn’t recall a fear after a consolidation-blocking drug, when engram cells were switched on with light',['Froze, as if remembering','Stayed calm','Learned a new fear'],0,'The trace was stored; the path was lost.'],
 ['A memory that has become harder to retrieve, when it is retrieved again',['Gains more','Gains less','Gains nothing'],0,'In the Bjorks’ framework, harder retrieval is a bigger boost.']]''','The pattern: forgetting is rarely erasing. Mostly, the way back is lost or crowded out.'))
open('m09/template.html','w').write(page(o))

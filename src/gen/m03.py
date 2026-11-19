import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='m03',n='3',label='The Learning Brain · Memory · Topic 3',epi='The Learning Brain, Memory, episode 3',
title='Depth and Meaning: What You Think About Is What You Keep',h1='Depth and meaning',em='What you think about is what you keep',read='8',mins='2½ minutes',vtitle='Depth and meaning',
dek='The same word is remembered far better after a question about its meaning than after a question about its letters. Trying to remember matters less than you might expect.',
jumps='<span><a href="#dT">Shallow or deep</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex and the temporal lobe glowing orange and labelled. Judging a word’s meaning engages the left prefrontal cortex more than judging its letters, and stronger prefrontal and temporal activity while studying predicts later memory.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.tem.lab=[600,770];BR.R.tem.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc','tem'],labels:['pfc','tem'],labelT:{pfc:0.8,tem:1.0},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.dq{font:600 clamp(18px,2.3vw,21px)/1.4 var(--body);color:#C9D3E3;text-align:center;max-width:32ch;min-height:2.8em;margin:0}
.dw{font:700 38px var(--body);color:#fff;min-height:48px;text-align:center}
.keys2{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
.keys2[hidden]{display:none}
.keys2 button{min-width:140px;min-height:54px;border-radius:12px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;font:800 19px var(--body);cursor:pointer}
.keys2 button small{display:block;font:600 13px var(--body);color:#C9D3E3}
.keys2 button:focus-visible{outline:3px solid #FCB316;outline-offset:2px}''',
body='''  <div class="col lede">
    <p>Three questions about the same word. Is it in capital letters? Does it rhyme with <i>train</i>? Would it fit the sentence “The student used her ___ to solve the problem”?</p>
    <p>On a surprise test later, people in Fergus Craik and Endel Tulving’s 1975 study recognized about 1 in 7 of the words they had judged for capital letters, about half the rhyme words, and about 4 in 5 of the words they had fitted into a sentence. The same kinds of words appeared in every condition, and nobody was trying to memorize them. What people were asked to think about decided what stayed.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>15%</strong><span>of words recognized after a question about capital letters</span></div>
      <div role="listitem"><strong>48%</strong><span>after a question about rhyme</span></div>
      <div role="listitem"><strong>81%</strong><span>after a question about meaning</span></div>
      <div role="listitem"><strong>About a quarter</strong><span>for capital-letter words, even when people knew a test was coming</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Levels of processing</span>Meaning leaves a deeper trace</h2>
    <p>This is the levels-of-processing idea, proposed by Craik and Robert Lockhart in 1972: processing for meaning leaves a more durable trace than processing for surface features like letters or sound.</p>
    <p>In the brain, a 1994 study by Shitij Kapur and colleagues scanned 12 people as they read nouns. When they decided whether each noun was living or non-living, the left inferior prefrontal cortex was more active than when they checked each word for the letter <i>a</i>, and they later recognized the living/non-living words far better. In 1998, Anthony Wagner and colleagues found that stronger left prefrontal and temporal activity while judging a word predicted whether it would be remembered.</p>
  </div>

  <section class="night" aria-labelledby="dT">
    <div class="col">
      <h2 class="sec" id="dT"><span class="n">Try it</span>Shallow or deep</h2>
      <p>You’ll answer a quick yes-or-no question about each of 24 words. Some questions are about letters, some about rhyme, some about meaning. Then there’s one more step. About 3 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="dScreen">
          <p class="dq" id="dQ" aria-live="polite"></p>
          <div class="dw" id="dW" aria-live="polite"></div>
          <div class="keys2" id="dKeys" hidden role="group"><button type="button" data-v="1" id="dYes">Yes<small>key Y</small></button><button type="button" data-v="0" id="dNo">No<small>key N</small></button></div>
          <p class="prog" id="dProg" aria-live="polite">Press Start.</p>
        </div>
        <div>
          <p class="phase" id="dPhase">Ready</p>
          <p class="mtitle" id="dTitle">Answer each question</p>
          <p class="mtext" id="dText" aria-live="polite">The question appears first, then the word. Answer as quickly and accurately as you can, with the buttons or the Y and N keys.</p>
          <div id="dRes"></div>
          <div class="mrow"><button class="nbtn" id="dGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Intent</span>Trying to remember matters less than you’d think</h2>
    <p>When Craik and Tulving warned people about the test, memory for capital-letter words rose only to about a quarter, and meaning words stayed at about 80%. In earlier studies by Thomas Hyde and James Jenkins, rating words for pleasantness produced recall about as good as deliberately studying them. Counting the letter <i>e</i> in each word did not.</p>
    <h2 class="sec"><span class="n">Not just time</span>Depth isn’t the same as effort</h2>
    <p>Meaning questions usually take a little longer. But in one of Craik and Tulving’s experiments, a slow, fiddly task about the pattern of consonants and vowels in each word took longer than an easy question about meaning, and still produced worse memory.</p>
    <h2 class="sec"><span class="n">Two cautions</span>Partly circular, and not always best</h2>
    <p>First, depth has never had a clean measure apart from memory itself, so the idea is partly circular: deep processing is what leads to good memory, and good memory shows the processing was deep. Second, deep isn’t always best. In 1977, Donald Morris, John Bransford and Jeffery Franks showed that on a test about rhymes, studying for rhyme beat studying for meaning. What matters is the match between how something is learned and how it is used, which <a href="@@LB:lb18@@">the transfer page</a> takes further.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Look at what your activities make students think about</h3>
      <p>Highlighting and copying keep attention on the surface. Instead, ask for judgments about meaning: why does this step work? How is this case like the last one? Which example would break the rule? Have students sort, compare and explain, rather than transcribe. And be wary of tasks that are busy but shallow. Memory is a by-product of thinking.</p>
    </aside>
  </div>
''',
tips_h='What students think about is what they keep',
tips='''      <li><b>Audit your tasks</b><span>What does each activity make students think about?</span></li>
      <li><b>Swap surface for meaning</b><span>Replace copying and highlighting with why and how questions.</span></li>
      <li><b>Sort, compare, explain</b><span>And beware tasks that are busy but shallow.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1037/0096-3445.104.3.268">Craik, F. I. M., &amp; Tulving, E. (1975). Depth of processing and the retention of words in episodic memory. <i>Journal of Experimental Psychology: General</i>.</a></li>
        <li><a href="https://doi.org/10.1016/S0022-5371(72)80001-X">Craik, F. I. M., &amp; Lockhart, R. S. (1972). Levels of processing: A framework for memory research. <i>Journal of Verbal Learning and Verbal Behavior</i>.</a></li>
        <li><a href="https://doi.org/10.1037/h0028372">Hyde, T. S., &amp; Jenkins, J. J. (1969). Differential effects of incidental tasks on the organization of recall of a list of highly associated words. <i>Journal of Experimental Psychology</i>.</a></li>
        <li><a href="https://doi.org/10.1016/S0022-5371(77)80016-9">Morris, C. D., Bransford, J. D., &amp; Franks, J. J. (1977). Levels of processing versus transfer appropriate processing. <i>Journal of Verbal Learning and Verbal Behavior</i>.</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC43298">Kapur, S., Craik, F. I. M., Tulving, E., et al. (1994). Neuroanatomical correlates of encoding in episodic memory: Levels of processing effect. <i>PNAS</i>.</a></li>
        <li><a href="https://www.nmr.mgh.harvard.edu/publications/journal_articles/3493">Wagner, A. D., et al. (1998). Building memories: Remembering and forgetting of verbal experiences as predicted by brain activity. <i>Science</i>.</a></li>''',
quiz='''[
 {q:'Which question about a word led to the best memory for it?',o:['Does it fit this sentence?','Does it rhyme with train?','Is it in capital letters?'],a:0,f:'About 4 in 5 recognized, against about half for rhyme and 1 in 7 for capitals.'},
 {q:'Rating words for pleasantness, compared with deliberately studying them, gave…',o:['About as good recall','Much worse recall','No recall at all'],a:0,f:'Thinking about meaning did the work, with or without the intent to remember.'},
 {q:'When can processing sound beat processing meaning?',o:['When the test is about sound','Never','When there is more time'],a:0,f:'Transfer-appropriate processing: the match between learning and test matters.'}]''',
js=BASE+r'''
/* ---------- shallow or deep ----------
   24 words, 8 per level (case, rhyme, sentence) assigned at random; 6 yes and 2 no per level.
   Question 1.5 s, then word; Yes/No. Then a surprise recognition test: 24 old + 24 new, random order.
   Hit rate by level, false alarms, and decision time by level. */
const W=[['cake','LAKE','She cut a slice of ___ for the party.'],['boat','COAT','They rowed the ___ across the river.'],['shoe','BLUE','He tied the lace on his left ___.'],['bell','SHELL','The school ___ rang at noon.'],['chair','HAIR','Pull up a ___ and sit down.'],['tree','BEE','The bird built a nest high in the ___.'],['hat','CAT','She wore a wool ___ on her head.'],['cloud','LOUD','A dark ___ drifted across the sky.'],['drum','THUMB','He beat the ___ with two sticks.'],['lamp','CAMP','Switch on the ___ so we can read.'],['bread','HEAD','He spread butter on the ___.'],['coin','JOIN','She dropped a ___ into the slot.'],
 ['frog','DOG','The ___ jumped into the pond.'],['nail','MAIL','Hammer the ___ into the wood.'],['rope','SOAP','Climb the ___ to the top.'],['cheese','KNEES','A mouse nibbled the ___.'],['pen','TEN','Sign your name with this ___.'],['ring','KING','He slipped the ___ onto her finger.'],['sock','CLOCK','Her ___ had a hole in the toe.'],['horse','COURSE','She rode the ___ across the field.'],['moon','SPOON','The full ___ lit up the night.'],['brick','STICK','They built the wall one ___ at a time.'],['sheep','SLEEP','The dog herded the ___ into the yard.'],['plate','GATE','Put the food on a clean ___.']];
const FOILS=['apple','goat','desk','glove','kite','vase','jar','fork','tent','duck','map','sink','rose','ball','cup','door','fish','lock','bus','comb','flag','barn','wheel','corn'];
const LV={c:'Capital letters',r:'Rhyme',s:'Sentence'};
let dr=null;
function yn(){return new Promise(res=>{dr.res=res;dr.t0=performance.now();$('dKeys').hidden=false;$('dYes').focus()})}
const ans=v=>{if(!dr||!dr.res)return;const r=dr.res;dr.res=null;$('dKeys').hidden=true;r([v,performance.now()-dr.t0])};
$('dKeys').addEventListener('click',e=>{const b=e.target.closest('button');if(b)ans(+b.dataset.v)});
addEventListener('keydown',e=>{if(!dr||!dr.res)return;const k=e.key.toLowerCase();if(k==='y'||k==='n'){e.preventDefault();ans(k==='y'?1:0)}});
$('dGo').addEventListener('click',async()=>{if(dr)return;dr={};const g=$('dGo');g.disabled=true;g.textContent='In progress';$('dRes').innerHTML='';
 const idx=shuf([...Array(24).keys()]);const trials=[];
 ['c','r','s'].forEach((lv,k)=>idx.slice(k*8,k*8+8).forEach((i,j)=>{const yes=j<6,other=W[(i+12)%24];const [w,rh,fr]=W[i];
  let q,show=w;if(lv==='c'){q='Is the word in capital letters?';show=yes?w.toUpperCase():w}else if(lv==='r')q=`Does it rhyme with ${yes?rh:other[1]}?`;else q=`Does it fit? “${yes?fr:other[2]}”`;
  trials.push({w,lv,yes,q,show,rt:0,old:null})}));
 shuf(trials);$('dPhase').textContent='Step 1 of 2 · Questions';$('dTitle').textContent='Answer each question';
 $('dKeys').setAttribute('aria-label','Your answer: yes or no');
 for(let i=0;i<24;i++){const t=trials[i];$('dProg').textContent=`Word ${i+1} of 24`;$('dQ').textContent=t.q;$('dW').textContent='…';await sw(1500);if(!dr)return;
  $('dW').textContent=t.show;const [v,rt]=await yn();if(!dr)return;t.rt=rt;$('dW').textContent='';await sw(300);if(!dr)return}
 $('dPhase').textContent='Step 2 of 2 · Surprise test';$('dTitle').textContent='A surprise memory test';
 $('dText').textContent='Some of these words were in the questions you just answered; some are new. Did you see each one? Yes means seen, No means new.';
 $('dKeys').setAttribute('aria-label','Did you see this word? Yes or no');
 const test=shuf([...trials.map(t=>({w:t.w,t})),...FOILS.map(w=>({w,t:null}))]);let fa=0;
 for(let i=0;i<test.length;i++){const x=test[i];$('dProg').textContent=`Word ${i+1} of 48`;$('dQ').textContent='Did you see this word?';$('dW').textContent=x.w;
  const [v]=await yn();if(!dr)return;if(x.t)x.t.old=v;else if(v)fa++}
 $('dQ').textContent='';$('dW').textContent='Done';$('dProg').textContent='';$('dPhase').textContent='Your results';
 const H={},R={};['c','r','s'].forEach(l=>{const L=trials.filter(t=>t.lv===l);H[l]=L.filter(t=>t.old).length;R[l]=L.reduce((a,t)=>a+t.rt,0)/L.length/1000});
 const tot=H.c+H.r+H.s,f1=x=>x.toFixed(1);
 $('dRes').innerHTML=`<div class="res wl2"><p class="gh">Words recognized, out of 8</p>${barRow(LV.c,H.c,8,H.c+' of 8','#C9D3E3')}${barRow(LV.r,H.r,8,H.r+' of 8','#8FA3C2')}${barRow(LV.s,H.s,8,H.s+' of 8','#FCB316')}<p class="gh">New words you called “seen”</p>${barRow('New words',fa,24,fa+' of 24','#FFB38A')}</div>`;
 const faT=fa>=4?` You also said “seen” to ${fa} of the 24 new words, so some of those hits may be guesses.`:'';
 const time=R.s>R.c+0.3?` The sentence questions took you about ${f1(R.s-R.c)} seconds longer than the capital-letter ones, but in Craik and Tulving’s study a slow surface task still lost to a quick meaning question, so time alone doesn’t explain it.`:'';
 let title,text;
 if(fa>=12){title='You said “seen” to most words';text=`You called ${fa} of the 24 new words “seen”, so your yes answers can’t tell old from new. Try again, and answer yes only when you’re fairly sure.`}
 else if(tot<4){title='Too few words recognized to compare';text=`You recognized ${tot} of the 24 words, too few to compare the questions. Try again; the words will be assigned to different questions.`}
 else if(H.s-H.c>=2){title='Meaning won';text=`You recognized ${H.s} of 8 sentence words, ${H.r} of 8 rhyme words, and ${H.c} of 8 capital-letter words. The kinds of words were the same; only the question changed.`+time+faT}
 else if(H.c-H.s>=2){title='The surface won this time';text=`You recognized ${H.c} of 8 capital-letter words and only ${H.s} of 8 sentence words, the reverse of the usual result. With 8 words per question, chance plays a big part, and a word shown in capitals can stand out on its own. Try again; the words will be assigned to different questions.`+faT}
 else{title='No clear difference this time';text=`You recognized ${H.c} capital-letter words, ${H.r} rhyme words and ${H.s} sentence words, out of 8 each. With 8 words per question, chance plays a big part. And if you expected a test, you may have thought about every word’s meaning; Craik and Tulving found that warning people narrowed the gap a little, but didn’t close it.`+faT}
 $('dTitle').textContent=title;$('dText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();dr=null});
'''+grid('''[
 ['A surprise test after judging whether words were in capital letters: how many were recognized?',['About 1 in 7','About half','About 4 in 5'],0,'Surface processing left a weak trace.'],
 ['After judging whether words fit a sentence',['About 4 in 5','About 1 in 7','About half'],0,'Meaning left the strongest trace.'],
 ['Capital-letter words, when people knew a test was coming',['Rose only to about a quarter','Rose to match meaning words','Stayed the same'],0,'Trying to remember helped less than thinking about meaning.'],
 ['Rating words for pleasantness, compared with deliberately studying them',['About as good recall','Much worse recall','Much better recall'],0,'Hyde and Jenkins: the meaning task did the work.'],
 ['A slow consonant-and-vowel task, compared with a quick question about meaning',['Worse memory, despite taking longer','Better memory, because it took longer','The same memory'],0,'Depth is not the same as time or effort.'],
 ['On a test about rhymes, which study task did better?',['Judging rhymes','Judging meaning','No difference'],0,'Morris, Bransford and Franks, 1977: the match between learning and test matters.']]''','The pattern: what you think about decides what you keep, and the best study task matches how the knowledge will be used.'))
open('m03/template.html','w').write(page(o))

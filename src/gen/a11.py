import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='a11',n='11',label='The Learning Brain · Generative AI · Topic 11',epi='The Learning Brain, Generative AI, episode 11',
title='Trust, but Verify: Fabricated Citations and Lateral Reading',h1='Trust, but verify',em='Fluency is free; verification is the skill',read='7',mins='2 minutes',vtitle='Trust, but verify',
dek='ChatGPT invented many of the citations it gave, and the fake ones looked real. Professional fact checkers show how to check: leave the page, and see what others say.',
jumps='<span><a href="#kT">Check the reading list</a></span><span><a href="#bT">Lateral or vertical?</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, and the occipital lobe, at the back, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.occ.lab=[900,760];BR.R.occ.al='right';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc','occ'],labels:['pfc','occ'],labelT:{pfc:0.8,occ:1.0},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS+'''
.cite{background:#0F2240;border:1px solid #3A4E72;border-radius:10px;padding:12px 14px;max-width:46ch;width:100%;margin:0;color:#E9EEF6;font-size:17px;line-height:1.5}
.cite b{display:block;font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#FCB316;margin-bottom:4px}
.cite[hidden]{display:none}
.jb{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}
.jb[hidden]{display:none}
.gfb{font:600 17px/1.45 var(--body);color:#E9EEF6;min-height:1.5em;margin:0;text-align:center;max-width:44ch}
.gfb b.ok{color:#7DD3A8}.gfb b.no{color:#FFB38A}
.rlist{margin:8px 0 14px;padding-left:20px;color:#E9EEF6;font-size:16px;line-height:1.5}
.rlist .ok{color:#7DD3A8}.rlist .no{color:#FFB38A}''',
body='''  <div class="col lede">
    <p>Researchers asked two versions of ChatGPT to write 84 short literature reviews, then checked all 636 citations against library databases. With the older model, GPT-3.5, 55% of the citations did not exist. With GPT-4, 18% did not. William Walters and Esther Isabelle Wilder reported this in 2023.</p>
    <p>The fabricated citations looked real, with plausible titles, often in real journals. Even among real citations, many had substantive errors, such as wrong volumes or pages: 43% for the older model, and 24% for the newer one.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>636</strong><span>citations in 84 AI-written literature reviews, all checked</span></div>
      <div role="listitem"><strong>55% → 18%</strong><span>fabricated, from GPT-3.5 to GPT-4</span></div>
      <div role="listitem"><strong>43% → 24%</strong><span>of real citations with substantive errors</span></div>
      <div role="listitem"><strong>10 of 10</strong><span>fact checkers found the more reliable website, against half of the historians</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Better, not solved</span>Verification is a core skill</h2>
    <p>Newer models do better, and tools that search before answering reduce fabrication. But they do not eliminate it. So verification is a core skill.</p>
  </div>

  <section class="night" aria-labelledby="kT">
    <div class="col">
      <h2 class="sec" id="kT"><span class="n">Try it</span>Check the reading list</h2>
      <p>A simulated assistant has given a reading list on retrieval practice. The list was written for this page: some entries are real, and some are not. For each, accept it or check it in a simulated library search. About 2 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="kScreen">
          <p class="cite" id="kC" aria-live="polite">Press Start.</p>
          <div class="jb" id="kB" hidden><button class="nbtn" type="button" data-v="a">Looks fine</button><button class="nbtn ghost" type="button" data-v="c">Check it</button></div>
          <p class="gfb" id="kFb" aria-live="polite"></p>
          <div class="mrow" style="justify-content:center"><button class="nbtn ghost" id="kNext" type="button" hidden>Next source</button></div>
          <p class="prog" id="kProg" aria-live="polite"></p>
        </div>
        <div>
          <p class="phase" id="kPhase">Ready</p>
          <p class="mtitle" id="kTitle">Six sources</p>
          <p class="mtext" id="kText" aria-live="polite">Each one looks like a proper reference. You decide which to check.</p>
          <div id="kRes"></div>
          <div class="mrow"><button class="nbtn" id="kGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Lateral reading</span>How fact checkers check</h2>
    <p>In a study of how people judge websites, Sam Wineburg and Sarah McGrew compared 10 professional fact checkers, 10 PhD historians and 25 Stanford students. Asked to find the more reliable of two websites, every fact checker succeeded, against half of the historians and a fifth of the students.</p>
    <p>The fact checkers’ method was lateral reading: leaving the page after a quick look, and opening new tabs to see what other sources say about it. The historians and students read vertically, staying on the page and judging it by how it looked: its logo, its domain name, its About page.</p>
  </div>

'''+cls_html('bT','Lateral or vertical?','Eight ways to judge a source. For each, decide: is it lateral reading (leaving the page to see what others say) or vertical reading (judging the page from the inside)? You’ll get feedback after each one.',[('L','Lateral','leave the page'),('V','Vertical','stay on the page')],'Lateral or vertical?','Lateral or vertical?','The question is always: did you leave the page?')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Older models, a small study</h2>
    <p>The citation study used models from 2023, and the lateral reading study was small. But the principle holds: fluent output is not evidence.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Make verification the assignment</h3>
      <p>Require students to verify every AI-supplied source, and show how they did it. Teach lateral reading explicitly: leave the page, and check who is behind a claim. And set an assignment where AI output contains planted errors to find.</p>
    </aside>
  </div>
''',
tips_h='Fluency is free. Verification is the skill.',
tips='''      <li><b>Verify every AI source</b><span>And show how.</span></li>
      <li><b>Teach lateral reading</b><span>Leave the page; check who is behind a claim.</span></li>
      <li><b>Plant errors to find</b><span>In AI output students must check.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1038/s41598-023-41032-5">Walters, W. H., &amp; Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. <i>Scientific Reports, 13</i>, 14045.</a></li>
        <li><a href="https://doi.org/10.1177/016146811912101102">Wineburg, S., &amp; McGrew, S. (2019). Lateral reading and the nature of expertise: Reading less and learning more when evaluating digital information. <i>Teachers College Record, 121</i>(11).</a></li>''',
quiz='''[
 {q:'With GPT-3.5, what share of the citations in the AI-written reviews did not exist?',o:['55%','5%','95%'],a:0,f:'With GPT-4, 18%.'},
 {q:'What did the fabricated citations look like?',o:['Real: plausible titles, often in real journals','Obviously fake','Blank'],a:0,f:'So they have to be checked, not eyeballed.'},
 {q:'Lateral reading means…',o:['Leaving the page to see what other sources say about it','Reading the page more carefully','Checking the About page'],a:0,f:'Every fact checker found the more reliable site.'}]''',
js=BASE+r'''
/* ---------- check the reading list ----------
   6 entries: 3 correct, 2 fabricated (invented authors), 1 real paper with wrong details. Accept or check.
   Checking shows a simulated library search result. Results at the end list everything. */
const KC=[
 ['Roediger, H. L., &amp; Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. <i>Psychological Science, 17</i>(3), 249–255.','ok','Found. The details match.','Roediger and Karpicke (2006)'],
 ['Karpicke, J. D., &amp; Blunt, J. R. (2011). Retrieval practice produces more learning than elaborative studying with concept mapping. <i>Science, 331</i>(6018), 772–775.','ok','Found. The details match.','Karpicke and Blunt (2011)'],
 ['Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., &amp; Willingham, D. T. (2013). Improving students’ learning with effective learning techniques. <i>Psychological Science in the Public Interest, 14</i>(1), 4–58.','ok','Found. The details match.','Dunlosky and colleagues (2013)'],
 ['Halvorsen, M., &amp; Price, T. (2019). Retrieval practice and long-term retention in undergraduate chemistry. <i>Journal of Educational Psychology, 111</i>(4), 612–627.','fab','No such article. The journal is real, but this paper and its authors do not exist.','Halvorsen and Price (2019)'],
 ['Rowland, C. A. (2016). The effect of testing versus restudy on retention: A meta-analytic review of the testing effect. <i>Psychological Bulletin, 142</i>(6), 1432–1463.','err','Found, with errors. The paper is real, but it was published in 2014, in volume 140.','Rowland (listed as 2016)'],
 ['Okafor, L., &amp; Brandt, S. (2021). Spaced retrieval quizzes in online courses: A randomized trial. <i>Computers &amp; Education</i>.','fab','No such article. The journal is real, but this paper and its authors do not exist.','Okafor and Brandt (2021)']];
let kr=null;
function kChoose(){return new Promise(res=>{kr.res=res;const b=$('kB');b.hidden=false;b.querySelector('button').focus()})}
$('kB').addEventListener('click',e=>{const b=e.target.closest('button');if(!b||!kr||!kr.res)return;const r=kr.res;kr.res=null;$('kB').hidden=true;r(b.dataset.v)});
function kNext(){return new Promise(res=>{const b=$('kNext');b.hidden=false;b.focus();b.onclick=()=>{b.onclick=null;b.hidden=true;res()}})}
$('kGo').addEventListener('click',async()=>{if(kr)return;kr={};const g=$('kGo');g.disabled=true;g.textContent='In progress';$('kRes').innerHTML='';
 const order=shuf([...KC]);const log=[];$('kPhase').textContent='Check the list';$('kTitle').textContent='Accept or check?';$('kText').textContent='Checking takes a moment. Accepting is instant.';
 for(let i=0;i<6;i++){const [c,s,res,sh]=order[i];$('kProg').textContent=`Source ${i+1} of 6`;$('kC').innerHTML=`<b>Assistant’s source</b>${c}`;$('kFb').textContent='';
  const v=await kChoose();if(!kr)return;log.push({c,s,res,sh,checked:v==='c'});
  $('kFb').innerHTML=v==='a'?'Accepted.':`<b class="${s==='ok'?'ok':'no'}">Library search:</b> ${res}`;
  if(i<5){await kNext();if(!kr)return}}
 $('kC').textContent='Done.';$('kFb').textContent='';$('kProg').textContent='';$('kPhase').textContent='Your results';
 const chk=log.filter(x=>x.checked).length,fabIn=log.filter(x=>x.s==='fab'&&!x.checked).length,errIn=log.filter(x=>x.s==='err'&&!x.checked).length,caught=log.filter(x=>x.s!=='ok'&&x.checked).length;
 $('kRes').innerHTML=`<div class="res wl2"><p class="gh">Out of 6</p>${barRow('Checked',chk,6,chk+' of 6','#FCB316')}${barRow('Problems caught',caught,3,caught+' of 3','#7DD3A8')}</div><p class="gh">The whole list</p><ul class="rlist">${log.map(x=>`<li>${x.s==='ok'?'<b class="ok">Real</b>':x.s==='fab'?'<b class="no">Fabricated</b>':'<b class="no">Real, wrong details</b>'}${x.checked?' (checked)':' (accepted)'}: ${x.sh}.${x.s==='ok'?'':' '+x.res}</li>`).join('')}</ul>`;
 let title,text;
 if(fabIn+errIn===0&&chk===6){title='Every source checked';text='You checked all six and caught all three problems. Two sources didn’t exist and one had the wrong year and volume, yet all six looked equally real. Checking every AI-supplied source is the habit to teach.'}
 else if(fabIn+errIn===0){title='Nothing got through, this time';text=`You checked ${chk} and caught all three problems. The ones you accepted happened to be real, but they looked no different from the fakes. With AI-supplied sources, check every one.`}
 else if(fabIn>0){title=fabIn===2?'Two fabricated sources got through':'A fabricated source got through';text=`You accepted ${fabIn===2?'both fabricated sources':'a source that does not exist'}`+(errIn?', and one with the wrong year and volume':'')+(fabIn===2?'. They had plausible titles, plausible authors and real journals.':'. It had a plausible title, plausible authors and a real journal.')+` In the study, even GPT-4 invented 18% of its citations.`}
 else{title='An error slipped through';text='You caught both fabricated sources, but accepted a real paper with the wrong year and volume. In the study, about a quarter of GPT-4’s real citations had errors like this. A citation can be real and still wrong.'}
 $('kTitle').textContent=title;$('kText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();kr=null});
'''+cls_js("{L:'Lateral',V:'Vertical'}",'''[
 ['Reading the website’s About page to see who runs it','V','Vertical: the About page is the site describing itself.'],
 ['Searching the organization’s name to see what news outlets and others say about it','L','Lateral: leaving the page to see what others say.'],
 ['Judging a site as trustworthy because it ends in .org','V','Vertical: anyone can register a .org domain.'],
 ['Opening a new tab to look up the author of an article','L','Lateral: checking who is behind a claim, from outside.'],
 ['Checking whether a citation exists in a library database','L','Lateral: confirming the source somewhere other than where you found it.'],
 ['Deciding a page is reliable because it looks professional and has many references','V','Vertical: looks and references can be borrowed or faked.'],
 ['Reading the Wikipedia entry on an unfamiliar organization before reading its site','L','Lateral: a quick outside view, as the fact checkers did.'],
 ['Asking the same AI whether its own answer is correct','V','Vertical: it stays inside the same source. Check somewhere else.']]''','Lateral or vertical?',r'''
 if(right>=7){title='You read like a fact checker';text=`${right} of 8 right. The question is always: did you leave the page? Fact checkers read less, and learned more.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Anything the source says about itself, including how it looks, is vertical. Lateral means checking from outside.`}
 else{title='Worth another look';text=`${right} of 8 right. Lateral reading means leaving the page: searching the name, the author or the citation elsewhere. Everything judged from inside the page is vertical.`}'''))
open('a11/template.html','w').write(page(o))

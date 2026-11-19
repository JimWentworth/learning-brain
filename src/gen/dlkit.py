"""Shared bits for the Digital Learning pages (d01-d12)."""
PRED_CSS='''
.qq{font:600 clamp(18px,2.2vw,21px)/1.45 var(--body);color:#fff;max-width:42ch;margin:0}
.jb{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}
.jb[hidden]{display:none}
.gfb{font:600 17px/1.45 var(--body);color:#E9EEF6;min-height:1.5em;margin:0;text-align:center;max-width:42ch}
.gfb b.ok{color:#7DD3A8}.gfb b.no{color:#FFB38A}
.prog{color:#C9D3E3;font-size:15px;margin:0}
.res .gh{color:#C9D3E3;font:700 14px var(--body);letter-spacing:.04em;margin:10px 0 2px}'''

def pred_html(tid,title,intro,mtitle,mtext):
    return f'''  <section class="night" aria-labelledby="{tid}">
    <div class="col">
      <h2 class="sec" id="{tid}"><span class="n">Try it</span>{title}</h2>
      <p>{intro}</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="eScreen">
          <p class="qq" id="eQ" aria-live="polite">Press Start.</p>
          <div class="jb" id="eB" hidden role="group" aria-label="Your prediction"></div>
          <p class="gfb" id="eFb" aria-live="polite"></p>
          <p class="prog" id="eProg" aria-live="polite"></p>
        </div>
        <div>
          <p class="phase" id="ePhase">Ready</p>
          <p class="mtitle" id="eTitle">{mtitle}</p>
          <p class="mtext" id="eText" aria-live="polite">{mtext}</p>
          <div id="eRes"></div>
          <div class="mrow"><button class="nbtn" id="eGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>
'''

def pred_js(EQ,bars,summary):
    """EQ: JS array of [question,[options],correctIndex,explanation].
    bars: JS template-literal body for the results (may use barRow).
    summary: JS that reads got (array of booleans) and n (count right) and sets title,text."""
    return r'''
/* ---------- predict ---------- */
const EQ='''+EQ+r''';
let er=null;
function eChoose(opts){return new Promise(res=>{er.res=res;const b=$('eB');b.innerHTML=opts.map((t,j)=>`<button class="nbtn${j?' ghost':''}" type="button" data-v="${j}">${t}</button>`).join('');b.hidden=false;b.querySelector('button').focus()})}
$('eB').addEventListener('click',e=>{const b=e.target.closest('button');if(!b||!er||!er.res)return;const r=er.res;er.res=null;$('eB').hidden=true;r(+b.dataset.v)});
function eNext(label){return new Promise(res=>{const g=$('eGo');g.textContent=label;g.disabled=false;g.focus();g.onclick=()=>{g.onclick=null;g.disabled=true;g.textContent='In progress';res()}})}
$('eGo').addEventListener('click',async()=>{if(er||$('eGo').onclick)return;er={};const g=$('eGo');g.disabled=true;g.textContent='In progress';$('eRes').innerHTML='';
 const got=[],N=EQ.length;$('ePhase').textContent='Predict';$('eTitle').textContent='Your prediction';$('eText').textContent='Pick one answer.';
 for(let i=0;i<N;i++){const [q,o,a,ex]=EQ[i];$('eProg').textContent=`Prediction ${i+1} of ${N}`;$('eQ').textContent=q;$('eFb').textContent='';
  const c=await eChoose(o);if(!er)return;got.push(c===a);
  $('eFb').innerHTML=(c===a?'<b class="ok">Right.</b> ':'<b class="no">Not quite.</b> ')+ex;
  if(i<N-1){await eNext('Next prediction');if(!er)return}}
 $('eQ').textContent='Done.';$('eProg').textContent='';$('ePhase').textContent='The results';
 $('eRes').innerHTML=`<div class="res wl2">'''+bars+r'''</div>`;
 const n=got.filter(Boolean).length;let title,text;
'''+summary+r'''
 $('eTitle').textContent=title;$('eText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();er=null});
'''

def hero(regions,labs,aria):
    """regions: list of keys; labs: dict key->([x,y],align)."""
    s=''.join(f"BR.R.{k}.lab=[{x},{y}];BR.R.{k}.al='{a}';" for k,((x,y),a) in labs.items())
    lt='{'+','.join(f'{k}:{0.8+0.2*i:.1f}' for i,k in enumerate(regions))+'}'
    r=','.join(f"'{k}'" for k in regions)
    return aria, s+f"\nstage('heroBrain',({{W,H,t}})=>{{brainDraw({{cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:[{r}],labels:[{r}],labelT:{lt},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))}})}});"

def base(n,title,h1,em,vtitle,dek,jumps):
    return dict(id=f'd{n:02d}',n=str(n),label=f'The Learning Brain · Digital Learning · Topic {n}',epi=f'The Learning Brain, Digital Learning, episode {n}',
        title=title,h1=h1,em=em,read='7',mins='2 minutes',vtitle=vtitle,dek=dek,jumps=jumps)

def box(text):
    return f'''  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">For teaching</h3>
      <p>{text}</p>
    </aside>
  </div>
'''

def sbase(prefix,series,n,title,h1,em,vtitle,dek,jumps):
    return dict(id=f'{prefix}{n:02d}',n=str(n),label=f'The Learning Brain · {series} · Topic {n}',epi=f'The Learning Brain, {series}, episode {n}',
        title=title,h1=h1,em=em,read='7',mins='2 minutes',vtitle=vtitle,dek=dek,jumps=jumps)

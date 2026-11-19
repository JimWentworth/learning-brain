BASE = r'''
const shuf=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
const sw=ms=>new Promise(r=>setTimeout(r,ms));
function ed1(a,b){if(a===b)return true;if(Math.abs(a.length-b.length)>1)return false;let i=0,j=0,d=0;while(i<a.length&&j<b.length){if(a[i]===b[j]){i++;j++;continue}if(++d>1)return false;if(a.length>b.length)i++;else if(b.length>a.length)j++;else{i++;j++}}return d+(a.length-i)+(b.length-j)<=1}
const match=(t,w)=>t===w||t===w+'s'||t===w+'es'||(w.length>=5&&ed1(t,w));
const toks=v=>[...new Set(v.toLowerCase().split(/[^a-z]+/).filter(Boolean))];
const barRow=(l,val,mx,lab,c)=>`<div class="row"><span>${l}</span><div class="bar"><i style="width:${mx?val/mx*100:0}%;background:${c}"></i></div><b>${lab}</b></div>`;
'''

# timer bar + easy break + free recall for a screen whose ids start with prefix P
def recall_kit(P, state):
    return r"""
function @PTimer(sec,me){const t0=performance.now();const tick=()=>{if(!@S||@S.tok!==me)return;const f=Math.min(1,(performance.now()-t0)/(sec*1000));$('@PTb').style.width=(100-f*100)+'%';if(f<1)requestAnimationFrame(tick)};tick()}
async function @PHold(sec){const me=Symbol();@S.tok=me;@PTimer(sec,me);await sw(sec*1000);if(!@S)return false;@S.tok=null;$('@PTb').style.width='0';return true}
function @PRecall(ph){return new Promise(res=>{@S.rres=res;$('@PForm').hidden=false;$('@PIn').value='';$('@PIn').placeholder=ph||'Type the words, in any order';$('@PIn').focus()})}
$('@PForm').addEventListener('submit',e=>{e.preventDefault();if(!@S||!@S.rres)return;const r=@S.rres;@S.rres=null;$('@PForm').hidden=true;r($('@PIn').value)});
async function @PBreak(sec,msg){sec=sec||30;$('@PW').textContent=msg?'':'Easy break';$('@PBrk').hidden=false;$('@PBrk').focus();let on=false;const me=Symbol();@S.tok=me;
 $('@PProg').textContent=msg||`For ${sec} seconds, tap the circle (or press Space) whenever it turns orange.`;
 const brk=$('@PBrk');brk.onclick=()=>{if(on){on=false;brk.classList.remove('on')}};const t0=performance.now();@PTimer(sec,me);
 while(performance.now()-t0<sec*1000){await sw(1000+Math.random()*1800);if(!@S)return;on=true;brk.classList.add('on');await sw(900);on=false;brk.classList.remove('on')}
 brk.hidden=true;@S.tok=null;$('@PTb').style.width='0';$('@PProg').textContent='';$('@PW').textContent=''}
$('@PBrk').addEventListener('keydown',e=>{if(e.key===' '){e.preventDefault();$('@PBrk').click()}});
""".replace('@P',P).replace('@S',state)

RECALL_CSS = '''.fw{font-family:var(--body);font-weight:700;color:#fff;text-align:center;min-height:64px;display:flex;align-items:center;justify-content:center;line-height:1.15;font-size:36px;flex-direction:column;gap:6px}
.fw small{font-size:15px;letter-spacing:.08em;text-transform:uppercase;color:#C9D3E3;font-weight:800}
.fin{display:flex;flex-direction:column;gap:10px;align-items:center;width:100%}
.fin[hidden]{display:none}
.fin textarea{width:100%;max-width:440px;min-height:120px;padding:10px 12px;font:600 19px/1.4 var(--body);border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;resize:vertical}
.fin textarea::placeholder{color:#AEBBD0}
.fin textarea:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.tbar{width:100%;max-width:420px;height:8px;background:#1B2E50;border-radius:4px;overflow:hidden}.tbar i{display:block;height:100%;background:#FCB316}
.brk{width:110px;height:110px;border-radius:50%;background:#3A4E72;border:4px solid #8FA3C2;cursor:pointer}
.brk.on{background:#FF8A3D}
.brk[hidden]{display:none}
.brk:focus-visible{outline:3px solid #FCB316;outline-offset:3px}
.res.wl2 .row{grid-template-columns:170px minmax(0,1fr) 90px}
@media (max-width:520px){.res.wl2 .row{grid-template-columns:110px minmax(0,1fr) 76px}}
.res .gh{font-size:15px;letter-spacing:.08em;text-transform:uppercase;font-weight:800;color:#C9D3E3;margin:6px 0 0}'''

def grid(PI, summary):
    return r'''
/* ---------- predict the findings ---------- */
const PI=''' + PI + r''';
const NP=PI.length;
$('pGrid').innerHTML=PI.map(([q,o],i)=>`<div class="prow"><p class="it" id="pq${i}">${i+1}. ${q}</p><fieldset aria-labelledby="pq${i}"><legend>${q}</legend>${shuf(o.map((t,j)=>[t,j])).map(([t,j])=>`<label><input type="radio" name="p${i}" value="${j}">${t}</label>`).join('')}</fieldset><p class="ex" id="px${i}" hidden></p></div>`).join('');
$('pCheck').addEventListener('click',()=>{let right=0,ans=0;PI.forEach(([q,o,a,ex],i)=>{const sel=document.querySelector(`input[name="p${i}"]:checked`);let lead;
  if(!sel)lead=`<b class="no">Not answered.</b> ${o[a]}. `;else{ans++;const ok=+sel.value===a;if(ok)right++;lead=ok?`<b>Right.</b> `:`<b class="no">Not quite.</b> ${o[a]}. `}
  const x=$('px'+i);x.innerHTML=lead+ex;x.hidden=false});
 document.querySelectorAll('#pGrid input').forEach(n=>n.disabled=true);
 $('pSum').textContent=(ans===0?'You didn’t make any predictions, so here are the answers. ':`You got ${right} of ${ans} prediction${ans>1?'s':''} right${ans<NP?` (${NP-ans} left blank)`:''}. `)+''' + repr(summary) + r''';
 $('pCheck').hidden=true;$('pReset').hidden=false;$('pReset').focus()});
$('pReset').addEventListener('click',()=>{document.querySelectorAll('#pGrid input').forEach(n=>{n.disabled=false;n.checked=false});document.querySelectorAll('#pGrid .ex').forEach(x=>{x.hidden=true;x.innerHTML=''});$('pSum').textContent='';$('pReset').hidden=true;$('pCheck').hidden=false;document.querySelector('#pGrid input').focus()});
'''

GRID_HTML = '''  <section aria-labelledby="brT" style="margin:24px 0 40px">
    <div class="col">
      <h2 class="sec" id="brT"><span class="n">Try it</span>Predict the findings</h2>
      <p>For each study in the video, predict what was found. Then check.</p>
    </div>
    <div class="wide">
      <form class="pgrid" id="pGrid"></form>
      <div class="qrow"><button class="pbtn" id="pCheck" type="button">Check my predictions</button><button class="pbtn" id="pReset" type="button" hidden>Try again</button></div>
      <p class="pmsg" id="pSum" aria-live="polite"></p>
    </div>
  </section>
'''

def recall_screen(P):
    return f'''          <div class="fw" id="{P}W" aria-live="polite"></div>
          <form class="fin" id="{P}Form" hidden><label class="sr-only" for="{P}In">Type the words you remember</label><textarea id="{P}In" autocomplete="off" autocapitalize="off" spellcheck="false"></textarea><button class="nbtn" type="submit">Done</button></form>
          <button class="brk" id="{P}Brk" hidden aria-label="Tap when the circle is orange"></button>'''

def tail(P):
    return f'''          <div class="tbar" aria-hidden="true"><i id="{P}Tb" style="width:0"></i></div>
          <p class="prog" id="{P}Prog" aria-live="polite">Press Start.</p>'''

CLS_CSS = '''.bscen{font:600 clamp(19px,2.4vw,22px)/1.45 var(--body);color:#fff;max-width:40ch;min-height:5.8em;margin:0}
.bopts{display:grid;grid-template-columns:repeat(var(--nb,3),minmax(0,1fr));gap:8px;width:100%;max-width:600px}
@media (max-width:520px){.bopts{grid-template-columns:1fr}}
.bopts[hidden]{display:none}
.bopts button{min-height:52px;border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;font:700 17px/1.2 var(--body);cursor:pointer;padding:4px 8px}
.bopts button small{display:block;font-size:13px;color:#C9D3E3;font-weight:600}
.bopts button:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.bopts button.ok{border-color:#7DD3A8;background:#173B33}.bopts button.no{border-color:#FFB38A;background:#3B2420}
.bopts button:disabled{cursor:default}
.bfb{font-size:18px;line-height:1.45;color:#E9EEF6;margin:0;min-height:3em;max-width:44ch}
.bfb b.ok{color:#7DD3A8}.bfb b.no{color:#FFB38A}'''

def cls_html(tid, title, intro, buttons, label, mtitle, fb):
    """buttons: list of (key, label, small)"""
    bt = ''.join(f'<button type="button" data-k="{k}">{l}{f"<small>{s}</small>" if s else ""}</button>' for k, l, s in buttons)
    return f'''  <section class="night" aria-labelledby="{tid}">
    <div class="col">
      <h2 class="sec" id="{tid}"><span class="n">Try it</span>{title}</h2>
      <p>{intro}</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="bScreen">
          <p class="bscen" id="bScen" aria-live="polite">Press Start.</p>
          <div class="bopts" id="bOpts" hidden role="group" aria-label="{label}" style="--nb:{len(buttons)}">{bt}</div>
          <p class="prog" id="bProg" aria-live="polite"></p>
        </div>
        <div>
          <p class="phase" id="bPhase">Ready</p>
          <p class="mtitle" id="bTitle">{mtitle}</p>
          <p class="bfb" id="bFb" aria-live="polite">{fb}</p>
          <div id="bRes"></div>
          <div class="mrow"><button class="nbtn" id="bGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>
'''

def cls_js(NM, CASES, question, summary_js):
    """NM: JS object literal of key->name; CASES: JS array [text,key,explanation]; summary_js: JS that sets title,text using right,n,miss,NM,weak"""
    return r'''
/* ---------- classifier ---------- */
const NM=''' + NM + ''';
const CASES=''' + CASES + r''';
let br=null;
function bAnswer(){return new Promise(res=>{br.res=res;const o=$('bOpts');o.hidden=false;o.querySelectorAll('button').forEach(b=>{b.disabled=false;b.classList.remove('ok','no')});o.querySelector('button').focus()})}
$('bOpts').addEventListener('click',e=>{const b=e.target.closest('button');if(!b||!br||!br.res)return;const r=br.res;br.res=null;r(b.dataset.k)});
function bWait(label){return new Promise(res=>{const g=$('bGo');g.textContent=label;g.disabled=false;g.focus();g.onclick=()=>{g.onclick=null;g.disabled=true;g.textContent='In progress';res()}})}
$('bGo').addEventListener('click',async()=>{if(br||$('bGo').onclick)return;br={};const g=$('bGo');g.disabled=true;g.textContent='In progress';$('bRes').innerHTML='';
 const order=shuf([...CASES]);const n=order.length;let right=0;const tot={},got={},miss={};Object.keys(NM).forEach(k=>{tot[k]=0;got[k]=0;miss[k]=0});
 $('bTitle').textContent=''' + repr(question) + r''';
 for(let i=0;i<n;i++){const [txt,k,ex]=order[i];tot[k]++;$('bPhase').textContent=`Case ${i+1} of ${n}`;$('bScen').textContent=txt;$('bProg').textContent='';$('bFb').textContent='';
  const a=await bAnswer();if(!br)return;const ok=a===k;if(ok){right++;got[k]++}else miss[k]++;
  $('bOpts').querySelectorAll('button').forEach(b=>{b.disabled=true;if(b.dataset.k===k)b.classList.add('ok');else if(b.dataset.k===a)b.classList.add('no')});
  $('bFb').innerHTML=(ok?'<b class="ok">Right.</b> ':`<b class="no">Not quite.</b> You chose “${NM[a]}”. `)+ex;$('bProg').textContent=`${right} of ${i+1} right so far.`;
  if(i<n-1){await bWait('Next case');if(!br)return}}
 $('bOpts').hidden=true;$('bScen').textContent='Done.';$('bProg').textContent='';$('bPhase').textContent='Your results';
 $('bRes').innerHTML=`<div class="res wl2">${Object.keys(NM).map(k=>barRow(NM[k],got[k],tot[k],got[k]+' of '+tot[k],'#FCB316')).join('')}</div>`;
 const weak=Object.keys(miss).filter(k=>miss[k]>0).map(k=>'“'+NM[k]+'”');const wj=a=>a.length<2?a.join(''):a.slice(0,-1).join(', ')+' and '+a[a.length-1];const missed=weak.length===Object.keys(NM).length?(weak.length===2?'cases in both groups':'cases in every group'):'some '+wj(weak)+' cases';let title,text;
''' + summary_js + r'''
 $('bTitle').textContent=title;$('bFb').textContent=text;g.onclick=null;g.textContent='Try again';g.disabled=false;g.focus();br=null});
'''

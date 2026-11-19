/* The Learning Brain: shared site menu, previous/next links, related topics and topic cards.
   GENERATED FILE: site/assets/nav.js is built by src/tools/make_nav.py from src/nav/nav_src.js,
   src/nav/nav.css, src/nav/site.json and src/nav/related.json. Edit those, not site/assets/nav.js.

   Every page loads it near the top of <body>:
     <script src="../assets/nav.js" data-page="lb02"></script>      (topic pages, one folder deep)
     <script src="assets/nav.js" data-page="home"></script>         (home page)
   Links are worked out from this file's own address, so the site works at a domain root
   (Vercel) or in a sub-folder (GitHub Pages, e.g. /learning-brain/). */
(()=>{
const SCRIPT=document.currentScript;
const CUR=(SCRIPT&&SCRIPT.dataset.page)||'';
const ROOT=new URL('../',SCRIPT?SCRIPT.src:location.href).href;   /* the site root, with a trailing slash */
const SITE=__SITE__;
const REL=__REL__;
const CSS=__CSS__;
const url=id=>id==='home'?ROOT:ROOT+id+'/';
const HOME=url('home');

/* Always open at the top: on first load, on reload, and when returning with Back/Forward.
   In-page links (#section) still work after load, because this only runs on load and pageshow. */
try{if('scrollRestoration' in history)history.scrollRestoration='manual'}catch(e){}
const top=()=>{window.scrollTo(0,0);document.documentElement.scrollTop=0;document.body&&(document.body.scrollTop=0)};
top();addEventListener('DOMContentLoaded',top);addEventListener('load',()=>{top();requestAnimationFrame(top)});addEventListener('pageshow',top);

/* styles and the menu button/panel, placed where the script tag is */
const st=document.createElement('style');st.textContent=CSS;document.head.appendChild(st);
const MARKUP=`<div class="lbnav" id="lbnav">
  <button class="lbnav-btn" id="lbnavBtn" aria-expanded="false" aria-controls="lbnavPanel">
    <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M3 5h14M3 10h14M3 15h14" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
    All topics
    <svg class="chev" viewBox="0 0 20 20" aria-hidden="true"><path d="M5 8l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
  </button>
  <nav class="lbnav-panel" id="lbnavPanel" aria-label="All topics in The Learning Brain" tabindex="-1" hidden>
    <div class="lbnav-head">
      <p>The Learning Brain</p>
      <label class="lbnav-sr" for="lbnavQ">Find a topic</label>
      <input id="lbnavQ" type="search" placeholder="Find a topic, e.g. sleep" autocomplete="off">
    </div>
    <div id="lbnavBody"></div>
  </nav>
</div>`;
if(SCRIPT&&SCRIPT.parentNode)SCRIPT.insertAdjacentHTML('beforebegin',MARKUP);
else document.body.insertAdjacentHTML('afterbegin',MARKUP);

const $=id=>document.getElementById(id),btn=$('lbnavBtn'),panel=$('lbnavPanel'),body=$('lbnavBody');
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const ALL={};SITE.forEach(g=>g.items.forEach((it,k)=>{ALL[it.id]={...it,u:url(it.id),series:g.title,k,g}}));
const me=ALL[CUR];

/* menu: every series as an expandable list (the current page's series starts open), with a search box */
const q=$('lbnavQ');
function item(it){if(it.id===CUR)return`<li class="lbnav-item here"><span aria-current="page"><span>${esc(it.t)}</span><small>You are here</small></span></li>`;
 return`<li class="lbnav-item"><a href="${url(it.id)}"><span>${esc(it.t)}</span></a></li>`}
function full(){let h='<section class="lbnav-group" aria-labelledby="lbg0"><h2 class="lbnav-gt" id="lbg0">Illustrated pages</h2><ul>';
 SITE.forEach((g,i)=>{const id='lbc'+i,open=g.items.some(it=>it.id===CUR);
  h+=`<li><button class="lbnav-dis" aria-expanded="${open}" aria-controls="${id}">${esc(g.title)}<small>${g.items.length} topics</small><svg viewBox="0 0 14 14" aria-hidden="true"><path d="M4 2l5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></button><ul class="lbnav-sub" id="${id}"${open?'':' hidden'}>${g.items.map(item).join('')}</ul></li>`});
 if(CUR!=='home')h+=`<li class="lbnav-item lbnav-all"><a href="${HOME}"><span>Home</span></a></li>`;
 h+='</ul></section>';body.innerHTML=h;
 body.querySelectorAll('.lbnav-dis').forEach(b=>b.onclick=()=>{const o=b.getAttribute('aria-expanded')==='true';b.setAttribute('aria-expanded',!o);$(b.getAttribute('aria-controls')).hidden=o})}
function search(s){const words=s.toLowerCase().split(/\s+/).filter(Boolean);const hit=t=>words.every(w=>t.toLowerCase().includes(w));
 const mk=t=>{let o=esc(t);words.forEach(w=>{o=o.replace(new RegExp('('+w.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')','ig'),'<mark>$1</mark>')});return o};const rows=[];
 SITE.forEach(g=>g.items.forEach(it=>{if(hit(it.t+' '+g.title))rows.push([it.t,it.id===CUR?null:url(it.id),g.title])}));
 body.innerHTML=rows.length?`<ul class="lbnav-res" aria-label="${rows.length} matching topics">${rows.slice(0,60).map(([t,u,where])=>`<li class="lbnav-item">${u?`<a href="${u}"><span>${mk(t)}</span><small>${esc(where)}</small></a>`:`<span><span>${mk(t)}</span><small>${esc(where)}</small></span>`}</li>`).join('')}</ul>`:`<p class="lbnav-empty">No topics match “${esc(s)}”.</p>`}
q.oninput=()=>q.value.trim()?search(q.value.trim()):full();
function open(o){panel.hidden=!o;btn.setAttribute('aria-expanded',o);if(o){q.value='';full();(matchMedia('(pointer:fine)').matches?q:panel).focus()}}
btn.onclick=()=>open(panel.hidden);
body.addEventListener('click',e=>{if(e.target.closest('a'))open(false)});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!panel.hidden){open(false);btn.focus()}});
document.addEventListener('pointerdown',e=>{if(!panel.hidden&&!$('lbnav').contains(e.target))open(false)});
full();

/* bottom of page: previous/next in the series, then 3 related topics (fills <div id="lbmore">) */
function more(){const el=$('lbmore');if(!el||!me)return;const its=me.g.items,p=its[me.k-1],n=its[me.k+1];
 let h=`<nav class="lbpn" aria-label="Previous and next in ${esc(me.series)}">`;
 if(p)h+=`<a class="pv" href="${url(p.id)}"><span class="pl">← Previous · Topic ${me.k}</span><b>${esc(p.t)}</b></a>`;
 if(n)h+=`<a class="nx" href="${url(n.id)}"><span class="pl">Next · Topic ${me.k+2} →</span><b>${esc(n.t)}</b></a>`;
 h+='</nav>';
 const rel=(REL[CUR]||[]).map(id=>ALL[id]).filter(Boolean);
 if(rel.length)h+=`<h2 class="sec" style="max-width:700px;margin-left:auto;margin-right:auto"><span class="n">Keep going</span>Related topics</h2><ul class="lbrel">`+rel.map(r=>`<li><a href="${r.u}"><span class="rs">${esc(r.series)}</span><b>${esc(r.t)}</b><span class="rb">${esc(r.b)}</span></a></li>`).join('')+'</ul>';
 h+=`<p class="lball"><a href="${HOME}#pagesT">See all topics</a></p>`;el.innerHTML=h}
if(document.readyState==='loading')addEventListener('DOMContentLoaded',more);else more();

/* topic cards for every series (used by the home page): a heading per series, then one card per topic */
window.renderColl=function(elId,current){
 const el=document.getElementById(elId);if(!el)return;
 const card=it=>{const here=it.id===current;
  const inner=`<b>${esc(it.t)}</b><p>${esc(it.b)}</p>${it.pick?`<i>On screen: ${esc(it.pick)}</i>`:''}<span class="st">${here?'You are here':'Read it'}</span>`;
  return `<div class="card${here?' here':' live'}"${here?' aria-current="page"':''}>${here?inner:`<a href="${url(it.id)}">${inner}</a>`}</div>`};
 el.innerHTML=SITE.map(g=>`<h3 class="collsub">${esc(g.title)} · ${g.items.length} topics</h3>`+g.items.map(card).join('')).join('');
};
})();

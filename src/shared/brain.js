// ===== Labelled "glass brain": lateral view facing left, local box 1000 x 680
function crPath(pts,closed){const p=new Path2D();const n=pts.length;const P=i=>closed?pts[(i+n)%n]:pts[Math.max(0,Math.min(n-1,i))];
 p.moveTo(pts[0][0],pts[0][1]);const last=closed?n:n-1;
 for(let i=0;i<last;i++){const p0=P(i-1),p1=P(i),p2=P(i+1),p3=P(i+2);p.bezierCurveTo(p1[0]+(p2[0]-p0[0])/6,p1[1]+(p2[1]-p0[1])/6,p2[0]-(p3[0]-p1[0])/6,p2[1]-(p3[1]-p1[1])/6,p2[0],p2[1])}
 if(closed)p.closePath();return p}
function polyPath(pts){const p=new Path2D();p.moveTo(pts[0][0],pts[0][1]);pts.slice(1).forEach(q=>p.lineTo(q[0],q[1]));p.closePath();return p}
const BR=(()=>{
 const OUT=[[90,330],[98,245],[150,165],[250,102],[375,64],[500,50],[625,56],[735,88],[805,128],[872,188],[920,268],[936,350],[908,418],[852,452],[762,470],[640,484],[500,482],[385,472],[305,452],[272,416],[225,424],[165,428],[112,398]];
 const CS=[[500,50],[482,128],[458,212],[440,300],[436,338]];
 const SF=[[272,416],[360,372],[440,338],[520,312],[600,298],[662,306]];
 const PO=[[805,128],[788,228],[772,330],[766,470]];
 const TP=[[662,306],[715,316],[772,330]];
 const fro=[[272,416],[225,424],[165,428],[112,398],[90,330],[98,245],[150,165],[250,102],[375,64],[500,50],...CS.slice(1),[360,372]];
 const par=[[500,50],[625,56],[735,88],[805,128],...PO.slice(1,3),...TP.slice().reverse().slice(1),...SF.slice(2,5).reverse(),...CS.slice(1).reverse()];
 const occ=[[805,128],[872,188],[920,268],[936,350],[908,418],[852,452],[766,470],[772,330],[788,228]];
 const tem=[[272,416],...SF.slice(1),...TP.slice(1),[766,470],[640,484],[500,482],[385,472],[305,452]];
 const pfc=[[272,416],[225,424],[165,428],[112,398],[90,330],[98,245],[150,165],[250,102],[330,76],[300,190],[290,300],[300,400]];
 const cer=[[760,440],[830,420],[900,418],[946,450],[956,505],[922,556],[850,580],[786,570],[748,536],[744,480]];
 const stem=[[650,430],[730,440],[744,520],[736,630],[700,632],[686,540]];
 const hip=[[505,398],[545,384],[590,372],[640,364],[690,360],[718,352],[728,334],[716,322]];
 const amy=[[452,392],[478,378],[502,386],[504,408],[482,420],[458,414]];
 const ent=[[500,428],[560,414],[620,410],[640,428],[600,446],[530,450]];
 const caud=[[330,250],[372,212],[430,196],[500,198],[560,214],[600,244],[612,282],[600,318],[580,340]];
 const put=[[380,268],[430,252],[478,262],[490,300],[458,330],[404,326],[376,300]];
 const tha=[[520,262],[566,250],[606,268],[608,300],[570,316],[526,304]];
 const vta=[[664,404],[694,398],[706,418],[684,432],[662,424]];
 const ffa=[[590,452],[650,446],[712,448],[722,462],[652,470],[592,468]];
 const ips=[[560,128],[620,150],[690,184],[748,226]];
 const v1=[[880,250],[922,282],[936,350],[912,410],[870,420],[858,340]];
 const GYRI=[[[160,200],[220,170],[260,210],[300,170]],[[130,300],[190,280],[230,320],[280,300]],[[300,130],[340,160],[380,120],[420,150]],[[340,240],[380,270],[400,230]],
  [[560,90],[600,120],[650,100],[700,130]],[[540,230],[590,250],[640,230],[690,270]],[[400,420],[460,400],[520,430],[580,410],[650,420],[720,400]],[[820,220],[860,260],[880,320]],[[820,380],[860,400],[890,380]]];
 const P={OUT:crPath(OUT,true),fro:polyPath(fro),par:polyPath(par),occ:polyPath(occ),tem:polyPath(tem),pfc:polyPath(pfc),cer:crPath(cer,true),stem:crPath(stem,true),
  hip:crPath(hip,false),amy:crPath(amy,true),ent:crPath(ent,true),caud:crPath(caud,false),put:crPath(put,true),tha:crPath(tha,true),vta:crPath(vta,true),ffa:crPath(ffa,true),ips:crPath(ips,false),v1:crPath(v1,true),
  CS:crPath(CS,false),SF:crPath(SF,false),PO:crPath(PO,false),GY:GYRI.map(g=>crPath(g,false))};
 // region specs: path keys, label anchor (local), label position (local), kind (fill|line|deep)
 const R={
  fro:{name:'frontal lobe',k:['fro'],pt:[250,170],lab:[150,-40],al:'right'},
  pfc:{name:'prefrontal cortex',k:['pfc'],pt:[175,300],lab:[-30,260],al:'right'},
  par:{name:'parietal lobe',k:['par'],pt:[650,140],lab:[720,-40],al:'left'},
  tem:{name:'temporal lobe',k:['tem'],pt:[420,440],lab:[260,560],al:'right'},
  occ:{name:'occipital lobe',k:['occ'],pt:[870,300],lab:[1040,250],al:'left'},
  cer:{name:'cerebellum',k:['cer'],pt:[870,520],lab:[1040,560],al:'left'},
  stem:{name:'brainstem',k:['stem'],pt:[716,590],lab:[640,680],al:'right'},
  hip:{name:'hippocampus',k:['hip'],pt:[640,366],lab:[600,660],al:'left',deep:1,line:1},
  amy:{name:'amygdala',k:['amy'],pt:[478,400],lab:[300,610],al:'right',deep:1},
  ent:{name:'entorhinal cortex',k:['ent'],pt:[580,432],lab:[480,680],al:'right',deep:1},
  str:{name:'striatum',k:['caud','put'],pt:[440,290],lab:[330,-40],al:'right',deep:1},
  tha:{name:'thalamus',k:['tha'],pt:[566,284],lab:[560,-40],al:'left',deep:1},
  vta:{name:'midbrain dopamine area',k:['vta'],pt:[684,414],lab:[1040,660],al:'left',deep:1},
  ffa:{name:'fusiform face area',k:['ffa'],pt:[680,458],lab:[1040,470],al:'left',deep:1},
  ips:{name:'intraparietal sulcus',k:['ips'],pt:[690,184],lab:[1040,120],al:'left',line:1},
  v1:{name:'visual cortex',k:['v1'],pt:[905,330],lab:[1040,360],al:'left'}};
 const GYR=[];{let sd=7;const rnd=()=>{sd=(sd*16807)%2147483647;return sd/2147483647};for(let i=0;i<46;i++){const x0=80+rnd()*860,y0=60+rnd()*420,ang=rnd()*Math.PI,len=50+rnd()*90;const pts=[];for(let k=0;k<6;k++){const u=k/5-0.5;pts.push([x0+Math.cos(ang)*len*u+Math.sin(ang)*Math.sin(k*2.1+i)*14,y0+Math.sin(ang)*len*u-Math.cos(ang)*Math.sin(k*2.1+i)*14])}GYR.push(crPath(pts,false))}}
 return{P,R,GYR}})();
// draw the brain. o: {cx,cy,s,t,active:[keys],labels:[keys],alpha,draw(0..1),glow(0..1),dim,labelAlpha}
function brainDraw(o){const{cx=960,cy=560,s=0.9,sy=1.16,t=0,active=[],labels=[],alpha=1,draw=1,glow=1,deep=0.55,labelT={},la=1,labSize=32,lobeTint=1,gmap={}}=o;const GL=k=>glow*(gmap[k]??1);if(alpha<=0)return;
 const{P,R}=BR;const L=([x,y])=>[cx+(x-500)*s,cy+(y-300)*s*sy];
 ctx.save();ctx.translate(cx,cy);ctx.scale(s,s*sy);ctx.translate(-500,-300);
 ctx.lineJoin='round';ctx.lineCap='round';
 // cerebellum + stem first, so the cortex overlaps them
 [['stem','#18304F'],['cer','#1A3459']].forEach(([k,c])=>{ga(alpha*sat(draw*1.5-0.3));ctx.fillStyle=c;ctx.fill(P[k])});
 active.forEach(k=>{if(k==='cer'||k==='stem'){ga(alpha*0.9*GL(k));ctx.fillStyle='rgba(255,95,5,0.5)';ctx.fill(P[k])}});
 ctx.save();ctx.clip(P.cer);ctx.strokeStyle='rgba(200,215,235,0.18)';ctx.lineWidth=2;ga(alpha*sat(draw*1.6-0.5));for(let k=0;k<7;k++){ctx.beginPath();ctx.ellipse(852,500,120-k*15,70-k*8,-0.12,Math.PI*0.02,Math.PI*0.98);ctx.stroke()}ctx.restore();
 ctx.strokeStyle='#E9EEF6';ctx.lineWidth=4;ga(alpha);if(draw<1){ctx.setLineDash([900*draw,900])}ctx.stroke(P.cer);ctx.stroke(P.stem);ctx.setLineDash([]);
 // cortex base fill (hides what lies under it)
 ga(alpha*sat(draw*2));ctx.fillStyle='#16305A';ctx.fill(P.OUT);
 // lobe tints
 const tints={fro:'#1E3B66',par:'#1B3760',tem:'#1A3459',occ:'#1D3964'};
 ctx.save();ctx.clip(P.OUT);for(const k in tints){ga(alpha*0.9*lobeTint*sat(draw*1.5-0.3));ctx.fillStyle=tints[k];ctx.fill(P[k])}
 // gyri texture
 ctx.strokeStyle='rgba(200,215,235,0.11)';ctx.lineWidth=2.4;ctx.lineCap='round';ga(alpha*sat(draw*1.6-0.5));BR.GYR.forEach(g=>ctx.stroke(g));
 // active glows inside clip (cortical)
 active.forEach((k,i)=>{const r=R[k];if(!r||r.deep||r.line||k==='cer'||k==='stem')return;const g=GL(k)*(0.85+0.15*Math.sin(t*2.4+i));const gr=ctx.createRadialGradient(r.pt[0],r.pt[1],0,r.pt[0],r.pt[1],260);gr.addColorStop(0,'rgba(255,110,30,0.85)');gr.addColorStop(1,'rgba(255,95,5,0.32)');ga(alpha*g);ctx.fillStyle=gr;r.k.forEach(q=>ctx.fill(P[q]));ctx.strokeStyle='rgba(255,140,70,0.9)';ctx.lineWidth=3;r.k.forEach(q=>ctx.stroke(P[q]))});
 ctx.restore();
 // sulci
 ctx.strokeStyle='rgba(233,238,246,0.55)';ctx.lineWidth=3;ga(alpha*sat(draw*1.6-0.6));[P.CS,P.SF,P.PO].forEach(q=>ctx.stroke(q));
 // outline (draw-on)
 ctx.strokeStyle='#E9EEF6';ctx.lineWidth=4;ga(alpha);if(draw<1){ctx.setLineDash([2600*draw,2600])}ctx.stroke(P.OUT);ctx.setLineDash([]);
 // deep structures (glass view)
 const dk=['hip','amy','ent','str','tha','vta','ffa'];
 dk.forEach(k=>{const r=R[k],on=active.includes(k);const a=alpha*(on?1:deep)*sat(draw*1.5-0.5);if(a<=0)return;
  r.k.forEach(q=>{if(on){ctx.save();ga(a*GL(k));ctx.shadowColor=ORANGE;ctx.shadowBlur=24;ctx.fillStyle='rgba(255,95,5,0.75)';ctx.strokeStyle=ORANGE;ctx.lineWidth=(q==='caud'||q==='hip')?16:4;
    if(q==='caud'||q==='hip'){ctx.stroke(P[q])}else{ctx.fill(P[q]);ctx.stroke(P[q])}ctx.restore()}
   else{ga(a*0.8);ctx.setLineDash([7,7]);ctx.strokeStyle='rgba(201,211,227,0.7)';ctx.lineWidth=(q==='caud'||q==='hip')?5:2.5;ctx.stroke(P[q]);ctx.setLineDash([])}})});
 // IPS line
 {const on=active.includes('ips');ga(alpha*(on?Math.max(0.6,GL('ips')):0.6)*sat(draw*1.6-0.6));ctx.strokeStyle=on?ORANGE:'rgba(233,238,246,0.5)';ctx.lineWidth=on?7:3;if(on){ctx.shadowColor=ORANGE;ctx.shadowBlur=18}ctx.stroke(P.ips);ctx.shadowBlur=0}
 // v1 glow
 if(active.includes('v1')){ctx.save();ctx.clip(P.OUT);ga(alpha*GL('v1')*0.9);ctx.fillStyle='rgba(255,95,5,0.6)';ctx.fill(P.v1);ctx.restore()}
 ctx.restore();
 // labels
 labels.forEach((k,i)=>{const r=R[k];if(!r)return;const t0=labelT[k]??0,p=sat((t-t0)/0.45);if(p<=0)return;const on=active.includes(k);
  const a=L(r.pt),b=L(r.lab);const ex=r.al==='right'?b[0]+12:r.al==='left'?b[0]-12:b[0];
  ctx.save();ga(alpha*la);ctx.strokeStyle=on?ORANGE:'rgba(201,211,227,0.85)';ctx.lineWidth=2.4;ctx.beginPath();ctx.moveTo(a[0],a[1]);ctx.lineTo(lerp(a[0],ex,ez(p)),lerp(a[1],b[1],ez(p)));ctx.stroke();
  ctx.fillStyle=on?ORANGE:'#E9EEF6';ctx.beginPath();ctx.arc(a[0],a[1],on?7:5,0,7);ctx.fill();ctx.restore();
  const q=sat((t-t0-0.25)/0.35);if(q>0){ctx.save();ga(alpha*la*q);ctx.font=`${on?700:600} ${labSize}px ${BODY}`;ctx.textAlign=r.al==='right'?'right':r.al==='left'?'left':'center';ctx.textBaseline='middle';ctx.fillStyle=on?ORANGE:'#E9EEF6';ctx.fillText(r.name,b[0],b[1]);ctx.restore()}})}

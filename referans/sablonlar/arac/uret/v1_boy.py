from base import build
import json, sys

B = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {
    "q": 1.2, "start": 3.0, "fiyat": 4.4, "ml": 10.0, "ml2": 12.0, "yirmi": 13.6, "orta": 16.4, "cunku": 20.6, "END": 23.0}

SVG = r'''
   <g id="cups"><g id="c0"></g><g id="c1"></g><g id="c2"></g></g>
   <g id="steam" fill="none" stroke="#b9b4a8" stroke-width="9" stroke-linecap="round"><path id="s0"/><path id="s1"/><path id="s2"/></g>
   <g id="tags"></g>
   <path id="mL" stroke="#1c1b18" stroke-width="10" stroke-linecap="round" fill="none"/><circle id="mD" r="13" fill="#ff5a1f"/>
   <text id="mT" font-size="34" fill="#1c1b18" text-anchor="start"></text>
   <path id="hL" stroke="#1c1b18" stroke-width="10" stroke-linecap="round" fill="none"/><circle id="hD" r="13" fill="#ff5a1f"/>
   <text id="hT" font-size="38" fill="#ff5a1f" text-anchor="middle"></text>
   <g id="stamp" filter="url(#ps)"><rect x="-95" y="-38" width="190" height="76" fill="#ff5a1f" stroke="#1c1b18" stroke-width="5"/><text y="14" font-size="40" fill="#FFF8EB" text-anchor="middle">1,66 KAT</text></g>
   <g id="arw"><path id="aL" stroke="#ff5a1f" stroke-width="10" stroke-linecap="round" fill="none"/><path id="aH" fill="#ff5a1f"/><text id="aT" font-size="44" fill="#ff5a1f" text-anchor="middle">+10</text></g>
'''

SCENE = r'''
const B=__B__; const END=B.END;
const P=[L(B.fiyat,B.ml,.23),L(B.fiyat,B.ml,.5),L(B.fiyat,B.ml,.73)];
window.V={sfx:[[0.02,'thud'],[B.start,'whoosh'],[P[0],'pop'],[P[1],'pop'],[P[2],'pop'],[B.ml+.1,'scratch'],[B.ml2+.1,'scratch'],[B.yirmi+.1,'drop'],[B.orta+.4,'pop'],[B.cunku+.3,'whoosh']]};
const LINES=[[B.start,B.fiyat-.1,'Kahveden<br><span class="o">diyorum.</span>'],
 [B.fiyat,B.ml-.1,'Küçük, orta,<br><span class="o">büyük.</span>'],
 [B.ml,B.ml2-.05,'Küçüğü <span class="o">355 ml</span>'],
 [B.ml2,B.yirmi-.05,'Büyüğü <span class="o">591 ml</span>'],
 [B.yirmi,B.orta-.1,'<span class="o">20 lira</span> farkla<br>bir buçuk katı.'],
 [B.orta,B.cunku-.1,'Ortadaki diyor ki:<br><span class="o">10 lira ver, geç.</span>'],
 [B.cunku,END-.45,'Çünkü soru<br><span class="o">hep aynı:</span>']];
const BIG=[[B.yirmi,B.orta-.1]], HITS=[0.02,B.yirmi+.1];
const FY=1262;
const SZ=[{h:210,t:128,b:94},{h:270,t:150,b:106},{h:345,t:174,b:120}], XS=[205,465,725];
const cup=(z,body,band)=>{const {h,t,b}=z;return `<g filter="url(#ps)"><path d="M${-b/2} 0 L${-t/2} ${-h} L${t/2} ${-h} L${b/2} 0Z" fill="${body}"/>`+
 `<path d="M${-L(b,t,.38)/2} ${-h*.38} L${-L(b,t,.66)/2} ${-h*.66} L${L(b,t,.66)/2} ${-h*.66} L${L(b,t,.38)/2} ${-h*.38}Z" fill="${band}"/>`+
 `<rect x="${-t/2-8}" y="${-h-24}" width="${t+16}" height="26" rx="6" fill="#243139"/><rect x="${-t/2+16}" y="${-h-38}" width="${t-32}" height="16" rx="5" fill="#243139"/></g>`};
['#e6dfcd','#e6dfcd','#FFF8EB'].forEach((c,i)=>$('c'+i).innerHTML=cup(SZ[i],c,i==2?'#ff5a1f':'#C56B50'));
const PR=[175,185,195];
$('tags').innerHTML=PR.map((v,i)=>`<g id="tg${i}" filter="url(#ps)"><rect x="-82" y="-32" width="164" height="64" fill="${i==2?'#ff5a1f':'#FFF8EB'}" stroke="#1c1b18" stroke-width="4"/><text id="tn${i}" y="14" text-anchor="middle" font-size="38" fill="${i==2?'#FFF8EB':'#1c1b18'}">${v}</text></g>`).join('');
function scene(t){
  // kanca: büyük bardak ortada, soruda kabarır
  const puff=(t>B.q&&t<B.start+.2)?ob(p(t,B.q+.1,.5))*(1-io(p(t,B.start-.35,.4))):0;
  const wob=(t>B.q+.7&&t<B.start-.3)?Math.sin((t-B.q-.7)*16)*4*Math.exp(-(t-B.q-.7)*2.5):0;
  const inK=oc(p(st(t),B.start,.6)), outK=io(p(st(t),B.cunku+.3,.6)), back=io(p(st(t),B.cunku+.5,.7));
  // büyük bardak: ortadan sağa, sonda ortaya döner
  const bx=L(L(470,XS[2],inK),470,back), bs=L(L(1.25,1,inK),1.25,back);
  const dim=io(p(t,B.orta,.4))*(1-io(p(t,B.cunku,.3)));
  const lean=io(p(t,B.orta+.2,.5))*(1-io(p(t,B.cunku,.3)));
  [0,1].forEach(i=>{const x=L(-260,XS[i],inK)+outK*1300;
    tr('c'+i,`translate(${x} ${FY}) rotate(${i==1?lean*13:0})`); op('c'+i,i==0?1-.6*dim:1)});
  tr('c2',`translate(${bx} ${FY}) rotate(${wob}) scale(${bs*(1+.06*puff)} ${bs*(1+.16*puff)})`);
  // buhar sadece soruda
  [0,1,2].forEach(i=>{const k=p(t,B.q+.3+i*.15,1.2), on=t>B.q+.3&&t<B.start; const x=bx-40+i*40, y0=FY-345*bs*(1+.16*puff)-60-k*120;
    $('s'+i).setAttribute('d',`M${x} ${y0} q 18 -25 0 -50 q -18 -25 0 -50`); $('s'+i).style.opacity=on?Math.sin(Math.PI*k):0});
  // fiyat etiketleri
  const out=io(p(t,B.cunku,.3));
  PR.forEach((v,i)=>{const k=ob(p(t,P[i],.35)); const x=(i==2?bx:L(-260,XS[i],inK)+outK*1300);
    tr('tg'+i,`translate(${x} ${FY+80}) rotate(${i-1}) scale(1 ${t>P[i]?k*(1-out):0})`);
    $('tn'+i).textContent=Math.round(L(0,v,oc(p(t,P[i],.5))))+' TL'; op('tg'+i,i==0?1-.6*dim:1)});
  // ml ölçüm çizgisi: önce küçük, sonra büyük
  const a1=io(p(t,B.ml+.1,.6)), a2=io(p(t,B.ml2+.1,.6)), mOff=io(p(t,B.yirmi-.2,.25));
  const useBig=t>=B.ml2, ci=useBig?2:0, cx=useBig?XS[2]:XS[0], hh=SZ[ci].h*(useBig?1:1), k=useBig?a2:a1;
  const mx=cx, y1=FY-14, y2=L(y1,FY-hh+18,k);
  $('mL').setAttribute('d',`M${mx} ${y1} L${mx} ${y2}`); $('mD').setAttribute('cx',mx); $('mD').setAttribute('cy',y2);
  const mon=t>B.ml+.1&&t<B.yirmi; [ 'mL','mD'].forEach(id=>op(id,mon?1-mOff:0));
  $('mT').textContent=useBig?'591 ml':'355 ml'; $('mT').setAttribute('x',mx+(useBig?-62:85)); $('mT').setAttribute('y',useBig?FY-hh-62:y2-6); op('mT',mon?k*(1-mOff):0);
  // +20 TL yatay çizgi ve damga
  const h1=io(p(t,B.yirmi,.5)), hOff=io(p(t,B.orta,.3)); const hy=FY-450, hx0=XS[0], hx1=L(hx0,XS[2],h1);
  $('hL').setAttribute('d',`M${hx0} ${hy} L${hx1} ${hy}`); $('hD').setAttribute('cx',hx1); $('hD').setAttribute('cy',hy);
  const hon=t>B.yirmi&&t<B.orta+.3; ['hL','hD'].forEach(id=>op(id,hon?1-hOff:0));
  $('hT').textContent='+20 TL'; $('hT').setAttribute('x',(XS[0]+XS[2])/2); $('hT').setAttribute('y',hy-30); op('hT',hon?h1*(1-hOff):0);
  const sk=ob(p(t,B.yirmi+.7,.35)), sOut=io(p(t,B.orta,.3));
  tr('stamp',`translate(${XS[2]} ${FY-470}) rotate(-8) scale(${t>B.yirmi+.7?sk*(1-sOut):0})`);
  // ortadan büyüğe ok: +10
  const ak=io(p(t,B.orta+.6,.5)), aOff=io(p(t,B.cunku,.3)); const ay=FY-330, ax0=XS[1]+40, ax1=L(ax0,XS[2]-70,ak);
  $('aL').setAttribute('d',`M${ax0} ${ay} Q ${(ax0+ax1)/2} ${ay-90*ak} ${ax1} ${ay}`);
  $('aH').setAttribute('d',`M${ax1+22} ${ay} L${ax1-8} ${ay-20} L${ax1-8} ${ay+20}Z`);
  $('aT').setAttribute('x',(XS[1]+XS[2])/2); $('aT').setAttribute('y',ay-80);
  op('arw',t>B.orta+.6&&t<B.cunku+.3?(ak>0?1:0)*(1-aOff):0); op('aT',ak);
}
'''.replace('__B__', json.dumps(B))

build('/home/claude/kasaonu-medya/referans/sablonlar/boy01/index.html', 'KAHVE · 01', 'FİŞ 0006', 'FARK', '10 TL',
      'Hep büyüğünü', 'mü alırsın?', SVG, SCENE)
print('ok')

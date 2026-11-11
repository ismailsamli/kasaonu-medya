from base import build
import json, sys

B = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {
    "q": 1.2, "start": 2.6, "egik": 4.9, "sabah": 6.9, "yetmis": 10.0, "tam": 13.8, "uzan": 15.9, "el": 17.7, "bu": 20.6, "END": 23.2}

SVG = r'''
   <g transform="translate(470 1262) scale(1.3) translate(-470 -1262)">
   <g id="minis"></g>
   <path id="same" stroke="#8c8880" stroke-width="5" stroke-dasharray="18 14" fill="none"/>
   <g id="lap" filter="url(#ps)">
     <rect x="330" y="1226" width="300" height="22" rx="6" fill="#243139"/>
     <rect x="380" y="1218" width="210" height="8" rx="3" fill="#8c8880"/>
     <g id="lid"><rect x="0" y="-16" width="285" height="16" rx="6" fill="#243139"/><rect x="12" y="-2" width="258" height="6" rx="2" fill="#7C9DA5"/>
       <g id="phone"><rect x="70" y="-34" width="110" height="20" rx="5" fill="#1c1b18"/><rect x="78" y="-31" width="94" height="14" rx="3" fill="#E8B65C"/><circle id="bub" cx="125" cy="-24" r="6" fill="#FFF8EB"/></g>
     </g>
   </g>
   <path id="arc" stroke="#1c1b18" stroke-width="9" stroke-linecap="round" fill="none"/><circle id="arcD" r="12" fill="#ff5a1f"/>
   <text id="arcT" font-size="46" text-anchor="middle" fill="#1c1b18"></text>
   <g id="head" filter="url(#ps)"><circle cx="0" cy="0" r="62" fill="#e9c9a6"/><path d="M-60 -6 Q-66 -76 4 -72 Q60 -70 62 -30 L18 -32 Q-14 -34 -22 6Z" fill="#243139"/><circle cx="-30" cy="2" r="7" fill="#243139"/></g>
   <path id="sight" stroke="#8c8880" stroke-width="5" stroke-dasharray="4 14" stroke-linecap="round" fill="none"/>
   <g id="hand"><path id="arm" stroke="#a95a43" stroke-width="58" stroke-linecap="round" fill="none" filter="url(#ps)"/><circle id="palm" r="30" fill="#e9c9a6" filter="url(#ps)"/></g>
   </g>
   <g id="own" filter="url(#ps)"><rect x="-98" y="-36" width="196" height="72" fill="#ff5a1f" stroke="#1c1b18" stroke-width="5"/><text y="15" font-size="40" fill="#FFF8EB" text-anchor="middle">SENİN</text></g>
'''

SCENE = r'''
const B=__B__; const END=B.END; B.s76=L(B.yetmis,B.tam,.5);
window.V={sfx:[[0.02,'thud'],[B.start,'whoosh'],[B.egik+.1,'pop'],[B.sabah+.2,'ticks'],[B.yetmis+.1,'scratch'],[B.s76,'drop'],[B.tam+.1,'scratch'],[B.uzan,'whoosh'],[B.el+.35,'pop'],[B.el+.9,'drop'],[B.bu+.3,'whoosh']]};
const LINES=[[B.start,B.egik-.1,'Apple mağazasındaki<br><span class="o">laptoplar.</span>'],
 [B.egik,B.sabah-.1,'Hepsi aynı açıyla<br><span class="o">eğik.</span>'],
 [B.sabah,B.yetmis-.1,'Her sabah<br><span class="o">su terazisiyle.</span>'],
 [B.yetmis,B.s76-.05,'Önce <span class="o">70°</span>'],
 [B.s76,B.tam-.1,'Sonra <span class="o">76°</span>'],
 [B.tam,B.uzan-.1,'Tam göremeyeceğin<br><span class="o">kadar eğik.</span>'],
 [B.uzan,B.el-.1,'Düzeltmek için<br><span class="o">uzanıyorsun.</span>'],
 [B.el,B.bu-.1,'Bir değdi mi,<br><span class="o">artık senin.</span>'],
 [B.bu,END-.45,'İçeri giren herkese<br><span class="o">aynı soru:</span>']];
const BIG=[[B.s76,B.tam-.1]], HITS=[0.02,B.s76];
const FY=1262, HX=330, HY=1226;
const mini=(x)=>`<g transform="translate(${x} ${FY}) scale(.5)" filter="url(#ps)"><rect x="0" y="-36" width="300" height="22" rx="6" fill="#243139"/><g transform="translate(0 -36) rotate(-70)"><rect x="0" y="-16" width="285" height="16" rx="6" fill="#243139"/></g></g>`;
$('minis').innerHTML=mini(-10)+mini(150);
function scene(t){
  // açı: 70 -> 76, dokununca 105, sonda yine 70
  let th=70+6*io(p(t,B.s76,.5))*(1-io(p(t,B.bu+.2,.6)));
  const open=io(p(st(t),B.el+.45,.6))*(1-io(p(st(t),B.bu+.3,.6))); th+=(105-th)*open;
  // laptop girişi
  const inK=oc(p(st(t),B.start,.6));
  
  tr('lid',`translate(${HX} ${HY}) rotate(${-th})`);
  // minyatürler + aynı açı çizgisi
  const mIn=oc(p(st(t),B.egik,.5)), mOut=io(p(t,B.sabah+.2,.4))*(1-0);
  tr('minis',`translate(${-420*(1-mIn)} 0)`); op('minis',(t>B.egik?1:0)*(1-.55*io(p(t,B.sabah,.4)))*(1-io(p(t,B.bu,.4))));
  const sk=io(p(t,B.egik+.3,.6)), sOff=io(p(t,B.sabah,.3)); const a=-70*R, len=L(0,900,sk);
  $('same').setAttribute('d',`M${-5} ${FY-18+40} L${-5+len*Math.cos(a)*0+len} ${FY-18+40}`);
  $('same').setAttribute('d',[ -10,150,HX/1].map((x,i)=>{const hx=i<2?x:HX, hy=i<2?FY-18:HY, l=(i<2?142:285)*sk;return `M${hx} ${hy} L${hx+l*Math.cos(a)} ${hy+l*Math.sin(a)}`}).join(' '));
  op('same',(t>B.egik+.3?1:0)*(1-sOff)*.9);
  // su terazisi telefonu
  const ph=ob(p(t,B.sabah+.1,.4)), phOut=io(p(t,B.yetmis+.1,.3));
  const bx=125+28*Math.sin((t-B.sabah)*9)*Math.exp(-(t-B.sabah)*1.6);
  $('bub').setAttribute('cx',bx); tr('phone',`translate(0 ${-30*(1-ph)})`); op('phone',(t>B.sabah+.1?ph:0)*(1-phOut));
  // açı yayı
  const ak=io(p(t,B.yetmis+.1,.6)), aOff=io(p(t,B.tam-.2,.3)), r=150, th2=th*ak;
  const ex=HX+r*Math.cos(-th2*R), ey=HY+r*Math.sin(-th2*R);
  $('arc').setAttribute('d',`M${HX+r} ${HY} A ${r} ${r} 0 0 0 ${ex} ${ey}`); $('arcD').setAttribute('cx',ex); $('arcD').setAttribute('cy',ey);
  const aon=t>B.yetmis+.1&&t<B.tam; ['arc','arcD'].forEach(i=>op(i,aon?1-aOff:0));
  const lt=t>=B.s76?'76°':'70°'; if($('arcT').textContent!==lt)$('arcT').textContent=lt;
  $('arcT').setAttribute('x',HX+235*Math.cos(-th2/2*R)); $('arcT').setAttribute('y',HY+235*Math.sin(-th2/2*R)+16);
  $('arcT').setAttribute('fill',t>=B.s76?'#ff5a1f':'#1c1b18'); op('arcT',aon?ak*(1-aOff):0);
  // kafa ve bakış: ekranı göremiyor
  const hd=oc(p(st(t),B.tam,.5)), hdOut=io(p(st(t),B.el+1.2,.5));
  tr('head',`translate(${L(1200,820,hd*(1-hdOut))} ${FY-430})`);
  const sv=io(p(t,B.tam+.4,.5)), sOff2=io(p(t,B.uzan,.3));
  const lc=[HX+200*Math.cos(-th*R)+14, HY+200*Math.sin(-th*R)+10];
  $('sight').setAttribute('d',`M${790} ${FY-430} L${L(790,lc[0],sv)} ${L(FY-430,lc[1],sv)}`); op('sight',(t>B.tam+.4?1:0)*(1-sOff2));
  // el: kancada yaklaşır-kaçar, uzan'da uzanır, değer, sonra çekilir
  const tease=(t>B.q&&t<B.start+.2)?Math.sin(Math.PI*p(t,B.q+.1,B.start-B.q))*(.55+.08*Math.sin(t*14)):0;
  const reach=io(p(st(t),B.uzan+.1,.9))*(1-io(p(st(t),B.bu+.2,.6)));
  const tip=[HX+272*Math.cos(-th*R)+10, HY+272*Math.sin(-th*R)+14];
  let k=Math.max(tease,reach); const sx=1060, sy=FY-250;
  const hx=L(sx+80,tip[0]+22,k), hy=L(sy,tip[1]+8,k);
  $('arm').setAttribute('d',`M${sx+140} ${sy+40} L${hx+20} ${hy+6}`); $('palm').setAttribute('cx',hx); $('palm').setAttribute('cy',hy);
  op('hand',k>0.001?1:0);
  // SENİN etiketi
  const ow=ob(p(t,B.el+.9,.4)), owOut=io(p(t,B.bu,.3));
  tr('own',`translate(${470+(HX+150-470)*1.3} ${1262+(FY-560-1262)*1.3}) rotate(-6) scale(${t>B.el+.9?ow*(1-owOut):0})`);
}
'''.replace('__B__', json.dumps(B))

build('/home/claude/kasaonu-medya/referans/sablonlar/egik01/index.html', 'MAĞAZA · 02', 'FİŞ 0007', 'AÇI', '76°',
      'Sen de', 'dokundun mu?', SVG, SCENE)
print('ok')

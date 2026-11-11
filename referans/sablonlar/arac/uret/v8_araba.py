from base import build
import json, sys

B = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {
    "q": 1.2, "start": 3.8, "ilk": 5.2, "cunku": 7.6, "sonra": 12.2, "deneme": 13.6, "uc": 19.2, "dolunca": 21.6, "araba": 23.0, "END": 26.4}

SVG = r'''
   <g id="cart"><g filter="url(#ps)">
     <path d="M-230 -330 L230 -330 L190 -110 L-190 -110Z" fill="#7C9DA5"/>
     <g stroke="#5f7d85" stroke-width="5"><path d="M-150 -330 L-130 -110 M-70 -330 L-65 -110 M10 -330 L5 -110 M90 -330 L75 -110 M170 -330 L145 -110 M-222 -260 L216 -260 M-208 -185 L203 -185"/></g>
     <path d="M-230 -330 L-290 -390 L-330 -390" stroke="#243139" stroke-width="16" fill="none" stroke-linecap="round"/>
     <path d="M-190 -110 L-170 -40 L190 -40 L190 -110" stroke="#243139" stroke-width="12" fill="none"/>
     <circle cx="-150" cy="-20" r="20" fill="#1c1b18"/><circle cx="160" cy="-20" r="20" fill="#1c1b18"/></g>
     <g id="items"></g></g>
   <g id="bask" filter="url(#ps)"><path d="M-110 -150 L110 -150 L90 0 L-90 0Z" fill="#C56B50"/><path d="M-80 -150 Q0 -260 80 -150" stroke="#243139" stroke-width="12" fill="none"/>
     <g id="bitems"></g></g>
   <g id="yr" filter="url(#ps)"><rect x="-120" y="-50" width="240" height="100" fill="#FFF8EB" stroke="#1c1b18" stroke-width="5"/><text y="20" font-size="58" text-anchor="middle" fill="#1c1b18">1937</text></g>
   <g id="done" filter="url(#ps)"><circle r="58" fill="#ff5a1f" stroke="#1c1b18" stroke-width="5"/><path d="M-26 2 l18 18 l36 -40" stroke="#FFF8EB" stroke-width="12" fill="none" stroke-linecap="round"/></g>
   <g id="cnt"></g>
'''

SCENE = r'''
const B=__B__; const END=B.END; const FULL=L(B.cunku,B.sonra,.55);
window.V={sfx:[[0.02,'thud'],[B.q+.3,'whoosh'],[B.start,'pop'],[B.ilk+.2,'drop'],[B.cunku+.3,'pop'],[B.cunku+.7,'pop'],[B.cunku+1.1,'pop'],[FULL+.2,'thud'],[B.sonra+.2,'whoosh'],[B.deneme+1,'ticks'],[L(B.deneme,B.uc,.75),'pop'],[B.uc+.3,'whoosh'],[B.dolunca+.3,'thud'],[B.araba+.3,'whoosh']]};
const LINES=[[B.start,B.ilk-.1,'Market<br><span class="o">arabası.</span>'],
 [B.ilk,B.cunku-.1,'İlk araba:<br><span class="o">1937.</span>'],
 [B.cunku,B.sonra-.1,'Sepet dolunca<br><span class="o">alışveriş biter.</span>'],
 [B.sonra,B.deneme-.1,'Sonra arabalar<br><span class="o">büyüdü.</span>'],
 [B.deneme,B.uc-.1,'Araba 2 kat:<br><span class="o">5 değil 7 ürün.</span>'],
 [B.uc,B.dolunca-.1,'3 şey alacaksan<br><span class="o">sepet al.</span>'],
 [B.dolunca,B.araba-.1,'Sepet dolunca<br><span class="o">durursun.</span>'],
 [B.araba,END-.45,'Araba ise<br><span class="o">hep fısıldar:</span>']];
const BIG=[[B.deneme,B.uc-.1]], HITS=[0.02,FULL+.2,L(B.deneme,B.uc,.75)];
const FY=1262, C=['#E8B65C','#8A9B7C','#C56B50','#E8B65C','#8A9B7C','#ff5a1f','#ff5a1f'];
const IP=[[-150,-200],[-60,-210],[30,-195],[120,-205],[-110,-290],[-20,-300],[70,-290]];
$('items').innerHTML=IP.map((p,i)=>`<g id="it${i}" filter="url(#ps)"><rect x="${p[0]-36}" y="${p[1]-80}" width="72" height="${80+(i%3)*14}" fill="${C[i]}"/><rect x="${p[0]-22}" y="${p[1]-56}" width="44" height="26" fill="#FFF8EB"/></g>`).join('');
const BP=[[-55,-30],[0,-40],[55,-30],[-30,-100],[30,-100]];
$('bitems').innerHTML=BP.map((p,i)=>`<rect id="bi${i}" x="${p[0]-26}" y="${p[1]-70}" width="52" height="70" fill="${C[i]}"/>`).join('');
$('cnt').innerHTML=[0,1,2,3,4,5,6].map(i=>`<g id="ct${i}" filter="url(#ps)"><rect x="${130+i*100}" y="1110" width="76" height="96" fill="${i>4?'#ff5a1f':'#e6dfcd'}" stroke="#1c1b18" stroke-width="4"/></g>`).join('');
function scene(t){
  // araba: kancada büyür ve dolar; sonra'da tekrar büyür; uc'ta çekilir; araba'da geri gelir
  const hookG=(t>B.q&&t<B.start+.3)?Math.sin(Math.PI*p(t,B.q+.1,B.start-B.q+.2)):0;
  const gro=io(p(st(t),B.sonra+.1,.7))*(1-io(p(st(t),B.uc,.5)));
  const away=io(p(st(t),B.ilk,.5))*(1-io(p(st(t),B.sonra,.5))) + io(p(st(t),B.uc,.5))*(1-io(p(st(t),B.araba,.6)));
  const cs=(1+.45*hookG)*(1+.35*gro)*(1-.0*away);
  const cx=L(470,1400,cl(away)), cy=FY;
  tr('cart',`translate(${cx} ${cy}) scale(${cs*.95})`);
  // eşya sayısı: başta 3, kancada 7'ye dolar
  let n=3+Math.round(4*hookG); if(t>B.deneme) n=7; if(t>B.uc+.5) n=3;
  if(t>=B.sonra&&t<B.deneme) n=5;
  IP.forEach((p,i)=>op('it'+i,i<n?1:0));
  // sepet: ilk'te gelir, dolar, uc'ta tekrar
  const bIn=oc(p(st(t),B.ilk+.1,.5))*(1-io(p(st(t),B.sonra,.4))) + oc(p(st(t),B.uc+.2,.5))*(1-io(p(st(t),B.araba,.4)));
  tr('bask',`translate(${L(-300,470,cl(bIn))} ${FY}) scale(1.4)`);
  let bn=0; if(t>B.cunku+.3&&t<B.sonra) bn=Math.min(5,1+Math.floor((t-B.cunku-.3)/.4)); if(t>B.uc+.6&&t<B.araba) bn=Math.min(3,1+Math.floor((t-B.uc-.6)/.4)); if(t>B.dolunca+.1&&t<B.araba) bn=5;
  BP.forEach((p,i)=>op('bi'+i,i<bn?1:0));
  const yk=ob(p(t,B.ilk+.2,.35)), yOut=io(p(t,B.cunku,.3)); tr('yr',`translate(470 760) rotate(-4) scale(${t>B.ilk+.2?yk*(1-yOut):0})`);
  const dk=t>FULL+.2&&t<B.sonra?ob(p(t,FULL+.2,.35)):(t>B.dolunca+.3&&t<B.araba?ob(p(t,B.dolunca+.3,.35)):0);
  tr('done',`translate(640 ${FY-300}) scale(${dk})`);
  // sayaç: 5 + 2 turuncu
  const cOut=io(p(t,B.uc,.3));
  [0,1,2,3,4,5,6].forEach(i=>{const a=i<5?B.deneme+.6+i*.12:L(B.deneme,B.uc,.75)+(i-5)*.2; const k=ob(p(t,a,.3)); tr('ct'+i,`translate(0 ${-590+(1-k)*60})`); op('ct'+i,(t>a?1:0)*(1-cOut))});
}
'''.replace('__B__', json.dumps(B))

build('/home/claude/kasaonu-medya/referans/sablonlar/araba01/index.html', 'ARABA · 08', 'FİŞ 0013', 'FAZLADAN', '2 ÜRÜN',
      'Büyüdükçe daha çok', 'dolduruyorsun?', SVG, SCENE)
print('ok')

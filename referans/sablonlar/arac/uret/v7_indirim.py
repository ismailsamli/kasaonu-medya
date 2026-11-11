from base import build
import json, sys

B = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {
    "q": 1.2, "start": 3.6, "bin": 4.7, "kural": 10.0, "agustos": 11.6, "ceza": 16.4, "yani": 18.6, "sepet": 23.4, "END": 26.2}

SVG = r'''
   <g id="tagW"><g id="tag" filter="url(#ps)">
     <path d="M-230 -150 L170 -150 L250 0 L170 150 L-230 150Z" fill="#FFF8EB" stroke="#1c1b18" stroke-width="6"/><circle cx="170" cy="0" r="16" fill="#f3efe4" stroke="#1c1b18" stroke-width="5"/>
     <text id="old" x="-20" y="-48" font-size="48" fill="#8c8880" text-anchor="middle"></text><path id="oldS" stroke="#1c1b18" stroke-width="8" stroke-linecap="round"/>
     <text id="pr" x="-20" y="66" font-size="74" fill="#1c1b18" text-anchor="middle">1.000 TL</text>
   </g></g>
   <g id="ban" filter="url(#ps)"><rect x="-200" y="-46" width="400" height="92" fill="#ff5a1f" stroke="#1c1b18" stroke-width="5"/><text y="18" font-size="52" fill="#FFF8EB" text-anchor="middle" letter-spacing="6">İNDİRİM!</text></g>
   <g id="cal"></g>
   <path id="calL" stroke="#1c1b18" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/><circle id="calD" r="12" fill="#ff5a1f"/>
   <text id="calT" font-size="30" fill="#ff5a1f" text-anchor="middle">EN DÜŞÜK</text>
   <g id="fine" filter="url(#ps)"><rect x="-210" y="-80" width="420" height="160" fill="#ff5a1f" stroke="#1c1b18" stroke-width="6"/><text y="-12" font-size="46" fill="#FFF8EB" text-anchor="middle" letter-spacing="5">CEZA</text><text y="50" font-size="40" fill="#1c1b18" text-anchor="middle">≈ 40 MİLYON TL</text></g>
   <g id="xx"><path d="M-70 -70 L70 70 M70 -70 L-70 70" stroke="#ff5a1f" stroke-width="18" stroke-linecap="round"/></g>
'''

SCENE = r'''
const B=__B__; const END=B.END;
const P1=L(B.bin,B.kural,.25), P2=L(B.bin,B.kural,.55), P3=L(B.bin,B.kural,.72);
window.V={sfx:[[0.02,'thud'],[B.q+.2,'whoosh'],[B.start,'pop'],[P1,'ticks'],[P2,'scratch'],[P3,'thud'],[B.agustos+.2,'ticks'],[L(B.ceza,B.yani,.35),'thud'],[B.yani+.6,'drop'],[B.sepet+.3,'whoosh']]};
const LINES=[[B.start,B.bin-.1,'Fiyatı<br><span class="o">diyorum.</span>'],
 [B.bin,P2-.05,'Önce<br><span class="o">şişir...</span>'],
 [P2,B.kural-.1,'...sonra<br><span class="o">"indirim".</span>'],
 [B.kural,B.agustos-.1,'Bu oyunun artık<br><span class="o">kuralı var.</span>'],
 [B.agustos,B.ceza-.1,'Eski fiyat =<br><span class="o">son 10 günün en düşüğü</span>'],
 [B.ceza,B.yani-.1,'Uymayana<br><span class="o">~40 milyon ceza.</span>'],
 [B.yani,B.sepet-.1,'10 günde görmediysen<br><span class="o">indirim değil.</span>'],
 [B.sepet,END-.45,'Sepete atmadan<br><span class="o">bir kere sor:</span>']];
const BIG=[[B.agustos,B.ceza-.1]], HITS=[0.02,P3,L(B.ceza,B.yani,.35)];
const PX=[1000,1000,950,1000,1000,980,1000,1000,1000,1000];
$('cal').innerHTML=PX.map((v,i)=>`<g id="d${i}"><rect x="${110+i*72}" y="1080" width="60" height="60" rx="8" fill="${i==2?'#E8B65C':'#FFF8EB'}" stroke="#1c1b18" stroke-width="4"/><text x="${140+i*72}" y="1122" font-size="24" text-anchor="middle" fill="#1c1b18">${i+1}</text></g>`).join('');
function scene(t){
  // kanca: etiket balon gibi şişer
  const inf=(t>B.q&&t<B.start+.3)?Math.sin(Math.PI*p(t,B.q+.1,B.start-B.q+.2)):0;
  const wob=inf*4*Math.sin(t*16);
  const kural=io(p(t,B.kural,.5))*(1-io(p(t,B.sepet,.5)));
  const ty=L(820,760,kural), ts=L(1,.72,kural);
  tr('tagW',`translate(470 ${ty}) scale(${ts*(1+.35*inf)} ${ts*(1+.28*inf)}) rotate(${wob})`);
  // bin'de: 1.500 sayar, üstü çizilir, altında 1.000 indirimli
  const up=oc(p(t,P1,.5));
  const showOld=t>=P1&&t<B.sepet;
  $('old').textContent=showOld?Math.round(L(1000,1500,up)).toLocaleString('tr-TR')+' TL':'';
  const sk=io(p(t,P2,.4)); $('oldS').setAttribute('d',`M-170 -66 L${L(-170,130,sk)} -66`); op('oldS',t>P2&&t<B.sepet?1:0);
  $('pr').textContent='1.000 TL'; op('pr',(t<P1||t>=P2)?1:0.15);
  $('pr').setAttribute('fill',t>=P3&&t<B.sepet?'#ff5a1f':'#1c1b18');
  const bk=ob(p(t,P3,.35)), bOut=io(p(t,B.kural,.3));
  tr('ban',`translate(470 ${560}) rotate(-6) scale(${t>P3?bk*(1-bOut):0})`);
  // 10 günlük takvim + çizgi
  const ck=p(t,B.agustos+.2,1.6), cOut=io(p(t,B.yani,.3));
  PX.forEach((v,i)=>{const k=ob(p(t,B.agustos+.1+i*.06,.3)); tr('d'+i,`translate(0 ${(1-k)*60})`); op('d'+i,(t>B.agustos+.1+i*.06?1:0)*(1-cOut))});
  const pts=PX.map((v,i)=>[140+i*72,1040-(v-940)*1.2]); const n=Math.max(1,Math.ceil(ck*pts.length));
  $('calL').setAttribute('d','M'+pts.slice(0,n).map(p=>p.join(' ')).join(' L')); const lp=pts[n-1];
  $('calD').setAttribute('cx',lp[0]); $('calD').setAttribute('cy',lp[1]);
  const con=t>B.agustos+.2&&t<B.yani+.3; ['calL','calD'].forEach(i=>op(i,con?1-cOut:0));
  $('calT').setAttribute('x',pts[2][0]); $('calT').setAttribute('y',1180); op('calT',con&&ck>.4?1-cOut:0);
  // ceza damgası
  const fs=L(B.ceza,B.yani,.35), fp=p(t,fs-.12,.12), fOut=io(p(t,B.yani,.3));
  tr('fine',`translate(470 1110) rotate(-6) scale(${t>fs-.12?L(2,1,io(fp))*(1-fOut):0})`);
  // yani: eski fiyata çarpı
  const xk=ob(p(t,B.yani+.6,.35)), xOut=io(p(t,B.sepet,.3));
  tr('xx',`translate(${470-20*ts} ${ty-50*ts}) scale(${t>B.yani+.6?xk*(1-xOut):0})`);
}
'''.replace('__B__', json.dumps(B))

build('/home/claude/kasaonu-medya/referans/sablonlar/indirim01/index.html', 'İNDİRİM · 07', 'FİŞ 0012', 'KURAL', '10 GÜN',
      'Seni de önce şişirip', 'sonra mı indirdiler?', SVG, SCENE)
print('ok')

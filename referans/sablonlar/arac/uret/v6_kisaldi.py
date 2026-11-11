from base import build
import json, sys

B = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {
    "q": 1.2, "start": 2.8, "kur": 4.6, "eni": 8.2, "rulo": 12.6, "paket": 15.6, "birim": 18.6, "etiket": 23.0, "END": 27.0}

SVG = r'''
   <g id="roll">
     <rect x="250" y="760" width="440" height="16" rx="8" fill="#243139"/>
     <path id="sheet" fill="#FFF8EB" filter="url(#ps)"/>
     <g filter="url(#ps)"><rect x="330" y="680" width="280" height="190" rx="40" fill="#FFF8EB"/><rect x="330" y="740" width="280" height="6" fill="#e6dfcd"/><rect x="330" y="800" width="280" height="6" fill="#e6dfcd"/></g>
     <path id="perf" stroke="#b9b4a8" stroke-width="4" stroke-dasharray="6 10"/>
   </g>
   <g id="ztag" filter="url(#ps)"><rect x="-120" y="-44" width="240" height="88" fill="#ff5a1f" stroke="#1c1b18" stroke-width="5"/><text y="14" font-size="38" fill="#FFF8EB" text-anchor="middle">ZAM YOK</text></g>
   <g id="leaf"><rect id="lf" fill="#FFF8EB" filter="url(#ps)"/><path id="wL" stroke="#1c1b18" stroke-width="9" stroke-linecap="round"/><circle id="wD" r="12" fill="#ff5a1f"/><text id="wT" font-size="40" text-anchor="middle" fill="#1c1b18"></text>
     <path id="hL" stroke="#1c1b18" stroke-width="9" stroke-linecap="round"/><circle id="hD" r="12" fill="#ff5a1f"/><text id="hT" font-size="40" text-anchor="start" fill="#1c1b18"></text></g>
   <g id="xsec" filter="url(#ps)"><circle id="xo" cx="470" cy="900" r="190" fill="#FFF8EB"/><circle cx="470" cy="900" r="150" fill="none" stroke="#e6dfcd" stroke-width="4"/><circle cx="470" cy="900" r="115" fill="none" stroke="#e6dfcd" stroke-width="4"/><circle id="core" cx="470" cy="900" r="60" fill="#C56B50"/><circle id="hole" cx="470" cy="900" r="40" fill="#f3efe4"/></g>
   <path id="cL" stroke="#ff5a1f" stroke-width="9" stroke-linecap="round"/><text id="cT" font-size="38" fill="#ff5a1f" text-anchor="middle"></text>
   <g id="pack" filter="url(#ps)"><rect x="250" y="760" width="440" height="300" rx="20" fill="#7C9DA5"/><g fill="#FFF8EB"><circle cx="360" cy="860" r="70"/><circle cx="580" cy="860" r="70"/><circle cx="360" cy="980" r="0"/></g><rect x="300" y="960" width="340" height="60" fill="#FFF8EB"/><text x="470" y="1002" font-size="34" text-anchor="middle" fill="#1c1b18">AYNI PAKET</text></g>
   <g id="shelf" filter="url(#ps)"><rect x="-230" y="-110" width="460" height="220" fill="#FFF8EB" stroke="#1c1b18" stroke-width="5"/>
     <text x="-200" y="-56" font-size="30" fill="#1c1b18">TUVALET KAĞIDI</text><text x="190" y="40" font-size="70" fill="#1c1b18" text-anchor="end">FİYAT</text>
     <text id="unit" x="-200" y="84" font-size="26" fill="#8c8880">BİRİM FİYAT</text></g>
   <ellipse id="ring" fill="none" stroke="#ff5a1f" stroke-width="7"/>
'''

SCENE = r'''
const B=__B__; const END=B.END; const BOY=L(B.eni,B.rulo,.45);
window.V={sfx:[[0.02,'thud'],[B.q+.3,'scratch'],[B.start,'whoosh'],[B.kur+.3,'pop'],[B.eni+.2,'scratch'],[BOY+.1,'scratch'],[B.rulo+.2,'whoosh'],[B.rulo+1,'drop'],[B.paket+.2,'pop'],[B.birim+.3,'whoosh'],[B.birim+1.2,'pop'],[B.etiket+.3,'whoosh']]};
const LINES=[[B.start,B.kur-.1,'Tuvalet<br><span class="o">kağıdı.</span>'],
 [B.kur,B.eni-.1,'Zam yerine<br><span class="o">yaprak küçüldü.</span>'],
 [B.eni,BOY-.05,'Eni: 10 cm<br><span class="o">→ 9,5 cm</span>'],
 [BOY,B.rulo-.1,'Boyu: 12,5 cm<br><span class="o">→ 12,3 cm</span>'],
 [B.rulo,B.paket-.1,'Rulonun içi<br><span class="o">genişledi.</span>'],
 [B.paket,B.birim-.1,'Paket aynı, fiyat aynı,<br><span class="o">kağıt az.</span>'],
 [B.birim,B.etiket-.1,'Fiyata değil<br><span class="o">birim fiyata bak.</span>'],
 [B.etiket,END-.45,'Etiket söylemez,<br><span class="o">rulo söyler:</span>']];
const BIG=[[B.eni,B.rulo-.1]], HITS=[0.02,B.rulo+1];
const show=(id,a,b,base='')=>{const k=ob(p(t_,a,.35)),o=io(p(t_,b,.3));const s=t_>a&&t_<b+.35?k*(1-o):0;tr(id,`${base} translate(470 900) scale(${s}) translate(-470 -900)`);return s};
let t_=0;
function scene(t){ t_=t;
  // rulo ve sarkan yaprak: kancada kısalır, sonra eski haline döner
  const shr=(t>B.q&&t<B.start+.4)?Math.sin(Math.PI*p(t,B.q+.1,B.start-B.q+.2)):0;
  const len=440-230*shr+(shr>0?10*Math.sin(t*18)*shr:0);
  $('sheet').setAttribute('d',`M560 860 L610 860 L606 ${860+len} L556 ${860+len-8}Z`);
  $('perf').setAttribute('d',`M558 ${860+len*.5} L608 ${860+len*.5}`);
  const rollOn=(t<B.eni)||(t>=B.etiket); const rIn=t<B.eni?1-io(p(t,B.eni-.3,.3)):io(p(t,B.etiket,.4));
  tr('roll',`translate(470 900) scale(${rIn}) translate(-470 -900)`); op('roll',rollOn?1:0);
  const zk=ob(p(t,B.kur+.3,.35)), zOut=io(p(t,B.eni-.3,.3));
  tr('ztag',`translate(720 1120) rotate(-8) scale(${t>B.kur+.3?zk*(1-zOut):0})`);
  // tek yaprak ölçümü
  const ls=show('leaf',B.eni,B.rulo);
  const w=L(400,380,io(p(t,B.eni+.6,.6))), h=L(500,492,io(p(t,BOY+.3,.6))), x=470-w/2, y=900-h/2;
  $('lf').setAttribute('x',x); $('lf').setAttribute('y',y); $('lf').setAttribute('width',w); $('lf').setAttribute('height',h);
  const wk=io(p(t,B.eni+.1,.5)); $('wL').setAttribute('d',`M${x} ${y-40} L${x+w*wk} ${y-40}`); $('wD').setAttribute('cx',x+w*wk); $('wD').setAttribute('cy',y-40);
  $('wT').textContent=t>B.eni+.9?'9,5 cm':'10 cm'; $('wT').setAttribute('x',470); $('wT').setAttribute('y',y-64); $('wT').setAttribute('fill',t>B.eni+.9?'#ff5a1f':'#1c1b18');
  const hk=io(p(t,BOY,.5)); $('hL').setAttribute('d',`M${x+w+40} ${y} L${x+w+40} ${y+h*hk}`); $('hD').setAttribute('cx',x+w+40); $('hD').setAttribute('cy',y+h*hk);
  $('hT').textContent=t>BOY+.6?'12,3':'12,5'; $('hT').setAttribute('x',x+w+58); $('hT').setAttribute('y',900); $('hT').setAttribute('fill',t>BOY+.6?'#ff5a1f':'#1c1b18'); op('hT',hk); op('hL',hk); op('hD',hk);
  // kesit: göbek büyür
  show('xsec',B.rulo,B.paket);
  const ck=io(p(t,B.rulo+.6,.8)); $('core').setAttribute('r',60+50*ck); $('hole').setAttribute('r',40+50*ck);
  $('cL').setAttribute('d',`M${470-60} 900 L${470-60-50*ck} 900 M${470+60} 900 L${470+60+50*ck} 900`); op('cL',t>B.rulo+.6&&t<B.paket?1:0);
  $('cT').textContent='göbek büyüdü'; $('cT').setAttribute('x',470); $('cT').setAttribute('y',1190); op('cT',t>B.rulo+.6&&t<B.paket?ck:0);
  // paket
  show('pack',B.paket,B.birim);
  // raf etiketi + birim fiyat halkası
  const sk=ob(p(t,B.birim,.35)), sOut=io(p(t,B.etiket,.3));
  tr('shelf',`translate(470 900) rotate(-2) scale(${t>B.birim?sk*(1-sOut)*1.15:0})`);
  const rg=t>B.birim+1.2&&t<B.etiket+.3?ob(p(t,B.birim+1.2,.35))*(1-sOut):0;
  $('ring').setAttribute('cx',470-90*1.15+20); $('ring').setAttribute('cy',900+76*1.15); $('ring').setAttribute('rx',190*rg); $('ring').setAttribute('ry',38*rg);
}
'''.replace('__B__', json.dumps(B))

build('/home/claude/kasaonu-medya/referans/sablonlar/kisaldi01/index.html', 'RULO · 06', 'FİŞ 0011', 'YAPRAK', '9,5 CM',
      'Seninki de mi', 'kısaldı?', SVG, SCENE)
print('ok')

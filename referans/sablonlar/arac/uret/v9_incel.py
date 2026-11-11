from base import build
import json, sys

B = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {
    "q": 1.2, "start": 2.9, "almanya": 4.1, "paket": 8.9, "milim": 10.6, "takilan": 12.6, "bizde": 15.4, "arka": 21.6, "gram": 23.4, "ve": 24.6, "END": 27.3}

SVG = r'''
   <g id="bar">
     <rect id="wr" x="210" y="0" width="520" height="0" rx="10" fill="#7C9DA5" filter="url(#ps)"/>
     <rect id="ch" x="235" y="0" width="470" height="0" rx="6" fill="#243139"/>
     <rect id="lab" x="380" y="0" width="180" height="0" fill="#FFF8EB"/><path id="seg" stroke="#3d4f59" stroke-width="5"/>
   </g>
   <g id="gtag" filter="url(#ps)"><rect x="-150" y="-50" width="300" height="100" fill="#FFF8EB" stroke="#1c1b18" stroke-width="5"/><text id="gt" y="18" font-size="52" text-anchor="middle" fill="#1c1b18">100 g</text></g>
   <g id="zam" filter="url(#ps)"><rect x="-90" y="-40" width="180" height="80" fill="#ff5a1f" stroke="#1c1b18" stroke-width="5"/><text y="14" font-size="40" fill="#FFF8EB" text-anchor="middle">ZAM ↑</text></g>
   <path id="cal" stroke="#ff5a1f" stroke-width="8" fill="none" stroke-linecap="round"/><text id="calT" font-size="44" fill="#ff5a1f" text-anchor="start">-1 mm</text>
   <g id="court" filter="url(#ps)"><rect x="-190" y="-60" width="380" height="120" fill="#ff5a1f" stroke="#1c1b18" stroke-width="5"/><text y="16" font-size="48" fill="#FFF8EB" text-anchor="middle" letter-spacing="6">MAHKEME</text></g>
   <g id="box"><g id="boxIn" filter="url(#ps)"><rect x="-150" y="-260" width="300" height="260" fill="#E8B65C"/><rect x="-120" y="-220" width="240" height="70" fill="#FFF8EB"/><text id="bxT" y="-172" font-size="34" text-anchor="middle" fill="#1c1b18">KRAKER</text>
     <text id="bxG" y="-50" font-size="56" text-anchor="middle" fill="#ff5a1f"></text></g></g>
   <g id="stag" filter="url(#ps)"><rect x="-110" y="-44" width="220" height="88" fill="#FFF8EB" stroke="#1c1b18" stroke-width="5"/><text x="-90" y="-14" font-size="20" fill="#8c8880">RAF</text><text y="28" font-size="46" text-anchor="middle" fill="#1c1b18">60 g</text></g>
   <ellipse id="ring" fill="none" stroke="#ff5a1f" stroke-width="7"/>
'''

SCENE = r'''
const B=__B__; const END=B.END;
const ZAM=L(B.almanya,B.paket,.42), GR=L(B.almanya,B.paket,.68), K52=L(B.bizde,B.arka,.8);
window.V={sfx:[[0.02,'thud'],[B.q+.3,'scratch'],[B.start,'whoosh'],[ZAM,'pop'],[GR,'drop'],[B.paket+.2,'pop'],[B.milim+.2,'scratch'],[L(B.takilan,B.bizde,.6),'thud'],[B.bizde+.3,'whoosh'],[K52,'drop'],[B.arka+.2,'whoosh'],[B.ve+.3,'whoosh']]};
const LINES=[[B.start,B.almanya-.1,'Çikolata<br><span class="o">diyorum.</span>'],
 [B.almanya,GR-.05,'Önce<br><span class="o">zam.</span>'],
 [GR,B.paket-.1,'Sonra<br><span class="o">100 g → 90 g.</span>'],
 [B.paket,B.milim-.1,'Paket aynı,<br><span class="o">tasarım aynı.</span>'],
 [B.milim,B.takilan-.1,'Sadece<br><span class="o">bir milim inceldi.</span>'],
 [B.takilan,B.bizde-.1,'Fark eden yok,<br><span class="o">ta ki mahkemeye kadar.</span>'],
 [B.bizde,K52-.05,'Bizde: rafta<br><span class="o">60 gram...</span>'],
 [K52,B.arka-.1,'...pakette<br><span class="o">52 gram.</span>'],
 [B.arka,B.ve-.1,'Önüne değil,<br><span class="o">arkasına bak.</span>'],
 [B.ve,END-.45,'Ve hep aynı<br><span class="o">şeyi sorar:</span>']];
const BIG=[[K52,B.arka-.1]], HITS=[0.02,GR,L(B.takilan,B.bizde,.6),K52];
const CY=900;
function scene(t){
  // çikolata: kancada incelir; GR'de kalıcı incelir; sonda eski haline
  const hookT=(t>B.q&&t<B.start+.3)?Math.sin(Math.PI*p(t,B.q+.1,B.start-B.q+.2)):0;
  const thin=io(p(t,GR,.6))*(1-io(p(t,B.ve,.5)));
  const th=L(100,80,thin)-40*hookT+(hookT>0?6*Math.sin(t*20)*hookT:0);
  const barOn=t<B.bizde+.1||t>=B.ve; const bIn=t<B.bizde?1-io(p(t,B.bizde-.2,.3)):io(p(t,B.ve,.4));
  tr('bar',`translate(470 ${CY}) scale(${bIn}) translate(-470 ${-CY})`); op('bar',barOn?1:0);
  const wh=150; $('wr').setAttribute('y',CY-wh/2); $('wr').setAttribute('height',wh);
  $('ch').setAttribute('y',CY-th/2); $('ch').setAttribute('height',th);
  $('lab').setAttribute('y',CY-wh/2+14); $('lab').setAttribute('height',wh-28); op('lab',.25); $('seg').setAttribute('d',[313,391,469,547,625].map(x=>`M${x} ${CY-th/2+6} L${x} ${CY+th/2-6}`).join(' '));
  // gram etiketi + zam
  const gk=ob(p(t,B.almanya+.2,.35)), gOut=io(p(t,B.milim,.3));
  tr('gtag',`translate(470 ${CY+190}) scale(${t>B.almanya+.2?gk*(1-gOut):0})`);
  $('gt').textContent=t>GR?'90 g':'100 g'; $('gt').setAttribute('fill',t>GR?'#ff5a1f':'#1c1b18');
  const zk=ob(p(t,ZAM,.35)), zOut=io(p(t,B.paket,.3)); tr('zam',`translate(700 ${CY-170}) rotate(8) scale(${t>ZAM?zk*(1-zOut):0})`);
  // milim: kaliper
  const ck=io(p(t,B.milim+.2,.5)), cOut=io(p(t,B.takilan,.3)); const cx=170;
  $('cal').setAttribute('d',`M${cx-40} ${CY-th/2} L${cx+40} ${CY-th/2} M${cx-40} ${CY+th/2} L${cx+40} ${CY+th/2} M${cx} ${CY-th/2} L${cx} ${CY-th/2+th*ck}`);
  op('cal',t>B.milim+.2&&t<B.takilan+.3?1-cOut:0); $('calT').setAttribute('x',cx-30); $('calT').setAttribute('text-anchor','end'); $('calT').setAttribute('y',CY+14); op('calT',t>B.milim+.2&&t<B.takilan+.3?ck*(1-cOut):0);
  // mahkeme
  const ms=L(B.takilan,B.bizde,.6), mp=p(t,ms-.12,.12), mOut=io(p(t,B.bizde,.3));
  tr('court',`translate(470 ${CY-200}) rotate(-6) scale(${t>ms-.12?L(2,1,io(mp))*(1-mOut):0})`);
  // kraker: raf 60, paket 52; arka'da döner
  const bxIn=oc(p(t,B.bizde+.2,.5)), bxOut=io(p(t,B.ve,.4));
  const flip=t>B.arka+.2?Math.cos(Math.PI*cl(p(t,B.arka+.2,.5))):1;
  tr('box',`translate(${L(1200,560,bxIn)+bxOut*700} ${CY+200}) scale(${Math.abs(flip)} 1)`); op('box',t>B.bizde+.2&&t<B.ve+.5?1:0);
  const back=t>B.arka+.45; $('bxT').textContent=back?'NET MİKTAR':'KRAKER'; $('bxG').textContent=(t>K52||back)?'52 g':'';
  const sk=ob(p(t,B.bizde+.6,.35)), sOut=io(p(t,B.arka,.3)); tr('stag',`translate(260 ${CY+150}) rotate(-3) scale(${t>B.bizde+.6?sk*(1-sOut):0})`);
  const rg=t>B.arka+.8&&t<B.ve?ob(p(t,B.arka+.8,.35))*(1-io(p(t,B.ve-.2,.3))):0;
  $('ring').setAttribute('cx',560); $('ring').setAttribute('cy',CY+200-66); $('ring').setAttribute('rx',110*rg); $('ring').setAttribute('ry',50*rg);
}
'''.replace('__B__', json.dumps(B))

build('/home/claude/kasaonu-medya/referans/sablonlar/incel01/index.html', 'PAKET · 09', 'FİŞ 0014', 'EKSİK', '8 GRAM',
      'Seninki de mi', 'inceldi?', SVG, SCENE)
print('ok')

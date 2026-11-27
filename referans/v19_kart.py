import json, sys
from kit import make, box, TAGS, yrn, JS_HEAD, JS_TAIL
B = json.loads(sys.argv[1]); out = sys.argv[2]
segs = json.load(open('/home/claude/uret/metin/kart01_segs.json'))
REPL = [("iki katından","2 katından"),("İki katından","2 katından"),("yirmi dokuz dolar","29 dolar"),("altmış bir dolar","61 dolar"),("yüzde otuz sekiz","%38")]
B['start'] = B['ben']
SVG = r'''
 <g id="pill" transform="translate(470 92)"><rect x="-300" y="-26" width="600" height="52" rx="26" fill="#1c1b18"/><text y="10" font-size="24" text-anchor="middle" fill="#FFF8EB">SONDA: KENDİNE SORACAĞIN TEK SORU ↓</text></g>
 <g id="pay"><g id="cash" transform="translate(-180 0) rotate(-6)"><g filter="url(#ps)"><rect x="-150" y="-80" width="300" height="160" rx="10" fill="#8A9B7C" stroke="#1c1b18" stroke-width="5"/></g>
   <circle r="44" fill="none" stroke="#FFF8EB" stroke-width="6"/><text y="20" font-size="56" text-anchor="middle" fill="#FFF8EB">₺</text><text x="-120" y="-44" font-size="26" fill="#FFF8EB">NAKİT</text></g>
  <g id="card" transform="translate(180 0) rotate(6)"><g filter="url(#ps)"><rect x="-150" y="-95" width="300" height="190" rx="18" fill="#ff5a1f" stroke="#1c1b18" stroke-width="5"/></g>
   <rect x="-150" y="-55" width="300" height="34" fill="#1c1b18"/><rect x="-110" y="0" width="60" height="44" rx="8" fill="#E8B65C"/><text x="20" y="70" font-size="26" fill="#FFF8EB">KART</text></g>
  <g id="x2q" transform="translate(0 -170)"><circle r="70" fill="#1c1b18"/><text y="18" font-size="52" text-anchor="middle" fill="#E8B65C">×2?</text></g></g>
 <g id="mit"><g filter="url(#ps)"><rect x="-280" y="-110" width="560" height="220" fill="#243139"/></g><text y="-14" font-size="76" text-anchor="middle" fill="#E8B65C">MIT · 2001</text>
   <text y="56" font-size="34" text-anchor="middle" fill="#FFF8EB">AÇIK ARTIRMA DENEYİ</text></g>
 <g id="tik"><g filter="url(#ps)"><path d="M-300 -90 h480 v60 a30 30 0 0 0 0 60 v60 h-480 v-60 a30 30 0 0 0 0 -60z" fill="#E8B65C" stroke="#1c1b18" stroke-width="5"/></g>
   <path d="M120 -90 v180" stroke="#1c1b18" stroke-width="4" stroke-dasharray="10 8"/><text x="-90" y="-10" font-size="40" text-anchor="middle" fill="#1c1b18">BASKETBOL</text><text x="-90" y="44" font-size="34" text-anchor="middle" fill="#1c1b18">MAÇ BİLETİ</text>
   <text x="150" y="16" font-size="40" text-anchor="middle" fill="#1c1b18">🏀</text></g>
 <g id="env"><g filter="url(#ps)"><rect x="-200" y="-120" width="400" height="240" fill="#FFF8EB" stroke="#1c1b18" stroke-width="6"/></g><path d="M-200 -120 L0 20 L200 -120" fill="none" stroke="#1c1b18" stroke-width="6"/>
   <text y="90" font-size="40" text-anchor="middle" fill="#ff5a1f">KAPALI TEKLİF</text></g>
 ''' + box('gN', 380, 140, '#8A9B7C', 'NAKİT ÖDER', 40) + box('gK', 380, 140, '#ff5a1f', 'KARTLA ÖDER', 40) + r'''
 <g id="eq"><text y="0" font-size="46" text-anchor="middle" fill="#1c1b18">AYNI BİLET · <tspan fill="#ff5a1f">AYNI MAÇ</tspan></text></g>
 <g id="chart"><path d="M-260 300 H260" stroke="#1c1b18" stroke-width="6"/>
   <rect id="barA" x="-200" y="300" width="160" height="0" fill="#8A9B7C"/><rect id="barB" x="40" y="300" width="160" height="0" fill="#ff5a1f"/>
   <text id="tA1" x="-120" y="0" font-size="64" text-anchor="middle" fill="#1c1b18">$29</text><text id="tB1" x="120" y="0" font-size="64" text-anchor="middle" fill="#ff5a1f">$61</text>
   <text x="-120" y="350" font-size="30" text-anchor="middle" fill="#1c1b18">NAKİT</text><text x="120" y="350" font-size="30" text-anchor="middle" fill="#1c1b18">KART</text>
   <g id="x2" transform="translate(0 -250) rotate(-5)"><g filter="url(#ps)"><rect x="-210" y="-50" width="420" height="100" fill="#1c1b18"/></g><text y="16" font-size="40" text-anchor="middle" fill="#E8B65C">2 KATTAN FAZLA</text></g>
   <text id="topT" y="420" font-size="30" text-anchor="middle" fill="#8c8880">EN YÜKSEK TEKLİFLER: $53 → $142</text></g>
 <g id="pain"><g id="icC"><g filter="url(#ps)"><rect x="-120" y="-70" width="240" height="140" rx="10" fill="#8A9B7C" stroke="#1c1b18" stroke-width="5"/></g><text y="20" font-size="56" text-anchor="middle" fill="#FFF8EB">₺</text>
     <path id="fly" d="M150 -20 l60 -40 M150 20 l70 0 M150 60 l60 40" stroke="#e02424" stroke-width="8" stroke-linecap="round"/></g>
   <g id="icK"><g filter="url(#ps)"><rect x="-140" y="-90" width="280" height="180" rx="14" fill="#FFF8EB" stroke="#1c1b18" stroke-width="6"/></g><rect x="-140" y="-90" width="280" height="56" rx="14" fill="#243139"/>
     <text y="-50" font-size="28" text-anchor="middle" fill="#FFF8EB">TAKVİM</text><text y="40" font-size="46" text-anchor="middle" fill="#e02424">AY SONU</text></g>
   <g id="icT"><g filter="url(#ps)"><rect x="-150" y="-95" width="300" height="190" rx="18" fill="#ff5a1f" stroke="#1c1b18" stroke-width="5"/></g>
     <path d="M-20 -40 a50 50 0 0 1 0 80 M10 -60 a80 80 0 0 1 0 120 M40 -80 a110 110 0 0 1 0 160" fill="none" stroke="#FFF8EB" stroke-width="10" stroke-linecap="round"/></g>
   <rect x="-300" y="190" width="600" height="44" rx="22" fill="#e3ded2" stroke="#1c1b18" stroke-width="4"/><rect id="painF" x="-300" y="190" width="0" height="44" rx="22" fill="#e02424"/>
   <text id="painL" y="290" font-size="34" text-anchor="middle" fill="#1c1b18">ACI: HEMEN</text></g>
 ''' + box('adi', 560, 140, '#1c1b18', 'ÖDEME ACISI', 64, '#ff5a1f', '#ff5a1f', -4) + TAGS + r'''
 <g id="soru"><g filter="url(#ps)"><rect x="-320" y="-110" width="640" height="220" rx="24" fill="#FFF8EB" stroke="#1c1b18" stroke-width="6"/></g><path d="M-60 110 l-30 60 l90 -60z" fill="#FFF8EB" stroke="#1c1b18" stroke-width="6"/>
   <text y="-14" font-size="44" text-anchor="middle" fill="#1c1b18">Bunu NAKİT</text><text y="50" font-size="44" text-anchor="middle" fill="#ff5a1f">öder miydim?</text></g>
 <g id="sep"><path d="M-160 -60 h320 l-30 170 h-260z" fill="#7C9DA5" stroke="#1c1b18" stroke-width="6"/><path d="M-120 -60 q120 -110 240 0" fill="none" stroke="#1c1b18" stroke-width="8"/>
   <rect id="it0" x="-110" y="-120" width="60" height="80" fill="#C56B50"/><rect id="it1" x="-30" y="-140" width="60" height="100" fill="#E8B65C"/><rect id="it2" x="50" y="-110" width="60" height="70" fill="#8A9B7C"/>
   <text y="190" font-size="38" text-anchor="middle" fill="#ff5a1f">HAYIRSA → HAFİFLET</text></g>
 <g id="pos"><g filter="url(#ps)"><rect x="-150" y="-200" width="300" height="400" rx="30" fill="#243139"/></g><rect x="-110" y="-160" width="220" height="120" rx="10" fill="#b9d0ea"/>
   <text y="-90" font-size="34" text-anchor="middle" fill="#1c1b18">KART ✓</text><text y="-50" font-size="28" text-anchor="middle" fill="#1c1b18">TEMASSIZ ✓</text>
   <g fill="#FFF8EB"><circle cx="-60" cy="30" r="20"/><circle cx="0" cy="30" r="20"/><circle cx="60" cy="30" r="20"/><circle cx="-60" cy="90" r="20"/><circle cx="0" cy="90" r="20"/><circle cx="60" cy="90" r="20"/></g></g>
 <g id="nkt"><g filter="url(#ps)"><rect x="-260" y="-70" width="520" height="140" fill="#FFF8EB" stroke="#1c1b18" stroke-width="6"/></g><text y="16" font-size="46" text-anchor="middle" fill="#1c1b18">SADECE NAKİT</text>
   <path id="nktX" d="M-240 -60 L240 60 M-240 60 L240 -60" stroke="#e02424" stroke-width="12" stroke-linecap="round"/></g>
 <g id="kac"><text y="0" font-size="42" text-anchor="middle" fill="#e02424">SATIŞ KAPIDA KAÇAR</text></g>
''' + yrn(r'''<g transform="translate(0 -20)"><path d="M-40 40 v-110 l100 -24 v110" fill="none" stroke="#E8B65C" stroke-width="12"/><circle cx="-60" cy="44" r="26" fill="#E8B65C"/><circle cx="40" cy="20" r="26" fill="#E8B65C"/></g>
   <text y="120" font-size="38" text-anchor="middle" fill="#FFF8EB">Market neden <tspan fill="#ff5a1f">yavaş</tspan></text><text y="170" font-size="38" text-anchor="middle" fill="#FFF8EB">müzik çalıyor? <tspan fill="#ff5a1f">%38</tspan></text>''')

SCENE = r'''
const B=__B__; const END=B.END; const SUBS=__SUBS__;
window.V={sfx:[[0.02,'thud'],[B.ben+.1,'pop'],[B.soz+.1,'whoosh'],[B.uni+.1,'whoosh'],[B.odul+.1,'pop'],[B.zarf+.1,'whoosh'],[B.fark+.1,'pop'],[B.kartG+.1,'pop'],[B.ayni+.1,'whoosh'],
 [B.nakit+.3,'ticks'],[B.kart+.3,'ticks'],[B.iki,'thud'],[B.neden,'whoosh'],[B.aci+.1,'pop'],[B.erte+.1,'whoosh'],[B.adi,'thud'],[B.temas+.1,'pop'],[B.alici+.1,'whoosh'],[B.hafif+.2,'pop'],
 [B.satici+.1,'whoosh'],[B.kacir+.1,'thud'],[B.yarin+.1,'whoosh'],[B.takip+.1,'pop']]};
const LINES=[[B.ben,B.uni-.1,'Bir deney<br><span class="o">söylüyor.</span>'],[B.uni,B.fark-.1,'Açık artırma:<br><span class="o">aynı bilet.</span>'],
 [B.fark,B.nakit-.1,'Nakit mi,<br><span class="o">kart mı?</span>'],[B.nakit,B.neden-.1,'$29 vs<br><span class="o">$61</span>'],[B.neden,B.alici-.1,'Ödeme<br><span class="o">acısı.</span>'],
 [B.alici,B.satici-.1,'<span class="o">Alıcıysan:</span><br>nakit öder miydin?'],[B.satici,B.yarin-.1,'<span class="o">Satıcıysan:</span><br>kartı kabul et.'],
 [B.yarin,B.takip-.1,'Yarın<br><span class="o">Kasa Önü\'nde:</span>'],[B.takip,END,'Hoşuna gittiyse<br><span class="o">takip et.</span>']];
const BIG=[[B.adi,B.temas]], HITS=[0.02,B.iki,B.adi,B.kacir];
function scene(t){
  __HEAD__
  const pv=t<B.uni?(1-io(p(t,B.uni-.3,.3))):0;
  tr('pay',`translate(470 ${t<B.ben?900:L(900,960,io(p(t,B.ben,.4)))}) scale(${pv})`);
  tr('x2q',`translate(0 -190) scale(${t>B.ben?ob(p(t,B.ben,.35))*(1+Math.sin(t*5)*.04):0})`);
  tr('cash',`translate(-180 ${Math.sin(t*2)*8}) rotate(-6)`); tr('card',`translate(180 ${Math.cos(t*2)*8}) rotate(6)`);
  const pl=t>B.soz+.4&&t<B.alici; tr('pill',`translate(470 92) scale(${pl?ob(p(t,B.soz+.4,.4))*(1-io(p(t,B.alici-.3,.3))):0})`);
  tr('mit',`translate(470 880) scale(${W(B.uni,B.odul+.1)})`);
  tr('tik',`translate(470 ${t<B.zarf?880:L(880,700,io(p(t,B.zarf,.4)))}) scale(${W(B.odul,B.fark+.2)*(t<B.zarf?1:L(1,.7,io(p(t,B.zarf,.4))))})`);
  tr('env',`translate(470 1020) scale(${W(B.zarf,B.fark+.2)})`);
  const gv=W(B.fark,B.nakit+.2);
  tr('gN',`translate(240 ${t<B.ayni?880:L(880,820,io(p(t,B.ayni,.3)))}) scale(${t>B.fark+.6?gv*ob(p(t,B.fark+.6,.35)):0})`);
  tr('gK',`translate(700 ${t<B.ayni?880:L(880,820,io(p(t,B.ayni,.3)))}) scale(${t>B.kartG?gv*ob(p(t,B.kartG,.35)):0})`);
  tr('eq',`translate(470 1080) scale(${W(B.ayni,B.nakit+.2)})`);
  const cv=W(B.nakit,B.neden+.2); op('chart',cv>0?1:0); tr('chart',`translate(470 760) scale(${cv})`);
  const ha=420*29/61*io(p(t,B.nakit+.3,.8)), hb=420*io(p(t,B.kart+.3,.8));
  $('barA').setAttribute('y',300-ha); $('barA').setAttribute('height',ha); $('barB').setAttribute('y',300-hb); $('barB').setAttribute('height',hb);
  $('tA1').setAttribute('y',280-ha); $('tB1').setAttribute('y',280-hb); op('tA1',t>B.nakit+.5?1:0); op('tB1',t>B.kart+.5?1:0);
  tr('x2',`translate(0 -250) rotate(-5) scale(${t>B.iki?L(1.8,1,io(p(t,B.iki,.15))):0})`); op('topT',t>B.yuksek+.3?1:0);
  // ödeme acısı
  const av=W(B.aci,B.alici+.2); tr('pain',`translate(470 760) scale(${av})`);
  const ph=t<B.erte?1:(t<B.temas?L(1,.35,io(p(t,B.erte,.6))):L(.35,.04,io(p(t,B.temas,.6))));
  $('painF').setAttribute('width',600*ph*io(p(t,B.aci+.2,.6)));
  $('painL').textContent=t<B.erte?'ACI: HEMEN':(t<B.temas?'ACI: AY SONUNA ERTELENDİ':'ACI: NEREDEYSE YOK');
  op('icC',t<B.erte?1:0); op('icK',t>=B.erte&&t<B.temas?1:0); op('icT',t>=B.temas?1:0);
  tr('fly',`translate(${(t*60)%30} 0)`);
  tr('adi',`translate(470 1190) scale(${t>B.adi&&t<B.temas+.2?L(2,1,io(p(t,B.adi,.15)))*(1-io(p(t,B.temas,.2))):0})`);
  // alıcıysan
  const a2=W(B.alici,B.satici+.2); tr('tagA',`translate(470 560) scale(${a2})`);
  tr('soru',`translate(470 ${t<B.hafif?820:L(820,740,io(p(t,B.hafif,.3)))}) scale(${a2*(t<B.hafif?1:L(1,.8,io(p(t,B.hafif,.3))))})`);
  tr('sep',`translate(470 1040) scale(${t>B.hafif?a2*ob(p(t,B.hafif,.35)):0})`);
  for(let i=0;i<3;i++){const k=io(p(t,B.hafif+.5+i*.25,.4)); op('it'+i,i<2?1-k:1); tr('it'+i,`translate(${i<2?k*(i?160:-160):0} ${i<2?-k*120:0})`)}
  // satıcıysan
  const s2=W(B.satici,B.yarin+.2); tr('tagS',`translate(470 560) scale(${s2})`);
  tr('pos',`translate(${t<B.kacir?470:L(470,260,io(p(t,B.kacir,.4)))} 860) scale(${s2*(t<B.kacir?1:.75)})`);
  tr('nkt',`translate(660 880) rotate(4) scale(${t>B.kacir?s2*ob(p(t,B.kacir,.35))*.7:0})`); op('nktX',t>B.kacir+.6?1:0);
  tr('kac',`translate(470 1170) scale(${t>B.kacir+.8?s2:0})`);
  __TAIL__
}
'''.replace('__HEAD__', JS_HEAD).replace('__TAIL__', JS_TAIL)
make(out, B, segs, REPL, 'TAKTİK · 28', 'FİŞ 0024', 'ÖDEME ACISI', 'Kartla ödeyince', '2 kat harcarsın?', SVG, SCENE)

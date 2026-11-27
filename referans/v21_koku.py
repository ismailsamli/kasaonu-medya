import json, sys
from kit import make, box, TAGS, yrn, JS_HEAD, JS_TAIL
B = json.loads(sys.argv[1]); out = sys.argv[2]
segs = json.load(open('/home/claude/uret/metin/koku01_segs.json'))
REPL = [("üç cumartesi","3 cumartesi"),("on beş dakika","15 dakika"),("on yedi buçuk avrodan","17,5 avrodan"),("yirmi bir avroya","21 avroya"),("yüzde yirmi","%20")]
B['start'] = B['fransa']
LAV = '<g transform="translate({x} {y}) scale({s})"><path d="M0 70 v-140" stroke="#5f8a4f" stroke-width="8"/><g fill="#9b7fc4"><ellipse cx="-14" cy="-60" rx="14" ry="22"/><ellipse cx="14" cy="-40" rx="14" ry="22"/><ellipse cx="-14" cy="-20" rx="14" ry="22"/><ellipse cx="14" cy="0" rx="14" ry="22"/><ellipse cx="0" cy="-86" rx="12" ry="20"/></g></g>'
def sat(id, n, title, col, icon):
    return (f'<g id="{id}"><g filter="url(#ps)"><rect x="-135" y="-120" width="270" height="240" rx="14" fill="#FFF8EB" stroke="#1c1b18" stroke-width="5"/></g>'
            f'<rect x="-135" y="-120" width="270" height="56" rx="14" fill="{col}"/><text y="-82" font-size="26" text-anchor="middle" fill="#FFF8EB">{n}. CUMARTESİ</text>{icon}'
            f'<text y="96" font-size="34" text-anchor="middle" fill="{col}">{title}</text><g id="{id}x"><rect x="-135" y="-120" width="270" height="240" rx="14" fill="#f3efe4" opacity=".7"/></g></g>')
SVG = (r'''
 <g id="pill" transform="translate(470 92)"><rect x="-300" y="-26" width="600" height="52" rx="26" fill="#1c1b18"/><text y="10" font-size="24" text-anchor="middle" fill="#FFF8EB">SONDA: KOKUYA KARŞI TEK SORU ↓</text></g>
 <g id="hk"><g filter="url(#ps)"><path d="M-170 -230 h340 v440 l-28 20 l-28 -20 l-28 20 l-28 -20 l-28 20 l-28 -20 l-28 20 l-28 -20 l-28 20 l-28 -20 l-28 20 l-28 -20z" fill="#FFF8EB" stroke="#1c1b18" stroke-width="5"/></g>
   <text y="-180" font-size="30" text-anchor="middle" fill="#1c1b18">HESAP</text><path d="M-130 -150 H130" stroke="#b9b4a8" stroke-width="4" stroke-dasharray="8 6"/>
   <text x="-130" y="-100" font-size="28" fill="#1c1b18">Pizza</text><text x="-130" y="-50" font-size="28" fill="#1c1b18">İçecek</text>
   <text id="hk1" x="-130" y="0" font-size="28" fill="#ff5a1f">+ Tatlı</text><text id="hk2" x="-130" y="50" font-size="28" fill="#ff5a1f">+ Kahve</text>
   <path d="M-130 90 H130" stroke="#1c1b18" stroke-width="4"/><text id="hkT" x="130" y="150" font-size="44" text-anchor="end" fill="#1c1b18">€17,5</text>
   <g id="lv0">''' + LAV.format(x=250, y=-40, s=1.1) + r'''<g id="wv" fill="none" stroke="#9b7fc4" stroke-width="6" stroke-linecap="round"><path d="M200 -170 q20 -20 0 -40 q-20 -20 0 -40"/><path d="M250 -190 q20 -20 0 -40 q-20 -20 0 -40"/><path d="M300 -170 q20 -20 0 -40 q-20 -20 0 -40"/></g></g></g>
 <g id="fr"><g filter="url(#ps)"><rect x="-280" y="-110" width="560" height="220" fill="#243139"/></g><text y="-16" font-size="64" text-anchor="middle" fill="#E8B65C">FRANSA · 2006</text>
   <text y="56" font-size="32" text-anchor="middle" fill="#FFF8EB">KÜÇÜK PİZZACI · 3 CUMARTESİ</text></g>
 ''' + sat('s1', 1, 'KOKU YOK', '#8c8880', '<text y="30" font-size="70" text-anchor="middle" fill="#8c8880">—</text>')
     + sat('s2', 2, 'LİMON', '#d4a017', '<g transform="translate(0 10)"><ellipse rx="56" ry="40" fill="#f2d24b" stroke="#1c1b18" stroke-width="4"/><circle cx="58" cy="0" r="8" fill="#f2d24b" stroke="#1c1b18" stroke-width="4"/></g>')
     + sat('s3', 3, 'LAVANTA', '#7d5fb0', LAV.format(x=0, y=20, s=.8)) + r'''
 <g id="eq"><text y="0" font-size="44" text-anchor="middle" fill="#1c1b18">MENÜ AYNI · <tspan fill="#ff5a1f">FİYAT AYNI</tspan></text></g>
 <g id="clk"><g filter="url(#ps)"><circle r="150" fill="#FFF8EB" stroke="#1c1b18" stroke-width="8"/></g><path id="cH" d="M0 0 V-110" stroke="#1c1b18" stroke-width="10" stroke-linecap="round"/><path d="M0 0 H70" stroke="#1c1b18" stroke-width="10" stroke-linecap="round"/>
   <path id="cArc" d="" fill="#9b7fc4" opacity=".55"/><circle r="12" fill="#1c1b18"/><text y="220" font-size="40" text-anchor="middle" fill="#1c1b18">91 DK → <tspan fill="#7d5fb0">106 DK</tspan></text>
   <g id="p15" transform="translate(220 -130) rotate(8)"><g filter="url(#ps)"><rect x="-120" y="-46" width="240" height="92" fill="#1c1b18"/></g><text y="18" font-size="50" text-anchor="middle" fill="#E8B65C">+15 DK</text></g></g>
 <g id="chart"><path d="M-260 300 H260" stroke="#1c1b18" stroke-width="6"/>
   <rect id="barA" x="-200" y="300" width="160" height="0" fill="#8c8880"/><rect id="barB" x="40" y="300" width="160" height="0" fill="#7d5fb0"/>
   <text id="tA1" x="-120" y="0" font-size="56" text-anchor="middle" fill="#1c1b18">€17,5</text><text id="tB1" x="120" y="0" font-size="56" text-anchor="middle" fill="#7d5fb0">€21,1</text>
   <text x="-120" y="350" font-size="28" text-anchor="middle" fill="#1c1b18">KOKUSUZ</text><text x="120" y="350" font-size="28" text-anchor="middle" fill="#1c1b18">LAVANTA</text>
   <g id="p20" transform="translate(0 -230) rotate(-5)"><g filter="url(#ps)"><rect x="-190" y="-54" width="380" height="108" fill="#1c1b18"/></g><text y="20" font-size="56" text-anchor="middle" fill="#E8B65C">≈ +%20</text></g>
   <text y="410" font-size="26" text-anchor="middle" fill="#8c8880">KİŞİ BAŞI HESAP · GUÉGUEN &amp; PETR, 2006</text></g>
 ''' + box('rlx', 500, 120, '#7d5fb0', 'RAHATLATIR', 58, '#FFF8EB', '#1c1b18', -4) + r'''
 <g id="ord"><g id="o1"><g filter="url(#ps)"><rect x="-130" y="-110" width="260" height="220" rx="20" fill="#FFF8EB" stroke="#1c1b18" stroke-width="5"/></g>
     <path d="M-70 40 h140 l-20 -70 h-100z" fill="#C56B50"/><circle cy="-50" r="20" fill="#e02424"/><text y="90" font-size="30" text-anchor="middle" fill="#1c1b18">+1 TATLI</text></g>
   <g id="o2"><g filter="url(#ps)"><rect x="-130" y="-110" width="260" height="220" rx="20" fill="#FFF8EB" stroke="#1c1b18" stroke-width="5"/></g>
     <path d="M-60 -40 h100 v70 a50 40 0 0 1 -100 0z" fill="#243139"/><path d="M40 -20 a26 26 0 0 1 0 44" fill="none" stroke="#243139" stroke-width="10"/><text y="90" font-size="30" text-anchor="middle" fill="#1c1b18">+1 KAHVE</text></g></g>
 <g id="kms"><text y="0" font-size="40" text-anchor="middle" fill="#1c1b18">"Kokuya para verdim"</text><text y="56" font-size="40" text-anchor="middle" fill="#ff5a1f">diyen yok.</text></g>
 ''' + TAGS + r'''
 <g id="soru"><g filter="url(#ps)"><rect x="-320" y="-120" width="640" height="240" rx="24" fill="#FFF8EB" stroke="#1c1b18" stroke-width="6"/></g><path d="M-60 120 l-30 60 l90 -60z" fill="#FFF8EB" stroke="#1c1b18" stroke-width="6"/>
   <text y="-20" font-size="56" text-anchor="middle" fill="#1c1b18">AÇ MISIN?</text><text y="56" font-size="56" text-anchor="middle" fill="#7d5fb0">RAHAT MISIN?</text></g>
 <g id="dif"><g filter="url(#ps)"><path d="M-90 120 h180 l-20 -170 h-140z" fill="#243139"/></g><rect x="-30" y="-90" width="60" height="40" rx="8" fill="#8c8880"/>
   <g id="mist" fill="none" stroke="#9b7fc4" stroke-width="7" stroke-linecap="round"><path d="M-20 -110 q20 -25 0 -50 q-20 -25 0 -50"/><path d="M20 -120 q20 -25 0 -50 q-20 -25 0 -50"/></g></g>
 ''' + box('ok1', 380, 100, '#5f8a4f', 'SAKİN ✓', 50) + box('no1', 460, 100, '#e02424', 'AĞIR ✗', 50) + r'''
 <g id="kac"><text y="0" font-size="38" text-anchor="middle" fill="#e02424">BAŞ AĞRITAN KOKU = KAÇAN MÜŞTERİ</text></g>
''' + yrn(r'''<g transform="translate(-120 -45)"><path d="M-50 -70 h100 l-14 130 h-72z" fill="#b9d0ea" stroke="#FFF8EB" stroke-width="4"/><text y="110" font-size="34" text-anchor="middle" fill="#FFF8EB">₺50</text></g>
   <g transform="translate(120 -45)"><path d="M-50 -70 h100 l-14 130 h-72z" fill="#b9d0ea" stroke="#FFF8EB" stroke-width="4"/><text y="110" font-size="34" text-anchor="middle" fill="#ff5a1f">₺500</text></g>
   <text y="150" font-size="34" text-anchor="middle" fill="#FFF8EB">Aynı içecek,</text><text y="196" font-size="34" text-anchor="middle" fill="#ff5a1f">hangisi lezzetli?</text>'''))

SCENE = r'''
const B=__B__; const END=B.END; const SUBS=__SUBS__;
window.V={sfx:[[0.02,'thud'],[B.fransa+.1,'whoosh'],[B.soz+.1,'whoosh'],[B.c1+.1,'pop'],[B.c2+.1,'pop'],[B.c3+.1,'pop'],[B.ayni+.1,'whoosh'],[B.limon+.1,'pop'],[B.lav+.1,'pop'],
 [B.sure+.3,'ticks'],[B.sure+2.4,'thud'],[B.hesap+.3,'ticks'],[B.yuzde,'thud'],[B.neden+.6,'thud'],[B.rahat+1.2,'pop'],[B.rahat+2.6,'pop'],[B.kimse+.1,'whoosh'],[B.alici+.1,'whoosh'],
 [B.satici+.1,'whoosh'],[B.bas+.1,'thud'],[B.yarin+.1,'whoosh'],[B.takip+.1,'pop']]};
const LINES=[[B.fransa,B.c1-.1,'3 cumartesi,<br><span class="o">3 koku.</span>'],[B.c1,B.limon-.1,'Menü aynı,<br><span class="o">koku farklı.</span>'],
 [B.limon,B.sure-.1,'Limon: yok.<br><span class="o">Lavanta: var.</span>'],[B.sure,B.neden-.1,'+15 dakika,<br><span class="o">+%20 hesap.</span>'],[B.neden,B.alici-.1,'Rahat olan<br><span class="o">acele etmez.</span>'],
 [B.alici,B.satici-.1,'<span class="o">Alıcıysan:</span><br>aç mısın, rahat mı?'],[B.satici,B.yarin-.1,'<span class="o">Satıcıysan:</span><br>sakin, ağır değil.'],
 [B.yarin,B.takip-.1,'Yarın<br><span class="o">Kasa Önü\'nde:</span>'],[B.takip,END,'Hoşuna gittiyse<br><span class="o">takip et.</span>']];
const BIG=[[B.yuzde,B.neden]], HITS=[0.02,B.yuzde,B.bas];
function scene(t){
  __HEAD__
  const hv=t<B.c1?(1-io(p(t,B.c1-.3,.3))):0;
  tr('hk',`translate(${t<B.fransa?400:L(400,420,io(p(t,B.fransa,.4)))} ${t<B.fransa?880:L(880,980,io(p(t,B.fransa,.4)))}) scale(${hv*(t<B.fransa?1:.75)})`);
  const k=io(p(t,.6,1.6)); op('hk1',t>.9?1:0); op('hk2',t>1.5?1:0); $('hkT').textContent='€'+(17.5+3.6*k).toFixed(1).replace('.',',');
  tr('wv',`translate(0 ${-((t*25)%40)})`);
  const pl=t>B.soz+.4&&t<B.alici; tr('pill',`translate(470 92) scale(${pl?ob(p(t,B.soz+.4,.4))*(1-io(p(t,B.alici-.3,.3))):0})`);
  tr('fr',`translate(470 560) scale(${W(B.fransa,B.c1+.1)*.85})`);
  // 3 cumartesi
  const sv=W(B.c1,B.sure+.2);
  [['s1',B.c1,175],['s2',B.c2,470],['s3',B.c3,765]].forEach(([id,kk,x])=>{
    const big=(id==='s3'&&t>B.lav)?L(1,1.12,io(p(t,B.lav,.3))):1;
    tr(id,`translate(${x} ${t<B.ayni?860:L(860,820,io(p(t,B.ayni,.3)))}) scale(${t>kk?sv*ob(p(t,kk,.35))*.95*big:0})`)});
  op('s1x',t>B.limon?1:0); op('s2x',t>B.limon+.3?1:0); op('s3x',0);
  tr('eq',`translate(470 1100) scale(${W(B.ayni,B.limon+.2)})`);
  // saat
  const cv=W(B.sure,B.hesap+.2); tr('clk',`translate(470 840) scale(${cv})`);
  const ca=io(p(t,B.sure+.4,1.8)); const ang=ca*(15/60)*2*Math.PI;
  tr('cH',`rotate(${ang*180/Math.PI})`);
  $('cArc').setAttribute('d',`M0 0 L0 -140 A140 140 0 0 1 ${140*Math.sin(ang)} ${-140*Math.cos(ang)} Z`);
  tr('p15',`translate(220 -130) rotate(8) scale(${t>B.sure+2.4?L(1.8,1,io(p(t,B.sure+2.4,.15))):0})`);
  // hesap grafiği
  const gv=W(B.hesap,B.neden+.2); op('chart',gv>0?1:0); tr('chart',`translate(470 760) scale(${gv})`);
  const ha=400*17.5/21.1*io(p(t,B.hesap+.6,.8)), hb=400*io(p(t,B.hesap+2,.8));
  $('barA').setAttribute('y',300-ha); $('barA').setAttribute('height',ha); $('barB').setAttribute('y',300-hb); $('barB').setAttribute('height',hb);
  $('tA1').setAttribute('y',280-ha); $('tB1').setAttribute('y',280-hb); op('tA1',t>B.hesap+.8?1:0); op('tB1',t>B.hesap+2.2?1:0);
  tr('p20',`translate(0 -230) rotate(-5) scale(${t>B.yuzde?L(1.8,1,io(p(t,B.yuzde,.15))):0})`);
  // neden
  const nv=W(B.neden,B.alici+.2);
  tr('rlx',`translate(470 ${t<B.rahat?820:L(820,600,io(p(t,B.rahat,.4)))}) rotate(-4) scale(${t>B.neden+.6?nv*L(1.6,1,io(p(t,B.neden+.6,.15)))*(t<B.rahat?1:.8):0})`);
  tr('o1',`translate(-150 0) scale(${t>B.rahat+1.2?ob(p(t,B.rahat+1.2,.35)):0})`); tr('o2',`translate(150 0) scale(${t>B.rahat+2.6?ob(p(t,B.rahat+2.6,.35)):0})`);
  tr('ord',`translate(470 ${t<B.kimse?880:L(880,820,io(p(t,B.kimse,.3)))}) scale(${nv})`);
  tr('kms',`translate(470 1080) scale(${t>B.kimse?nv*ob(p(t,B.kimse,.35)):0})`);
  // alıcıysan
  const a2=W(B.alici,B.satici+.2); tr('tagA',`translate(470 560) scale(${a2})`); tr('soru',`translate(470 860) scale(${a2})`);
  // satıcıysan
  const s2=W(B.satici,B.yarin+.2); tr('tagS',`translate(470 560) scale(${s2})`);
  tr('dif',`translate(240 960) scale(${s2})`); tr('mist',`translate(0 ${-((t*20)%40)}) scale(${t<B.bas?1:L(1,1.25,io(p(t,B.bas,.4)))})`);
  tr('ok1',`translate(640 800) scale(${t>B.satici+.8?s2*ob(p(t,B.satici+.8,.35))*.8:0})`);
  tr('no1',`translate(640 960) rotate(-4) scale(${t>B.bas?s2*L(1.6,.8,io(p(t,B.bas,.15))):0})`);
  tr('kac',`translate(470 1170) scale(${t>B.bas+.8?s2:0})`);
  __TAIL__
}
'''.replace('__HEAD__', JS_HEAD).replace('__TAIL__', JS_TAIL)
make(out, B, segs, REPL, 'TAKTİK · 30', 'FİŞ 0026', 'KOKU PAZARLAMASI', 'Lavanta kokusu', 'hesabı büyütür', SVG, SCENE)

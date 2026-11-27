import json, sys
from kit import make, box, TAGS, yrn, JS_HEAD, JS_TAIL
B = json.loads(sys.argv[1]); out = sys.argv[2]
segs = json.load(open('/home/claude/uret/metin/muzik01_segs.json'))
REPL = [("Bin dokuz yüz seksen ikide","1982'de"),("dokuz hafta","9 hafta"),("üç şeyden","3 şeyden"),("yüzde otuz sekiz","%38")]
B['start'] = B['tes']
NOTE = '<g transform="translate({x} {y}) scale({s})"><path d="M0 0 v-70 l40 -12 v70" fill="none" stroke="{c}" stroke-width="9"/><circle cx="-12" cy="2" r="16" fill="{c}"/><circle cx="28" cy="-10" r="16" fill="{c}"/></g>'
def day(id, title, col, sub):
    return (f'<g id="{id}"><g filter="url(#ps)"><rect x="-130" y="-110" width="260" height="220" rx="14" fill="#FFF8EB" stroke="#1c1b18" stroke-width="5"/></g>'
            f'<rect x="-130" y="-110" width="260" height="60" rx="14" fill="{col}"/><text y="-68" font-size="30" text-anchor="middle" fill="#FFF8EB">{title}</text>'
            f'<text y="40" font-size="54" text-anchor="middle" fill="{col}">{sub}</text></g>')
SVG = r'''
 <g id="pill" transform="translate(470 92)"><rect x="-300" y="-26" width="600" height="52" rx="26" fill="#1c1b18"/><text y="10" font-size="24" text-anchor="middle" fill="#FFF8EB">SONDA: MÜZİĞİ KENDİ LEHİNE ÇEVİR ↓</text></g>
 <g id="spk"><g filter="url(#ps)"><rect x="-150" y="-200" width="300" height="400" rx="26" fill="#243139"/></g><circle cy="-90" r="56" fill="#1c1b18" stroke="#7C9DA5" stroke-width="10"/>
   <circle cy="70" r="90" fill="#1c1b18" stroke="#7C9DA5" stroke-width="12"/><circle id="cone" cy="70" r="40" fill="#7C9DA5"/>
   <g id="nts">''' + NOTE.format(x=230, y=-120, s=1, c='#ff5a1f') + NOTE.format(x=-250, y=-40, s=.8, c='#E8B65C') + NOTE.format(x=240, y=120, s=.7, c='#8A9B7C') + r'''</g></g>
 ''' + box('tsd', 460, 110, '#ff5a1f', 'TESADÜF DEĞİL', 50, '#FFF8EB', '#1c1b18', -5) + r'''
 <g id="dny"><g filter="url(#ps)"><rect x="-280" y="-110" width="560" height="220" fill="#243139"/></g><text y="-14" font-size="80" text-anchor="middle" fill="#E8B65C">1982</text>
   <text y="56" font-size="34" text-anchor="middle" fill="#FFF8EB">SÜPERMARKET · 9 HAFTA</text></g>
 ''' + day('d0', 'HIZLI', '#e02424', '♪♪♪') + day('d1', 'YAVAŞ', '#5f8a4f', '♪ . ♪') + day('d2', 'SESSİZ', '#8c8880', '—') + r'''
 <g id="ais"><rect x="-340" y="-170" width="680" height="70" fill="#C56B50"/><rect x="-340" y="100" width="680" height="70" fill="#C56B50"/>
   <g fill="#E8B65C"><rect x="-320" y="-160" width="40" height="50"/><rect x="-200" y="-160" width="40" height="50"/><rect x="-80" y="-160" width="40" height="50"/><rect x="40" y="-160" width="40" height="50"/><rect x="160" y="-160" width="40" height="50"/>
   <rect x="-260" y="110" width="40" height="50"/><rect x="-140" y="110" width="40" height="50"/><rect x="-20" y="110" width="40" height="50"/><rect x="100" y="110" width="40" height="50"/><rect x="220" y="110" width="40" height="50"/></g>
   <g id="wk"><circle cy="-30" r="24" fill="#243139"/><rect x="-18" y="-6" width="36" height="60" rx="14" fill="#243139"/></g>
   <text id="spd" y="250" font-size="34" text-anchor="middle" fill="#1c1b18">YÜRÜME HIZI ÖLÇÜLDÜ</text></g>
 <g id="reg"><g filter="url(#ps)"><rect x="-200" y="-90" width="400" height="180" rx="14" fill="#1c1b18"/></g><rect x="-170" y="-60" width="340" height="70" fill="#b9d0ea"/><text id="regN" y="-12" font-size="40" text-anchor="middle" fill="#1c1b18">₺ 0</text>
   <text y="60" font-size="28" text-anchor="middle" fill="#FFF8EB">KASA SATIŞI</text></g>
 ''' + box('ch0', 520, 110, '#243139', 'YAVAŞ YÜRÜR', 46) + box('ch1', 520, 110, '#C56B50', 'RAFA BAKAR', 46) + box('ch2', 520, 110, '#ff5a1f', 'DAHA ÇOK ALIR', 46) + r'''
 <g id="arw"><path d="M0 -150 v40 M-16 -126 l16 16 l16 -16 M0 20 v40 M-16 44 l16 16 l16 -16" fill="none" stroke="#1c1b18" stroke-width="7"/></g>
 <g id="chart"><path d="M-260 300 H260" stroke="#1c1b18" stroke-width="6"/>
   <rect id="barA" x="-200" y="300" width="160" height="0" fill="#e02424"/><rect id="barB" x="40" y="300" width="160" height="0" fill="#5f8a4f"/>
   <text x="-120" y="350" font-size="30" text-anchor="middle" fill="#1c1b18">HIZLI</text><text x="120" y="350" font-size="30" text-anchor="middle" fill="#1c1b18">YAVAŞ</text>
   <g id="p38" transform="translate(0 -250) rotate(-5)"><g filter="url(#ps)"><rect x="-200" y="-56" width="400" height="112" fill="#1c1b18"/></g><text y="22" font-size="60" text-anchor="middle" fill="#E8B65C">+%38</text></g>
   <text y="410" font-size="28" text-anchor="middle" fill="#8c8880">GÜNLÜK SATIŞ · MILLIMAN, 1982</text></g>
 <g id="bub"><g filter="url(#ps)"><rect x="-320" y="-100" width="640" height="200" rx="24" fill="#FFF8EB" stroke="#1c1b18" stroke-width="6"/></g><path d="M80 100 l40 60 l-100 -60z" fill="#FFF8EB" stroke="#1c1b18" stroke-width="6"/>
   <text y="-14" font-size="42" text-anchor="middle" fill="#1c1b18">Müziği hatırlıyor</text><text y="46" font-size="42" text-anchor="middle" fill="#1c1b18">musun?</text></g>
 ''' + box('fe', 520, 110, '#e02424', 'ÇOĞU: FARK ETMEDİ', 44, '#FFF8EB', '#1c1b18', -4) + TAGS + r'''
 <g id="hp"><path d="M-130 40 v-40 a130 130 0 0 1 260 0 v40" fill="none" stroke="#1c1b18" stroke-width="22"/><rect x="-170" y="20" width="80" height="120" rx="24" fill="#ff5a1f"/><rect x="90" y="20" width="80" height="120" rx="24" fill="#ff5a1f"/>
   <text y="220" font-size="36" text-anchor="middle" fill="#1c1b18">KENDİ HIZLI LİSTEN</text></g>
 <g id="lst"><g filter="url(#ps)"><rect x="-170" y="-120" width="340" height="240" fill="#FFF8EB" stroke="#1c1b18" stroke-width="5"/></g><text x="-130" y="-60" font-size="32" fill="#1c1b18">✓ süt</text><text x="-130" y="0" font-size="32" fill="#1c1b18">✓ ekmek</text><text x="-130" y="60" font-size="32" fill="#1c1b18">✓ yumurta</text></g>
 <g id="vol"><g filter="url(#ps)"><rect x="-300" y="-110" width="600" height="220" rx="20" fill="#243139"/></g><text y="-50" font-size="32" text-anchor="middle" fill="#FFF8EB">SAKİN · YAVAŞ MÜZİK</text>
   <rect x="-240" y="10" width="480" height="20" rx="10" fill="#8c8880"/><rect id="volF" x="-240" y="10" width="380" height="20" rx="10" fill="#E8B65C"/><circle id="volK" cx="140" cy="20" r="26" fill="#ff5a1f"/>
   <text id="volT" y="90" font-size="30" text-anchor="middle" fill="#E8B65C">SES: YÜKSEK</text></g>
''' + yrn(r'''<g transform="translate(0 -30)"><path d="M0 60 v-130" stroke="#5f8a4f" stroke-width="8"/><g fill="#9b7fc4"><ellipse cx="-14" cy="-60" rx="14" ry="22"/><ellipse cx="14" cy="-40" rx="14" ry="22"/><ellipse cx="-14" cy="-20" rx="14" ry="22"/><ellipse cx="14" cy="0" rx="14" ry="22"/><ellipse cx="0" cy="-84" rx="12" ry="20"/></g></g>
   <text y="110" font-size="38" text-anchor="middle" fill="#FFF8EB">Lavanta kokusu</text><text y="160" font-size="38" text-anchor="middle" fill="#ff5a1f">hesabı büyütür mü?</text>''')

SCENE = r'''
const B=__B__; const END=B.END; const SUBS=__SUBS__;
window.V={sfx:[[0.02,'thud'],[B.tes,'thud'],[B.deney+.1,'whoosh'],[B.soz+.1,'whoosh'],[B.hizli+.1,'pop'],[B.yavasM+.1,'pop'],[B.yok+.1,'pop'],[B.olc+.1,'whoosh'],[B.kasa+.2,'ticks'],
 [B.yavas+.1,'pop'],[B.bak+.1,'pop'],[B.al+.1,'pop'],[B.sonuc+.3,'ticks'],[B.sonuc+2.6,'thud'],[B.ilginc+.1,'whoosh'],[B.fark,'thud'],[B.alici+.1,'whoosh'],[B.satici+.1,'whoosh'],[B.kis+.2,'ticks'],
 [B.yarin+.1,'whoosh'],[B.takip+.1,'pop']]};
const LINES=[[B.tes,B.deney-.1,'Tesadüf<br><span class="o">değil.</span>'],[B.deney,B.olc-.1,'9 hafta,<br><span class="o">3 tür gün.</span>'],
 [B.olc,B.sonuc-.1,'Yavaş müzik,<br><span class="o">yavaş adım.</span>'],[B.sonuc,B.ilginc-.1,'Satış<br><span class="o">%38 fazla.</span>'],[B.ilginc,B.alici-.1,'Kimse<br><span class="o">fark etmedi.</span>'],
 [B.alici,B.satici-.1,'<span class="o">Alıcıysan:</span><br>kendi listeni dinle.'],[B.satici,B.yarin-.1,'<span class="o">Satıcıysan:</span><br>sakin ama kısık.'],
 [B.yarin,B.takip-.1,'Yarın<br><span class="o">Kasa Önü\'nde:</span>'],[B.takip,END,'Hoşuna gittiyse<br><span class="o">takip et.</span>']];
const BIG=[[B.sonuc+2.5,B.ilginc]], HITS=[0.02,B.tes,B.fark];
const SOK=B.sonuc+2.6;
function scene(t){
  __HEAD__
  const sv=t<B.deney?(1-io(p(t,B.deney-.3,.3))):0;
  tr('spk',`translate(470 ${t<B.tes?880:L(880,930,io(p(t,B.tes,.4)))}) scale(${sv*(t<B.tes?1:.85)})`);
  tr('cone',`scale(${1+Math.sin(t*4)*.12})`); tr('nts',`translate(0 ${-((t*20)%40)})`);
  tr('tsd',`translate(470 560) rotate(-5) scale(${t>B.tes&&t<B.deney?L(1.8,1,io(p(t,B.tes,.15)))*(1-io(p(t,B.deney-.25,.25))):0})`);
  const pl=t>B.soz+.4&&t<B.alici; tr('pill',`translate(470 92) scale(${pl?ob(p(t,B.soz+.4,.4))*(1-io(p(t,B.alici-.3,.3))):0})`);
  tr('dny',`translate(470 880) scale(${W(B.deney,B.uc+.1)})`);
  const dv=W(B.uc,B.olc+.2);
  [['d0',B.hizli,175,0],['d1',B.yavasM,470,.35],['d2',B.yok,765,.7]].forEach(([id,k,x,o])=>{const a0=B.uc+.3+o; const pk=(t>k&&t<k+.5)?1+.12*Math.sin(p(t,k,.5)*Math.PI):1; tr(id,`translate(${x} ${880+Math.sin(t*3+x)*6}) scale(${t>a0?dv*ob(p(t,a0,.35))*.95*pk:0})`)});
  // koridor
  const av=W(B.olc,B.bak+.2); tr('ais',`translate(470 ${t<B.kasa?860:L(860,760,io(p(t,B.kasa,.4)))}) scale(${av*(t<B.kasa?1:.8)})`);
  const sp=t<B.yavas?2.2:.7; const wx=((t-B.olc)*sp*60)%600-300; tr('wk',`translate(${wx} 0)`);
  $('spd').textContent=t<B.yavas?'YÜRÜME HIZI ÖLÇÜLDÜ':'YAVAŞ MÜZİK → YAVAŞ ADIM';
  tr('reg',`translate(470 1130) scale(${t>B.kasa&&t<B.yavas+.2?ob(p(t,B.kasa,.35))*(1-io(p(t,B.yavas,.2)))*.85:0})`);
  $('regN').textContent='₺ '+Math.round(4800*io(p(t,B.kasa+.2,1.2))).toLocaleString('tr-TR');
  // zincir
  const zv=W(B.bak,B.sonuc+.2);
  tr('ch0',`translate(470 760) scale(${t>B.bak?zv:0})`); tr('ch1',`translate(470 930) scale(${t>B.bak+.3?zv*ob(p(t,B.bak+.3,.35)):0})`);
  tr('ch2',`translate(470 1100) scale(${t>B.al?zv*ob(p(t,B.al,.35))*L(1.15,1,io(p(t,B.al+.35,.3))):0})`); tr('arw',`translate(470 960) scale(${t>B.bak+.3?zv:0})`);
  // grafik
  const gv=W(B.sonuc,B.ilginc+.2); op('chart',gv>0?1:0); tr('chart',`translate(470 760) scale(${gv})`);
  const ha=300*io(p(t,B.sonuc+.3,.8)), hb=414*io(p(t,B.sonuc+1.0,1.2));
  $('barA').setAttribute('y',300-ha); $('barA').setAttribute('height',ha); $('barB').setAttribute('y',300-hb); $('barB').setAttribute('height',hb);
  tr('p38',`translate(0 -250) rotate(-5) scale(${t>SOK?L(1.8,1,io(p(t,SOK,.15))):0})`);
  // hatırlıyor mu
  const hv=W(B.ilginc,B.alici+.2); tr('bub',`translate(470 820) scale(${hv})`);
  tr('fe',`translate(470 1100) rotate(-4) scale(${t>B.fark?hv*L(1.8,1,io(p(t,B.fark,.15))):0})`);
  // alıcıysan
  const a2=W(B.alici,B.satici+.2); tr('tagA',`translate(470 560) scale(${a2})`);
  tr('hp',`translate(280 850) scale(${a2*.9})`); tr('lst',`translate(680 900) rotate(4) scale(${t>B.alici+1.8?a2*ob(p(t,B.alici+1.8,.35))*.9:0})`);
  // satıcıysan
  const s2=W(B.satici,B.yarin+.2); tr('tagS',`translate(470 560) scale(${s2})`); tr('vol',`translate(470 880) scale(${s2})`);
  const vk=io(p(t,B.kis+.3,1)); const vx=L(140,-100,vk); $('volF').setAttribute('width',vx+240); $('volK').setAttribute('cx',vx);
  $('volT').textContent=vk>.5?'SES: KISIK ✓':'SES: YÜKSEK';
  __TAIL__
}
'''.replace('__HEAD__', JS_HEAD).replace('__TAIL__', JS_TAIL)
make(out, B, segs, REPL, 'TAKTİK · 29', 'FİŞ 0025', 'MÜZİK TEMPOSU', 'Market müziği', 'neden yavaş?', SVG, SCENE)

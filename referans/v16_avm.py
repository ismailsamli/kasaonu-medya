from base import build
import json, sys, re
from pathlib import Path

B = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {}
SENTS = json.load(open('/tmp/avm_sents.json'))
KEYS = ['q','start','duvar','pencere','plan','soz','gruen','cephe','avust','bir','tabela','yok','kaybet','etki','ilginc','alici','poset','satici','kose','soru','sik','yaz','gonder','takip','yarin']

# Altyazı: her cümleyi 2-4 kelimelik parçalara böl, cümle süresine harf oranıyla yay
def subs():
    out = []
    starts = [B[k] for k in KEYS] + [B['END'] - 0.6]
    for i, s in enumerate(SENTS):
        a, b = starts[i], starts[i + 1] - 0.12
        for a_,b_ in [("bin dokuz yüz elli altıda","1956'da"),("dört AVM'yi","4 AVM'yi"),("sekiz dükkân","8 dükkân"),("üç dakikada","3 dakikada"),("bir tane saat","1 tane saat"),("iki damga","2 damga")]: s=s.replace(a_,b_)
        words = s.split()
        chunks, cur = [], []
        for w in words:
            cur.append(w)
            if len(cur) >= 3 or w[-1] in ',:.?' and len(cur) >= 2:
                chunks.append(' '.join(cur)); cur = []
        if cur:
            if chunks and len(cur) == 1: chunks[-1] += ' ' + cur[0]
            else: chunks.append(' '.join(cur))
        tot = sum(len(c) for c in chunks); t = a
        for c in chunks:
            d = (b - a) * len(c) / tot
            out.append([round(t, 2), round(t + d, 2), c]); t += d
    return out

INK, OR, PAP, NAV, YEL, GRN, BLU, TER = '#1c1b18', '#ff5a1f', '#FFF8EB', '#243139', '#E8B65C', '#8A9B7C', '#7C9DA5', '#C56B50'

SVG = r'''
   <defs>
    <g id="bagG"><path d="M-90 -60 h180 l20 170 h-220z" fill="#C56B50"/><path d="M-45 -60 q0 -60 45 -60 q45 0 45 60" stroke="#1c1b18" stroke-width="10" fill="none"/></g>
    <g id="mallG"><rect x="-70" y="-50" width="140" height="100" fill="#b9b4a8"/><rect x="-18" y="10" width="36" height="40" fill="#243139"/><text y="-12" font-size="20" text-anchor="middle" fill="#1c1b18">AVM</text></g>
   </defs>
   <g id="pill" transform="translate(470 92)"><rect x="-230" y="-26" width="460" height="52" rx="26" fill="#1c1b18"/><text y="10" font-size="26" text-anchor="middle" fill="#FFF8EB">SONDA: ÇIKIŞ YOLU ↓</text></g>
   <g id="ck"><g filter="url(#ps)"><circle r="150" fill="#FFF8EB" stroke="#1c1b18" stroke-width="10"/></g>
     <g stroke="#1c1b18" stroke-width="8"><path d="M0 -132 V-112 M0 132 V112 M-132 0 H-112 M132 0 H112"/></g>
     <path id="ckh" d="M0 0 V-70" stroke="#1c1b18" stroke-width="14" stroke-linecap="round"/><path id="ckm" d="M0 0 V-110" stroke="#ff5a1f" stroke-width="8" stroke-linecap="round"/><circle r="12" fill="#1c1b18"/>
     <text id="ckq" x="170" y="-90" font-size="140" fill="#ff5a1f">?</text></g>
   <g id="wall"><rect x="110" y="500" width="720" height="762" fill="#e3ded2"/><path d="M110 500 H830" stroke="#b9b4a8" stroke-width="8"/>
     <g id="wClock" transform="translate(470 700)"><circle r="110" fill="none" stroke="#8c8880" stroke-width="6" stroke-dasharray="14 12"/><circle cy="-112" r="8" fill="#1c1b18"/>
       <path id="wX1" d="M-80 -80 L80 80 M80 -80 L-80 80" stroke="#ff5a1f" stroke-width="16" stroke-linecap="round"/><text y="170" font-size="34" text-anchor="middle" fill="#1c1b18">SAAT YOK</text></g>
     <g id="wWin" transform="translate(470 1060)"><rect x="-160" y="-100" width="320" height="180" fill="none" stroke="#8c8880" stroke-width="6" stroke-dasharray="14 12"/><path d="M0 -100 V80 M-160 -10 H160" stroke="#8c8880" stroke-width="4" stroke-dasharray="10 10"/>
       <path id="wX2" d="M-110 -70 L110 50 M110 -70 L-110 50" stroke="#ff5a1f" stroke-width="16" stroke-linecap="round"/><text y="140" font-size="34" text-anchor="middle" fill="#1c1b18">PENCERE YOK</text></g></g>
   <g id="stPlan"><g filter="url(#ps)"><rect x="-200" y="-70" width="400" height="140" fill="#ff5a1f" stroke="#1c1b18" stroke-width="6"/></g><text y="26" font-size="78" text-anchor="middle" fill="#FFF8EB" letter-spacing="10">PLAN</text></g>
   <g id="yr"><text y="0" font-size="170" text-anchor="middle" fill="#1c1b18">1956</text><text y="56" font-size="30" text-anchor="middle" fill="#8c8880">İLK KAPALI AVM · VICTOR GRUEN</text></g>
   <g id="bld"><g filter="url(#ps)"><rect x="-300" y="-170" width="600" height="300" fill="#b9b4a8"/><rect x="-330" y="-190" width="660" height="30" fill="#8c8880"/><rect x="-45" y="40" width="90" height="90" fill="#243139"/></g>
     <g id="glow"><rect x="-270" y="-140" width="540" height="160" fill="#243139"/><g id="spk"></g><text y="-50" font-size="30" text-anchor="middle" fill="#E8B65C">IŞILTI İÇERİDE</text></g></g>
   <g id="malls"><g id="m0" transform="translate(170 900)"><use href="#mallG"/></g><g id="m1" transform="translate(370 900)"><use href="#mallG"/></g><g id="m2" transform="translate(570 900)"><use href="#mallG"/></g><g id="m3" transform="translate(770 900)"><use href="#mallG"/></g>
     <g id="mc" transform="translate(570 800)"><circle r="34" fill="#FFF8EB" stroke="#ff5a1f" stroke-width="7"/><path d="M0 0 V-22 M0 0 H16" stroke="#1c1b18" stroke-width="6"/></g>
     <text id="eq" x="470" y="1130" font-size="74" text-anchor="middle" fill="#1c1b18">4 AVM = <tspan fill="#ff5a1f">1 SAAT</tspan></text>
     <text id="au" x="470" y="760" font-size="30" text-anchor="middle" fill="#8c8880">AVUSTRALYA · TÜKETİCİ DERNEĞİ</text></g>
   <g id="mz"><path id="mzp" d="M180 1180 H360 V980 H220 V820 H520 V1060 H680 V760" stroke="#ff5a1f" stroke-width="12" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
     <circle cx="180" cy="1180" r="22" fill="#1c1b18"/><text x="180" y="1240" font-size="28" text-anchor="middle" fill="#1c1b18">A</text>
     <g transform="translate(680 760)"><rect x="-60" y="-80" width="120" height="70" fill="#243139"/><text y="-36" font-size="26" text-anchor="middle" fill="#FFF8EB">B</text></g>
     <g id="sw" transform="translate(720 1120)"><g filter="url(#ps)"><circle r="80" fill="#FFF8EB" stroke="#1c1b18" stroke-width="8"/></g><rect x="-14" y="-104" width="28" height="22" fill="#1c1b18"/><text id="swt" y="16" font-size="40" text-anchor="middle" fill="#ff5a1f">0:00</text></g>
     <text x="380" y="740" font-size="34" text-anchor="middle" fill="#1c1b18">8 DÜKKÂN ÖTESİ</text></g>
   <g id="yk"><g id="y0" transform="translate(220 900)"><circle r="80" fill="#FFF8EB" stroke="#1c1b18" stroke-width="8"/><path d="M0 0 V-50 M0 0 H36" stroke="#1c1b18" stroke-width="10"/><text y="140" font-size="30" text-anchor="middle" fill="#1c1b18">SAAT</text></g>
     <g id="y1" transform="translate(470 900)"><circle r="50" fill="#E8B65C"/><g stroke="#E8B65C" stroke-width="10"><path d="M0 -80 V-64 M0 80 V64 M-80 0 H-64 M80 0 H64 M-57 -57 L-45 -45 M57 57 L45 45 M57 -57 L45 -45 M-57 57 L-45 45"/></g><text y="140" font-size="30" text-anchor="middle" fill="#1c1b18">GÖKYÜZÜ</text></g>
     <g id="y2" transform="translate(720 900)"><path d="M-70 40 H70 M40 10 L70 40 L40 70" stroke="#1c1b18" stroke-width="12" fill="none"/><text y="140" font-size="30" text-anchor="middle" fill="#1c1b18">DÜZ YOL</text></g>
     <path id="x0" d="M160 840 L280 960 M280 840 L160 960" stroke="#ff5a1f" stroke-width="16" stroke-linecap="round"/><path id="x1" d="M410 840 L530 960 M530 840 L410 960" stroke="#ff5a1f" stroke-width="16" stroke-linecap="round"/><path id="x2" d="M660 840 L780 960 M780 840 L660 960" stroke="#ff5a1f" stroke-width="16" stroke-linecap="round"/></g>
   <g id="kb"><g transform="translate(470 1080) scale(1.6)"><use href="#bagG"/></g><g id="itms"></g>
     <g id="kc" transform="translate(470 700)"><circle r="90" fill="#FFF8EB" stroke="#1c1b18" stroke-width="8"/><path id="kch" d="M0 0 V-60" stroke="#ff5a1f" stroke-width="8" stroke-linecap="round"/></g></g>
   <g id="ge"><g filter="url(#ps)"><rect x="-300" y="-80" width="600" height="160" fill="#1c1b18" stroke="#ff5a1f" stroke-width="8"/></g><text y="24" font-size="66" text-anchor="middle" fill="#FFF8EB" letter-spacing="4">GRUEN ETKİSİ</text></g>
   <g id="qt"><g filter="url(#ps)"><rect x="-330" y="-170" width="660" height="340" fill="#FFF8EB"/></g><text x="-290" y="-80" font-size="120" fill="#ff5a1f">“</text>
     <text y="20" font-size="64" text-anchor="middle" fill="#1c1b18">Fikrimi bozdular.</text><text y="110" font-size="30" text-anchor="middle" fill="#8c8880">— Victor Gruen, AVM'nin mucidi</text></g>
   <g id="tagA"><rect x="-200" y="-36" width="400" height="72" fill="#8A9B7C"/><text y="14" font-size="40" text-anchor="middle" fill="#FFF8EB">ALICIYSAN</text></g>
   <g id="ph"><g filter="url(#ps)"><rect x="-150" y="-280" width="300" height="560" rx="38" fill="#1c1b18"/></g><rect x="-132" y="-260" width="264" height="520" rx="24" fill="#243139"/>
     <text y="-160" font-size="30" text-anchor="middle" fill="#b9d0ea">ALARM</text><text id="alt" y="-80" font-size="62" text-anchor="middle" fill="#FFF8EB">1:00:00</text>
     <g id="bell" transform="translate(0 80)"><path d="M-60 40 q0 -110 60 -110 q60 0 60 110z" fill="#E8B65C"/><rect x="-70" y="40" width="140" height="16" fill="#E8B65C"/><circle cy="74" r="14" fill="#E8B65C"/></g>
     <g id="pBag" transform="translate(0 150) scale(.8)"><use href="#bagG"/><text y="70" font-size="40" text-anchor="middle" fill="#FFF8EB">?</text></g></g>
   <g id="tagS"><rect x="-200" y="-36" width="400" height="72" fill="#243139"/><text y="14" font-size="40" text-anchor="middle" fill="#FFF8EB">SATICIYSAN</text></g>
   <g id="sat"><g id="noRush"><g filter="url(#ps)"><rect x="-290" y="-70" width="580" height="140" fill="#FFF8EB" stroke="#1c1b18" stroke-width="6"/></g><text y="20" font-size="52" text-anchor="middle" fill="#1c1b18">ACELE ETTİRME</text></g>
     <g id="bench" transform="translate(0 300)"><g filter="url(#ps)"><rect x="-200" y="-110" width="400" height="70" rx="20" fill="#C56B50"/><rect x="-220" y="-40" width="440" height="60" rx="16" fill="#C56B50"/></g><rect x="-200" y="20" width="22" height="70" fill="#1c1b18"/><rect x="178" y="20" width="22" height="70" fill="#1c1b18"/>
       <text y="150" font-size="32" text-anchor="middle" fill="#1c1b18">KALAN MÜŞTERİ = ALAN MÜŞTERİ</text></g></g>
   <g id="poll"><g filter="url(#ps)"><rect x="-320" y="-260" width="640" height="520" fill="#FFF8EB"/></g><text y="-190" font-size="36" text-anchor="middle" fill="#1c1b18">AVM'DE EN FAZLA KAÇ SAAT?</text>
     <g id="o0" transform="translate(0 -90)"><rect x="-270" y="-40" width="540" height="80" rx="14" fill="#e3ded2"/><text x="-240" y="14" font-size="38" fill="#1c1b18">A) 1 SAAT</text></g>
     <g id="o1" transform="translate(0 10)"><rect x="-270" y="-40" width="540" height="80" rx="14" fill="#e3ded2"/><text x="-240" y="14" font-size="38" fill="#1c1b18">B) 3 SAAT</text></g>
     <g id="o2" transform="translate(0 110)"><rect x="-270" y="-40" width="540" height="80" rx="14" fill="#e3ded2"/><text x="-240" y="14" font-size="38" fill="#1c1b18">C) HİÇ BİLMİYORUM</text></g>
     <g id="cm" transform="translate(0 210)"><path d="M-150 -26 h300 v52 h-200 l-30 26 v-26 h-70z" fill="#ff5a1f"/><text y="10" font-size="28" text-anchor="middle" fill="#FFF8EB">YORUMA YAZ</text></g></g>
   <g id="snd"><path id="plane" d="M-120 0 L120 -80 L40 90 L10 20z" fill="#ff5a1f" stroke="#1c1b18" stroke-width="6"/><text y="190" font-size="40" text-anchor="middle" fill="#1c1b18">AVM'DEN ÇIKAMAYANA</text><text y="250" font-size="56" text-anchor="middle" fill="#ff5a1f">GÖNDER</text></g>
   <g id="fol"><g filter="url(#ps)"><rect x="-320" y="-220" width="640" height="440" rx="24" fill="#FFF8EB"/></g><circle cy="-110" r="70" fill="#ff5a1f"/><text y="-90" font-size="54" text-anchor="middle" fill="#FFF8EB">KÖ</text>
     <text y="10" font-size="44" text-anchor="middle" fill="#1c1b18">@kasaonu.tr</text><g id="fb"><rect x="-200" y="50" width="400" height="80" rx="16" fill="#3b82f6"/><text y="104" font-size="40" text-anchor="middle" fill="#fff">+ TAKİP ET</text></g>
     <text y="180" font-size="30" text-anchor="middle" fill="#8c8880">HER GÜN 1 KASA ÖNÜ TAKTİĞİ</text></g>
   <g id="yrn"><g filter="url(#ps)"><rect x="-320" y="-230" width="640" height="460" fill="#243139"/></g><text y="-150" font-size="44" text-anchor="middle" fill="#E8B65C">YARIN</text>
     <g transform="translate(0 -20)"><rect x="-260" y="-70" width="520" height="140" rx="14" fill="#FFF8EB"/><g id="dm"></g></g>
     <text y="140" font-size="40" text-anchor="middle" fill="#FFF8EB">Neden 2 damga <tspan fill="#ff5a1f">hediye?</tspan></text></g>
'''

SCENE = r'''
const B=__B__; const END=B.END; const SUBS=__SUBS__;
window.NOLOOP=true;
window.V={sfx:[[0.02,'thud'],[B.duvar+.1,'pop'],[B.pencere+.1,'pop'],[B.plan,'thud'],[B.soz+.1,'whoosh'],[B.gruen+.1,'whoosh'],[B.cephe+.2,'ticks'],[B.avust+.1,'whoosh'],[B.avust+.4,'pop'],[B.avust+.8,'pop'],[B.avust+1.2,'pop'],[B.avust+1.6,'pop'],[B.bir+.2,'thud'],
 [B.tabela+.1,'whoosh'],[B.tabela+.5,'ticks'],[B.yok+.1,'scratch'],[B.yok+.9,'scratch'],[B.yok+1.7,'scratch'],[B.kaybet+.2,'ticks'],[B.etki,'thud'],[B.ilginc+.1,'whoosh'],[B.alici+.1,'whoosh'],[B.poset+.1,'ticks'],[B.satici+.1,'whoosh'],[B.kose+.2,'pop'],
 [B.soru+.1,'whoosh'],[B.sik+.1,'pop'],[B.sik+.7,'pop'],[B.sik+1.3,'pop'],[B.yaz+.1,'pop'],[B.gonder+.1,'whoosh'],[B.takip+.1,'whoosh'],[B.takip+.8,'pop'],[B.yarin+.1,'whoosh'],[B.yarin+.8,'pop']]};
const LINES=[[B.start,B.plan-.1,'Duvarda<br><span class="o">saat yok.</span>'],[B.plan,B.gruen-.1,'Tesadüf değil.<br><span class="o">Plan.</span>'],
 [B.gruen,B.avust-.1,'<span class="o">1956:</span><br>ilk kapalı AVM.'],[B.avust,B.tabela-.1,'4 AVM,<br><span class="o">1 saat.</span>'],[B.tabela,B.yok-.1,'8 dükkân,<br><span class="o">3 dakika.</span>'],
 [B.yok,B.ilginc-.1,'Zaman kaybolur,<br><span class="o">sepet dolar.</span>'],[B.ilginc,B.alici-.1,'Mucidi bile<br><span class="o">pişman.</span>'],
 [B.alici,B.satici-.1,'<span class="o">Alıcıysan:</span><br>alarm kur.'],[B.satici,B.soru-.1,'<span class="o">Satıcıysan:</span><br>acele ettirme.'],
 [B.soru,B.gonder-.1,'Sen kaç saat<br><span class="o">kaldın?</span>'],[B.gonder,B.takip-.1,'Bunu birine<br><span class="o">gönder.</span>'],[B.takip,B.yarin-.1,'Her gün<br><span class="o">1 taktik.</span>'],[B.yarin,END,'Yarın:<br><span class="o">2 damga sırrı.</span>']];
const BIG=[[B.etki-.1,B.ilginc-.1]], HITS=[0.02,B.plan,B.etki];
$('spk').innerHTML=Array.from({length:14},(_,i)=>`<path id="sp${i}" d="M0 -14 L4 -4 L14 0 L4 4 L0 14 L-4 4 L-14 0 L-4 -4z" fill="#E8B65C" transform="translate(${-240+(i%7)*80} ${-110+Math.floor(i/7)*70+(i%2)*20})"/>`).join('');
$('itms').innerHTML=Array.from({length:6},(_,i)=>`<rect id="it${i}" x="-30" y="-30" width="60" height="60" rx="8" fill="${['#7C9DA5','#E8B65C','#8A9B7C','#ff5a1f','#243139','#b9b4a8'][i]}"/>`).join('');
$('dm').innerHTML=Array.from({length:10},(_,i)=>`<circle id="d${i}" cx="${-216+i*48}" cy="0" r="18" fill="none" stroke="#243139" stroke-width="5"/>`).join('');
function scene(t){
  const W=(a,b)=>(t<a||t>b)?0:ob(p(t,a,.35))*(1-io(p(t,b-.25,.25)));
  const show=(id,on)=>op(id,on?1:0);
  // kanca altı: soru işaretli saat
  const hk=t<B.duvar?1-io(p(t,B.duvar-.2,.3)):0;
  tr('ck',`translate(470 900) scale(${hk}) rotate(${Math.sin(t*2.5)*5})`);
  tr('ckm',`rotate(${t*140})`); tr('ckh',`rotate(${t*12+40})`);
  // duvar: saat yok, pencere yok
  const wv=W(B.duvar,B.gruen+.25); op('wall',wv>0?1:0); tr('wall',`translate(0 ${(1-wv)*600})`);
  $('wX1').style.strokeDasharray='240'; $('wX1').style.strokeDashoffset=240*(1-p(t,B.duvar+.3,.35));
  op('wWin',t>B.pencere-.05?1:0); $('wX2').style.strokeDasharray='260'; $('wX2').style.strokeDashoffset=260*(1-p(t,B.pencere+.3,.35));
  tr('stPlan',`translate(470 880) rotate(-9) scale(${t>B.plan&&t<B.gruen+.2?L(2,1,io(p(t,B.plan,.15)))*(1-io(p(t,B.gruen,.2))):0})`);
  // sonda çıkış yolu rozeti
  const pv=t>B.soz+.4&&t<B.alici; tr('pill',`translate(470 ${92+(pv?0:-200)*(1-0)}) scale(${pv?ob(p(t,B.soz+.4,.4))*(1-io(p(t,B.alici-.3,.3))):0})`);
  // 1956 + bina
  tr('yr',`translate(470 640) scale(${W(B.gruen,B.avust+.25)})`);
  tr('bld',`translate(470 1080) scale(${W(B.gruen+.3,B.avust+.25)})`);
  const gl=p(t,B.cephe,.5); op('glow',t>B.cephe?gl:0);
  for(let i=0;i<14;i++) op('sp'+i,t>B.cephe+.3+i*.08?(.5+.5*Math.abs(Math.sin(t*4+i))):0);
  // Avustralya: 4 AVM, 1 saat
  const mv=W(B.avust,B.tabela+.25); op('malls',mv>0?1:0); op('au',mv);
  for(let i=0;i<4;i++) tr('m'+i,`translate(${170+i*200} 900) scale(${t>B.avust+.4+i*.4&&t<B.tabela+.25?ob(p(t,B.avust+.4+i*.4,.3))*(1-io(p(t,B.tabela,.25))):0})`);
  tr('mc',`translate(570 790) scale(${t>B.bir+.1&&t<B.tabela+.25?ob(p(t,B.bir+.1,.35))*(1-io(p(t,B.tabela,.25))):0})`);
  op('eq',t>B.bir+.3&&t<B.tabela?1:0);
  // labirent + kronometre
  const zv=W(B.tabela,B.yok+.25); op('mz',zv>0?1:0); tr('mz',`translate(${470*(1-zv)} ${900*(1-zv)}) scale(${zv})`);
  const mp=$('mzp'); const ml=mp.getTotalLength(); mp.style.strokeDasharray=ml; mp.style.strokeDashoffset=ml*(1-p(t,B.tabela+.3,(B.yok-B.tabela)-.8));
  const sec=Math.round(180*p(t,B.tabela+.3,(B.yok-B.tabela)-.8)); $('swt').textContent=Math.floor(sec/60)+':'+String(sec%60).padStart(2,'0');
  // saat yok, gökyüzü yok, yol dolambaçlı
  const yv=W(B.yok,B.kaybet+.25); op('yk',yv>0?1:0); tr('yk',`translate(${470*(1-yv)} ${900*(1-yv)}) scale(${yv})`);
  for(let i=0;i<3;i++){const x=$('x'+i); x.style.strokeDasharray='360'; x.style.strokeDashoffset=360*(1-p(t,B.yok+.2+i*.8,.3))}
  // zaman kaybı + poşet dolar
  const kv=W(B.kaybet,B.etki+.25); op('kb',kv>0?1:0); tr('kb',`translate(0 ${(1-kv)*500})`);
  tr('kch',`rotate(${t*360})`);
  for(let i=0;i<6;i++){const a=B.kaybet+.3+i*.35, k=oc(p(t,a,.35)); tr('it'+i,`translate(${410+(i%3)*60} ${L(560,1010-Math.floor(i/3)*40,k)}) rotate(${i*17})`); op('it'+i,t>a?1:0)}
  tr('ge',`translate(470 900) rotate(-5) scale(${t>B.etki&&t<B.ilginc+.2?L(2,1,io(p(t,B.etki,.15)))*(1-io(p(t,B.ilginc,.2))):0})`);
  tr('qt',`translate(470 880) scale(${W(B.ilginc+.2,B.alici+.25)})`);
  // alıcıysan: alarm
  const av=W(B.alici,B.satici+.25);
  tr('tagA',`translate(470 560) scale(${av})`); tr('ph',`translate(470 ${L(1900,960,av)}) rotate(${t>B.poset?Math.sin(t*40)*3:0})`); op('ph',av>0?1:0);
  const rem=Math.max(0,3600-Math.floor(3600*p(t,B.alici+.6,B.poset-B.alici-.6))); $('alt').textContent=t>=B.poset?'ÇALIYOR':(Math.floor(rem/3600)+':'+String(Math.floor(rem%3600/60)).padStart(2,'0')+':'+String(rem%60).padStart(2,'0'));
  $('alt').setAttribute('fill',t>=B.poset?'#ff5a1f':'#FFF8EB');
  tr('bell',`translate(0 40) rotate(${t>B.poset?Math.sin(t*30)*14:0})`); op('bell',t<B.poset+.8?1:0);
  tr('pBag',`translate(0 120) scale(${t>B.poset+.6?.8*ob(p(t,B.poset+.6,.35)):0})`);
  // satıcıysan
  const sv=W(B.satici,B.soru+.25); tr('tagS',`translate(470 560) scale(${sv})`); op('sat',sv>0?1:0);
  tr('noRush',`translate(0 0) scale(${sv})`); tr('sat',`translate(470 760)`); tr('bench',`translate(0 330) scale(${t>B.kose?ob(p(t,B.kose,.35))*sv:0})`);
  // anket
  const qv=W(B.soru,B.gonder+.25); tr('poll',`translate(470 900) scale(${qv})`);
  for(let i=0;i<3;i++){const a=B.sik+.1+i*.6; const on=t>a&&t<a+.6; tr('o'+i,`translate(0 ${-90+i*100}) scale(${on?1.06:1})`); $('o'+i).querySelector('rect').setAttribute('fill',on?'#E8B65C':'#e3ded2')}
  tr('cm',`translate(0 210) scale(${t>B.yaz?ob(p(t,B.yaz,.35)):0})`);
  // gönder
  const gv=W(B.gonder,B.takip+.25); op('snd',gv>0?1:0); tr('snd',`translate(470 860) scale(${gv})`);
  tr('plane',`translate(${L(-260,60,oc(p(t,B.gonder+.1,.8)))} ${L(120,-40,oc(p(t,B.gonder+.1,.8)))}) rotate(-8)`);
  // takip
  tr('fol',`translate(470 900) scale(${W(B.takip,B.yarin+.25)})`);
  tr('fb',`scale(${t>B.takip+.7?L(1.12,1,oc(p(t,B.takip+.7,.3)))+Math.sin(t*6)*.015:1})`); $('fb').style.transformBox='fill-box'; $('fb').style.transformOrigin='center';
  // yarın
  tr('yrn',`translate(470 900) scale(${t>B.yarin?ob(p(t,B.yarin,.4)):0})`);
  for(let i=0;i<10;i++){const f=i<2&&t>B.yarin+.8+i*.3; $('d'+i).setAttribute('fill',f?'#ff5a1f':'none')}
  // altyazı
  const sb=$('sub'); let st='';for(const [a,b,x] of SUBS) if(t>=a&&t<b){st=x}
  if(sb.dataset.t!==st){sb.textContent=st;sb.dataset.t=st} sb.style.opacity=(st&&t>=B.start)?1:0;
}
'''

out = sys.argv[2] if len(sys.argv) > 2 else 'avm01'
path = f'/home/claude/kasaonu-medya/referans/sablonlar/{out}/index.html'
build(path, 'TAKTİK · 25', 'FİŞ 0021', 'GRUEN ETKİSİ', '1 TAKTİK',
      "AVM'de en son ne zaman", 'saat gördün?', SVG, SCENE.replace('__B__', json.dumps(B)).replace('__SUBS__', json.dumps(subs(), ensure_ascii=False)))
# v3 formatı: döngü yok (sonda kanca dönmez), altyazı bandı
h = Path(path).read_text(encoding='utf-8')
h = h.replace("hk.style.display=(t<B.start+.3||t>=END-HK)?'block':'none';", "hk.style.display=(t<B.start+.3)?'block':'none';")
h = h.replace("push=io(p(t,END-HK,HK));", "push=0;")
h = h.replace("tA.style.opacity=txt?cl(p(t,t0,.1)*2)*(1-p(t,END-HK-.15,.15)):0;", "tA.style.opacity=txt?cl(p(t,t0,.1)*2):0;")
h = h.replace('<div id="tA"', '<div id="sub" class="abs gk" style="left:60px;right:60px;bottom:120px;text-align:center;font-size:50px;letter-spacing:-1px;line-height:1.1;color:#FFF8EB;background:#1c1b18;padding:18px 24px;border-radius:10px"></div>\n  <div id="tA"')
Path(path).write_text(h, encoding='utf-8')
print('ok')

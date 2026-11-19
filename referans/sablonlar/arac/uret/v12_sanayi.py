from base import build
import json, sys

B = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {}

SVG = r'''
   <g id="car"><g filter="url(#ps)"><path d="M-270 -40 q0 -34 34 -40 l70 -12 l76 -70 q18 -16 44 -16 h170 q28 0 42 16 l64 70 l58 12 q32 8 32 40 v40 h-590z" fill="#7C9DA5"/>
     <path d="M-150 -96 l56 -50 q10 -8 24 -8 h66 v58z M20 -96 v-58 h70 q14 0 22 8 l46 50z" fill="#f3efe4"/><rect x="230" y="-64" width="34" height="16" fill="#E8B65C"/></g>
     <g filter="url(#ps)"><circle cx="-160" cy="0" r="52" fill="#1c1b18"/><circle cx="-160" cy="0" r="22" fill="#e3ded2"/><circle cx="170" cy="0" r="52" fill="#1c1b18"/><circle cx="170" cy="0" r="22" fill="#e3ded2"/></g></g>
   <g id="tag"><path d="M0 -150 V-40" stroke="#1c1b18" stroke-width="5"/><g filter="url(#ps)"><path d="M-110 -40 h220 v120 h-220z" fill="#FFF8EB"/><circle cx="0" cy="-20" r="9" fill="#f3efe4" stroke="#1c1b18" stroke-width="4"/></g><text y="44" font-size="46" text-anchor="middle" fill="#ff5a1f">??? TL</text></g>
   <g id="oil" filter="url(#ps)"><path d="M-70 0 v-150 q0 -20 20 -20 h60 l40 -40 h30 v40 q20 0 20 20 v150z" fill="#E8B65C"/><rect x="-50" y="-120" width="100" height="70" fill="#FFF8EB"/><text y="-74" font-size="30" text-anchor="middle" fill="#1c1b18">YAĞ</text></g>
   <g id="bub" filter="url(#ps)"><path d="M-190 -60 h380 v100 h-300 l-40 40 v-40 h-40z" fill="#FFF8EB"/><text y="6" font-size="36" text-anchor="middle" fill="#1c1b18">"SADECE YAĞ"</text></g>
   <g id="rcp" filter="url(#ps)"></g>
   <g id="yok"><g filter="url(#ps)"><rect x="-210" y="-60" width="420" height="120" fill="#ff5a1f" stroke="#1c1b18" stroke-width="6"/></g><text y="22" font-size="58" fill="#FFF8EB" text-anchor="middle" letter-spacing="4">BELGE YOK</text></g>
   <g id="fis" filter="url(#ps)"><rect x="-200" y="-300" width="400" height="560" fill="#FFF8EB"/><text y="-240" font-size="32" text-anchor="middle" fill="#1c1b18">SERVİS FİŞİ</text>
     <path d="M-160 -210 H160" stroke="#b9b4a8" stroke-width="4" stroke-dasharray="10 8"/>
     <g fill="#e3ded2"><rect x="-160" y="-180" width="320" height="18"/><rect x="-160" y="-140" width="260" height="18"/><rect x="-160" y="-100" width="300" height="18"/><rect x="-160" y="-60" width="220" height="18"/><rect x="-160" y="-20" width="280" height="18"/></g>
     <path d="M40 180 q30 -40 60 0 t60 -10" stroke="#243139" stroke-width="5" fill="none"/></g>
   <g id="zor"><rect x="-190" y="-50" width="380" height="100" fill="none" stroke="#ff5a1f" stroke-width="10"/><text y="22" font-size="54" fill="#ff5a1f" text-anchor="middle" letter-spacing="6">ZORUNLU</text></g>
   <g id="prn" filter="url(#ps)"><rect x="-110" y="-60" width="220" height="120" rx="14" fill="#243139"/><rect x="-80" y="-90" width="160" height="40" fill="#e3ded2"/><rect id="prnP" x="-80" y="40" width="160" height="0" fill="#FFF8EB"/><text x="0" y="100" font-size="26" text-anchor="middle" fill="#1c1b18" id="prnT">KÂĞIT</text></g>
   <g id="chk" filter="url(#ps)"><rect x="-330" y="-200" width="660" height="400" fill="#FFF8EB"/><text x="-290" y="-130" font-size="30" fill="#8c8880">İŞE BAŞLAMADAN</text>
     <rect x="-290" y="-80" width="64" height="64" fill="none" stroke="#1c1b18" stroke-width="6"/><path id="ck1" d="M-280 -50 l20 22 l40 -50" stroke="#ff5a1f" stroke-width="12" fill="none" stroke-linecap="round"/><text x="-200" y="-34" font-size="40" fill="#1c1b18">FİYAT YAZILI</text>
     <rect x="-290" y="40" width="64" height="64" fill="none" stroke="#1c1b18" stroke-width="6"/><path id="ck2" d="M-280 70 l20 22 l40 -50" stroke="#ff5a1f" stroke-width="12" fill="none" stroke-linecap="round"/><text x="-200" y="86" font-size="40" fill="#1c1b18">ESKİ PARÇA GERİ</text></g>
   <g id="pad" filter="url(#ps)"><path d="M-90 0 q0 -60 90 -70 q90 10 90 70 v20 h-180z" fill="#8c8880"/><path d="M-80 0 q0 -48 80 -58 q80 10 80 58" fill="none" stroke="#1c1b18" stroke-width="5"/></g>
   <g id="usta"><g filter="url(#ps)"><circle cx="0" cy="-120" r="70" fill="#e9c9a6"/><path d="M-76 -136 q4 -70 76 -72 q72 2 76 72z" fill="#243139"/><rect x="-90" y="-146" width="130" height="18" fill="#243139"/><path d="M-120 100 q0 -110 120 -110 q120 0 120 110z" fill="#7C9DA5"/></g>
     <g transform="translate(110 40) rotate(-35)" filter="url(#ps)"><rect x="-12" y="-90" width="24" height="150" fill="#8c8880"/><path d="M-36 -90 a36 36 0 1 1 72 0 l-18 0 v-30 h-36 v30z" fill="#8c8880"/></g></g>
   <g id="ubub" filter="url(#ps)"><path d="M-170 -60 h340 v100 h-100 l40 40 l-80 -40 h-160z" fill="#ff5a1f"/><text y="6" font-size="40" text-anchor="middle" fill="#FFF8EB">FİŞ VAR MI?</text></g>
   <g id="ph"><g filter="url(#ps)"><rect x="-190" y="-360" width="380" height="720" rx="40" fill="#1c1b18"/><rect x="-172" y="-330" width="344" height="660" rx="24" fill="#FFF8EB"/></g>
     <rect x="-172" y="-330" width="344" height="80" fill="#243139"/><text y="-280" font-size="28" text-anchor="middle" fill="#FFF8EB" letter-spacing="3">OTOİŞLERİM</text>
     <g id="sc1"><g id="rs"><rect x="-140" y="-210" width="280" height="170" rx="10" fill="#C56B50"/><rect x="-120" y="-190" width="90" height="110" fill="#e3ded2"/><g fill="#FFF8EB"><rect x="-14" y="-186" width="130" height="14"/><rect x="-14" y="-156" width="100" height="14"/><rect x="-14" y="-126" width="120" height="14"/></g><text x="0" y="-60" font-size="20" text-anchor="middle" fill="#FFF8EB">RUHSAT</text></g>
       <path id="frm" d="M-156 -170 v-56 h56 M100 -226 h56 v56 M156 -24 v56 h-56 M-100 32 h-56 v-56" stroke="#ff5a1f" stroke-width="8" fill="none"/>
       <g id="flds">${''}</g></g>
     <g id="sc2"><circle cx="0" cy="-130" r="80" fill="#ff5a1f"/><rect x="-22" y="-182" width="44" height="80" rx="22" fill="#FFF8EB"/><path d="M-40 -126 q0 44 40 44 q40 0 40 -44 M0 -82 v26" stroke="#FFF8EB" stroke-width="8" fill="none"/>
       <g id="wv"></g><text id="say" y="170" font-size="28" text-anchor="middle" fill="#1c1b18"></text></g>
     <g id="sc3"><g id="pdf"><rect x="-110" y="-220" width="220" height="280" fill="#FFF8EB" stroke="#1c1b18" stroke-width="5"/><rect x="-110" y="-220" width="220" height="60" fill="#ff5a1f"/><text y="-180" font-size="30" text-anchor="middle" fill="#FFF8EB">TEKLİF</text><g fill="#e3ded2"><rect x="-80" y="-130" width="160" height="14"/><rect x="-80" y="-100" width="120" height="14"/><rect x="-80" y="-70" width="150" height="14"/></g><text y="30" font-size="26" text-anchor="middle" fill="#1c1b18">.PDF</text></g>
       <g id="snd"><rect x="-120" y="120" width="240" height="80" rx="40" fill="#8A9B7C"/><text y="172" font-size="30" text-anchor="middle" fill="#FFF8EB">GÖNDER</text></g></g>
   </g>
   <g id="pl" filter="url(#ps)"><path d="M-70 10 L80 -40 L-20 50Z" fill="#ff5a1f"/><path d="M-20 50 L80 -40 L0 20Z" fill="#C56B50"/></g>
   <g id="ok"><g filter="url(#ps)"><rect x="-260" y="-200" width="520" height="400" fill="#FFF8EB"/></g><text x="-210" y="-110" font-size="40" fill="#1c1b18">TEKLİF</text><text x="-210" y="0" font-size="40" fill="#1c1b18">ONAY</text><text x="-210" y="110" font-size="40" fill="#1c1b18">FİŞ</text>
     <g stroke="#8A9B7C" stroke-width="14" fill="none" stroke-linecap="round"><path id="o1" d="M120 -126 l24 26 l50 -60"/><path id="o2" d="M120 -16 l24 26 l50 -60"/><path id="o3" d="M120 94 l24 26 l50 -60"/></g></g>
'''

SCENE = r'''
const B=__B__; const END=B.END;
window.V={sfx:[[0.02,'thud'],[B.start+.1,'pop'],[B.aksam+.1,'whoosh'],[B.aksam+.5,'ticks'],[B.ne+.2,'pop'],[B.ne+2.05,'thud'],[B.oysa+.1,'whoosh'],[B.oysa+1.2,'thud'],[B.oysa+3.4,'ticks'],
 [B.hamle+.1,'whoosh'],[B.fiyat+.3,'scratch'],[B.parca+.3,'scratch'],[B.parca+.6,'drop'],[B.usta+.1,'whoosh'],[B.usta+1.6,'pop'],[B.ruhsat+.1,'whoosh'],[B.ruhsat+1.0,'pop'],[B.ses+.2,'ticks'],[B.wa+.9,'whoosh'],[B.hazir+.3,'pop'],[B.hazir+.6,'pop'],[B.hazir+.9,'pop'],[B.simdi+.1,'whoosh']]};
const LINES=[[B.start,B.aksam-.1,'Sabah:<br><span class="o">"sadece yağ."</span>'],
 [B.aksam,B.ne-.1,'Akşam<br><span class="o">liste uzamış.</span>'],
 [B.ne,B.oysa-.1,'Ne değişti?<br><span class="o">Kaça değişti?</span>'],
 [B.oysa,B.hamle-.1,'Yetkili serviste<br><span class="o">servis fişi zorunlu.</span>'],
 [B.hamle,B.usta-.1,'Sanayide<br><span class="o">tek hamle:</span>'],
 [B.usta,B.ruhsat-.1,'Usta, dinle:<br><span class="o">müşteri fiş istiyor.</span>'],
 [B.ruhsat,B.ses-.1,'Ruhsatın<br><span class="o">fotoğrafını çek.</span>'],
 [B.ses,B.wa-.1,'İş emrini<br><span class="o">sesle aç.</span>'],
 [B.wa,B.hazir-.1,'Teklifi<br><span class="o">telefona yolla.</span>'],
 [B.hazir,B.simdi-.1,'Fişi hazır usta<br><span class="o">tartışmaya girmez.</span>'],
 [B.simdi,END-.45,'Şimdi bir daha sor:']];
const BIG=[[B.ne+1.9,B.oysa-.1]], HITS=[0.02,B.ne+2.05,B.oysa+1.2];
const FY=1262;
const ITEMS=['YAĞ DEĞİŞİMİ','BALATA','FİLTRE','"ŞUNU DA..."'];
$('rcp').innerHTML=`<rect id="rcpR" x="-230" y="0" width="460" height="0" fill="#FFF8EB"/>`+ITEMS.map((a,i)=>`<g id="ri${i}"><text x="-200" y="${70+i*80}" font-size="32" fill="${i==3?'#ff5a1f':'#1c1b18'}">${a}</text><text id="rq${i}" x="200" y="${70+i*80}" font-size="40" text-anchor="end" fill="#ff5a1f">?</text></g>`).join('')+
 `<path id="rcL" d="M-200 ${70+4*80-30} H200" stroke="#b9b4a8" stroke-width="4" stroke-dasharray="10 8"/><g id="rcT"><text x="-200" y="${70+4*80+30}" font-size="34" fill="#1c1b18">TOPLAM</text><text x="200" y="${70+4*80+30}" font-size="38" text-anchor="end" fill="#ff5a1f">???</text></g>`;
$('flds').innerHTML=['PLAKA','MARKA','ŞASİ'].map((a,i)=>`<g id="fd${i}"><rect x="-140" y="${40+i*70}" width="280" height="54" fill="#f3efe4" stroke="#b9b4a8" stroke-width="3"/><text x="-120" y="${76+i*70}" font-size="24" fill="#8c8880">${a}</text><path d="M96 ${60+i*70} l12 14 l24 -28" stroke="#8A9B7C" stroke-width="7" fill="none"/></g>`).join('');
$('wv').innerHTML=Array.from({length:13},(_,i)=>`<rect id="wb${i}" x="${-130+i*20}" y="0" width="12" height="10" fill="#243139"/>`).join('');
function scene(t){
  const W=(a,b)=>(t<a||t>b)?0:ob(p(t,a,.35))*(1-io(p(t,b-.25,.25)));
  const ON=(a,b)=>t>=a&&t<=b;
  // araba + etiket: kancada ve sonda
  const cs=t<B.simdi-.1?1-io(p(t,B.aksam,.3)):ob(p(t,B.simdi-.1,.45));
  tr('car',`translate(${470-150*(t>B.start&&t<B.simdi?io(p(t,B.start,.4)):0)} 1200) scale(${cs})`); op('car',cs>.01?1:0);
  const sw=Math.sin(t*2.4)*10*p(t,.3,.5)*(1-p(t,END-.9,.4));
  const ts=t<B.simdi-.1?1-io(p(t,B.start,.3)):ob(p(t,B.simdi+.1,.45));
  tr('tag',`translate(720 760) rotate(${sw}) scale(${ts})`); op('tag',ts>.01?1:0);
  // sabah: yağ + balon
  tr('oil',`translate(700 1262) scale(${W(B.start+.1,B.aksam+.25)})`);
  tr('bub',`translate(560 620) scale(${W(B.start+.4,B.aksam+.25)})`);
  // akşam: fiş uzar
  const rw=ON(B.aksam,B.oysa+.25), ro=io(p(t,B.oysa,.25)), rk=oc(p(t,B.aksam+.1,1.2));
  tr('rcp',`translate(470 ${L(1300,520,oc(p(t,B.aksam,.4)))+ro*900})`); op('rcp',rw?1:0);
  $('rcpR').setAttribute('height',80+rk*440);
  ITEMS.forEach((_,i)=>{op('ri'+i,t>B.aksam+.4+i*.55?1:0); const q=$('rq'+i); q.setAttribute('font-size',t>B.ne+.2+i*.15?L(80,40,io(p(t,B.ne+.2+i*.15,.25))):0)});
  op('rcL',rk>.95?1:0); op('rcT',rk>.95?1:0);
  tr('yok',`translate(470 760) rotate(-8) scale(${t>B.ne+2.05&&t<B.oysa+.25?L(2,1,io(p(t,B.ne+2.05,.15)))*(1-io(p(t,B.oysa,.25))):0})`);
  // yetkili servis fişi
  tr('fis',`translate(300 900) scale(${W(B.oysa,B.hamle+.25)})`);
  tr('zor',`translate(300 980) rotate(-10) scale(${t>B.oysa+1.2&&t<B.hamle+.25?L(2.2,1,io(p(t,B.oysa+1.2,.15)))*(1-io(p(t,B.hamle,.25))):0})`);
  tr('prn',`translate(700 1100) scale(${W(B.oysa+3.3,B.hamle+.25)})`); $('prnP').setAttribute('height',140*oc(p(t,B.oysa+3.5,.8)));
  // tek hamle
  tr('chk',`translate(470 860) scale(${W(B.hamle,B.usta+.25)})`);
  const c1=p(t,B.fiyat+.3,.3), c2=p(t,B.parca+.3,.3);
  $('ck1').style.strokeDasharray='120';$('ck1').style.strokeDashoffset=120*(1-c1);
  $('ck2').style.strokeDasharray='120';$('ck2').style.strokeDashoffset=120*(1-c2);
  const pk=io(p(t,B.parca+.5,.5)); tr('pad',`translate(${L(940,700,pk)} ${L(1262,1200,pk)}) rotate(${L(40,0,pk)}) scale(${t>B.parca+.4&&t<B.usta+.25?1-io(p(t,B.usta,.25)):0})`);
  // usta
  tr('usta',`translate(330 1120) scale(${1.5*W(B.usta,B.ruhsat+.25)})`);
  tr('ubub',`translate(640 760) scale(${W(B.usta+1.5,B.ruhsat+.25)})`);
  // telefon
  const pw=ON(B.ruhsat,B.hazir+.25); const pin=oc(p(t,B.ruhsat,.45)), pout=io(p(t,B.hazir,.3));
  tr('ph',`translate(470 ${L(1700,880,pin)+pout*900})`); op('ph',pw?1:0);
  op('sc1',t<B.ses?1:0); op('sc2',ON(B.ses,B.wa)?1:0); op('sc3',t>=B.wa?1:0);
  const fr=p(t,B.ruhsat+.4,.5); op('frm',fr>0&&fr<1?1:(fr>=1?0:0)); $('frm').style.transform=`scale(${L(1.3,1,fr)})`;
  [0,1,2].forEach(i=>op('fd'+i,t>B.ruhsat+1.0+i*.35?1:0));
  for(let i=0;i<13;i++){const h=t>B.ses+.2&&t<B.wa?20+Math.abs(Math.sin(t*9+i*1.3))*70:10; const r=$('wb'+i); r.setAttribute('height',h); r.setAttribute('y',60-h/2)}
  const said='yağ filtresi · 2 adet'; $('say').textContent=said.slice(0,Math.floor(said.length*p(t,B.ses+.4,1.0)));
  const sp=io(p(t,B.wa+.8,1.0)); tr('pdf',`translate(${sp*420} ${-sp*300}) scale(${1-sp*.6})`); op('pdf',sp<1?1:0);
  tr('pl',`translate(${L(470,900,sp)} ${L(860,420,sp)}) rotate(-20) scale(${t>B.wa+.8&&t<B.hazir?ob(p(t,B.wa+.8,.2))*(1-p(t,B.wa+1.6,.2)):0})`);
  // tamam
  tr('ok',`translate(470 860) scale(${W(B.hazir,B.simdi+.2)})`);
  ['o1','o2','o3'].forEach((id,i)=>{const k=p(t,B.hazir+.3+i*.3,.25);$(id).style.strokeDasharray='130';$(id).style.strokeDashoffset=130*(1-k)});
}
'''.replace('__B__', json.dumps(B))

out = sys.argv[2] if len(sys.argv) > 2 else 'sanayi01'
build(f'/home/claude/kasaonu-medya/referans/sablonlar/{out}/index.html', 'SANAYİ · 12', 'FİŞ 0017', 'İŞ BİRLİĞİ', 'OTOİŞLERİM',
      'Sanayide neyin', 'parasını ödüyorsun?', SVG, SCENE)
print('ok')

from base import build
import json, sys
B = json.loads(sys.argv[1])

CH='#EDEAE0'; DIM='#7f8a83'
SVG = r'''
<style>
#rc{background:#18201d !important}
#furn .mono{color:#cfd4c9 !important}
#furn .abs[style*="dashed"]{border-top-color:#3c4a44 !important}
#tA.gk,#tA{color:#EDEAE0 !important}
#hook .hw{color:#EDEAE0}#hook .hw.o{color:#ff5a1f}
#floor{stroke:#cfd4c9}
</style>
   <defs><radialGradient id="vig" cx="50%" cy="45%" r="70%"><stop offset="0" stop-color="#22302a" stop-opacity="0"/><stop offset="1" stop-color="#0c100e" stop-opacity=".75"/></radialGradient>
   <g id="carn"><path d="M0 0 v34" stroke="#5f8a5a" stroke-width="5"/><path d="M0 22 q-12 -4 -16 6" stroke="#5f8a5a" stroke-width="4" fill="none"/><circle cx="-7" cy="-4" r="9" fill="#d23b2e"/><circle cx="7" cy="-4" r="9" fill="#d23b2e"/><circle cx="0" cy="-12" r="9" fill="#e5493b"/><circle cx="0" cy="0" r="8" fill="#b52d22"/></g></defs>
   <rect x="0" y="0" width="940" height="1620" fill="url(#vig)"/>
   <g id="dust"></g>
   <g id="desk"><rect x="-300" y="-20" width="600" height="34" fill="#6b4a33"/><rect x="-280" y="14" width="26" height="150" fill="#5a3d2a"/><rect x="254" y="14" width="26" height="150" fill="#5a3d2a"/><rect x="-250" y="14" width="500" height="70" fill="#5a3d2a"/><rect x="-60" y="30" width="120" height="14" rx="7" fill="#3f2b1e"/></g>
   <g id="kol" filter="url(#ps)"><rect x="-34" y="-150" width="68" height="150" rx="14" fill="#cfe3e8" opacity=".9"/><rect x="-18" y="-182" width="36" height="34" fill="#E8B65C"/><rect x="-30" y="-100" width="60" height="44" fill="#FFF8EB"/><text y="-70" font-size="16" text-anchor="middle" fill="#1c1b18">KOLONYA</text></g>
   <g id="cic"><use href="#carn" transform="scale(2.6)"/></g>
   <g id="alt" filter="url(#ps)"><circle r="54" fill="#E8B65C" stroke="#b8862f" stroke-width="6"/><text y="16" font-size="44" text-anchor="middle" fill="#7a5512">¼</text></g>
   <defs><clipPath id="rcClip"><rect x="0" y="0" width="940" height="1620"/></clipPath></defs><g clip-path="url(#rcClip)"><g id="rays"></g></g>
   <defs><g id="flagArt"><rect x="0" y="0" width="600" height="400" fill="#E30A17"/><circle cx="212" cy="200" r="100" fill="#fff"/><circle cx="237" cy="200" r="80" fill="#E30A17"/><polygon id="star" fill="#fff" points=""/></g></defs>
   <g id="flag"></g>
   <text id="bas" x="470" y="455" font-size="34" text-anchor="middle" fill="#E8B65C" letter-spacing="14">BAŞÖĞRETMEN</text>
   <g id="quote"><text id="q1" x="470" y="1010" font-size="62" text-anchor="middle" fill="#EDEAE0" style="font-family:'Space Grotesk'"></text><text id="q2" x="470" y="1090" font-size="62" text-anchor="middle" fill="#EDEAE0" style="font-family:'Space Grotesk'"></text>
     <path id="qline" d="M280 1135 H660" stroke="#E8B65C" stroke-width="4"/><text id="q3" x="660" y="1185" font-size="34" text-anchor="end" fill="#E8B65C" style="font-family:'Space Grotesk'">— M. K. Atatürk</text></g>
   <g id="bill"><g filter="url(#ps)"><rect id="billR" x="-260" y="0" width="520" height="0" fill="#EDEAE0"/></g>
     <text x="0" y="62" font-size="40" text-anchor="middle" fill="#1c1b18" letter-spacing="10">HESAP</text><path d="M-220 90 H220" stroke="#8c8880" stroke-width="4" stroke-dasharray="10 8"/>
     <g id="bl0"><use href="#carn" transform="translate(-200 150) scale(1.3)"/><text x="-160" y="164" font-size="34" fill="#1c1b18">AYBÜKE</text><text x="220" y="164" font-size="34" text-anchor="end" fill="#b52d22">22 YAŞ</text></g>
     <g id="bl1"><use href="#carn" transform="translate(-200 230) scale(1.3)"/><text x="-160" y="244" font-size="34" fill="#1c1b18">NECMETTİN</text><text x="220" y="244" font-size="34" text-anchor="end" fill="#b52d22">23 YAŞ</text></g>
     <g id="bl2"><path d="M-220 290 H220" stroke="#8c8880" stroke-width="4" stroke-dasharray="10 8"/><text x="0" y="344" font-size="30" text-anchor="middle" fill="#5a5650">TERÖR</text></g></g>
   <g id="field"></g><text id="f200" x="470" y="1210" font-size="96" text-anchor="middle" fill="#EDEAE0" style="font-family:'Space Grotesk'">~200</text>
   <g id="sira"><g filter="url(#ps)"><rect x="-260" y="-30" width="520" height="40" fill="#8a6a4e"/><rect x="-240" y="10" width="20" height="150" fill="#555"/><rect x="220" y="10" width="20" height="150" fill="#555"/><rect x="-200" y="60" width="400" height="16" fill="#555"/></g>
     <use href="#carn" transform="translate(0 -60) rotate(70) scale(2.4)"/><text x="0" y="230" font-size="38" text-anchor="middle" fill="#EDEAE0">AYLA ÖĞRETMEN</text><text x="0" y="280" font-size="28" text-anchor="middle" fill="#7f8a83">15 NİSAN 2026 · KAHRAMANMARAŞ</text></g>
   <g id="cal" filter="url(#ps)"><rect x="-150" y="-170" width="300" height="320" rx="16" fill="#EDEAE0"/><rect x="-150" y="-170" width="300" height="80" rx="16" fill="#ff5a1f"/><text id="calM" y="-114" font-size="40" text-anchor="middle" fill="#FFF8EB">NİSAN</text><text id="calN" y="70" font-size="120" text-anchor="middle" fill="#1c1b18" style="font-family:'Space Grotesk'">15</text></g>
   <g id="eleven"><text x="0" y="0" font-size="260" text-anchor="middle" fill="#EDEAE0" style="font-family:'Space Grotesk'">11</text><text x="0" y="70" font-size="34" text-anchor="middle" fill="#7f8a83">KAMU GÖREVLİSİ</text>
     <g id="izin" transform="rotate(-10)"><rect x="-230" y="-170" width="460" height="110" fill="none" stroke="#ff5a1f" stroke-width="10"/><text y="-92" font-size="64" text-anchor="middle" fill="#ff5a1f" letter-spacing="4">İZİN YOK</text></g></g>
   <g id="tcard"><g filter="url(#ps)"><rect x="-200" y="-150" width="400" height="300" rx="12" fill="#EDEAE0"/></g><circle cx="0" cy="-40" r="56" fill="#c9b8a4"/><path d="M-100 110 q0 -90 100 -90 q100 0 100 90z" fill="#7C9DA5"/><text x="0" y="140" font-size="26" text-anchor="middle" fill="#1c1b18">ÖĞRETMEN · YÖNETİCİ</text>
     <g id="sor" transform="rotate(8)"><rect x="-230" y="-40" width="460" height="90" fill="#ff5a1f" opacity=".95"/><text y="22" font-size="48" text-anchor="middle" fill="#FFF8EB" letter-spacing="3">SORUŞTURMA</text></g></g>
   <g id="kesil"><g filter="url(#ps)"><rect x="-240" y="-120" width="480" height="240" fill="#EDEAE0"/></g><text y="-40" font-size="40" text-anchor="middle" fill="#1c1b18" letter-spacing="8">HESAP</text><text y="40" font-size="54" text-anchor="middle" fill="#ff5a1f" style="font-family:'Space Grotesk'">→ ÖĞRETMEN</text></g>
   <g id="bars"><g filter="url(#ps)"><rect id="bM" x="-300" y="0" width="200" height="0" fill="#8A9B7C"/><rect id="bK" x="100" y="0" width="200" height="0" fill="#ff5a1f"/></g>
     <text id="tM" x="-200" y="60" font-size="32" text-anchor="middle" fill="#EDEAE0">MAAŞ ~70.000</text><text id="tK" x="200" y="60" font-size="32" text-anchor="middle" fill="#ff5a1f">KİRA 45.510</text><text id="tK2" x="200" y="100" font-size="22" text-anchor="middle" fill="#7f8a83">İSTANBUL ORT.</text></g>
   <g id="cols"></g>
   <g id="kut"><g id="kflag"></g><text x="470" y="930" font-size="84" text-anchor="middle" fill="#EDEAE0" style="font-family:'Space Grotesk'">24 KASIM</text>
     <text x="470" y="1010" font-size="54" text-anchor="middle" fill="#E8B65C" style="font-family:'Space Grotesk'">ÖĞRETMENLER GÜNÜ</text><text x="470" y="1080" font-size="54" text-anchor="middle" fill="#ff5a1f" style="font-family:'Space Grotesk'">KUTLU OLSUN</text>
     <use href="#carn" transform="translate(300 1180) scale(1.8)"/><use href="#carn" transform="translate(470 1170) scale(2.2)"/><use href="#carn" transform="translate(640 1180) scale(1.8)"/></g>
   <g id="note"><g filter="url(#ps)"><rect x="-250" y="-170" width="500" height="340" fill="#FFF8EB" transform="rotate(-3)"/></g><g transform="rotate(-3)"><path d="M-250 -110 H250 M-250 -50 H250 M-250 10 H250 M-250 70 H250" stroke="#cfe0ea" stroke-width="3"/><path d="M-190 -170 V170" stroke="#f0b4b4" stroke-width="3"/>
     <text id="nt1" x="-160" y="-60" font-size="44" fill="#243b8f" style="font-family:'Space Grotesk';font-style:italic"></text><text id="nt2" x="-160" y="0" font-size="44" fill="#243b8f" style="font-family:'Space Grotesk';font-style:italic"></text><use href="#carn" transform="translate(170 90) scale(1.6)"/></g></g>
'''

SCENE = r'''
const B=__B__; const END=B.END;
window.V={sfx:[[0.02,'thud'],[B.kolonya+.1,'pop'],[B.cicek+.1,'pop'],[B.altin+.1,'drop'],[B.ata+.1,'scratch'],[B.ata+1.4,'scratch'],[B.hesap+.1,'whoosh'],[B.aybuke+.2,'pop'],[B.necmettin+.2,'pop'],
 [B.ikiyuz+.1,'ticks'],[B.nisan+.1,'whoosh'],[B.yedi+.1,'ticks'],[B.izin+1.0,'thud'],[B.ama+1.2,'thud'],[B.kesildi+.2,'thud'],[B.maas+.1,'whoosh'],[B.kira+.3,'drop'],
 [B.b1+.05,'thud'],[B.b2+.05,'thud'],[B.b3+.05,'thud'],[B.kolonya2+.2,'scratch'],[B.kagit+.1,'whoosh'],[B.simdi+.1,'whoosh'],[B.kutlu+.1,'thud'],[B.kutlu+.6,'pop']]};
const LINES=[[B.start,B.ata-.1,'Kolonya mı, çiçek mi,<br><span class="o">altın mı?</span>'],
 [B.aybuke,B.teror-.1,'Aybüke 22,<br><span class="o">Necmettin 23.</span>'],
 [B.peki,B.hesap-.1,'Eserin sahibine<br><span class="o">ne veriyoruz?</span>'],
 [B.hesap,B.aybuke-.1,'Önce bir<br><span class="o">hesap yapalım.</span>'],
 [B.teror,B.nisan-.1,'Şehit<br><span class="o">öğretmenler.</span>'],
 [B.nisan,B.yedi-.1,'Öğrencilerini<br><span class="o">korurken.</span>'],
 [B.yedi,B.yani-.1,'Yedi ay sonra<br><span class="o">ne oldu?</span>'],
 [B.yani,B.maas-.1,'Hesap yine<br><span class="o">öğretmene kesildi.</span>'],
 [B.maas,B.borc-.1,'Maaşın üçte ikisi<br><span class="o">kiraya gidiyor.</span>'],
 [B.borc,B.kolonya2-.1,'Bu ülke öğretmenine<br><span class="o">borçlu.</span>'],
 [B.kolonya2,B.kagit-.1,'Bunu kolonyayla<br><span class="o">ödeyemezsin.</span>'],
 [B.kagit,B.gerisi-.1,'Bir kâğıt ver,<br><span class="o">teşekkür yazsın.</span>'],
 [B.gerisi,B.simdi-.1,'Gerisini<br><span class="o">yüksek sesle sor.</span>'],
 [B.simdi,B.kutlu-.1,'Şimdi söyle:']];
const BIG=[[B.yani,B.maas-.1],[B.gerisi,B.simdi-.1]], HITS=[B.izin+1.0,B.ama+1.2,B.kesildi+.2,B.b3+.05];
// toz
let d='';for(let i=0;i<40;i++){d+=`<circle id="d${i}" r="${1+Math.random()*2.5}" fill="#EDEAE0" opacity=".25"/>`}$('dust').innerHTML=d;
const DS=Array.from({length:40},(_,i)=>[Math.random()*940,Math.random()*1300,(Math.random()*.6+.2),Math.random()*6]);
// 200 karanfil
let f='';for(let i=0;i<200;i++){const c=i%20,r=Math.floor(i/20);f+=`<use id="c${i}" href="#carn" transform="translate(${80+c*41} ${640+r*48}) scale(.6)"/>`}$('field').innerHTML=f;
// sütunlar
const CL=['GÜVENLİ OKUL','MAAŞ','DEVLET'];
$('cols').innerHTML=CL.map((a,i)=>`<g id="col${i}"><g filter="url(#ps)"><rect x="-80" y="-420" width="160" height="420" fill="#EDEAE0"/><rect x="-100" y="-450" width="200" height="34" fill="#EDEAE0"/><rect x="-100" y="0" width="200" height="30" fill="#EDEAE0"/>${[0,1,2,3].map(j=>`<rect x="${-60+j*36}" y="-410" width="10" height="400" fill="#cfcabb"/>`).join('')}</g><text y="-470" font-size="30" text-anchor="middle" fill="#E8B65C">${a}</text></g>`).join('');
{const cx=338,cy=200,R1=50,R2=20;let pts=[];for(let i=0;i<10;i++){const a=-Math.PI/2+i*Math.PI/5+Math.PI/2*0, r=i%2?R2:R1;pts.push((cx+r*Math.cos(a+Math.PI/2*-0)).toFixed(1)+','+(cy+r*Math.sin(a)).toFixed(1))}$('star').setAttribute('points',pts.join(' '))}
const NS=60;let fl='<defs>'+Array.from({length:NS},(_,i)=>`<clipPath id="fs${i}"><rect x="${i*10}" y="-20" width="11" height="440"/></clipPath>`).join('')+'</defs>';
fl+=Array.from({length:NS},(_,i)=>`<g clip-path="url(#fs${i})"><use id="fu${i}" href="#flagArt"/></g>`).join('');
$('flag').innerHTML=fl;
let ry='';for(let i=0;i<16;i++){ry+=`<path d="M0 0 L${Math.cos(i*Math.PI/8)*900} ${Math.sin(i*Math.PI/8)*900} L${Math.cos(i*Math.PI/8+.09)*900} ${Math.sin(i*Math.PI/8+.09)*900}Z" fill="#E8B65C" opacity=".07"/>`}$('rays').innerHTML=ry;
const Q1='“Yeni nesil sizin', Q2='eseriniz olacaktır.”';
const N1='Teşekkürler', N2='öğretmenim.';
function scene(t){
  const W=(a,b)=>(t<a||t>b)?0:ob(p(t,a,.35))*(1-io(p(t,b-.25,.25)));
  op('dust',cl(p(t,B.start,.4))*(1-cl(p(t,END-.9,.4))));
  DS.forEach(([x,y,s,ph],i)=>{const yy=(y-t*30*s+1300*4)%1300;$('d'+i).setAttribute('cx',x+Math.sin(t*s+ph)*20);$('d'+i).setAttribute('cy',yy)});
  // masa: kanca + hediyeler + son
  const dk=t<B.ata?1:(t<B.simdi-.1?1-io(p(t,B.ata,.35)):ob(p(t,B.simdi-.1,.45)));
  tr('desk',`translate(470 1110) scale(${t>=B.kutlu?dk*(1-io(p(t,B.kutlu,.3))):dk})`);
  const gk=t<B.ata+.3?(1-io(p(t,B.ata,.3))):0;
  tr('kol',`translate(330 1090) scale(${t>B.kolonya?ob(p(t,B.kolonya,.35))*gk:0})`);
  tr('cic',`translate(470 1040) scale(${t>B.cicek?ob(p(t,B.cicek,.35))*gk:0})`);
  tr('alt',`translate(610 1036) rotate(${(1-oc(p(t,B.altin,.5)))*-200}) scale(${t>B.altin?ob(p(t,B.altin,.35))*gk:0})`);
  // Atatürk sahnesi: dalgalanan bayrak, ışınlar
  const aw=t>=B.ata-.2&&t<B.hesap+.3, ak=oc(p(t,B.ata,.6)), ao=io(p(t,B.hesap,.3));
  op('flag',aw?ak*(1-ao):0); op('rays',aw?ak*(1-ao):0); op('bas',aw?cl(p(t,B.ata+.4,.4))*(1-ao):0);
  $('rays').setAttribute('transform',`translate(470 680) rotate(${t*4})`);
  $('flag').setAttribute('transform',`translate(170 ${L(560,500,ak)})`);
  for(let i=0;i<NS;i++){const ph=t*5-i*.17, amp=6+i*.3; $('fu'+i).setAttribute('transform',`translate(0 ${Math.sin(ph)*amp}) `)}
  // söz
  const qw=t>=B.ata&&t<B.hesap+.3; op('quote',qw?(1-io(p(t,B.hesap,.3))):0);
  const k1=p(t,B.ata+.1,1.6), k2=p(t,B.ata+1.7,1.7);
  $('q1').textContent=Q1.slice(0,Math.floor(Q1.length*k1)); $('q2').textContent=Q2.slice(0,Math.floor(Q2.length*k2));
  op('qline',t>B.ata+3.3?1:0); op('q3',cl(p(t,B.ata+3.3,.3)));
  $('quote').setAttribute('transform',`translate(0 ${-30*io(p(t,B.peki,.5))})`);
  // hesap fişi
  const bw=t>=B.hesap&&t<B.ikiyuz+.3; const bk=oc(p(t,B.hesap+.1,.8)), bo=io(p(t,B.ikiyuz,.3));
  tr('bill',`translate(470 ${560-bo*40})`); op('bill',bw?(1-bo):0); $('billR').setAttribute('height',110+bk*270);
  op('bl0',t>B.aybuke+.2?1:0); op('bl1',t>B.necmettin+.2?1:0); op('bl2',t>B.teror+.2?1:0);
  // 200
  const fw=t>=B.ikiyuz&&t<B.nisan+.3, fo=1-io(p(t,B.nisan,.3));
  for(let i=0;i<200;i++){op('c'+i,fw&&t>B.ikiyuz+.1+i*.008?fo:0)}
  op('f200',fw?cl(p(t,B.ikiyuz+.3,.3))*fo:0);
  // Ayla
  tr('sira',`translate(470 1000) scale(${W(B.nisan,B.yedi+.25)})`);
  // takvim 7 ay
  const cw=W(B.yedi,B.izin+.25); tr('cal',`translate(470 900) scale(${cw})`);
  const MS=['NİSAN','MAYIS','HAZİRAN','TEMMUZ','AĞUSTOS','EYLÜL','EKİM','KASIM'];
  const mi=Math.min(7,Math.floor(p(t,B.yedi+.2,1.0)*8)); $('calM').textContent=MS[mi]; $('calN').textContent=mi>=7?'12':'15';
  tr('eleven',`translate(470 1010) scale(${W(B.izin,B.ama+.25)})`);
  tr('izin',`translate(0 250) rotate(-6) scale(${t>B.izin+1.0?L(2.2,1,io(p(t,B.izin+1.0,.15))):0})`);
  tr('tcard',`translate(470 920) scale(${W(B.ama,B.yani+.25)})`);
  tr('sor',`rotate(8) scale(${t>B.ama+1.2?L(2.2,1,io(p(t,B.ama+1.2,.15))):0})`);
  tr('kesil',`translate(470 960) rotate(-4) scale(${W(B.kesildi,B.maas+.25)})`);
  // maaş-kira
  const mw=t>=B.maas&&t<B.borc+.3; op('bars',mw?(1-io(p(t,B.borc,.3))):0); $('bars').setAttribute('transform','translate(470 1180)');
  const hm=520*oc(p(t,B.maas+.2,.6)), hk=520*(45510/70000)*oc(p(t,B.kira+.2,.7));
  $('bM').setAttribute('height',hm); $('bM').setAttribute('y',-hm); $('bK').setAttribute('height',hk); $('bK').setAttribute('y',-hk);
  op('tK',t>B.kira?1:0); op('tK2',t>B.kira?1:0);
  // sütunlar
  [B.b1,B.b2,B.b3].forEach((a,i)=>{const k=oc(p(t,a,.45)); const o=1-io(p(t,B.kolonya2,.25));
    tr('col'+i,`translate(${230+i*240} 1230) scale(1 ${t>a?k:0})`); op('col'+i,t>a&&t<B.kagit?o:0)});
  // kolonya ödeyemez: şişe sallanır
  if(t>=B.kolonya2&&t<B.kagit+.3){tr('kol',`translate(470 1150) rotate(${Math.sin(t*14)*8*(1-p(t,B.kolonya2+.8,.6))}) scale(${1.8*ob(p(t,B.kolonya2+.15,.3))*(1-io(p(t,B.kagit,.25)))})`)}
  // kutlama
  const kw=t>=B.kutlu; tr('kut',`translate(470 0) scale(${kw?ob(p(t,B.kutlu,.45)):0}) translate(-470 0)`); op('kut',kw?1:0);
  if(t>=B.kutlu-.2){ $('hook').style.display='none'; }
  // not
  tr('note',`translate(470 940) scale(${W(B.kagit,B.simdi+.2)})`);
  $('nt1').textContent=N1.slice(0,Math.floor(N1.length*p(t,B.kagit+.3,.9))); $('nt2').textContent=N2.slice(0,Math.floor(N2.length*p(t,B.kagit+1.2,.9)));
}
'''.replace('__B__', json.dumps(B))

out = sys.argv[2] if len(sys.argv) > 2 else 'ogretmen01'
build(f'/home/claude/kasaonu-medya/referans/sablonlar/{out}/index.html', '24 KASIM', 'FİŞ 0019', 'ÖĞRETMENLER GÜNÜ', 'HESAP',
      'Öğretmenine bu yıl', 'ne alıyorsun?', SVG, SCENE)
print('ok')

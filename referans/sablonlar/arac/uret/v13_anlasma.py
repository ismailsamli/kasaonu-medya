from base import build
import json, sys

# Varsayılan vuruşlar (ses gelince gerçek değerlerle değişir)
B = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {
 "q":0.3,"start":3.6,"sen":3.6,"usta":7.0,"bosluk":9.6,"kayit":11.8,"oi":14.0,"ruhsat":16.4,"ses":20.6,"foto":22.6,"tel":26.4,
 "kazanc":29.2,"platform":31.8,"bitti":34.0,"demo":36.4,"END":41.0}

SVG = r'''
   <g id="mus"><g filter="url(#ps)"><circle cx="0" cy="-130" r="66" fill="#e9c9a6"/><path d="M-68 -150 q6 -66 68 -66 q62 0 68 66 q-30 -26 -68 -26 q-38 0 -68 26z" fill="#1c1b18"/><path d="M-120 110 q0 -120 120 -120 q120 0 120 120z" fill="#C56B50"/></g></g>
   <g id="musB" filter="url(#ps)"><path d="M-220 -70 h440 v120 h-200 l-50 46 v-46 h-190z" fill="#FFF8EB"/><text y="-4" font-size="34" text-anchor="middle" fill="#1c1b18">"BİR TIK VAR…</text><text y="36" font-size="34" text-anchor="middle" fill="#1c1b18">AMA HEP DEĞİL"</text></g>
   <g id="ust"><g filter="url(#ps)"><circle cx="0" cy="-120" r="70" fill="#e9c9a6"/><path d="M-76 -136 q4 -70 76 -72 q72 2 76 72z" fill="#243139"/><rect x="-40" y="-146" width="130" height="18" fill="#243139"/><path d="M-120 110 q0 -120 120 -120 q120 0 120 120z" fill="#7C9DA5"/></g>
     <g transform="translate(-110 50) rotate(35)" filter="url(#ps)"><rect x="-12" y="-90" width="24" height="150" fill="#8c8880"/><path d="M-36 -90 a36 36 0 1 1 72 0 l-18 0 v-30 h-36 v30z" fill="#8c8880"/></g></g>
   <g id="ustB" filter="url(#ps)"><path d="M-220 -60 h440 v100 h-170 l50 46 l-100 -46 h-220z" fill="#243139"/><text y="8" font-size="31" text-anchor="middle" fill="#FFF8EB">"BAKTIK, HALLETTİK"</text></g>
   <g id="qm"><text x="-60" y="0" font-size="120" fill="#ff5a1f">?</text><text x="20" y="-50" font-size="90" fill="#ff5a1f">?</text><text x="80" y="20" font-size="70" fill="#ff5a1f">?</text></g>
   <path id="gap" d="M470 640 V1240" stroke="#ff5a1f" stroke-width="6" stroke-dasharray="14 12"/>
   <g id="bill" filter="url(#ps)"><rect id="billR" x="-170" y="0" width="340" height="0" fill="#FFF8EB"/><g id="billL"></g></g>
   <g id="ky"><g filter="url(#ps)"><rect x="-230" y="-64" width="460" height="128" fill="#ff5a1f" stroke="#1c1b18" stroke-width="6"/></g><text y="24" font-size="66" fill="#FFF8EB" text-anchor="middle" letter-spacing="6">KAYIT YOK</text></g>
   <g id="brandS"><g filter="url(#ps)"><rect x="-300" y="-110" width="600" height="220" rx="18" fill="#fff"/></g><image href="img/logo.png" x="-250" y="-80" width="500" height="160"/></g>
   <g id="ph"><defs><clipPath id="scr"><rect x="-198" y="-418" width="396" height="836" rx="34"/></clipPath></defs>
     <g filter="url(#ps)"><rect x="-214" y="-434" width="428" height="868" rx="48" fill="#1c1b18"/></g>
     <g clip-path="url(#scr)"><rect x="-198" y="-418" width="396" height="836" fill="#fff"/>
       <image id="im1" href="img/kabul.png" x="-198" y="-418" width="396" height="860"/>
       <image id="im2" href="img/servis.png" x="-198" y="-418" width="396" height="860"/>
       <image id="im3" href="img/teklif.png" x="-198" y="-418" width="396" height="860"/></g>
     <g id="ring"><rect x="-180" y="148" width="360" height="160" rx="18" fill="none" stroke="#ff5a1f" stroke-width="8"/></g>
     <g id="mic"><g filter="url(#ps)"><rect x="-170" y="80" width="340" height="230" rx="28" fill="#243139"/></g><circle cx="-110" cy="150" r="40" fill="#ff5a1f"/><rect x="-122" y="124" width="24" height="44" rx="12" fill="#FFF8EB"/><path d="M-134 154 q0 24 24 24 q24 0 24 -24 M-110 178 v12" stroke="#FFF8EB" stroke-width="5" fill="none"/>
       <g id="wv"></g><text id="say" x="0" y="262" font-size="26" text-anchor="middle" fill="#FFF8EB"></text></g></g>
   <g id="air"><g filter="url(#ps)"><rect x="-372" y="-200" width="744" height="400" rx="16" fill="#fff"/></g><image href="img/airuhsat.png" x="-362" y="-190" width="724" height="376"/>
     <rect x="-372" y="-200" width="744" height="400" rx="16" fill="none" stroke="#ff5a1f" stroke-width="6"/><g transform="translate(250 -236)"><rect x="-130" y="-30" width="260" height="56" rx="10" fill="#ff5a1f"/><text y="8" font-size="26" text-anchor="middle" fill="#FFF8EB">KENDİLİĞİNDEN</text></g></g>
   <g id="ps2"><g id="pA" filter="url(#ps)"><rect x="-190" y="-150" width="380" height="300" fill="#FFF8EB"/><rect x="-170" y="-130" width="340" height="210" fill="#8c8880"/><path d="M-120 60 q0 -90 120 -100 q120 10 120 100z" fill="#5d5a54"/><path d="M-60 -60 l40 30 l-30 30 l50 20" stroke="#C56B50" stroke-width="10" fill="none"/><text y="122" font-size="34" text-anchor="middle" fill="#1c1b18">ÖNCE</text></g>
     <g id="pB" filter="url(#ps)"><rect x="-190" y="-150" width="380" height="300" fill="#FFF8EB"/><rect x="-170" y="-130" width="340" height="210" fill="#7C9DA5"/><path d="M-120 60 q0 -90 120 -100 q120 10 120 100z" fill="#e3ded2"/><text y="122" font-size="34" text-anchor="middle" fill="#ff5a1f">SONRA</text></g></g>
   <g id="kz" filter="url(#ps)"><rect x="-300" y="-230" width="600" height="460" rx="18" fill="#FFF8EB"/><text x="-250" y="-160" font-size="32" fill="#1c1b18">KAZANÇ</text><text x="40" y="-160" font-size="32" fill="#1c1b18">ALACAK</text>
     <g id="kzb"></g><path d="M-260 170 H260" stroke="#1c1b18" stroke-width="4"/><text y="214" font-size="26" text-anchor="middle" fill="#8c8880">TEK EKRAN</text></g>
   <g id="pf"><g filter="url(#ps)"><rect x="-330" y="-200" width="440" height="290" rx="14" fill="#1c1b18"/><rect x="-312" y="-182" width="404" height="254" fill="#fff"/><path d="M-370 90 h520 l-30 36 h-460z" fill="#8c8880"/></g>
     <image href="img/airuhsat.png" x="-312" y="-182" width="404" height="210"/>
     <g transform="translate(240 0)" filter="url(#ps)"><rect x="-90" y="-190" width="180" height="370" rx="26" fill="#1c1b18"/><image href="img/kabul.png" x="-80" y="-180" width="160" height="350" preserveAspectRatio="xMidYMin slice"/></g>
     <text x="-110" y="200" font-size="30" text-anchor="middle" fill="#1c1b18">BİLGİSAYAR</text><text x="240" y="230" font-size="30" text-anchor="middle" fill="#1c1b18">TELEFON</text></g>
   <g id="ok" filter="url(#ps)"><rect x="-200" y="-260" width="400" height="420" fill="#FFF8EB"/><text y="-200" font-size="30" text-anchor="middle" fill="#1c1b18">FATURA</text>
     <path d="M-160 -170 H160" stroke="#b9b4a8" stroke-width="4" stroke-dasharray="10 8"/><g fill="#e3ded2"><rect x="-160" y="-130" width="320" height="18"/><rect x="-160" y="-90" width="260" height="18"/></g>
     <path d="M-160 -40 H160" stroke="#b9b4a8" stroke-width="4" stroke-dasharray="10 8"/><path id="okc" d="M-70 50 l50 50 l100 -120" stroke="#8A9B7C" stroke-width="22" fill="none" stroke-linecap="round"/></g>
   <g id="brand"><g filter="url(#ps)"><rect x="-330" y="-260" width="660" height="520" fill="#243139"/></g>
     <rect x="-300" y="-236" width="600" height="160" rx="14" fill="#fff"/><image href="img/logo.png" x="-250" y="-236" width="500" height="160"/>
     <g id="bd1"><rect x="-300" y="-60" width="600" height="110" fill="#ff5a1f"/><text y="14" font-size="38" text-anchor="middle" fill="#FFF8EB">20 DK ÜCRETSİZ DEMO</text></g>
     <text id="bd2" y="120" font-size="38" text-anchor="middle" fill="#FFF8EB">otoislerim.com.tr</text><text id="bd3" y="190" font-size="34" text-anchor="middle" fill="#E8B65C">@otoislerim</text></g>
'''

SCENE = r'''
const B=__B__; if(B.start===undefined)B.start=B.sen; const END=B.END;
window.V={sfx:[[0.02,'thud'],[B.sen+.1,'whoosh'],[B.sen+.8,'pop'],[B.usta+.1,'whoosh'],[B.usta+.8,'pop'],[B.bosluk+.2,'scratch'],[B.bosluk+.5,'ticks'],[B.kayit2,'thud'],
 [B.oi+.1,'whoosh'],[B.oi+.5,'pop'],[B.ruhsat+.1,'whoosh'],[B.plaka,'whoosh'],[B.ses+.2,'ticks'],[B.foto+.2,'pop'],[B.foto+1.2,'pop'],[B.tel+.1,'whoosh'],[B.tel+1.0,'pop'],
 [B.kazanc+.1,'whoosh'],[B.kazanc+.4,'ticks'],[B.platform+.1,'whoosh'],[B.bitti+.3,'pop'],[B.demo+.1,'whoosh'],[B.demo+.6,'thud'],[B.demo+1.2,'pop']]};
const LINES=[[B.start,B.sen-.1,'Cevap:<br><span class="o">anlaşamamak.</span>'],[B.sen,B.usta-.1,'Sen sesi<br><span class="o">anlatamazsın.</span>'],
 [B.usta,B.bosluk-.1,'Usta yaptığını<br><span class="o">anlatamaz.</span>'],
 [B.bosluk,B.kayit-.1,'Aradaki boşluk<br><span class="o">faturaya yazılır.</span>'],
 [B.kayit,B.oi-.1,'Sorun para değil.<br><span class="o">Kayıt yok.</span>'],
 [B.oi,B.ruhsat-.1,'Boşluğu kapatan:'],
 [B.ruhsat,B.ses-.1,'Ruhsatı çek,<br><span class="o">bilgiler dolsun.</span>'],
 [B.ses,B.foto-.1,'İş emri<br><span class="o">yazılmaz, söylenir.</span>'],
 [B.foto,B.tel-.1,'Önce, sonra:<br><span class="o">fotoğraflı kayıt.</span>'],
 [B.tel,B.kazanc-.1,'Teklif ve iş emri<br><span class="o">müşteriye gider.</span>'],
 [B.kazanc,B.platform-.1,'Kazanç ve alacak<br><span class="o">tek ekranda.</span>'],
 [B.platform,B.bitti-.1,'Telefonda da,<br><span class="o">bilgisayarda da.</span>'],
 [B.bitti,B.demo-.1,'Anlaşmazlık biter,<br><span class="o">fatura uzamaz.</span>'],
 [B.demo,END-.45,'Ücretsiz demo için<br><span class="o">@otoislerim</span>']];
const BIG=[[B.kayit2-.1,B.oi-.1]], HITS=[0.02,B.kayit2,B.demo+.6];
const FY=1262;
const BL=['SES ARANDI','BAKILDI','HALLEDİLDİ','?','?'];
$('billL').innerHTML=BL.map((a,i)=>`<g id="bl${i}"><text x="-140" y="${56+i*62}" font-size="28" fill="#1c1b18">${a}</text><text x="140" y="${56+i*62}" font-size="32" text-anchor="end" fill="#ff5a1f">???</text></g>`).join('');
$('wv').innerHTML=Array.from({length:11},(_,i)=>`<rect id="wb${i}" x="${-50+i*20}" y="0" width="12" height="10" fill="#FFF8EB"/>`).join('');
$('kzb').innerHTML=[0,1,2,3].map(i=>`<rect id="ka${i}" x="${-250+i*60}" y="0" width="40" height="0" fill="#8A9B7C"/><rect id="kb${i}" x="${40+i*60}" y="0" width="40" height="0" fill="#E8B65C"/>`).join('');
function scene(t){
  const W=(a,b)=>(t<a||t>b)?0:ob(p(t,a,.35))*(1-io(p(t,b-.25,.25)));
  // kanca + sen + usta: iki taraf
  const hs=t<B.oi?1-io(p(t,B.oi,.3)):0, he=t>B.demo?0:1;
  const back=t>=B.demo+2.2?ob(p(t,END-1.2,.5)):0;
  const sv=Math.max(hs,back);
  tr('mus',`translate(220 1180) scale(${sv})`); tr('ust',`translate(720 1180) scale(${sv})`);
  tr('musB',`translate(250 790) scale(${W(B.sen+.6,B.bosluk+.25)})`);
  tr('ustB',`translate(640 640) scale(${W(B.usta+.6,B.bosluk+.25)})`);
  tr('qm',`translate(470 760) scale(${t<B.sen?1:0}) rotate(${Math.sin(t*3)*6*p(t,.3,.4)*(1-p(t,END-.9,.4))})`); op('qm',(t<B.sen||t>END-1.2)?1:0);
  if(t>END-1.2) tr('qm',`translate(470 760) scale(${ob(p(t,END-1.2,.4))})`);
  op('gap',t>B.bosluk-.1&&t<B.oi?cl(p(t,B.bosluk-.1,.3))*(1-io(p(t,B.kayit,.3))):0);
  const bk=oc(p(t,B.bosluk+.2,1.4)), bo=io(p(t,B.oi,.3));
  tr('bill',`translate(470 ${560+bo*900})`); op('bill',t>B.bosluk&&t<B.oi+.3?1:0); $('billR').setAttribute('height',40+bk*320);
  BL.forEach((_,i)=>op('bl'+i,t>B.bosluk+.4+i*.3?1:0));
  tr('ky',`translate(470 760) rotate(-8) scale(${t>B.kayit2&&t<B.oi+.25?L(2,1,io(p(t,B.kayit2,.15)))*(1-io(p(t,B.oi,.25))):0})`);
  // Otoİşlerim
  tr('brandS',`translate(470 860) scale(${W(B.oi+.2,B.ruhsat+.25)})`);
  const pw=t>=B.ruhsat&&t<=B.foto+.3, pin=oc(p(t,B.ruhsat,.45)), pout=io(p(t,B.foto,.3));
  const pw2=t>=B.tel&&t<=B.kazanc+.3, pin2=oc(p(t,B.tel,.45)), pout2=io(p(t,B.kazanc,.3));
  if(pw) tr('ph',`translate(470 ${L(1800,880,pin)+pout*1000})`); else if(pw2) tr('ph',`translate(470 ${L(1800,880,pin2)+pout2*1000})`);
  op('ph',pw||pw2?1:0);
  op('im1',t<B.ses?1:0); op('im2',t>=B.ses&&t<B.tel?1:0); op('im3',t>=B.tel?1:0);
  const ak=oc(p(t,B.plaka,.45)), ao=io(p(t,B.ses-.1,.3));
  tr('air',`translate(470 ${L(1600,1030,ak)+ao*700}) rotate(${L(6,-2,ak)})`); op('air',t>B.plaka&&t<B.ses+.3?1:0);
  op('mic',t>B.ses&&t<B.foto?1:0); $('mic').setAttribute('transform',`translate(0 ${(1-oc(p(t,B.ses,.3)))*120})`);
  for(let i=0;i<11;i++){const h=t>B.ses+.2&&t<B.foto?14+Math.abs(Math.sin(t*9+i*1.3))*50:10; const r=$('wb'+i); r.setAttribute('height',h); r.setAttribute('y',150-h/2)}
  const said='yağ filtresi · 2 adet'; $('say').textContent=said.slice(0,Math.floor(said.length*p(t,B.ses+.3,1.0)));
  const pa=W(B.foto+.1,B.tel+.25), pb=W(B.foto+1.1,B.tel+.25);
  tr('pA',`translate(300 ${780}) rotate(-5) scale(${pa})`); tr('pB',`translate(640 ${1020}) rotate(4) scale(${pb})`);
  op('ring',t>B.tel+1.0&&t<B.kazanc?1:0); $('ring').setAttribute('transform',`scale(${L(1.2,1,oc(p(t,B.tel+1.0,.4)))+Math.sin(t*6)*.015})`);
  tr('kz',`translate(470 900) scale(${W(B.kazanc,B.platform+.25)})`);
  const HA=[90,140,120,190], HB=[80,60,110,70];
  [0,1,2,3].forEach(i=>{const k=oc(p(t,B.kazanc+.4+i*.15,.4));const a=$('ka'+i),b=$('kb'+i);a.setAttribute('height',HA[i]*k);a.setAttribute('y',160-HA[i]*k);b.setAttribute('height',HB[i]*k);b.setAttribute('y',160-HB[i]*k)});
  tr('pf',`translate(470 960) scale(${W(B.platform,B.bitti+.25)})`);
  tr('ok',`translate(470 900) scale(${W(B.bitti,B.demo+.25)})`);
  $('okc').style.strokeDasharray='260'; $('okc').style.strokeDashoffset=260*(1-p(t,B.bitti+.3,.35));
  tr('brand',`translate(470 880) scale(${W(B.demo,END-1.1)})`);
  const bd=p(t,B.demo+.6,.15); tr('bd1',`scale(${t>B.demo+.6?L(1.5,1,io(bd)):0})`); op('bd2',t>B.demo+1.2?1:0); op('bd3',t>B.demo+1.6?1:0);
}
'''.replace('__B__', json.dumps(B))

out = sys.argv[2] if len(sys.argv) > 2 else 'anlasma01'
build(f'/home/claude/kasaonu-medya/referans/sablonlar/{out}/index.html', 'SANAYİ · 13', 'FİŞ 0018', 'İŞ BİRLİĞİ', 'OTOİŞLERİM',
      'Sanayinin en büyük', 'derdi ne?', SVG, SCENE)
print('ok')

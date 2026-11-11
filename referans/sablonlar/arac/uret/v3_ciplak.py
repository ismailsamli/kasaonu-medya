from base import build
import json, sys

B = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {
    "q": 1.2, "start": 3.3, "yurt": 4.6, "onsekiz": 8.4, "isaret": 10.6, "bizde": 12.6, "antalya": 14.0, "giyinik": 18.6, "ama": 20.4, "END": 23.0}

SVG = r'''
   <g id="card"><g filter="url(#ps)"><rect x="160" y="560" width="620" height="640" fill="#FFF8EB"/><rect x="160" y="560" width="620" height="22" fill="#C56B50"/></g>
     <text id="mh" x="470" y="672" font-size="58" text-anchor="middle" fill="#1c1b18" letter-spacing="10">MENÜ</text>
     <path d="M210 712 H730" stroke="#b9b4a8" stroke-width="4" stroke-dasharray="10 10"/>
     <g id="rows"></g></g>
   <g id="drops"></g>
   <g id="wallet" filter="url(#ps)"><rect x="-90" y="-60" width="180" height="120" rx="14" fill="#8A9B7C"/><path d="M-90 -20 H90 V10 H-90Z" fill="#243139"/><circle cx="56" cy="-5" r="12" fill="#E8B65C"/></g>
   <text id="q2" font-size="120" fill="#ff5a1f" text-anchor="middle">?</text>
   <g id="stamp" filter="url(#ps)"><rect x="-200" y="-90" width="400" height="180" fill="#ff5a1f" stroke="#1c1b18" stroke-width="6"/>
     <text y="-14" font-size="64" fill="#FFF8EB" text-anchor="middle" letter-spacing="8">CEZA</text><text y="58" font-size="54" fill="#1c1b18" text-anchor="middle">50.000 TL</text></g>
'''

SCENE = r'''
const B=__B__; const END=B.END;
const DEL=L(B.yurt,B.onsekiz,.62), STAMP=L(B.antalya,B.giyinik,.6);
window.V={sfx:[[0.02,'thud'],[B.start,'whoosh'],[B.yurt+.1,'whoosh'],[DEL,'drop'],[DEL+.25,'drop'],[DEL+.5,'drop'],[B.onsekiz+.1,'scratch'],[B.isaret+.1,'pop'],[B.bizde+.1,'whoosh'],[STAMP,'thud'],[B.giyinik+.1,'pop'],[B.giyinik+.4,'pop'],[B.giyinik+.7,'pop'],[B.ama+.3,'whoosh']]};
const LINES=[[B.start,B.yurt-.1,'Menüde<br><span class="o">diyorum.</span>'],
 [B.yurt,B.onsekiz-.1,'Yurt dışında<br><span class="o">para işareti yok.</span>'],
 [B.onsekiz,B.isaret-.1,'<span class="o">$18</span> değil,<br>sadece 18.'],
 [B.isaret,B.bizde-.1,'İşaret yoksa<br><span class="o">cüzdan da yok.</span>'],
 [B.bizde,B.antalya-.1,'Bizde bu oyun<br><span class="o">tutmaz.</span>'],
 [B.antalya,B.giyinik-.1,'TL yazmadı:<br><span class="o">50.000 lira ceza.</span>'],
 [B.giyinik,B.ama-.1,'Bizde fiyat<br><span class="o">hep giyinik.</span>'],
 [B.ama,END-.45,'Ama soru yine de<br><span class="o">soruluyor:</span>']];
const BIG=[[B.antalya,B.giyinik-.1]], HITS=[0.02,STAMP];
const FY=1262, RY=[800,920,1040];
const TR=[['Makarna','480'],['Salata','320'],['Tatlı','260']], EN=[['Pasta','18'],['Salad','12'],['Dessert','9']];
$('rows').innerHTML=RY.map((y,i)=>`<text id="rn${i}" x="210" y="${y}" font-size="40" fill="#1c1b18"></text><path id="rl${i}" stroke="#b9b4a8" stroke-width="4" stroke-dasharray="3 12" stroke-linecap="round"/>`+
 `<text id="rv${i}" y="${y}" font-size="44" fill="#1c1b18" text-anchor="end"></text><text id="rc${i}" y="${y}" font-size="44" fill="#ff5a1f"></text>`).join('');
$('drops').innerHTML=RY.map((y,i)=>`<text id="dd${i}" font-size="44" fill="#ff5a1f">$</text>`).join('');
let MODE='';
function setMode(m){ if(MODE===m)return; MODE=m; const en=m==='en';
  $('mh').textContent=en?'MENU':'MENÜ';
  RY.forEach((y,i)=>{$('rn'+i).textContent=(en?EN:TR)[i][0]; $('rv'+i).textContent=(en?EN:TR)[i][1]}); }
function scene(t){
  // menü hangi dilde: başta TR (TL'li), yurt'ta EN, bizde'de TR (TL'siz), giyinik'te TL geri
  const f1=p(t,B.yurt-.15,.3), f2=p(t,B.bizde-.15,.3);
  const mode=(t>=B.yurt&&t<B.bizde)?'en':'tr'; setMode(mode);
  const flip=Math.abs(Math.cos(Math.PI*f1))*Math.abs(Math.cos(Math.PI*f2));
  // kanca: TL kayar, fiyat kızarır
  const slip=(t>B.q&&t<B.start)?Math.sin(Math.PI*p(t,B.q+.2,1.4)):0;
  const pull=oc(p(st(t),B.start,.6))*(1-io(p(t,END-.45,.45)));
  const cs=1, cy=L(130,0,pull);
  tr('card',`translate(0 ${cy}) translate(470 880) scale(${cs*flip} ${cs}) translate(-470 -880)`);
  const tlIn=ob(p(t,B.giyinik+.1,.35)), tlIn2=[0,1,2].map(i=>ob(p(t,B.giyinik+.1+i*.3,.35)));
  RY.forEach((y,i)=>{
    const en=mode==='en', nx=en?730:650;
    $('rv'+i).setAttribute('x',nx); const w=$('rv'+i).getComputedTextLength();
    const nw=$('rn'+i).getComputedTextLength();
    // para birimi
    let cur='',cx=0,cy=y,co=1;
    if(en){ cur='$'; const dk=io(p(t,DEL+i*.25,.45)); cx=nx-w-34+dk*0; co=t<DEL+i*.25?1:0;
      const dx=nx-w-34+dk*180, dy=y+dk*dk*420; const d=$('dd'+i); d.setAttribute('x',dx); d.setAttribute('y',dy); d.style.opacity=(t>=DEL+i*.25&&t<B.onsekiz+.6)?1-dk*.6:0;
    } else { $('dd'+i).style.opacity=0;
      const dressed=t<B.bizde||t>=B.giyinik+.1; cur='TL'; cx=nx+12+(t<B.bizde?28*slip:0)+(t>=B.giyinik?(1-tlIn2[i])*160:0);
      co=dressed?(t>=B.giyinik+.1?cl(tlIn2[i]):1):0; }
    $('rc'+i).textContent=cur; $('rc'+i).setAttribute('x',cx); $('rc'+i).style.opacity=co;
    $('rl'+i).setAttribute('d',`M${210+nw+18} ${y-8} H${(en?nx-w-44:nx-w)-18}`);
    // kancada fiyat kızarır
    $('rv'+i).setAttribute('fill',slip>.25&&i==0?'#ff5a1f':'#1c1b18');
  });
  // 18 vurgusu: onsekiz'de ilk satır büyür
  const zoom=ob(p(t,B.onsekiz+.1,.4))*(1-io(p(t,B.isaret,.3)));
  $('rv0').setAttribute('font-size',44+30*zoom);
  // cüzdan: gelir, solar
  const wk=ob(p(t,B.isaret+.1,.4)), wFade=io(p(t,L(B.isaret,B.bizde,.45),.6));
  tr('wallet',`translate(780 ${FY-80}) rotate(${8*Math.sin(t*3)}) scale(${t>B.isaret+.1?wk:0})`); op('wallet',(1-wFade*.85)*(1-io(p(t,B.bizde,.4))));
  $('q2').setAttribute('x',780); $('q2').setAttribute('y',FY-170); op('q2',(t>B.isaret+.1&&t<B.bizde)?wFade:0);
  // ceza damgası
  const sk=p(t,STAMP-.12,.12), sOut=io(p(t,B.ama,.3));
  tr('stamp',`translate(470 ${880}) rotate(-9) scale(${t>STAMP-.12?L(2.2,1,io(sk))*(1-sOut):0})`);
}
'''.replace('__B__', json.dumps(B))

build('/home/claude/kasaonu-medya/referans/sablonlar/ciplak01/index.html', 'MENÜ · 03', 'FİŞ 0008', 'CEZA', '50.000 TL',
      'Hiç çıplak fiyat', 'gördün mü?', SVG, SCENE)
print('ok')

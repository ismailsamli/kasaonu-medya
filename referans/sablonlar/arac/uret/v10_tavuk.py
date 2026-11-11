from base import build
import json, sys

B = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {
    "q": 1.2, "start": 3.8, "bir": 7.6, "iki": 12.2, "uc": 17.4, "dort": 22.0, "ama": 29.5, "biri": 36.0, "END": 41.4}

SVG = r'''
   <g id="big"><g id="bigC"></g></g>
   <g id="egg" filter="url(#ps)"><ellipse rx="34" ry="44" fill="#FFF8EB" stroke="#e6dfcd" stroke-width="3"/></g>
   <g id="coin" filter="url(#ps)"><circle r="40" fill="#E8B65C" stroke="#1c1b18" stroke-width="5"/><text y="12" font-size="30" text-anchor="middle" fill="#1c1b18">100</text></g>
   <g id="kids"></g>
   <g id="flocks"></g>
   <g id="cnts"></g>
   <g id="tags"></g>
   <g id="salgin" filter="url(#ps)"><rect x="-200" y="-56" width="400" height="112" fill="#ff5a1f" stroke="#1c1b18" stroke-width="6"/><text y="20" font-size="58" fill="#FFF8EB" text-anchor="middle" letter-spacing="8">SALGIN</text></g>
'''

SCENE = r'''
const B=__B__; const END=B.END;
const KR=L(B.dort,B.ama,.45), DUR=L(B.ama,B.biri,.5);
window.V={sfx:[[0.02,'thud'],[B.q+.4,'drop'],[B.q+.9,'pop'],[B.start+.1,'whoosh'],[B.start+.8,'ticks'],[B.bir+.3,'pop'],[B.iki+.3,'pop'],[B.iki+1.2,'ticks'],[B.uc+.3,'pop'],[B.uc+1.6,'ticks'],[B.dort+.3,'whoosh'],[KR,'thud'],[KR+.6,'ticks'],[B.ama+.2,'thud'],[DUR,'drop'],[B.biri+.3,'whoosh']]};
const LINES=[[B.start,B.bir-.1,'Baba dört oğluna<br><span class="o">yüzer lira verdi.</span>'],
 [B.bir,B.iki-.1,'1. tavuk aldı:<br><span class="o">yılda 365 lira.</span>'],
 [B.iki,B.uc-.1,'2. kiraladı:<br><span class="o">5 tavuk, yılda 1.825.</span>'],
 [B.uc,B.dort-.1,'3. yumurtayı peşin sattı:<br><span class="o">78 tavuk.</span>'],
 [B.dort,B.ama-.1,'4. kardeşlerin parası<br><span class="o">+ kredi: 702 tavuk.</span>'],
 [B.ama,B.biri-.1,'Bir salgın gelse?<br><span class="o">4. her şeyini kaybeder.</span>'],
 [B.biri,END-.45,'"Paranı ver, katlayayım"<br><span class="o">diyene tek soru:</span>']];
const BIG=[[B.ama,B.biri-.1]], HITS=[0.02,KR,B.ama+.2,DUR];
const FY=1262, KX=[140,350,590,800], KC=['#8A9B7C','#7C9DA5','#C56B50','#243139'];
const hen=(s)=>`<g transform="scale(${s})"><ellipse cx="0" cy="-34" rx="40" ry="32" fill="#FFF8EB"/><circle cx="28" cy="-66" r="18" fill="#FFF8EB"/><path d="M22 -86 q6 -12 12 0 q6 -12 12 2" fill="#ff5a1f"/><path d="M44 -66 l14 5 l-14 5z" fill="#E8B65C"/><circle cx="32" cy="-70" r="3" fill="#1c1b18"/><path d="M-40 -40 q-18 -14 -10 -34" stroke="#e6dfcd" stroke-width="8" fill="none"/><path d="M-6 -2 v10 M10 -2 v10" stroke="#E8B65C" stroke-width="5"/></g>`;
$('bigC').innerHTML=`<g filter="url(#ps)">${hen(3)}</g>`;
$('kids').innerHTML=KX.map((x,i)=>`<g id="k${i}" filter="url(#ps)"><path d="M${x-42} ${FY} L${x-36} ${FY-120} Q${x} ${FY-140} ${x+36} ${FY-120} L${x+42} ${FY}Z" fill="${KC[i]}"/><circle cx="${x}" cy="${FY-168}" r="40" fill="#e9c9a6"/><path d="M${x-40} ${FY-172} Q${x-38} ${FY-214} ${x} ${FY-212} Q${x+40} ${FY-212} ${x+40} ${FY-176} Q${x+14} ${FY-196} ${x-40} ${FY-172}Z" fill="#243139"/><circle cx="${x}" cy="${FY-60}" r="22" fill="#FFF8EB"/><text x="${x}" y="${FY-50}" font-size="28" text-anchor="middle" fill="#1c1b18">${i+1}</text></g>`).join('');
// sürüler: her kardeş için en fazla 40 minik tavuk
const CAP=[1,5,30,48];
$('flocks').innerHTML=KX.map((x,i)=>`<g id="f${i}">`+Array.from({length:CAP[i]},(_,j)=>{const cols=i<2?1:(i==2?5:6), c=j%cols, r=Math.floor(j/cols); const s=i<2?(i==0?.9:.55):.32; const gx=x+(c-(cols-1)/2)*(i<2?0:30), gy=FY-250-r*(i<2?(i==0?0:44):24);return `<g id="h${i}_${j}" transform="translate(${gx} ${gy})">${hen(s)}</g>`}).join('')+`</g>`).join('');
$('cnts').innerHTML=KX.map((x,i)=>`<g id="c${i}"><rect x="${x-92}" y="560" width="184" height="64" fill="#FFF8EB" stroke="#1c1b18" stroke-width="4"/><text id="ct${i}" x="${x}" y="604" font-size="32" text-anchor="middle" fill="${i==3?'#ff5a1f':'#1c1b18'}"></text></g>`).join('');
const VAL=[365,1825,22776,204984], AT=[B.bir,B.iki,B.uc,B.dort], NT=[1,5,78,702];
$('tags').innerHTML=[['KİRA',1],['PEŞİN',2],['KREDİ',3]].map(([t,i])=>`<g id="tg${i}" filter="url(#ps)"><rect x="-70" y="-28" width="140" height="56" fill="#ff5a1f" stroke="#1c1b18" stroke-width="4"/><text y="11" font-size="28" fill="#FFF8EB" text-anchor="middle">${t}</text></g>`).join('');
const fmt=n=>Math.round(n).toLocaleString('tr-TR');
function scene(t){
  // kanca: büyük tavuk ortada, kimin parası: üstüne bozuk para düşer, yumurta çıkar
  const bigOut=io(p(st(t),B.start+.2,.4)), bigBack=io(p(st(t),B.biri+.4,.6));
  const bs=(1-bigOut)+bigBack*(1-0); tr('big',`translate(470 ${FY-40}) scale(${cl(bs)})`); op('big',cl(bs)>0.01?1:0);
  const cd=io(p(t,B.q+.1,.5)), cin=(t>B.q&&t<B.start)?1:0;
  tr('coin',`translate(470 ${L(380,FY-260,cd)}) scale(${1-io(p(t,B.q+.6,.2))})`); op('coin',cin);
  const ek=ob(p(t,B.q+.9,.4)), eOut=io(p(t,B.start,.3));
  tr('egg',`translate(${L(470,600,ek)} ${FY-30}) scale(${t>B.q+.9?ek*(1-eOut):0})`);
  // kardeşler gelir
  const kin=oc(p(st(t),B.start+.2,.6)), kout=io(p(st(t),B.biri,.5));
  KX.forEach((x,i)=>{tr('k'+i,`translate(0 ${(1-kin)*500+kout*500})`); op('k'+i,(t>B.start&&t<B.biri+.55)?1:0)});
  // sayaçlar ve sürüler
  const loss=io(p(t,DUR,.8));
  KX.forEach((x,i)=>{
    const a=AT[i], k=oc(p(t,a+.4,1.4)), on=t>a&&t<B.biri+.4;
    let v=VAL[i]*k; if(i==3) v*=1-loss; if(i==0&&t>B.ama+.6) v=VAL[0];
    $('ct'+i).textContent=on?fmt(v):''; op('c'+i,on?ob(p(t,a,.3))*(1-io(p(t,B.biri,.3))):0);
    const n=CAP[i], show=t<a?0:Math.ceil(n*cl(p(t,a+.3,i<2?.6:1.4)));
    for(let j=0;j<n;j++){let fall=0;
      if(i==3) fall=loss; if(i==0&&j==0) fall=io(p(t,B.ama+.5,.6))*0; if(i==2) fall=io(p(t,DUR+.3,.8))*0;
      const el=$('h'+i+'_'+j); el.style.opacity=(j<show&&t<B.biri+.3)?1-fall*.85:0;
      el.setAttribute('transform',el.getAttribute('transform').replace(/ rotate\([^)]*\)/,'')+` rotate(${fall*95})`);}
  });
  // birinci kardeş tek tavuğunu kaybeder (salgında)
  const one=io(p(t,B.ama+.6,.6)); const h0=$('h0_0'); if(t>B.ama+.6&&t<B.biri+.3){h0.style.opacity=1-one*.85}
  // etiketler
  [[1,B.iki+.6],[2,B.uc+.8],[3,KR]].forEach(([i,a])=>{const k=ob(p(t,a,.35)),o=io(p(t,B.ama,.3)); tr('tg'+i,`translate(${KX[i]} ${FY-30}) rotate(-6) scale(${t>a?k*(1-o):0})`)});
  // 4. kardeşe paralar akar
  // salgın damgası
  const sp=p(t,B.ama+.1,.12), sOut=io(p(t,B.biri,.3));
  tr('salgin',`translate(470 760) rotate(-7) scale(${t>B.ama+.1?L(2,1,io(sp))*(1-sOut):0})`);
}
'''.replace('__B__', json.dumps(B))

build('/home/claude/kasaonu-medya/referans/sablonlar/tavuk01/index.html', 'HİKÂYE · 10', 'FİŞ 0015', 'AYNI BABA', '100 TL',
      'Senin tavuğun kimin', 'parasıyla yumurtluyor?', SVG, SCENE)
print('ok')

from base import build
import json, sys

B = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {
    "q": 1.2, "start": 3.0, "raf": 4.0, "susup": 8.3, "kanun": 10.4, "yani": 14.0, "foto": 18.4, "sor": 20.6, "END": 23.4}

SVG = r'''
   <g transform="translate(-40 0) translate(470 1262) scale(1.15) translate(-470 -1262)">
   <g id="reg" filter="url(#ps)"><rect x="560" y="1040" width="300" height="222" fill="#243139"/><rect x="590" y="1000" width="240" height="60" rx="6" fill="#243139"/><rect x="606" y="1012" width="120" height="36" fill="#7C9DA5"/><rect x="740" y="1012" width="74" height="36" fill="#E8B65C"/></g>
   <g id="rcpt" filter="url(#ps)"><rect id="rcB" x="610" y="0" width="200" height="0" fill="#FFF8EB"/>
     <text id="rcL1" x="628" font-size="26" fill="#8c8880">FİŞ</text><text id="rcV" x="792" font-size="46" fill="#ff5a1f" text-anchor="end">89,90</text></g>
   <g id="tag" filter="url(#ps)"><rect x="-130" y="-60" width="260" height="120" fill="#FFF8EB" stroke="#1c1b18" stroke-width="5"/><text x="-110" y="-24" font-size="22" fill="#8c8880">RAF</text><text y="38" font-size="58" fill="#1c1b18" text-anchor="middle">79,90</text></g>
   <path id="cmp" stroke="#1c1b18" stroke-width="10" stroke-linecap="round" fill="none"/><circle id="cmpD" r="13" fill="#ff5a1f"/>
   <text id="neq" font-size="80" fill="#ff5a1f" text-anchor="middle">≠</text>
   <path id="tick" d="M-40 0 l26 26 l52 -60" stroke="#ff5a1f" stroke-width="14" fill="none" stroke-linecap="round"/>
   <path id="strike" stroke="#1c1b18" stroke-width="9" stroke-linecap="round"/>
   <g id="law" filter="url(#ps)"><rect x="-150" y="-62" width="300" height="124" fill="#ff5a1f" stroke="#1c1b18" stroke-width="5"/><text y="-8" font-size="44" fill="#FFF8EB" text-anchor="middle" letter-spacing="6">KANUN</text><text y="40" font-size="28" fill="#1c1b18" text-anchor="middle">DÜŞÜK OLAN</text></g>
   <g id="coin" filter="url(#ps)"><circle r="48" fill="#E8B65C" stroke="#1c1b18" stroke-width="6"/><text y="14" font-size="38" fill="#1c1b18" text-anchor="middle">10</text></g>
   <g id="phone" filter="url(#ps)"><rect x="-90" y="-160" width="180" height="320" rx="24" fill="#1c1b18"/><rect id="scr" x="-74" y="-130" width="148" height="250" rx="8" fill="#7C9DA5"/><rect x="-62" y="-40" width="124" height="60" fill="#FFF8EB"/><text y="2" font-size="30" text-anchor="middle" fill="#1c1b18">79,90</text></g>
   </g>
   <rect id="flash" x="-200" y="-200" width="1340" height="2200" fill="#FFF8EB"/>
'''

SCENE = r'''
const B=__B__; const END=B.END; const KS=L(B.raf,B.susup,.5);
window.V={sfx:[[0.02,'thud'],[B.q+.3,'ticks'],[B.start,'whoosh'],[B.raf+.1,'pop'],[KS,'drop'],[B.susup+.2,'pop'],[B.susup+.5,'pop'],[B.kanun+.2,'scratch'],[L(B.kanun,B.yani,.5),'thud'],[B.yani+.4,'whoosh'],[B.foto+.3,'pop'],[B.sor+.3,'whoosh']]};
const LINES=[[B.start,B.raf-.1,'Fiyatı<br><span class="o">diyorum.</span>'],
 [B.raf,KS-.05,'Rafta<br><span class="o">79,90</span>'],
 [KS,B.susup-.1,'Kasada<br><span class="o">89,90</span>'],
 [B.susup,B.kanun-.1,'Çoğu kişi<br><span class="o">susup ödüyor.</span>'],
 [B.kanun,B.yani-.1,'Kanun açık:<br><span class="o">düşük olan geçerli.</span>'],
 [B.yani,B.foto-.1,'Tek cümle yeter:<br><span class="o">"Rafta böyle yazıyor."</span>'],
 [B.foto,B.sor-.1,'Etiketi çek,<br><span class="o">fişi sakla.</span>'],
 [B.sor,END-.45,'Kasadan çıkmadan<br><span class="o">kendine sor:</span>']];
const BIG=[[B.kanun,B.yani-.1]], HITS=[0.02,L(B.kanun,B.yani,.5)];
const FY=1262, TX=250, TY=900;
function scene(t){
  // fiş: kancada uzar uzar, sonra normale döner (ilk/son kare aynı)
  const longK=(t>B.q&&t<B.start+.3)?Math.sin(Math.PI*p(t,B.q+.2,B.start-B.q+.1)):0;
  const rh=180+260*longK+18*Math.sin(t*20)*longK;
  $('rcB').setAttribute('y',1000-rh); $('rcB').setAttribute('height',rh);
  $('rcL1').setAttribute('y',1000-rh+40); $('rcV').setAttribute('y',1000-40);
  // raf etiketi
  const tk=ob(p(t,B.raf+.1,.4)), tOut=io(p(t,B.sor,.35));
  tr('tag',`translate(${TX} ${TY}) rotate(-3) scale(${t>B.raf+.1?tk*(1-tOut):0})`);
  // karşılaştırma çizgisi
  const c=io(p(t,KS+.1,.5)), cOff=io(p(t,B.yani,.3)); const x0=TX+130, x1=L(x0,600,c), cy=TY;
  $('cmp').setAttribute('d',`M${x0} ${cy} L${x1} ${cy}`); $('cmpD').setAttribute('cx',x1); $('cmpD').setAttribute('cy',cy);
  const con=t>KS+.1&&t<B.yani+.3; ['cmp','cmpD'].forEach(i=>op(i,con?1-cOff:0));
  $('neq').setAttribute('x',(x0+600)/2); $('neq').setAttribute('y',cy-30); op('neq',con?c*(1-cOff):0);
  // sus ve öde: para kasaya kayar; yani'de geri gelir
  const pay=io(p(t,B.susup+.2,.6)), back=io(p(t,B.yani+.4,.8));
  const cx=L(L(150,700,pay),180,back), cyy=L(L(1180,1030,pay),1170,back)-160*Math.sin(Math.PI*(back>0?back:pay));
  tr('coin',`translate(${cx} ${cyy}) rotate(${(pay+back)*360})`); op('coin',(t>B.susup+.1&&t<B.foto)?(pay<1||back>0?1:0):0);
  // kanun: tik, üstü çizik, damga
  const lk=io(p(t,B.kanun+.3,.4)), lOff=io(p(t,B.foto,.3));
  tr('tick',`translate(${TX+40} ${TY-130}) scale(${lk*(1-lOff)})`);
  const sk=io(p(t,B.kanun+.6,.4)); $('strike').setAttribute('d',`M${640} ${960} L${L(640,800,sk)} ${L(960,930,sk)}`); op('strike',t>B.kanun+.6&&t<B.sor?1-lOff:0);
  const st2=L(B.kanun,B.yani,.5), sp=p(t,st2-.12,.12), sOut=io(p(t,B.yani,.3));
  tr('law',`translate(470 680) rotate(-7) scale(${t>st2-.12?L(2,1,io(sp))*(1-sOut):0})`);
  // fotoğraf: telefon etikete gelir, flaş
  const ph=oc(p(t,B.foto,.4)), phOut=io(p(t,B.sor,.3));
  tr('phone',`translate(${TX} ${L(1500,TY+40,ph)+phOut*700})`); op('phone',t>B.foto&&t<B.sor+.4?1:0);
  const fl=t>B.foto+.5?Math.max(0,1-(t-B.foto-.5)*4):0; op('flash',fl*.85);
}
'''.replace('__B__', json.dumps(B))

build('/home/claude/kasaonu-medya/referans/sablonlar/kasa01/index.html', 'KASA · 05', 'FİŞ 0010', 'FARK', '10 TL',
      'Kasada sana', 'fazla mı çıktı?', SVG, SCENE)
print('ok')

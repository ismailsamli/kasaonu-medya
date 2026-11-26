from base import build
import json, sys
from pathlib import Path

B = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {}
SENTS = ["Berberin verdiği sadakat kartında neden iki damga hazır basılı?", "Hediye mi sanıyorsun?", "Değil.",
 "O kart, seni daha sık getirmek için tasarlandı.", "Sonunda bu kartı nasıl kendi lehine çevireceğini de söyleyeceğim.",
 "Amerika'da bir oto yıkamacıda deney yaptılar.", "Üç yüz müşteriye kart dağıttılar.", "Yarısına sekiz boş kutulu kart verdiler.",
 "Diğer yarısına on kutulu kart, ama ilk iki kutu zaten damgalı.", "Dikkat et: iki grup da sekiz yıkama yaptıracaktı.",
 "Fark sadece görüntüdeydi.", "Sonuç?", "Boş kartla başlayanların yüzde on dokuzu ödülü aldı.",
 "Hazır damgalı kartla başlayanların yüzde otuz dördü.", "Neredeyse iki kat.", "Buna hazır ilerleme etkisi deniyor.",
 "Yolun başladığını görünce bırakmak zor geliyor.", "Bir de şu var: ödüle yaklaştıkça daha sık geliyorsun.",
 "Bir kafe çalışmasında, bedava ikrama yaklaşan müşterinin daha sık uğradığı ölçüldü.",
 "Alıcıysan: kartta kaç damga olduğuna değil, kaç tane daha alman gerektiğine bak.", "Zaten gideceğin yer değilse, kart için gitme.",
 "Satıcıysan: kartı boş verme.", "İlk damgayı sen bas, yol başlamış görünsün.",
 "Yarın Kasa Önü'nde, Efsane Cuma'da: stokta son iki ürün yazısı ne zaman gerçek, ne zaman tuzak?",
 "Bu tür taktikler hoşuna gidiyorsa, takip et."]
KEYS = ['q','hediye','degil','tasar','soz','oto','uc','bos','on','dikkat','fark','sonuc','y19','y34','iki','etki','yol','yakin','kafe','alici','gitme','satici','bas','yarin','takip']
REPL = [("iki damga","2 damga"),("Üç yüz","300"),("sekiz boş","8 boş"),("on kutulu","10 kutulu"),("ilk iki","ilk 2"),("sekiz yıkama","8 yıkama"),
        ("yüzde on dokuzu","%19'u"),("yüzde otuz dördü","%34'ü"),("iki kat","2 kat"),("son iki","son 2")]

def subs():
    out = []; starts = [B[k] for k in KEYS] + [B['END'] - 0.6]
    for i, s in enumerate(SENTS):
        a, b = starts[i], starts[i + 1] - 0.12
        for x, y in REPL: s = s.replace(x, y)
        words = s.split(); chunks, cur = [], []
        for w in words:
            cur.append(w)
            if len(cur) >= 3 or w[-1] in ',:.?' and len(cur) >= 2: chunks.append(' '.join(cur)); cur = []
        if cur:
            if chunks and len(cur) == 1: chunks[-1] += ' ' + cur[0]
            else: chunks.append(' '.join(cur))
        tot = sum(len(c) for c in chunks); t = a
        for c in chunks:
            d = (b - a) * len(c) / tot; out.append([round(t, 2), round(t + d, 2), c]); t += d
    return out

def card(cid, n, title, w=560):
    # n kutulu sadakat kartı; kutular JS ile boyanır (id: cid_s0..)
    cols = 5; r = 30; gap = (w - 80) / cols
    slots = ''.join(f'<circle id="{cid}_s{i}" cx="{-w/2+40+gap/2+(i%cols)*gap:.0f}" cy="{-20+(i//cols)*78}" r="{r}" fill="none" stroke="#243139" stroke-width="5"/>' for i in range(n))
    gift = f'<g transform="translate({-w/2+40+gap/2+((n-1)%cols)*gap:.0f} {-20+((n-1)//cols)*78})"><text y="12" font-size="34" text-anchor="middle" fill="#ff5a1f">★</text></g>'
    h = 120 + ((n - 1) // cols + 1) * 78
    return (f'<g id="{cid}"><g filter="url(#ps)"><rect x="{-w/2}" y="-110" width="{w}" height="{h}" rx="22" fill="#FFF8EB" stroke="#1c1b18" stroke-width="5"/></g>'
            f'<text x="{-w/2+30}" y="-64" font-size="30" fill="#1c1b18">{title}</text>{slots}{gift}</g>')

SVG = r'''
   <g id="pill" transform="translate(470 92)"><rect x="-300" y="-26" width="600" height="52" rx="26" fill="#1c1b18"/><text y="10" font-size="24" text-anchor="middle" fill="#FFF8EB">SONDA: KARTI KENDİ LEHİNE ÇEVİR ↓</text></g>
   ''' + card('cH', 10, 'SADAKAT KARTI') + r'''
   <g id="gift"><rect x="-150" y="-40" width="300" height="80" fill="#8A9B7C"/><text y="14" font-size="44" text-anchor="middle" fill="#FFF8EB">HEDİYE?</text></g>
   <g id="xDeg"><g filter="url(#ps)"><rect x="-200" y="-60" width="400" height="120" fill="#ff5a1f" stroke="#1c1b18" stroke-width="6"/></g><text y="22" font-size="70" text-anchor="middle" fill="#FFF8EB" letter-spacing="6">DEĞİL</text></g>
   <g id="loop"><path d="M-330 0 a330 200 0 1 1 0 2" fill="none" stroke="#ff5a1f" stroke-width="10" stroke-dasharray="30 20"/><path d="M-342 -20 l12 22 l14 -20" fill="none" stroke="#ff5a1f" stroke-width="10"/><text y="270" font-size="36" text-anchor="middle" fill="#1c1b18">TEKRAR GEL · TEKRAR GEL</text></g>
   <g id="car"><g filter="url(#ps)"><path d="M-170 40 v-50 l50 -60 h170 l60 60 h60 v50z" fill="#7C9DA5"/></g><circle cx="-100" cy="44" r="34" fill="#1c1b18"/><circle cx="110" cy="44" r="34" fill="#1c1b18"/>
     <g id="drops" fill="#3b82f6"><path d="M-90 -160 q-14 22 0 30 q14 -8 0 -30z"/><path d="M0 -190 q-14 22 0 30 q14 -8 0 -30z"/><path d="M90 -160 q-14 22 0 30 q14 -8 0 -30z"/></g>
     <text y="150" font-size="34" text-anchor="middle" fill="#1c1b18">OTO YIKAMA · ABD · 2004</text></g>
   <g id="crowd"><g id="dots"></g><text id="cnt" y="250" font-size="64" text-anchor="middle" fill="#1c1b18">0 MÜŞTERİ</text></g>
   ''' + card('cA', 8, 'A KARTI · 8 KUTU', 440) + card('cB', 10, 'B KARTI · 10 KUTU', 440) + r'''
   <g id="eq"><text y="0" font-size="48" text-anchor="middle" fill="#1c1b18">İKİSİNDE DE <tspan fill="#ff5a1f">8 YIKAMA</tspan></text></g>
   <g id="frk"><g filter="url(#ps)"><rect x="-300" y="-60" width="600" height="120" fill="#243139"/></g><text y="16" font-size="44" text-anchor="middle" fill="#FFF8EB">FARK: SADECE GÖRÜNTÜ</text></g>
   <g id="chart"><path d="M-260 300 H260" stroke="#1c1b18" stroke-width="6"/>
     <rect id="barA" x="-200" y="300" width="160" height="0" fill="#b9b4a8"/><rect id="barB" x="40" y="300" width="160" height="0" fill="#ff5a1f"/>
     <text id="tA1" x="-120" y="0" font-size="64" text-anchor="middle" fill="#1c1b18">%19</text><text id="tB1" x="120" y="0" font-size="64" text-anchor="middle" fill="#ff5a1f">%34</text>
     <text x="-120" y="350" font-size="28" text-anchor="middle" fill="#1c1b18">BOŞ KART</text><text x="120" y="350" font-size="28" text-anchor="middle" fill="#1c1b18">2 DAMGALI</text>
     <g id="x2" transform="translate(150 -230) rotate(-8)"><g filter="url(#ps)"><rect x="-150" y="-50" width="300" height="100" fill="#1c1b18"/></g><text y="20" font-size="54" text-anchor="middle" fill="#E8B65C">≈ 2 KAT</text></g></g>
   <g id="eff"><g filter="url(#ps)"><rect x="-330" y="-90" width="660" height="180" fill="#1c1b18" stroke="#ff5a1f" stroke-width="8"/></g><text y="-6" font-size="56" text-anchor="middle" fill="#FFF8EB">HAZIR İLERLEME</text><text y="58" font-size="56" text-anchor="middle" fill="#ff5a1f">ETKİSİ</text></g>
   <g id="road"><path d="M-320 0 H320" stroke="#1c1b18" stroke-width="10" stroke-linecap="round"/><path id="roadDone" d="M-320 0 H-192" stroke="#ff5a1f" stroke-width="16" stroke-linecap="round"/>
     <g transform="translate(320 0)"><path d="M0 0 V-120" stroke="#1c1b18" stroke-width="8"/><path d="M0 -120 h70 l-14 22 l14 22 h-70z" fill="#ff5a1f"/></g><circle id="walker" cx="-192" cy="-30" r="26" fill="#243139"/>
     <text y="90" font-size="34" text-anchor="middle" fill="#1c1b18">YOL BAŞLADI → BIRAKMAK ZOR</text></g>
   <g id="gg"><path d="M-330 0 H330" stroke="#1c1b18" stroke-width="6"/><g id="ticks"></g><text x="330" y="-40" font-size="40" text-anchor="end" fill="#ff5a1f">★ ÖDÜL</text>
     <text y="110" font-size="32" text-anchor="middle" fill="#1c1b18">ÖDÜLE YAKLAŞTIKÇA DAHA SIK</text><text id="kafeT" y="170" font-size="28" text-anchor="middle" fill="#8c8880">KAFE ÇALIŞMASI · KIVETZ VD., 2006</text></g>
   <g id="tagA"><rect x="-200" y="-36" width="400" height="72" fill="#8A9B7C"/><text y="14" font-size="40" text-anchor="middle" fill="#FFF8EB">ALICIYSAN</text></g>
   <g id="kal"><text y="0" font-size="44" text-anchor="middle" fill="#8c8880"><tspan id="kal1">KARTTA 2 DAMGA</tspan></text><text y="80" font-size="64" text-anchor="middle" fill="#ff5a1f">8 DAHA ALMAN LAZIM</text></g>
   <g id="git"><g filter="url(#ps)"><rect x="-290" y="-60" width="580" height="120" fill="#FFF8EB" stroke="#1c1b18" stroke-width="6"/></g><text y="16" font-size="42" text-anchor="middle" fill="#1c1b18">KART İÇİN GİTME</text></g>
   <g id="tagS"><rect x="-200" y="-36" width="400" height="72" fill="#243139"/><text y="14" font-size="40" text-anchor="middle" fill="#FFF8EB">SATICIYSAN</text></g>
   ''' + card('cS', 10, 'SENİN KARTIN') + r'''
   <g id="stamp"><rect x="-40" y="-90" width="80" height="80" rx="10" fill="#C56B50"/><rect x="-60" y="-14" width="120" height="30" rx="8" fill="#1c1b18"/></g>
   <g id="yrn"><g filter="url(#ps)"><rect x="-320" y="-230" width="640" height="460" fill="#243139"/></g><text y="-150" font-size="40" text-anchor="middle" fill="#E8B65C">YARIN KASA ÖNÜ'NDE</text>
     <text y="-80" font-size="34" text-anchor="middle" fill="#b9d0ea">EFSANE CUMA ÖZEL</text>
     <g transform="translate(0 10)"><rect x="-240" y="-46" width="480" height="92" rx="14" fill="#ff5a1f"/><text y="14" font-size="42" text-anchor="middle" fill="#FFF8EB">STOKTA SON 2 ÜRÜN!</text></g>
     <text y="140" font-size="40" text-anchor="middle" fill="#FFF8EB">Gerçek mi, <tspan fill="#ff5a1f">tuzak mı?</tspan></text></g>
   <g id="ytk"><rect x="-210" y="-44" width="420" height="88" rx="18" fill="#3b82f6"/><text y="14" font-size="42" text-anchor="middle" fill="#fff">+ TAKİP ET</text><text y="86" font-size="28" text-anchor="middle" fill="#1c1b18">@kasaonu.tr</text></g>
'''

SCENE = r'''
const B=__B__; const END=B.END; const SUBS=__SUBS__;
window.V={sfx:[[0.02,'thud'],[B.hediye+.1,'pop'],[B.degil,'thud'],[B.tasar+.1,'whoosh'],[B.soz+.1,'whoosh'],[B.oto+.1,'whoosh'],[B.uc+.2,'ticks'],[B.bos+.1,'pop'],[B.on+.1,'pop'],[B.on+1.9,'thud'],[B.on+2.2,'thud'],
 [B.dikkat+.1,'pop'],[B.fark+.1,'whoosh'],[B.sonuc+.1,'whoosh'],[B.y19+.3,'ticks'],[B.y34+.3,'ticks'],[B.iki,'thud'],[B.etki,'thud'],[B.yol+.1,'whoosh'],[B.yakin+.2,'ticks'],
 [B.alici+.1,'whoosh'],[B.gitme+.1,'pop'],[B.satici+.1,'whoosh'],[B.bas+.4,'thud'],[B.yarin+.1,'whoosh'],[B.takip+.1,'pop']]};
const LINES=[[B.hediye,B.tasar-.1,'Hediye mi?<br><span class="o">Değil.</span>'],[B.tasar,B.oto-.1,'Seni daha sık<br><span class="o">getirmek için.</span>'],
 [B.oto,B.bos-.1,'Oto yıkamada<br><span class="o">deney.</span>'],[B.bos,B.dikkat-.1,'8 boş kutu mu,<br><span class="o">2\'si dolu 10 mu?</span>'],[B.dikkat,B.sonuc-.1,'İkisi de<br><span class="o">8 yıkama.</span>'],
 [B.sonuc,B.etki-.1,'%19 vs<br><span class="o">%34.</span>'],[B.etki,B.yakin-.1,'Başlamış yol<br><span class="o">bırakılmaz.</span>'],[B.yakin,B.alici-.1,'Ödüle yaklaştıkça<br><span class="o">daha sık.</span>'],
 [B.alici,B.satici-.1,'<span class="o">Alıcıysan:</span><br>kalana bak.'],[B.satici,B.yarin-.1,'<span class="o">Satıcıysan:</span><br>ilk damgayı bas.'],
 [B.yarin,B.takip-.1,'Yarın<br><span class="o">Kasa Önü\'nde:</span>'],[B.takip,END,'Hoşuna gittiyse<br><span class="o">takip et.</span>']];
const BIG=[[B.etki-.1,B.yol-.1]], HITS=[0.02,B.degil,B.iki,B.etki];
$('dots').innerHTML=Array.from({length:300},(_,i)=>`<circle id="dt${i}" cx="${-290+(i%25)*24}" cy="${-200+Math.floor(i/25)*30}" r="9" fill="${i<150?'#b9b4a8':'#ff5a1f'}"/>`).join('');
$('ticks').innerHTML=(()=>{let x=-320,s='',g=90;for(let i=0;i<9;i++){s+=`<path id="tk${i}" d="M${x} -24 V24" stroke="#243139" stroke-width="10" stroke-linecap="round"/>`;x+=g;g*=0.78}return s})();
const fill=(cid,n,k)=>{for(let i=0;i<n;i++){const e=$(cid+'_s'+i); if(e) e.setAttribute('fill',i<k?'#ff5a1f':'none')}};
function scene(t){
  const W=(a,b)=>(t<a||t>b)?0:ob(p(t,a,.35))*(1-io(p(t,b-.25,.25)));
  // kanca: 2 damgalı kart
  const hv=t<B.oto?(t<B.hediye?1:1-io(p(t,B.oto-.3,.3))):0;
  tr('cH',`translate(470 ${t<B.tasar?880:L(880,900,p(t,B.tasar,.4))}) scale(${hv}) rotate(${Math.sin(t*2)*2})`); fill('cH',10,2);
  tr('gift',`translate(470 680) rotate(-6) scale(${t>B.hediye&&t<B.tasar?ob(p(t,B.hediye,.3))*(1-io(p(t,B.tasar-.2,.2))):0})`);
  tr('xDeg',`translate(470 690) rotate(-8) scale(${t>B.degil&&t<B.tasar+.1?L(2,1,io(p(t,B.degil,.15)))*(1-io(p(t,B.tasar,.15))):0})`);
  tr('loop',`translate(470 900) rotate(${t*30} 0 0) scale(${W(B.tasar,B.oto+.1)})`);
  const pv=t>B.soz+.4&&t<B.alici; tr('pill',`translate(470 92) scale(${pv?ob(p(t,B.soz+.4,.4))*(1-io(p(t,B.alici-.3,.3))):0})`);
  // oto yıkama + 300 müşteri
  tr('car',`translate(${L(-400,470,oc(p(t,B.oto,.6)))} 920) scale(${W(B.oto,B.uc+.2)})`); tr('drops',`translate(0 ${(t*80)%40})`);
  const cv=W(B.uc,B.bos+.25); op('crowd',cv>0?1:0); tr('crowd',`translate(470 860) scale(${cv})`);
  const nd=Math.round(300*io(p(t,B.uc+.1,1.2))); for(let i=0;i<300;i++) op('dt'+i,i<nd?1:0); $('cnt').textContent=nd+' MÜŞTERİ';
  // A ve B kartları
  const av=W(B.bos,B.sonuc+.25), bv=W(B.on,B.sonuc+.25);
  tr('cA',`translate(470 ${t<B.on?820:L(820,640,io(p(t,B.on,.4)))}) scale(${av*(t<B.on?1:L(1,.85,io(p(t,B.on,.4))))})`); fill('cA',8,0);
  tr('cB',`translate(470 990) scale(${bv*.85})`); fill('cB',10,t>B.on+1.9?(t>B.on+2.2?2:1):0);
  op('eq',t>B.dikkat+.4&&t<B.fark?1:0); tr('eq',`translate(470 1250)`);
  tr('frk',`translate(470 1240) scale(${W(B.fark,B.sonuc+.2)})`);
  // grafik
  const gv=W(B.sonuc,B.etki+.25); op('chart',gv>0?1:0); tr('chart',`translate(470 830) scale(${gv})`);
  const ha=500*.19/.34*io(p(t,B.y19+.3,.8)), hb=500*io(p(t,B.y34+.3,.8));
  $('barA').setAttribute('y',300-ha); $('barA').setAttribute('height',ha); $('barB').setAttribute('y',300-hb); $('barB').setAttribute('height',hb);
  $('tA1').setAttribute('y',280-ha); $('tB1').setAttribute('y',280-hb); op('tA1',t>B.y19+.5?1:0); op('tB1',t>B.y34+.5?1:0);
  tr('x2',`translate(150 -260) rotate(-8) scale(${t>B.iki?L(1.8,1,io(p(t,B.iki,.15))):0})`);
  tr('eff',`translate(470 880) rotate(-4) scale(${t>B.etki&&t<B.yol+.2?L(2,1,io(p(t,B.etki,.15)))*(1-io(p(t,B.yol,.2))):0})`);
  // yol
  const rv=W(B.yol,B.yakin+.25); tr('road',`translate(470 940) scale(${rv})`);
  const wx=L(-192,-60,io(p(t,B.yol+.4,1.6))); $('walker').setAttribute('cx',wx); $('roadDone').setAttribute('d',`M-320 0 H${wx}`);
  // hedefe yaklaştıkça sıklaşan ziyaretler
  const kv=W(B.yakin,B.alici+.25); tr('gg',`translate(470 940) scale(${kv})`);
  for(let i=0;i<9;i++) op('tk'+i,t>B.yakin+.6+i*.45?1:0); op('kafeT',t>B.kafe?1:0);
  // alıcıysan
  const a2=W(B.alici,B.satici+.25); tr('tagA',`translate(470 560) scale(${a2})`);
  tr('kal',`translate(470 830) scale(${t<B.gitme?a2:a2*(1-io(p(t,B.gitme,.3)))})`);
  tr('git',`translate(470 960) scale(${t>B.gitme?ob(p(t,B.gitme,.35))*a2:0})`);
  // satıcıysan: ilk damga
  const s2=W(B.satici,B.yarin+.25); tr('tagS',`translate(470 560) scale(${s2})`); tr('cS',`translate(470 900) scale(${s2})`);
  const sp=p(t,B.bas,.5); fill('cS',10,t>B.bas+.45?1:0);
  const sx=-280+40+48, sy=-20; tr('stamp',`translate(${470+sx} ${900+sy+L(-260,-10,io(sp))-(t>B.bas+.55?L(0,-200,io(p(t,B.bas+.55,.4))):0)}) scale(${t>B.bas&&t<B.yarin?s2:0})`);
  // yarın + takip
  tr('yrn',`translate(470 ${t>B.takip?L(900,820,io(p(t,B.takip,.4))):900}) scale(${t>B.yarin?ob(p(t,B.yarin,.4)):0})`);
  tr('ytk',`translate(470 1150) scale(${t>B.takip?ob(p(t,B.takip,.35))*(1+Math.sin(t*6)*.02):0})`);
  // altyazı
  const sb=$('sub'); let st='';for(const [a,b,x] of SUBS) if(t>=a&&t<b){st=x}
  if(sb.dataset.t!==st){sb.textContent=st;sb.dataset.t=st} sb.style.opacity=(st&&t>=B.hediye)?1:0;
}
'''

out = sys.argv[2] if len(sys.argv) > 2 else 'damga01'
path = f'/home/claude/kasaonu-medya/referans/sablonlar/{out}/index.html'
B['start'] = B['hediye']
build(path, 'TAKTİK · 26', 'FİŞ 0022', 'HAZIR İLERLEME', '1 TAKTİK',
      'Sadakat kartında neden', '2 damga hazır?', SVG, SCENE.replace('__B__', json.dumps(B)).replace('__SUBS__', json.dumps(subs(), ensure_ascii=False)))
h = Path(path).read_text(encoding='utf-8')
for a, b in [("hk.style.display=(t<B.start+.3||t>=END-HK)?'block':'none';", "hk.style.display=(t<B.start+.3)?'block':'none';"),
             ("push=io(p(t,END-HK,HK));", "push=0;"),
             ("tA.style.opacity=txt?cl(p(t,t0,.1)*2)*(1-p(t,END-HK-.15,.15)):0;", "tA.style.opacity=txt?cl(p(t,t0,.1)*2):0;"),
             ('<div id="tA"', '<div id="sub" class="abs gk" style="left:60px;right:60px;bottom:120px;text-align:center;font-size:50px;letter-spacing:-1px;line-height:1.1;color:#FFF8EB;background:#1c1b18;padding:18px 24px;border-radius:10px"></div>\n  <div id="tA"')]:
    assert a in h, a[:40]; h = h.replace(a, b)
Path(path).write_text(h, encoding='utf-8')
print('ok')

from base import build
import json, sys
from pathlib import Path

B = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {}
SENTS = ['Sepette "stokta son iki ürün" yazıyor.', "Kalbin hızlandı, değil mi?", "Bugün Efsane Cuma, bu yazıyı çok göreceksin.",
 "Sonunda gerçeğini sahtesinden nasıl ayıracağını da söyleyeceğim.", "Bin dokuz yüz yetmiş beşte bir deney yapıldı.",
 "Aynı kurabiyeler iki kavanoza kondu.", "Birinde on tane vardı, diğerinde iki.", "İnsanlar iki kurabiyelik kavanozdakini daha değerli buldu.",
 "Kurabiye aynı, sadece az görünüyordu.", "Daha ilginci: kavanoz gözlerinin önünde ondan ikiye düşünce kurabiye daha da değerli göründü.",
 'Hele "çok istendiği için azaldı" denince.', "Son iki ürün yazısı tam olarak bunu yapıyor: azlık ve rekabet.",
 "Ama Türkiye'de bunun bir kuralı var.", "Stoğu gerçekten sınırlı ürünlerde adedi göstermek zorunlu.",
 'Bol olan ürüne "son fırsat" deyip seni aceleye getirmek ise yasak.', "Alıcıysan: sayfayı kapat, yarın tekrar aç.",
 'Hâlâ "son iki" yazıyorsa, o iki hiç bitmiyor demektir.', "Satıcıysan: stok gerçekten azsa yaz, gerçek sayıyı yaz.",
 "Yalan azlık bir kere yakalanır, müşteri bir daha inanmaz.",
 "Yarın Kasa Önü'nde: kartla ödeyince neden iki katından fazla harcayabiliyorsun?", "Bu tür taktikler hoşuna gidiyorsa, takip et."]
KEYS = ['q','kalp','efsane','soz','deney','kavanoz','on','deger','ayni','ilginc','talep','sonIki','kural','zorunlu','yasak','alici','hala','satici','yalan','yarin','takip']
REPL = [("son iki ürün","son 2 ürün"),("Bin dokuz yüz yetmiş beşte","1975'te"),("iki kavanoza","2 kavanoza"),("on tane","10 tane"),("diğerinde iki","diğerinde 2"),
        ("iki kurabiyelik","2 kurabiyelik"),("ondan ikiye","10'dan 2'ye"),("Son iki ürün","Son 2 ürün"),('"son iki"','"son 2"'),("o iki","o 2"),("iki katından","2 katından")]

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

def jar(jid, label):
    # 10 kurabiyelik kavanoz; kurabiyeler JS ile görünür/gizlenir (id: jid_c0..9, alttan üste)
    pos = [(-62,150),(0,150),(62,150),(-31,100),(31,100),(-62,50),(0,50),(62,50),(-31,0),(31,0)]
    ck = ''.join(f'<g id="{jid}_c{i}" transform="translate({x} {y})"><circle r="28" fill="#C9935A" stroke="#8a5a2b" stroke-width="4"/>'
                 f'<circle cx="-9" cy="-6" r="4" fill="#3b2412"/><circle cx="8" cy="4" r="4" fill="#3b2412"/><circle cx="-2" cy="12" r="3" fill="#3b2412"/></g>' for i, (x, y) in enumerate(pos))
    return (f'<g id="{jid}"><g filter="url(#ps)"><path d="M-110 -60 h220 v230 q0 30 -30 30 h-160 q-30 0 -30 -30z" fill="#e6efe9" fill-opacity=".85" stroke="#1c1b18" stroke-width="6"/></g>'
            f'<rect x="-90" y="-92" width="180" height="36" rx="8" fill="#C56B50" stroke="#1c1b18" stroke-width="5"/>{ck}'
            f'<text id="{jid}_n" y="260" font-size="40" text-anchor="middle" fill="#1c1b18">{label}</text></g>')

SVG = r'''
   <g id="pill" transform="translate(470 92)"><rect x="-300" y="-26" width="600" height="52" rx="26" fill="#1c1b18"/><text y="10" font-size="24" text-anchor="middle" fill="#FFF8EB">SONDA: GERÇEK Mİ, SAHTE Mİ? ↓</text></g>
   <g id="shop"><g filter="url(#ps)"><rect x="-260" y="-250" width="520" height="500" rx="26" fill="#FFF8EB" stroke="#1c1b18" stroke-width="6"/></g>
     <rect x="-200" y="-200" width="400" height="230" rx="14" fill="#7C9DA5"/><path d="M-80 -40 l50 -90 l40 60 l30 -40 l60 70z" fill="#FFF8EB" opacity=".8"/>
     <text x="-200" y="80" font-size="34" fill="#1c1b18">Kablosuz Kulaklık</text><text x="-200" y="130" font-size="40" fill="#ff5a1f">1.299 ₺</text>
     <g id="badge" transform="translate(0 190)"><rect x="-210" y="-36" width="420" height="72" rx="12" fill="#e02424"/><text y="13" font-size="36" text-anchor="middle" fill="#fff">STOKTA SON 2 ÜRÜN!</text></g></g>
   <g id="heart"><path d="M0 30 C-90 -30 -60 -110 0 -70 C60 -110 90 -30 0 30z" fill="#e02424" stroke="#1c1b18" stroke-width="5"/></g>
   <g id="efs"><g filter="url(#ps)"><rect x="-230" y="-50" width="460" height="100" fill="#1c1b18"/></g><text y="16" font-size="48" text-anchor="middle" fill="#E8B65C">EFSANE CUMA</text></g>
   <g id="dny"><g filter="url(#ps)"><rect x="-260" y="-110" width="520" height="220" fill="#243139"/></g><text y="-20" font-size="80" text-anchor="middle" fill="#E8B65C">1975</text>
     <text y="50" font-size="36" text-anchor="middle" fill="#FFF8EB">KURABİYE DENEYİ</text><text y="92" font-size="24" text-anchor="middle" fill="#b9b4a8">WORCHEL, LEE &amp; ADEWOLE</text></g>
   ''' + jar('jA', '10 KURABİYE') + jar('jB', '2 KURABİYE') + jar('jC', '') + r'''
   <g id="crown"><path d="M-60 0 l-10 -60 l35 30 l35 -50 l35 50 l35 -30 l-10 60z" fill="#E8B65C" stroke="#1c1b18" stroke-width="5"/><text y="60" font-size="34" text-anchor="middle" fill="#ff5a1f">DAHA DEĞERLİ</text></g>
   <g id="ayn"><text y="0" font-size="50" text-anchor="middle" fill="#1c1b18">KURABİYE <tspan fill="#ff5a1f">AYNI</tspan></text><text y="64" font-size="36" text-anchor="middle" fill="#8c8880">sadece az görünüyor</text></g>
   <g id="up2"><text y="0" font-size="44" text-anchor="middle" fill="#ff5a1f">▲ DAHA DA DEĞERLİ</text></g>
   <g id="cok"><g filter="url(#ps)"><rect x="-230" y="-50" width="460" height="100" fill="#ff5a1f" stroke="#1c1b18" stroke-width="6"/></g><text y="16" font-size="40" text-anchor="middle" fill="#FFF8EB">"ÇOK İSTENDİ"</text></g>
   <g id="az"><g filter="url(#ps)"><rect x="-330" y="-80" width="300" height="160" fill="#1c1b18"/></g><text x="-180" y="18" font-size="52" text-anchor="middle" fill="#FFF8EB">AZLIK</text></g>
   <g id="rk"><g filter="url(#ps)"><rect x="30" y="-80" width="300" height="160" fill="#ff5a1f"/></g><text x="180" y="18" font-size="48" text-anchor="middle" fill="#FFF8EB">REKABET</text></g>
   <g id="plus"><text y="22" font-size="80" text-anchor="middle" fill="#1c1b18">+</text></g>
   <g id="tr"><rect x="-220" y="-36" width="440" height="72" fill="#C56B50"/><text y="14" font-size="36" text-anchor="middle" fill="#FFF8EB">TÜRKİYE'DE KURAL</text></g>
   <g id="zr"><g filter="url(#ps)"><rect x="-320" y="-90" width="640" height="180" fill="#FFF8EB" stroke="#1c1b18" stroke-width="6"/></g>
     <text y="-26" font-size="32" text-anchor="middle" fill="#1c1b18">Stok gerçekten sınırlı →</text><text y="20" font-size="32" text-anchor="middle" fill="#1c1b18">adedi göster</text>
     <rect x="-130" y="38" width="260" height="44" rx="8" fill="#5f8a4f"/><text y="70" font-size="30" text-anchor="middle" fill="#fff">ZORUNLU</text></g>
   <g id="ys"><g filter="url(#ps)"><rect x="-320" y="-100" width="640" height="220" fill="#FFF8EB" stroke="#1c1b18" stroke-width="6"/></g>
     <text y="-44" font-size="32" text-anchor="middle" fill="#1c1b18">Bol ürüne "son fırsat" →</text><text y="0" font-size="32" text-anchor="middle" fill="#1c1b18">acele ettirmek</text>
     <g id="ysS" transform="translate(0 62) rotate(-6)"><rect x="-130" y="-28" width="260" height="56" rx="8" fill="none" stroke="#e02424" stroke-width="6"/><text y="14" font-size="40" text-anchor="middle" fill="#e02424">YASAK</text></g></g>
   <g id="tb"><text y="0" font-size="24" text-anchor="middle" fill="#8c8880">KAYNAK: T.C. TİCARET BAKANLIĞI</text></g>
   <g id="tagA"><rect x="-200" y="-36" width="400" height="72" fill="#8A9B7C"/><text y="14" font-size="40" text-anchor="middle" fill="#FFF8EB">ALICIYSAN</text></g>
   <g id="cal1"><g filter="url(#ps)"><rect x="-140" y="-120" width="280" height="240" rx="16" fill="#FFF8EB" stroke="#1c1b18" stroke-width="6"/></g><rect x="-140" y="-120" width="280" height="60" rx="16" fill="#243139"/>
     <text y="-78" font-size="30" text-anchor="middle" fill="#FFF8EB">BUGÜN</text><text y="30" font-size="54" text-anchor="middle" fill="#e02424">SON 2</text></g>
   <g id="cal2"><g filter="url(#ps)"><rect x="-140" y="-120" width="280" height="240" rx="16" fill="#FFF8EB" stroke="#1c1b18" stroke-width="6"/></g><rect x="-140" y="-120" width="280" height="60" rx="16" fill="#243139"/>
     <text y="-78" font-size="30" text-anchor="middle" fill="#FFF8EB">YARIN</text><text y="30" font-size="54" text-anchor="middle" fill="#e02424">SON 2</text></g>
   <g id="bit"><g filter="url(#ps)"><rect x="-280" y="-50" width="560" height="100" fill="#1c1b18"/></g><text y="16" font-size="42" text-anchor="middle" fill="#E8B65C">HİÇ BİTMİYOR</text></g>
   <g id="tagS"><rect x="-200" y="-36" width="400" height="72" fill="#243139"/><text y="14" font-size="40" text-anchor="middle" fill="#FFF8EB">SATICIYSAN</text></g>
   <g id="stk"><g filter="url(#ps)"><rect x="-260" y="-110" width="520" height="220" rx="20" fill="#FFF8EB" stroke="#1c1b18" stroke-width="6"/></g>
     <text y="-30" font-size="34" text-anchor="middle" fill="#8c8880">GERÇEK STOK</text><text id="stkN" y="60" font-size="100" text-anchor="middle" fill="#5f8a4f">2 ADET</text></g>
   <g id="yl"><g filter="url(#ps)"><rect x="-300" y="-60" width="600" height="120" fill="#e02424"/></g><text y="16" font-size="40" text-anchor="middle" fill="#fff">YALAN AZLIK = 1 KERE</text></g>
   <g id="yrn"><g filter="url(#ps)"><rect x="-320" y="-230" width="640" height="460" fill="#243139"/></g><text y="-150" font-size="40" text-anchor="middle" fill="#E8B65C">YARIN KASA ÖNÜ'NDE</text>
     <g transform="translate(-130 -20)"><rect x="-100" y="-50" width="200" height="100" rx="10" fill="#8A9B7C"/><text y="14" font-size="36" text-anchor="middle" fill="#fff">NAKİT</text></g>
     <g transform="translate(130 -20)"><rect x="-110" y="-62" width="220" height="124" rx="14" fill="#ff5a1f"/><rect x="-110" y="-30" width="220" height="22" fill="#1c1b18"/><text y="40" font-size="36" text-anchor="middle" fill="#fff">KART</text></g>
     <text y="120" font-size="38" text-anchor="middle" fill="#FFF8EB">Kartla neden <tspan fill="#ff5a1f">2 katından</tspan></text><text y="170" font-size="38" text-anchor="middle" fill="#ff5a1f">fazla harcıyorsun?</text></g>
   <g id="ytk"><rect x="-210" y="-44" width="420" height="88" rx="18" fill="#3b82f6"/><text y="14" font-size="42" text-anchor="middle" fill="#fff">+ TAKİP ET</text><text y="86" font-size="28" text-anchor="middle" fill="#1c1b18">@kasaonu.tr</text></g>
'''

SCENE = r'''
const B=__B__; const END=B.END; const SUBS=__SUBS__;
window.V={sfx:[[0.02,'thud'],[B.kalp+.1,'thud'],[B.kalp+.5,'thud'],[B.efsane+.1,'pop'],[B.soz+.1,'whoosh'],[B.deney+.1,'whoosh'],[B.kavanoz+.1,'pop'],[B.on+.2,'ticks'],[B.on+1.2,'pop'],
 [B.deger+.1,'pop'],[B.ayni+.1,'whoosh'],[B.ilginc+.1,'whoosh'],[B.dusus,'ticks'],[B.deger2,'pop'],[B.talep+.1,'thud'],[B.sonIki+.1,'whoosh'],[B.azlik,'thud'],[B.azlik+.6,'thud'],
 [B.kural+.1,'whoosh'],[B.zorunlu+.1,'pop'],[B.yasak+.1,'pop'],[B.yasakW,'thud'],[B.alici+.1,'whoosh'],[B.hala+.1,'pop'],[B.hala+1.4,'thud'],[B.satici+.1,'whoosh'],[B.yalan+.1,'thud'],
 [B.yarin+.1,'whoosh'],[B.takip+.1,'pop']]};
const LINES=[[B.kalp,B.efsane-.1,'Kalbin<br><span class="o">hızlandı mı?</span>'],[B.efsane,B.deney-.1,'Gerçek mi,<br><span class="o">tuzak mı?</span>'],
 [B.deney,B.deger-.1,'10 kurabiye mi,<br><span class="o">2 kurabiye mi?</span>'],[B.deger,B.ilginc-.1,'Az olan<br><span class="o">değerli görünür.</span>'],
 [B.ilginc,B.talep-.1,'Gözünün önünde<br><span class="o">azalırsa?</span>'],[B.talep,B.sonIki-.1,'Daha da<br><span class="o">değerli.</span>'],[B.sonIki,B.kural-.1,'"Son 2"<br><span class="o">= azlık + rekabet</span>'],
 [B.kural,B.alici-.1,'Gerçek azlık<br><span class="o">yazılır.</span>'],[B.alici,B.satici-.1,'<span class="o">Alıcıysan:</span><br>yarın tekrar bak.'],
 [B.satici,B.yarin-.1,'<span class="o">Satıcıysan:</span><br>gerçek sayıyı yaz.'],[B.yarin,B.takip-.1,'Yarın<br><span class="o">Kasa Önü\'nde:</span>'],[B.takip,END,'Hoşuna gittiyse<br><span class="o">takip et.</span>']];
const BIG=[[B.azlik,B.kural-.1]], HITS=[0.02,B.talep,B.azlik,B.yasakW];
const cks=(jid,k)=>{for(let i=0;i<10;i++) op(jid+'_c'+i,i<k?1:0)};
function scene(t){
  const W=(a,b)=>(t<a||t>b)?0:ob(p(t,a,.35))*(1-io(p(t,b-.25,.25)));
  // kanca: sepet + son 2 rozeti
  const sv=t<B.deney?(1-io(p(t,B.deney-.3,.3))):0;
  tr('shop',`translate(470 ${t<B.efsane?880:L(880,930,io(p(t,B.efsane,.4)))}) scale(${sv*(t<B.efsane?1:L(1,.9,io(p(t,B.efsane,.4))))})`);
  tr('badge',`translate(0 190) scale(${1+Math.max(0,Math.sin(t*7))*.06})`);
  const hb=1+(t>B.kalp?Math.abs(Math.sin((t-B.kalp)*9))*.25:0);
  tr('heart',`translate(760 560) scale(${W(B.kalp,B.efsane+.2)*hb})`);
  tr('efs',`translate(470 540) rotate(-5) scale(${t>B.efsane&&t<B.deney?L(1.8,1,io(p(t,B.efsane,.15)))*(1-io(p(t,B.deney-.25,.25))):0})`);
  const pv=t>B.soz+.4&&t<B.alici; tr('pill',`translate(470 92) scale(${pv?ob(p(t,B.soz+.4,.4))*(1-io(p(t,B.alici-.3,.3))):0})`);
  // deney kartı
  tr('dny',`translate(470 880) scale(${W(B.deney,B.kavanoz+.1)})`);
  // iki kavanoz
  const jv=W(B.kavanoz,B.ilginc+.2);
  tr('jA',`translate(${L(470,250,io(p(t,B.kavanoz,.4)))} 820) scale(${jv})`); tr('jB',`translate(${L(470,690,io(p(t,B.kavanoz,.4)))} 820) scale(${jv})`);
  cks('jA',Math.round(10*io(p(t,B.on+.1,.9)))); cks('jB',t>B.on+1.1?2:0); op('jA_n',t>B.on+.9?1:0); op('jB_n',t>B.on+1.3?1:0);
  tr('crown',`translate(690 610) scale(${W(B.deger,B.ilginc+.2)})`);
  tr('ayn',`translate(470 1180) scale(${W(B.ayni,B.ilginc+.2)})`);
  // tek kavanoz: 10 -> 2
  const cv=W(B.ilginc,B.sonIki+.2); tr('jC',`translate(470 ${t<B.talep?820:L(820,780,io(p(t,B.talep,.3)))}) scale(${cv})`);
  const kc=t<B.dusus?10:Math.round(L(10,2,io(p(t,B.dusus,1.6)))); cks('jC',kc);
  $('jC_n').textContent=kc+' KURABİYE'; op('jC_n',t>B.ilginc+.3?1:0);
  tr('up2',`translate(470 520) scale(${t>B.deger2?W(B.deger2,B.sonIki+.2):0})`);
  tr('cok',`translate(470 1180) rotate(-6) scale(${t>B.talep&&t<B.sonIki+.2?L(2,1,io(p(t,B.talep,.15)))*(1-io(p(t,B.sonIki,.2))):0})`);
  // azlık + rekabet
  const av=W(B.sonIki,B.kural+.2);
  tr('az',`translate(470 860) scale(${t>B.azlik?av*L(1.6,1,io(p(t,B.azlik,.15))):0})`);
  tr('plus',`translate(470 860) scale(${t>B.azlik+.3?av:0})`);
  tr('rk',`translate(470 860) scale(${t>B.azlik+.6?av*L(1.6,1,io(p(t,B.azlik+.6,.15))):0})`);
  // kural
  const kv=W(B.kural,B.alici+.2); tr('tr',`translate(470 560) scale(${kv})`); tr('tb',`translate(470 1220) scale(${kv})`);
  tr('zr',`translate(470 ${t<B.yasak?820:L(820,760,io(p(t,B.yasak,.4)))}) scale(${t>B.zorunlu?kv*ob(p(t,B.zorunlu,.35))*(t<B.yasak?1:L(1,.85,io(p(t,B.yasak,.4)))):0})`);
  tr('ys',`translate(470 1030) scale(${t>B.yasak?kv*ob(p(t,B.yasak,.35))*.85:0})`);
  tr('ysS',`translate(0 62) rotate(-6) scale(${t>B.yasakW?L(2.2,1,io(p(t,B.yasakW,.15))):0})`);
  // alıcıysan
  const a2=W(B.alici,B.satici+.2); tr('tagA',`translate(470 560) scale(${a2})`);
  tr('cal1',`translate(${t<B.hala?470:L(470,280,io(p(t,B.hala,.4)))} 860) scale(${a2})`);
  tr('cal2',`translate(660 860) scale(${t>B.hala?a2*ob(p(t,B.hala,.35)):0})`);
  tr('bit',`translate(470 1110) rotate(-4) scale(${t>B.hala+1.3?a2*L(1.8,1,io(p(t,B.hala+1.3,.15))):0})`);
  // satıcıysan
  const s2=W(B.satici,B.yarin+.2); tr('tagS',`translate(470 560) scale(${s2})`); tr('stk',`translate(470 ${t<B.yalan?850:L(850,800,io(p(t,B.yalan,.3)))}) scale(${s2})`);
  tr('yl',`translate(470 1080) rotate(-4) scale(${t>B.yalan?s2*L(1.8,1,io(p(t,B.yalan,.15))):0})`);
  // yarın + takip
  tr('yrn',`translate(470 ${t>B.takip?L(900,820,io(p(t,B.takip,.4))):900}) scale(${t>B.yarin?ob(p(t,B.yarin,.4)):0})`);
  tr('ytk',`translate(470 1150) scale(${t>B.takip?ob(p(t,B.takip,.35))*(1+Math.sin(t*6)*.02):0})`);
  // altyazı
  const sb=$('sub'); let st='';for(const [a,b,x] of SUBS) if(t>=a&&t<b){st=x}
  if(sb.dataset.t!==st){sb.textContent=st;sb.dataset.t=st} sb.style.opacity=(st&&t>=B.kalp)?1:0;
}
'''

out = sys.argv[2] if len(sys.argv) > 2 else 'son2'
path = f'/home/claude/kasaonu-medya/referans/sablonlar/{out}/index.html'
B['start'] = B['kalp']
build(path, 'TAKTİK · 27', 'FİŞ 0023', 'SAHTE AZLIK', '1 TAKTİK',
      '"Stokta son 2 ürün"', 'gerçek mi?', SVG, SCENE.replace('__B__', json.dumps(B)).replace('__SUBS__', json.dumps(subs(), ensure_ascii=False)))
h = Path(path).read_text(encoding='utf-8')
for a, b in [("hk.style.display=(t<B.start+.3||t>=END-HK)?'block':'none';", "hk.style.display=(t<B.start+.3)?'block':'none';"),
             ("push=io(p(t,END-HK,HK));", "push=0;"),
             ("tA.style.opacity=txt?cl(p(t,t0,.1)*2)*(1-p(t,END-HK-.15,.15)):0;", "tA.style.opacity=txt?cl(p(t,t0,.1)*2):0;"),
             ('<div id="tA"', '<div id="sub" class="abs gk" style="left:60px;right:60px;bottom:120px;text-align:center;font-size:50px;letter-spacing:-1px;line-height:1.1;color:#FFF8EB;background:#1c1b18;padding:18px 24px;border-radius:10px"></div>\n  <div id="tA"')]:
    assert a in h, a[:40]; h = h.replace(a, b)
Path(path).write_text(h, encoding='utf-8')
print('ok')

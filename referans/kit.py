# Ortak parçalar (v19+): altyazı, kapanış, etiketler
import json
from pathlib import Path
from base import build

def subs(B, segs, repl, end_key='END'):
    keys = [k for k, _ in segs]; out = []
    starts = [B[k] for k in keys] + [B[end_key] - 0.6]
    for i, (_, s) in enumerate(segs):
        a, b = starts[i], starts[i + 1] - 0.12
        for x, y in repl: s = s.replace(x, y)
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

def box(id, w, h, fill, text, fs=40, color='#FFF8EB', stroke=None, rot=0, ty=None):
    st = f' stroke="{stroke}" stroke-width="6"' if stroke else ''
    ty = fs * .36 if ty is None else ty
    return (f'<g id="{id}"><g transform="rotate({rot})"><g filter="url(#ps)"><rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" fill="{fill}"{st}/></g>'
            f'<text y="{ty:.0f}" font-size="{fs}" text-anchor="middle" fill="{color}">{text}</text></g></g>')

TAGS = ('<g id="tagA"><rect x="-200" y="-36" width="400" height="72" fill="#8A9B7C"/><text y="14" font-size="40" text-anchor="middle" fill="#FFF8EB">ALICIYSAN</text></g>'
        '<g id="tagS"><rect x="-200" y="-36" width="400" height="72" fill="#243139"/><text y="14" font-size="40" text-anchor="middle" fill="#FFF8EB">SATICIYSAN</text></g>')

def yrn(inner):
    return (f'<g id="yrn"><g filter="url(#ps)"><rect x="-320" y="-230" width="640" height="460" fill="#243139"/></g>'
            f'<text y="-150" font-size="40" text-anchor="middle" fill="#E8B65C">YARIN KASA ÖNÜ\'NDE</text>{inner}</g>'
            '<g id="ytk"><rect x="-210" y="-44" width="420" height="88" rx="18" fill="#3b82f6"/><text y="14" font-size="42" text-anchor="middle" fill="#fff">+ TAKİP ET</text>'
            '<text y="86" font-size="28" text-anchor="middle" fill="#1c1b18">@kasaonu.tr</text></g>')

# sahne başı ortak JS: W() ve kapanış + altyazı
JS_HEAD = "const W=(a,b)=>(t<a||t>b)?0:ob(p(t,a,.35))*(1-io(p(t,b-.25,.25)));"
JS_TAIL = r'''
  tr('yrn',`translate(470 ${t>B.takip?L(900,820,io(p(t,B.takip,.4))):900}) scale(${t>B.yarin?ob(p(t,B.yarin,.4)):0})`);
  tr('ytk',`translate(470 1150) scale(${t>B.takip?ob(p(t,B.takip,.35))*(1+Math.sin(t*6)*.02):0})`);
  const sb=$('sub'); let st='';for(const [a,b,x] of SUBS) if(t>=a&&t<b){st=x}
  if(sb.dataset.t!==st){sb.textContent=st;sb.dataset.t=st} sb.style.opacity=(st&&t>=B.start)?1:0;
'''

def make(out, B, segs, repl, series, fis, botl, h1, h2, svg, scene):
    path = f'/home/claude/kasaonu-medya/referans/sablonlar/{out}/index.html'
    sc = scene.replace('__B__', json.dumps(B)).replace('__SUBS__', json.dumps(subs(B, segs, repl), ensure_ascii=False))
    build(path, series, fis, botl, '1 TAKTİK', h1, h2, svg, sc)
    h = Path(path).read_text(encoding='utf-8')
    for a, b in [("hk.style.display=(t<B.start+.3||t>=END-HK)?'block':'none';", "hk.style.display=(t<B.start+.3)?'block':'none';"),
                 ("push=io(p(t,END-HK,HK));", "push=0;"),
                 ("tA.style.opacity=txt?cl(p(t,t0,.1)*2)*(1-p(t,END-HK-.15,.15)):0;", "tA.style.opacity=txt?cl(p(t,t0,.1)*2):0;"),
                 ('<div id="tA"', '<div id="sub" class="abs gk" style="left:60px;right:60px;bottom:120px;text-align:center;font-size:50px;letter-spacing:-1px;line-height:1.1;color:#FFF8EB;background:#1c1b18;padding:18px 24px;border-radius:10px"></div>\n  <div id="tA"')]:
        assert a in h, a[:40]; h = h.replace(a, b)
    Path(path).write_text(h, encoding='utf-8')
    print('ok')

# Ortak iskelet: fiş zemini, kamera, kanca, alt yazılar, sarsıntı.
BASE = r'''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fonts/space-grotesk/700.css"><link rel="stylesheet" href="../../fonts/space-mono/700.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#201f1b}
#cam{position:absolute;left:0;top:0;width:1080px;height:1920px;transform-origin:540px 960px}
#rc{position:absolute;left:70px;top:150px;width:940px;height:1620px;background:#f3efe4;filter:drop-shadow(0 14px 18px rgba(0,0,0,.45))}
.mono{font-family:"Space Mono";font-weight:700}
.gk{font-family:"Space Grotesk";font-weight:700;color:#1c1b18;letter-spacing:-3px;line-height:.95}
.o{color:#ff5a1f}
.abs{position:absolute}
svg{position:absolute;left:0;top:0;overflow:visible}
svg text{font-family:"Space Mono";font-weight:700}
</style></head><body>
<div id="cam">
 <div id="rc">
  <div id="furn">
   <div class="abs mono" style="left:0;right:0;top:40px;text-align:center;font-size:30px;letter-spacing:8px;color:#1c1b18">✻ KASA ÖNÜ ✻</div>
   <div class="abs" style="left:60px;right:60px;top:96px;border-top:4px dashed #b9b4a8"></div>
   <div class="abs mono" style="left:60px;top:116px;font-size:26px;color:#1c1b18">__SERIES__</div>
   <div class="abs mono" style="right:60px;top:116px;font-size:26px;color:#8c8880">__FIS__</div>
   <div class="abs" style="left:60px;right:60px;top:160px;height:6px;background:#e3ded2"><div id="prog" style="height:6px;background:#ff5a1f;width:0"></div></div>
   <div class="abs mono" style="left:60px;right:60px;bottom:50px;font-size:24px;color:#8c8880;display:flex"><span>__BOTL__</span><span style="flex:1;border-bottom:3px dotted #b9b4a8;margin:0 14px 8px"></span><span>__BOTR__</span></div>
  </div>
  <svg id="sv" width="940" height="1620" viewBox="0 0 940 1620">
   <defs><filter id="ps" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="6" dy="9" stdDeviation="5" flood-color="#243139" flood-opacity=".28"/></filter></defs>
   <path id="floor" d="M-40 1262 H980" stroke="#1c1b18" stroke-width="10" stroke-linecap="round"/>
__SVG__
  </svg>
  <div id="tA" class="abs gk" style="left:50px;right:50px;top:270px;font-size:84px;text-align:center"></div>
 </div>
 <div id="hook" class="abs gk" style="left:90px;top:300px;width:900px"><div class="hw" style="font-size:150px">__H1__</div><div class="hw o" style="font-size:176px">__H2__</div></div>
</div>
<script>
const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x)), p=(t,a,d)=>cl((t-a)/d);
const io=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2, oc=x=>1-Math.pow(1-x,3);
const ob=x=>{const c1=1.7,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2)};
const L=(a,b,k)=>a+(b-a)*k, st=t=>Math.floor(t*12)/12, R=Math.PI/180;
const tr=(id,s)=>$(id).setAttribute('transform',s);
const op=(id,v)=>{$(id).style.opacity=v};
// kanca yazısı 900px'e sığsın
let FIT=false;function fit(){if(FIT||!document.fonts.check('700 100px "Space Grotesk"'))return;FIT=true;document.querySelectorAll('#hook .hw').forEach(w=>{w.style.whiteSpace='nowrap';w.style.display='inline-block';let f=parseFloat(w.style.fontSize);while(w.offsetWidth>900&&f>60){f-=2;w.style.fontSize=f+'px'}w.style.display='block'})}
__SCENE__
const HK=.45;
window.seek=function(t){
  fit();
  const pull=io(p(t,B.start-.1,.6)), push=io(p(t,END-HK,HK));
  let s=L(1.18,1,pull); s=L(s,1.18,push);
  $('cam').style.transform=`scale(${s})`;
  $('furn').style.opacity=pull*(1-push); $('prog').style.width=(cl(t/END)*100)+'%';
  $('floor').style.opacity=pull*(1-push);
  $('sv').style.transform=`translateY(${110*pull*(1-push)}px)`;
  const hk=$('hook'); hk.style.display=(t<B.start+.3||t>=END-HK)?'block':'none';
  hk.querySelectorAll('.hw').forEach((w,i)=>{let y=0,sc=1,o=1;
    if(t<B.start+.3){y=-6*Math.sin(t*3)*(i?1:-1)*(1-p(t,1.0,.5));sc=1-io(p(t,B.start-.2+i*.05,.3))}
    else{const k=oc(p(t,END-HK+i*.06,.33));y=(1-k)*80;o=cl(p(t,END-HK+i*.06,.1)*2)}
    w.style.transform=`translateY(${y}px) scaleY(${sc})`;w.style.transformOrigin='0 85%';w.style.opacity=o});
  scene(t,pull,push);
  const tA=$('tA'); let txt='',t0=0;for(const [a,b2,x] of LINES) if(t>=a&&t<b2){txt=x;t0=a}
  if(tA.dataset.t!==txt){tA.innerHTML=txt;tA.dataset.t=txt}
  const k2=ob(p(t,t0,.4)); tA.style.opacity=txt?cl(p(t,t0,.1)*2)*(1-p(t,END-HK-.15,.15)):0;
  tA.style.transform=`translateY(${(1-k2)*40}px) scale(${BIG.some(([a,b])=>t>=a&&t<b)?1.15:1})`;
  const sh=HITS.some(a=>t>a&&t<a+.22)?Math.sin(t*90)*7:0;
  $('rc').style.transform=`translateX(${sh}px)`;
};
seek(0);
</script></body></html>'''


def build(path, series, fis, botl, botr, h1, h2, svg, scene):
    html = (BASE.replace('__SERIES__', series).replace('__FIS__', fis).replace('__BOTL__', botl)
            .replace('__BOTR__', botr).replace('__H1__', h1).replace('__H2__', h2)
            .replace('__SVG__', svg).replace('__SCENE__', scene))
    from pathlib import Path
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(html, encoding='utf-8')

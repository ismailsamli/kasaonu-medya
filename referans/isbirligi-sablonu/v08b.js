window.T08 = { s1: 0, s2: 2.6, s3: 3.5, s4: 12.3, s6: 20.35, s7: 24.15, s8: 26.2, s9: 30.3, end: 33.0,
  nakitBar: 6.6, kartBar: 8.4, twoX: 10.6, cashGone: 13.5, cardCalm: 16.0, stamp: 18.7, pBtn: 26.4, kasaIn: 28.85 };
window.CAPS08 = [
  [0, 2.39, 'Nakit öderken canın daha mı çok yanıyor?', ['çok', 'yanıyor']],
  [2.65, 3.23, 'Normal.', ['normal']],
  [3.53, 5.82, "MIT'de maç bileti için teklif toplamışlar.", ['mit']],
  [6.1, 9.13, 'Yarısına "nakit ödeyeceksiniz" demişler, yarısına "kartla".', ['nakit', 'kartla']],
  [9.38, 12.04, 'Kartçılar, iki katından fazlasını teklif etmiş.', ['iki', 'katından']],
  [12.33, 14.76, 'Çünkü nakitte paranın elinden çıktığını görürsün,'],
  [15.05, 15.56, 'can yakar.', ['can', 'yakar']],
  [15.87, 17.21, 'Kartta cüzdan eksilmez,'],
  [17.42, 18.42, 'acı sonraya kalır.', ['sonraya']],
  [18.67, 19.97, 'Buna ödeme acısı deniyor.', ['ödeme', 'acısı']],
  [20.38, 23.66, 'Satıcıysan, müşteri nasıl ödemek istiyorsa öyle ödet.', ['öyle', 'ödet']],
  [24.2, 25.97, 'Bu videoyu Optikod destekledi:', ['optikod']],
  [26.25, 28.68, 'nakit, kart, veresiye tek ekranda,', ['tek', 'ekranda']],
  [28.88, 30.05, 'gün sonunda ayrı ayrı.', ['ayrı']],
  [30.35, 31.75, 'Sen nakit mi, kart mı?', ['nakit', 'kart']],
  [32.05, 33.0, 'Tek kelime yaz.', ['yaz']],
];
// #08 Ödeme acısı — Optikod (REKLAM) v2: gerçek logo + gerçek ekranlar, deneyin "neden"i anlatılıyor
const T = window.T08 || { s1: 0, s2: 2.5, s3: 3.4, s4: 10.6, s5: 13.0, s6: 19.0, s7: 22.0, s8: 23.6, s9: 28.5, end: 32.5,
  nakitBar: 6.0, kartBar: 7.6, twoX: 9.0, cashGone: 13.8, cardCalm: 15.6, stamp: 17.6, pBtn: 24.6, kasaIn: 26.4 };
const BILL = (id, x, y, w, rot) => `<svg id="${id}" class="abs" style="left:${x}px;top:${y}px;width:${w}px;height:${w * .5}px;transform:rotate(${rot}deg)" viewBox="0 0 200 100">
  <rect x="4" y="4" width="192" height="92" rx="8" fill="#f3efe4" stroke="#1c1b18" stroke-width="7"/>
  <circle cx="100" cy="50" r="24" fill="none" stroke="#1c1b18" stroke-width="6"/>
  <text x="100" y="62" text-anchor="middle" font-family="Space Mono" font-weight="700" font-size="34" fill="#1c1b18">₺</text>
  <path d="M24 24 h20 M156 76 h20" stroke="#1c1b18" stroke-width="6" stroke-linecap="round"/></svg>`;
const CARD = (id, x, y, w, rot) => `<svg id="${id}" class="abs" style="left:${x}px;top:${y}px;width:${w}px;height:${w * .63}px;transform:rotate(${rot}deg)" viewBox="0 0 200 126">
  <rect x="4" y="4" width="192" height="118" rx="14" fill="#ff5a1f" stroke="#1c1b18" stroke-width="7"/>
  <rect x="26" y="40" width="38" height="28" rx="5" fill="#f3efe4" stroke="#1c1b18" stroke-width="5"/>
  <path d="M26 96 h40 M78 96 h40 M130 96 h40" stroke="#f3efe4" stroke-width="7" stroke-linecap="round"/></svg>`;
const TAPE = (x, y, r) => `<div style="position:absolute;left:${x}px;top:${y}px;width:120px;height:38px;background:rgba(214,204,178,.85);transform:rotate(${r}deg);box-shadow:0 1px 2px rgba(0,0,0,.15)"></div>`;
// photo print frame for real screenshots: white border + slight shadow, like a print stapled to the receipt
const PRINT = (id, src, x, y, w, rot) => `<div id="${id}" class="abs" style="left:${x}px;top:${y}px;width:${w}px;padding:14px;background:#fff;box-shadow:0 10px 22px rgba(0,0,0,.22);transform:rotate(${rot}deg)">
  <div style="position:relative;overflow:hidden"><img src="${src}" style="display:block;width:100%;filter:saturate(.85) contrast(1.02)"><div class="hl"></div></div></div>`;
// button boxes on pay.png (625x260): Nakit, Kredi Kartı, Kart+Nakit, Veresiye
const PB = [[25, 77, 292, 36], [325, 77, 292, 36], [25, 121, 292, 36], [325, 121, 292, 36]];

setup({
  no: '08', cat: 'ÖDEME',
  scenes: [
    { s: T.s1, e: T.s2 - .05, html: `
      <div id="a1" class="abs big" style="left:66px;top:20px;width:820px">Nakit öderken canın daha mı <span class="or">çok yanıyor?</span></div>
      ${BILL('a2', 140, 470, 330, -8)}${CARD('a3', 520, 450, 300, 7)}`,
      init(d) { this.w = E.wrapWords(d.querySelector('#a1')); },
      upd(t, lt, $) {
        E.popWords(this.w, t, T.s1 + .05, .12);
        E.slideX($('a2'), t, T.s1 + .6, .45, -500, 'rotate(-8deg)');
        E.slideX($('a3'), t, T.s1 + .8, .45, 500, 'rotate(7deg)');
      } },
    { s: T.s2, e: T.s3 - .05, html: `<div id="b2" class="abs ctr" style="top:300px"><span style="display:inline-block;background:#ff5a1f;color:#f3efe4;font-weight:700;font-size:150px;padding:0 34px">Normal.</span></div>`,
      upd(t, lt, $) { E.slam($('b2'), t, T.s2 + .02, .25, -3); } },
    { s: T.s3, e: T.s4 - .05, html: `
      <div id="c0" class="abs tag" style="left:66px;top:0;font-size:32px">DENEY · MIT · MAÇ BİLETİ</div>
      <div class="abs" style="left:66px;top:90px;width:808px;display:flex;gap:30px">
        <div id="c1a" style="flex:1;border:6px solid #1c1b18;padding:18px;text-align:center"><div class="sm" style="font-weight:700">YARISI</div><div style="font-weight:700;font-size:40px">"NAKİT ÖDE"</div></div>
        <div id="c1b" style="flex:1;border:6px solid #ff5a1f;padding:18px;text-align:center;color:#ff5a1f"><div class="sm" style="font-weight:700">YARISI</div><div style="font-weight:700;font-size:40px">"KARTLA ÖDE"</div></div></div>
      <div class="abs" style="left:66px;top:300px;width:808px;display:flex;justify-content:space-between;align-items:flex-end;height:470px">
        <div style="width:380px;text-align:center"><div id="c2n" class="sm" style="font-weight:700;opacity:0">TEKLİF</div><div id="c2" style="margin:0 auto;width:200px;height:0;background:#1c1b18"></div></div>
        <div style="width:380px;text-align:center"><div id="c3n" style="font-weight:700;font-size:96px;color:#ff5a1f;opacity:0">2x+</div><div id="c3" style="margin:0 auto;width:200px;height:0;background:#ff5a1f"></div></div></div>`,
      upd(t, lt, $) {
        E.pop($('c0'), t, T.s3 + .05, .35, .5);
        E.slideX($('c1a'), t, T.s3 + 1.6, .4, -400); E.slideX($('c1b'), t, T.s3 + 2.3, .4, 400);
        $('c2').style.height = (E.oc(E.p(t, T.nakitBar, .6)) * 170) + 'px'; E.rise($('c2n'), t, T.nakitBar, .3, 20);
        $('c3').style.height = (E.ob(E.p(t, T.kartBar, .8)) * 360) + 'px';
        E.pop($('c3n'), t, T.twoX, .4, .3);
      } },
    { s: T.s4, e: T.s6 - .05, html: `
      <div id="d0" class="abs ctr" style="top:0;font-weight:700;font-size:110px">NEDEN?</div>
      <div class="abs" style="left:66px;top:200px;width:808px;display:flex;gap:30px">
        <div id="dL" style="flex:1;height:440px;border:6px solid #1c1b18;position:relative;overflow:hidden">
          <div class="sm" style="position:absolute;left:0;right:0;top:18px;text-align:center;font-weight:700">NAKİT</div>
          <svg id="dWal" style="position:absolute;left:90px;top:200px;width:200px;height:140px" viewBox="0 0 200 140"><path class="stroke" d="M10 30 H170 a20 20 0 0 1 20 20 V120 a10 10 0 0 1 -10 10 H20 a10 10 0 0 1 -10 -10 Z M140 70 h50 v34 h-50 Z"/></svg>
          ${BILL('dBill', 110, 150, 160, -4)}
          <div id="dOuch" style="position:absolute;left:0;right:0;bottom:22px;text-align:center;font-weight:700;font-size:40px;color:#ff5a1f;opacity:0">ŞİMDİ ACITIR</div></div>
        <div id="dR" style="flex:1;height:440px;border:6px solid #1c1b18;position:relative;overflow:hidden">
          <div class="sm" style="position:absolute;left:0;right:0;top:18px;text-align:center;font-weight:700">KART</div>
          ${CARD('dCard', 105, 150, 170, 6)}
          <div id="dLater" style="position:absolute;left:0;right:0;bottom:22px;text-align:center;font-weight:700;font-size:40px;opacity:0">SONRA ACITIR</div></div></div>
      <div id="d9" class="abs ctr" style="top:700px"><span class="stamp" style="font-size:64px;padding:14px 30px;background:#f3efe4">ÖDEME ACISI</span></div>`,
      upd(t, lt, $) {
        E.slam($('d0'), t, T.s4 + .02, .25, -2);
        E.rise($('dL'), t, T.s4 + .5, .4, 50); E.rise($('dR'), t, T.s4 + .7, .4, 50);
        const g = E.io(E.p(t, T.cashGone, .9));
        $('dBill').style.transform = `translate(${g * 260}px, ${-g * 220}px) rotate(${-4 + g * 50}deg)`;
        $('dBill').style.opacity = 1 - g;
        E.pop($('dOuch'), t, T.cashGone + .6, .35, .4);
        if (t > T.cashGone + .3 && t < T.cashGone + 1.2) $('dWal').style.transform = `translateX(${Math.sin(t * 70) * 6}px)`; else $('dWal').style.transform = '';
        $('dCard').style.transform = `rotate(6deg) translateY(${Math.sin(t * 2.2) * 6}px)`;
        E.rise($('dLater'), t, T.cardCalm, .4, 20);
        E.slam($('d9'), t, T.stamp, .26, -4);
      } },
    { s: T.s6, e: T.s7 - .05, html: `
      <div id="e0" class="abs tag" style="left:66px;top:0;font-size:32px">SATICIYSAN</div>
      <div id="e1" class="abs mid" style="left:66px;top:110px;width:808px">Müşteri nasıl ödemek istiyorsa, <span class="or">öyle ödet.</span></div>
      <div class="abs" style="left:66px;top:420px;width:808px;display:flex;justify-content:space-around;align-items:flex-end">
        <div id="e2" style="text-align:center">${BILL('e2i', 0, 0, 200, -4).replace('class="abs"', '').replace(/left:0px;top:0px;/, '')}<div class="sm" style="font-weight:700;margin-top:12px">NAKİT</div></div>
        <div id="e3" style="text-align:center">${CARD('e3i', 0, 0, 190, 5).replace('class="abs"', '').replace(/left:0px;top:0px;/, '')}<div class="sm or" style="font-weight:700;margin-top:12px">KART</div></div>
        <div id="e4" style="text-align:center"><svg style="width:150px;height:170px" viewBox="0 0 150 170"><path class="stroke" d="M20 10 H130 V160 H20 Z M44 10 V160 M60 50 H112 M60 80 H112 M60 110 H96"/></svg><div class="sm" style="font-weight:700;margin-top:12px">VERESİYE</div></div></div>`,
      init(d) { this.w = E.wrapWords(d.querySelector('#e1')); },
      upd(t, lt, $) { E.pop($('e0'), t, T.s6 + .05, .35, .5); E.popWords(this.w, t, T.s6 + .3, .17); ['e2','e3','e4'].forEach((id, i) => E.pop($(id), t, T.s6 + 1.4 + i * .3, .4, .2)); } },
    { s: T.s7, e: T.s8 - .05, html: `
      <div id="f1" class="abs ctr sm" style="top:40px;font-weight:700;letter-spacing:8px">BU VİDEOYU DESTEKLEYEN</div>
      <div id="f2" class="abs" style="left:300px;top:130px;width:340px;height:340px">
        <div style="position:absolute;inset:0;padding:16px;background:#fff;box-shadow:0 10px 22px rgba(0,0,0,.25)"><img src="optikod/logo.png" style="width:100%;display:block;border-radius:18px"></div>
        ${TAPE(-30, -12, -28)}${TAPE(250, 300, -28)}</div>
      <div id="f3" class="abs ctr sm" style="top:540px">barkodlu satış programı</div>`,
      upd(t, lt, $) {
        E.rise($('f1'), t, T.s7 + .02, .3, 20);
        const x = E.p(t, T.s7 + .15, .45);
        $('f2').style.opacity = x > 0 ? 1 : 0;
        $('f2').style.transform = `rotate(${E.lerp(-18, -4, E.oc(x))}deg) scale(${E.lerp(1.8, 1, E.oc(x))})`;
        E.rise($('f3'), t, T.s7 + .6, .3, 20);
      } },
    { s: T.s8, e: T.s9 - .05, html: `
      <div id="g0" class="abs tag" style="left:66px;top:0;font-size:30px">OPTİKOD · SATIŞ EKRANI</div>
      ${PRINT('g1', 'optikod/pay.png', 66, 70, 808, -1.5)}
      ${PRINT('g2', 'optikod/kasa.png', 96, 450, 760, 2)}
      <div id="g3" class="abs" style="left:520px;top:400px"><span class="tag" style="font-size:30px;background:#ff5a1f">GÜN SONU · AYRI AYRI</span></div>`,
      init(d) {
        const hl = d.querySelector('#g1 .hl');
        hl.innerHTML = PB.map((b, i) => `<div class="pbx" style="position:absolute;left:${b[0] / 6.25}%;top:${b[1] / 1.8}%;width:${b[2] / 6.25}%;height:${b[3] / 1.8}%;border:5px solid #ff5a1f;border-radius:8px;opacity:0"></div>`).join('');
      },
      upd(t, lt, $) {
        E.pop($('g0'), t, T.s8 + .02, .3, .5);
        E.slideX($('g1'), t, T.s8 + .1, .45, 700, 'rotate(-1.5deg)');
        const boxes = document.querySelectorAll('#g1 .pbx');
        const order = [0, 1, 3];
        boxes.forEach(b => { b.style.opacity = 0; });
        order.forEach((bi, k) => { const at = T.pBtn + k * .5; if (t >= at && t < at + .6) { boxes[bi].style.opacity = 1; boxes[bi].style.transform = `scale(${1 + .06 * Math.sin((t - at) * 12)})`; } });
        E.rise($('g2'), t, T.kasaIn, .5, 400, 'rotate(2deg)');
        E.slam($('g3'), t, T.kasaIn + .6, .25, -3);
      } },
    { s: T.s9, e: T.end, html: `
      <div id="h1" class="abs big" style="left:66px;top:40px;width:820px">Sen nakit mi, <span class="or">kart mı?</span></div>
      <div class="abs" style="left:66px;top:360px;width:808px;display:flex;gap:40px">
        <div id="h2" style="flex:1;text-align:center;border:8px solid #1c1b18;padding:30px 0;font-weight:700;font-size:72px">NAKİT</div>
        <div id="h3" style="flex:1;text-align:center;border:8px solid #1c1b18;padding:30px 0;font-weight:700;font-size:72px">KART</div></div>
      <div id="h4" class="abs ctr" style="top:620px"><span class="tag" style="font-size:40px;background:#ff5a1f;padding:12px 26px">TEK KELİME YAZ ↓</span></div>`,
      init(d) { this.w = E.wrapWords(d.querySelector('#h1')); },
      upd(t, lt, $) {
        E.popWords(this.w, t, T.s9 + .05, .14);
        E.pop($('h2'), t, T.s9 + .6, .4, .3); E.pop($('h3'), t, T.s9 + 1.0, .4, .3);
        const a = t > T.s9 + 1.5 ? Math.floor((t - T.s9 - 1.5) * 1.6) % 2 : -1;
        [$('h2'), $('h3')].forEach((el, i) => { el.style.background = a === i ? '#ff5a1f' : ''; el.style.color = a === i ? '#f3efe4' : ''; el.style.borderColor = a === i ? '#ff5a1f' : '#1c1b18'; });
        E.pop($('h4'), t, T.s9 + 1.8, .4, .4);
      } },
  ],
  caps: window.CAPS08 || [],
  punch: [T.s2 + .02, T.kartBar, T.twoX, T.s4 + .02, T.stamp, T.s7 + .2, T.kasaIn + .6],
  shake: [T.s2 + .02, T.stamp],
  sfx: [[T.s1 + .05, 'whoosh'], [T.s1 + .6, 'whoosh'], [T.s1 + .8, 'whoosh'], [T.s2 + .02, 'thud'], [T.s3, 'whoosh'], [T.s3 + 1.6, 'whoosh'], [T.s3 + 2.3, 'whoosh'],
    [T.kartBar, 'ticks'], [T.twoX, 'pop'], [T.s4 + .02, 'thud'], [T.cashGone, 'whoosh'], [T.stamp, 'thud'], [T.s6, 'whoosh'], [T.s7, 'whoosh'], [T.s7 + .25, 'thud'],
    [T.s8 + .1, 'whoosh'], [T.pBtn, 'pop'], [T.pBtn + .5, 'pop'], [T.pBtn + 1, 'pop'], [T.kasaIn, 'whoosh'], [T.kasaIn + .6, 'thud'], [T.s9, 'whoosh'], [T.s9 + .6, 'pop'], [T.s9 + 1.0, 'pop']],
});

// Ad disclosure (Ticari Reklam Yönetmeliği md. 23/A): visible from the first frame, before every other label
(function () {
  const ad = document.createElement('div');
  ad.style.cssText = 'position:absolute;left:96px;top:84px;z-index:5;display:flex;align-items:center;gap:12px;background:#1c1b18;color:#f3efe4;font-family:"Space Mono";font-weight:700;font-size:28px;letter-spacing:3px;padding:8px 16px;transform:rotate(-1deg)';
  ad.innerHTML = '<img src="optikod/logo.png" style="width:36px;height:36px;border-radius:7px">REKLAM · OPTİKOD tarafından desteklendi';
  document.body.insertBefore(ad, document.getElementById('grain'));
  // footer: small logo next to the sponsor line ("bu fiş ... katkısıyla basıldı")
  const foot = document.querySelector('.foot span');
  foot.innerHTML = '<img src="optikod/logo.png" style="width:40px;height:40px;border-radius:8px;vertical-align:middle;margin-right:12px">OPTİKOD KATKISIYLA';
})();

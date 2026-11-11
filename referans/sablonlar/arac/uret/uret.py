"""Ses dosyasından vuruş zamanlarını çıkarır, şablonu yeniden kurar, videoyu render eder.
kullanım: python3 uret.py <vid> <ses.mp3>
"""
import json, re, subprocess, sys, sys as _s
from pathlib import Path
_s.path.insert(0, '/home/claude/kasaonu-medya/referans/sablonlar/arac')
from render import sfx_track  # noqa
from playwright.sync_api import sync_playwright

INTRO, TAIL, FPS = 1.2, 0.6, 30
S = '/home/claude/kasaonu-medya/referans/sablonlar'
VIDS = {
 'boy01': ('v1_boy.py', ['q', 'start', 'fiyat', 'ml', 'ml2', 'yirmi', 'orta', 'cunku'], [
   'Sen hep büyüğünü mü alırsın?', 'Kahveden diyorum.',
   'Bir kahve zincirinde küçük yüz yetmiş beş, orta yüz seksen beş, büyük yüz doksan beş lira.',
   'Küçüğü üç yüz elli beş mililitre.', 'Büyüğü beş yüz doksan bir.', 'Yirmi lira farkla bardak bir buçuk katından büyük.',
   'Ortadaki bardak sana tek şey söylüyor: on lira daha ver, büyüğe geç.', 'Çünkü soru hep aynı:']),
 'egik01': ('v2_egik.py', ['q', 'start', 'egik', 'sabah', 'yetmis', 'tam', 'uzan', 'el', 'bu'], [
   'Sen de dokundun mu?', 'Apple mağazasındaki laptoplara diyorum.', 'Hepsi aynı açıyla eğik duruyor.',
   'Çalışanlar her sabah su terazisiyle tek tek ayarlıyor.', 'Önce yetmiş dereceydi, sonra yetmiş altıya çektiler.',
   'Ekranı tam göremeyeceğin kadar eğik.', 'Düzeltmek için uzanıyorsun.', 'El bir kere değdi mi, o artık senin gibi geliyor.',
   'Bu yüzden içeri giren herkese aynı soru:']),
 'ciplak01': ('v3_ciplak.py', ['q', 'start', 'yurt', 'onsekiz', 'isaret', 'bizde', 'antalya', 'giyinik', 'ama'], [
   'Sen hiç çıplak fiyat gördün mü?', 'Menüde diyorum.',
   'Yurt dışında bazı restoranlar fiyatın yanındaki para işaretini siliyor.', 'On sekiz dolar yazmıyor, sadece on sekiz.',
   'İşaret yoksa cüzdan aklına gelmiyor.', 'Bizde bu oyun tutmaz.',
   "Antalya'da bir restoran menüye TL yazmadı diye elli bin lira ceza yedi.", 'Bizde fiyat hep giyinik.',
   'Ama soru yine de soruluyor:']),
 'uniforma01': ('v4_uniforma.py', ['q', 'start', 'urun', 'zincir', 'kasiyer', 'ozaman'], [
   'Sana üniforma verdiler mi?', 'Markette diyorum.',
   'Ürünü sen okutuyorsun, poşeti sen dolduruyorsun, ödemeyi sen alıyorsun.',
   'Bir zincir elli mağazasına üç yüz elliden fazla böyle kasa kurdu.',
   'Kasiyerin işini sen yaptın ama fişte senin emeğin yazmıyor.', 'O zaman soru şu:']),
 'egik02': ('v2_egik.py', ['q','start','egik','sabah','yetmis','tam','uzan','el','sure','kurcala','bu'], [
   'Sen de dokundun mu?','Apple mağazasındaki laptoplara diyorum.','Hepsi aynı açıyla eğik duruyor.',
   'Çalışanlar her sabah su terazisiyle ayarlıyor.','Önce yetmiş dereceydi, sonra yetmiş altıya çektiler.',
   'Ekranı tam göremeyeceğin kadar eğik.','Düzeltmek için uzanıyorsun.',
   'Amaç tam bu: elin bir kere değdi mi, o cihaz artık senin gibi geliyor.',
   'Mağaza da sana süre sınırı koymuyor, istediğin kadar kurcala.','Çünkü kurcaladıkça bırakmak zorlaşıyor.',
   'Kapıdan çıkarken tek soru kalıyor:']),
 'kasa01': ('v5_kasa.py', ['q','start','raf','susup','kanun','yani','foto','sor'], [
   'Kasada sana fazla mı çıktı?','Fiyatı diyorum.','Rafta yetmiş dokuz doksan yazıyor, kasada seksen dokuz doksan çıkıyor.',
   'Çoğu kişi fark etse de susup ödüyor.','Oysa kanun açık: raf ile kasa farklıysa düşük olan geçerli.',
   'Yani on lirayı geri almak için tek cümle yeter: rafta böyle yazıyor.','Etiketin fotoğrafını çek, fişi sakla.',
   'O yüzden kasadan çıkmadan bir kere kendine sor:']),
 'kisaldi01': ('v6_kisaldi.py', ['q','start','kur','eni','rulo','paket','birim','etiket'], [
   'Seninki de mi kısaldı?','Tuvalet kağıdından bahsediyorum.','Kur yükselince bazı üreticiler zam yapmak yerine yaprağı küçülttü.',
   'Eni on santimden dokuz buçuğa, boyu on iki buçuktan on iki üçe indi.','Rulonun içi de genişledi, yani daha az kağıt sarıldı.',
   'Paket aynı, fiyat aynı, sen daha azını alıyorsun.','Bu yüzden paketin fiyatına değil, etiketin köşesindeki birim fiyata bak.',
   'Etiket söylemez ama rulo söyler:']),
 'indirim01': ('v7_indirim.py', ['q','start','bin','kural','agustos','ceza','yani','sepet'], [
   'Seni de önce şişirip sonra mı indirdiler?','Fiyatı diyorum.',
   'Bin liralık ürüne önce bin beş yüz yazılıyor, sonra üstü çiziliyor, altına büyük harflerle indirim.',
   'Bu oyunun artık kuralı var.','Ağustostan beri indirimden önceki fiyat, son on günün en düşük fiyatı olmak zorunda.',
   'Uymayana kırk milyona yakın ceza var.','Yani üstü çizili fiyatı son on günde hiç görmediysen, o indirim değil.',
   'Sepete atmadan önce bir kere sor:']),
 'araba01': ('v8_araba.py', ['q','start','ilk','cunku','sonra','deneme','uc','dolunca','araba'], [
   'Büyüdükçe daha çok dolduruyorsun, değil mi?','Market arabasını diyorum.','İlk araba bin dokuz yüz otuz yedide çıktı.',
   'Çünkü market sahibi bir şey fark etmişti: sepet dolunca insan alışverişi bitiriyor.','Sonra arabalar büyüdü.',
   'Bir denemede araba iki katına çıkınca insanlar beş ürün yerine yedi ürün aldı.','Üç şey alacaksan arabayı bırak, sepeti al.',
   'Sepet dolunca durursun.','Araba ise hep aynı şeyi fısıldar:']),
 'incel01': ('v9_incel.py', ['q','start','almanya','paket','milim','takilan','bizde','arka','gram','ve'], [
   'Seninki de mi inceldi?','Çikolatayı diyorum.',"Almanya'da ünlü bir çikolata önce zamlandı, sonra yüz gramdan doksan grama indi.",
   'Paket aynı, tasarım aynı.','Çikolata sadece bir milim inceldi.','Takılan olmadı, ta ki biri mahkemeye taşıyana kadar.',
   'Bizde de görüldü: rafta altmış gram yazan çubuk kraker, paketin üstünde elli iki çıktı.',
   'Paketin önüne değil, arkasına bak.','Gramı orada yazar.','Ve hep aynı şeyi sorar:']),
}


def dur(f):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]))


def beats(vid, voice):
    gen, keys, sents = VIDS[vid]
    w = Path(f'/home/claude/uret/{vid}_voice.wav')
    subprocess.check_call(['ffmpeg', '-y', '-loglevel', 'error', '-i', voice, '-af',
                           'silenceremove=start_periods=1:start_threshold=-40dB,areverse,silenceremove=start_periods=1:start_threshold=-40dB,areverse',
                           '-ar', '44100', '-ac', '1', str(w)])
    D = dur(str(w))
    log = subprocess.run(['ffmpeg', '-i', str(w), '-af', 'silencedetect=noise=-35dB:d=0.15', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', log)]
    en = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', log)]
    gaps = [(a, b) for a, b in zip(st, en)]
    lens = [len(s) for s in sents]; tot = sum(lens)
    starts = [0.0]; used = set()
    for i in range(1, len(sents)):
        est = D * sum(lens[:i]) / tot
        cand = [(abs(b - est), j, b) for j, (a, b) in enumerate(gaps) if j not in used and b > starts[-1] + .3]
        if cand:
            c = min(cand)
            if c[0] < 1.6:
                used.add(c[1]); starts.append(c[2]); continue
        starts.append(est)
    B = {k: round(INTRO + s, 3) for k, s in zip(keys, starts)}
    B['q'] = INTRO
    B['END'] = round(INTRO + D + TAIL, 3)
    return gen, B, w, gaps, D


def render(vid, voice):
    gen, B, w, gaps, D = beats(vid, voice)
    print(vid, 'ses', round(D, 2), 'sn | vuruşlar', B)
    subprocess.check_call(['python3', f'/home/claude/uret/{gen}', json.dumps(B), vid], cwd='/home/claude/uret')
    html = Path(S) / vid / 'index.html'
    out = Path(f'/home/claude/uret/{vid}.mp4'); silent = Path(f'/home/claude/uret/_{vid}_s.mp4')
    n = int(B['END'] * FPS)
    ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(FPS), '-i', '-',
                           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', str(silent)], stdin=subprocess.PIPE)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--disable-gpu'])
        pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        pg.goto(html.resolve().as_uri()); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(800)
        events = pg.evaluate('V.sfx')
        for f in range(n):
            pg.evaluate(f'seek({f / FPS})'); ff.stdin.write(pg.screenshot(type='jpeg', quality=93))
        # döngü kontrolü: ilk kare ve son kare
        pg.evaluate('seek(0)'); pg.screenshot(path=f'/home/claude/uret/{vid}_ilk.png')
        pg.evaluate(f"seek({B['END']})"); pg.screenshot(path=f'/home/claude/uret/{vid}_son.png')
        b.close()
    ff.stdin.close(); ff.wait()
    sfx = Path(f'/home/claude/uret/_{vid}_sfx.wav'); sfx_track(events, B['END'], sfx)
    d = int(INTRO * 1000)
    subprocess.check_call(['ffmpeg', '-y', '-loglevel', 'error', '-i', str(silent), '-i', str(w), '-i', str(sfx), '-filter_complex',
        f'[1:a]adelay={d}|{d},apad[v];[2:a]volume=0.32[s];[v][s]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]',
        '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', str(out)])
    print('bitti', out, round(dur(str(out)), 2))


if __name__ == '__main__':
    render(sys.argv[1], sys.argv[2])

# Hızlı kontrol: şablonu kur, seçilen anlarda kare al, ızgara yap. python3 onizle.py vid gen.py fix.json t1,t2,...
import json, sys, subprocess
from playwright.sync_api import sync_playwright
from PIL import Image
vid, gen, fixf, ts = sys.argv[1], sys.argv[2], sys.argv[3], [float(x) for x in sys.argv[4].split(',')]
B = json.load(open(fixf)); B['q'] = 0.1
subprocess.check_call(['python3', gen, json.dumps(B), vid])
W = Image.new('RGB', (270 * 8, 480 * ((len(ts) + 7) // 8)), 'white')
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--disable-gpu']); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(f'file:///home/claude/kasaonu-medya/referans/sablonlar/{vid}/index.html'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(800)
    for i, t in enumerate(ts):
        pg.evaluate(f'seek({t})'); pg.screenshot(path='/tmp/_k.png')
        W.paste(Image.open('/tmp/_k.png').resize((270, 480)), ((i % 8) * 270, (i // 8) * 480))
    b.close()
print('hatalar', errs)
W.save(f'/home/claude/uret/{vid}_on.png')

import subprocess, sys
from pathlib import Path
from playwright.sync_api import sync_playwright
html, out, dur = sys.argv[1], sys.argv[2], float(sys.argv[3])
stills = [float(x) for x in sys.argv[4:]]
FPS = 30
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--disable-gpu"])
    pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.goto(Path(html).resolve().as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(800)
    if stills:
        for t in stills:
            pg.evaluate(f"seek({t})"); pg.screenshot(path=f"st_{Path(html).stem}_{t:05.2f}.png")
    else:
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-i", "-",
                               "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-shortest",
                               "-c:v", "libx264", "-preset", "veryfast", "-b:v", "6M", "-maxrate", "6M", "-bufsize", "12M",
                               "-pix_fmt", "yuv420p", "-c:a", "aac", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
        for f in range(int(dur * FPS)):
            pg.evaluate(f"seek({f / FPS})"); ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
        ff.stdin.close(); ff.wait()
    b.close()
print("ok")

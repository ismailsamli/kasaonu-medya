# Metin anahtarlarını sessizlik boşluklarına eşler. Kullanım: python3 esle.py <wav> <segs.json>
# segs.json: [[anahtar, "metin parçası"], ...] (parçalar sırayla tam metni oluşturur)
import json, re, subprocess, sys
wav, segf = sys.argv[1], sys.argv[2]
segs = json.load(open(segf))
D = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',wav]))
log = subprocess.run(['ffmpeg','-i',wav,'-af','silencedetect=n=-35dB:d=0.12','-f','null','-'],capture_output=True,text=True).stderr
st=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',log)]; en=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',log)]
gaps=list(zip(st,en))
L=[len(re.sub(r'\W','',s)) for _,s in segs]; tot=sum(L)
# pause weight: boşluk süresini metin oranından çıkar
sil=sum(b-a for a,b in gaps); speak=D-sil
out={}; prev=0; used=set()
for i,(k,s) in enumerate(segs):
    if i==0: out[k]=0.0; continue
    est=speak*sum(L[:i])/tot
    # tahmini konuşma süresine o ana kadarki boşlukları ekle (iteratif)
    t=est
    for _ in range(5): t=est+sum(min(b,t)-a for a,b in gaps if a<t)
    c=[(abs(b-t),j,b) for j,(a,b) in enumerate(gaps) if j not in used and b>prev+.4]
    if c and min(c)[0]<1.3: d,j,b=min(c); used.add(j); out[k]=b; flag='' if d<.6 else ' ?'
    else: out[k]=t; flag=' TAHMİN'
    prev=out[k]; print(f'{k:8s} {out[k]:6.2f} (tahmin {t:6.2f}){flag}  {s[:50]}')
print('D',round(D,2))
json.dump({k:round(v+0.1,2) for k,v in out.items()}|{'END':round(D+0.1+1.8,2)},open(segf.replace('.json','_fix.json'),'w'))

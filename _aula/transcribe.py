# -*- coding: utf-8 -*-
from faster_whisper import WhisperModel
import time, sys
MP3 = r"C:/Users/ivign/CYBERSEC/_aula/bloco1.mp3"
OUT = r"C:/Users/ivign/CYBERSEC/_aula/bloco1_transcricao.txt"
t0 = time.time()

def load():
    for dev, ct, model in [("cuda","int8_float16","medium"),("cuda","int8","small"),("cpu","int8","small")]:
        try:
            m = WhisperModel(model, device=dev, compute_type=ct)
            print(f"[modelo] {model} em {dev}/{ct}", flush=True)
            return m
        except Exception as e:
            print(f"[falhou] {model} {dev}/{ct}: {e}", flush=True)
    raise SystemExit("nenhum backend whisper carregou")

m = load()
segments, info = m.transcribe(MP3, language="pt", beam_size=1)
print(f"[info] duração detectada {info.duration/60:.1f} min", flush=True)
n = 0
with open(OUT, "w", encoding="utf-8") as f:
    for s in segments:
        line = f"[{int(s.start//60):02d}:{int(s.start%60):02d}] {s.text.strip()}"
        f.write(line + "\n"); f.flush()
        n += 1
        if n % 25 == 0:
            print(f"...{n} segmentos ({s.start/60:.0f} min) {time.time()-t0:.0f}s", flush=True)
print(f"[DONE] {n} segmentos em {time.time()-t0:.0f}s -> {OUT}", flush=True)

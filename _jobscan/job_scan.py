# -*- coding: utf-8 -*-
"""Varredura diária de vagas cyber -> alimenta o app (vagas_data.js) + digest datado.
Fontes: curadoria Dice (jobs_seed.json, mantida à mão/sessão) + APIs abertas (RemoteOK/Remotive).
Indeed/Monster/LinkedIn não entram (WAF/geo). Anti-gate-morto: grava data de atualização visível no app."""
import json, os, re, time, urllib.request, datetime

BASE = r"C:/Users/ivign/CYBERSEC/_jobscan"
APP  = r"C:/Users/ivign/CYBERSEC"

ROLE_WORDS = ["security","cyber","soc analyst","siem","vulnerab","grc","incident","threat",
              "infosec","penetration","pentest","appsec","devsecops","detection","malware",
              "risk analyst","compliance analyst","ai security","security analyst","security engineer"]
def is_cyber(title):
    t = (title or "").lower()
    return any(w in t for w in ROLE_WORDS)

def level_of(title):
    t = (title or "").lower()
    if any(w in t for w in ["intern","internship"]): return "estágio"
    if any(w in t for w in ["junior","jr ","associate","entry","early career","i "]): return "entry"
    if any(w in t for w in ["senior","sr ","lead","principal","staff","manager","director","architect"]): return "senior"
    return "pleno"

def fetch(url, ua=False):
    req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"} if ua else {})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode("utf-8","ignore"))

live = []
# RemoteOK (feed geral -> filtra título de verdade)
try:
    for j in fetch("https://remoteok.com/api", ua=True):
        if not isinstance(j, dict) or not j.get("position"): continue
        if is_cyber(j.get("position")):
            live.append({"role":j.get("position","")[:70],"company":j.get("company","")[:30],
                "loc":(j.get("location") or "Remoto")[:24],"pay":"—","level":level_of(j.get("position")),
                "source":"RemoteOK","req":["secplus"],"clearance":False,"sponsor":False,"student":False,
                "url":j.get("url",""),"note":"remoto (filtrado por título)"})
except Exception as e:
    print("RemoteOK falhou:", e)

# dedupe live
seen=set(); live2=[]
for j in live:
    k=(j["role"].lower(), j["company"].lower())
    if k in seen: continue
    seen.add(k); live2.append(j)
live = live2[:20]

# seed curado (Dice) — a espinha de qualidade
seed = json.load(open(os.path.join(BASE,"jobs_seed.json"), encoding="utf-8"))

allj = seed + [j for j in live if (j["role"].lower(),j["company"].lower()) not in
               {(s["role"].lower(),s["company"].lower()) for s in seed}]

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
entry_now = [j for j in allj if j["level"] in ("entry","estágio") and not j.get("clearance")]
sponsor = [j for j in allj if j.get("sponsor")]
insight = (f"{len(allj)} vagas no radar · {len(entry_now)} de entrada aplicáveis (sem cidadania) · "
           f"{len(sponsor)} patrocinam visto. Foco: Security+ destrava a maioria das de entrada; "
           f"a de IA+sponsor (Tymon) é o alvo-diferencial.")

js = ("// GERADO por job_scan.py — NÃO editar à mão\n"
      f"window.JOBS_UPDATED={json.dumps(now, ensure_ascii=False)};\n"
      f"window.JOBS_INSIGHT={json.dumps(insight, ensure_ascii=False)};\n"
      f"window.JOBS_LIVE={json.dumps(allj, ensure_ascii=False)};\n")
open(os.path.join(BASE,"vagas_data.js"),"w",encoding="utf-8").write(js)
# cópia ao lado do app (o app carrega _jobscan/vagas_data.js — mesma pasta base)
print(f"[ok] {len(allj)} vagas -> vagas_data.js @ {now} (live API: {len(live)}, seed: {len(seed)})")

# digest datado (append) + log
with open(os.path.join(BASE,"job_digest.md"),"a",encoding="utf-8") as f:
    f.write(f"\n## {now}\n- {insight}\n- entrada aplicável: "
            + ", ".join(f"{j['role']} @ {j['company']}" for j in entry_now[:6]) + "\n")
with open(os.path.join(BASE,"job_scan_log.ndjson"),"a",encoding="utf-8") as f:
    f.write(json.dumps({"ts":now,"total":len(allj),"live":len(live),"entry":len(entry_now)})+"\n")

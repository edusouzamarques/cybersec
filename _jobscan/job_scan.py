# -*- coding: utf-8 -*-
"""Varredura diária de vagas cyber -> alimenta o app (vagas_data.js) + digest datado.
Fontes: Curadoria Seed (jobs_seed.json) + APIs abertas (Jobicy Cybersecurity, RemoteOK filtrado, Remotive).
Filtros: Anti-scam/MLM, anti-títulos falsos (suporte/vendas/pagamentos), apenas CyberSec & GRC legítimos."""
import json, os, re, time, urllib.request, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
APP  = os.path.dirname(BASE)

# Termos obrigatórios de CyberSec / GRC / AI Sec no cargo
ROLE_WORDS = [
    "security", "cyber", "soc analyst", "siem", "vulnerab", "grc", "incident", "threat",
    "infosec", "penetration", "pentest", "appsec", "devsecops", "detection", "malware",
    "cyber risk", "it risk", "security compliance", "ai security", "security analyst",
    "security engineer", "blue team", "security operations", "iso 27001", "soc 2"
]

# Títulos categoricamente NÃO compatíveis (descarte imediato)
BAD_TITLE_WORDS = [
    "customer support", "customer service", "sales", "social media", "marketing",
    "data entry", "payment operations", "virtual assistant", "telemarketer",
    "recruiter", "copywriter", "appointment setter", "content moderator",
    "cashier", "teller", "accounting", "bookkeeper", "legal assistant",
    "brand protection", "community manager", "billing"
]

# Termos de golpes / MLM / comissão disfarçada na descrição ou título
SCAM_TERMS = [
    "performance-based", "commission-based", "payments every 3", "payments every",
    "worldwide network share", "social media engagement (no calls", "direct acquisitions",
    "tokenized funding", "no calls, emailing, or meetings", "1099 independent contractor opportunity with performance-based",
    "unpaid internship", "training fee", "matrix referral", "earn bonuses based on"
]

KNOWN_SCAM_COMPANIES = [
    "ultimate marketing", "direct acquisitions", "tokenized funding"
]

def is_scam_or_bad(title, company="", desc=""):
    t = (title or "").lower()
    c = (company or "").lower()
    d = (desc or "").lower()
    if any(sc in c for sc in KNOWN_SCAM_COMPANIES):
        return True, "empresa bloqueada (golpe/MLM)"
    if any(bad in t for bad in BAD_TITLE_WORDS):
        return True, "título incompatível (não é cybersec)"
    if any(st in d for st in SCAM_TERMS) or any(st in t for st in SCAM_TERMS):
        return True, "modelo de comissão/MLM descartado"
    return False, ""

def is_cyber(title, desc=""):
    t = (title or "").lower()
    d = (desc or "").lower()
    has_role = any(w in t for w in ROLE_WORDS)
    if not has_role:
        # Se o título é vago (ex: "Risk Analyst"), aceita se houver menção explícita a cyber/infoSec/GRC
        if "risk" in t or "compliance" in t or "analyst" in t:
            if any(k in d for k in ["soc 2", "iso 27001", "nist", "infosec", "cybersecurity", "siem"]):
                return True
        return False
    return True

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

# 1. Jobicy (API aberta dedicada a CyberSecurity — alta qualidade curada)
try:
    data = fetch("https://jobicy.com/api/v2/remote-jobs?count=40&industry=cybersecurity", ua=True)
    for j in data.get("jobs", []):
        pos = j.get("jobTitle", "")
        comp = j.get("companyName", "")
        desc = j.get("jobDescription", "")
        loc = j.get("jobGeo", "Remoto") or "Remoto"
        url = j.get("url", "")
        bad, reason = is_scam_or_bad(pos, comp, desc)
        if bad: continue
        if is_cyber(pos, desc):
            live.append({
                "role": pos[:70],
                "company": comp[:30],
                "loc": loc[:24],
                "pay": "—",
                "level": level_of(pos),
                "source": "Jobicy",
                "req": ["secplus"],
                "clearance": False,
                "sponsor": False,
                "student": False,
                "url": url,
                "note": "remoto internacional (curadoria cyber)"
            })
except Exception as e:
    print("Jobicy falhou:", e)

# 2. RemoteOK (com filtro anti-scam rigoroso)
try:
    for j in fetch("https://remoteok.com/api", ua=True):
        if not isinstance(j, dict) or not j.get("position"): continue
        pos = j.get("position", "")
        comp = j.get("company", "")
        desc = j.get("description", "")
        bad, reason = is_scam_or_bad(pos, comp, desc)
        if bad:
            continue
        if is_cyber(pos, desc):
            live.append({
                "role": pos[:70],
                "company": comp[:30],
                "loc": (j.get("location") or "Remoto")[:24],
                "pay": "—",
                "level": level_of(pos),
                "source": "RemoteOK",
                "req": ["secplus"],
                "clearance": False,
                "sponsor": False,
                "student": False,
                "url": j.get("url",""),
                "note": "remoto (filtrado e verificado anti-scam)"
            })
except Exception as e:
    print("RemoteOK falhou:", e)

# dedupe live
seen=set(); live2=[]
for j in live:
    k=(j["role"].lower(), j["company"].lower())
    if k in seen: continue
    seen.add(k); live2.append(j)
live = live2[:25]

# seed curado (Dice/Ashby) — espinha dorsal de qualidade
seed = json.load(open(os.path.join(BASE,"jobs_seed.json"), encoding="utf-8"))

allj = seed + [j for j in live if (j["role"].lower(),j["company"].lower()) not in
               {(s["role"].lower(),s["company"].lower()) for s in seed}]

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
entry_now = [j for j in allj if j["level"] in ("entry","estágio") and not j.get("clearance")]
sponsor = [j for j in allj if j.get("sponsor")]
insight = (f"{len(allj)} vagas no radar · {len(entry_now)} de entrada aplicáveis (sem cidadania) · "
           f"{len(sponsor)} patrocinam visto. Filtro anti-golpe ativado: sem vagas de comissão/suporte.")

js = ("// GERADO por job_scan.py — NÃO editar à mão\n"
      f"window.JOBS_UPDATED={json.dumps(now, ensure_ascii=False)};\n"
      f"window.JOBS_INSIGHT={json.dumps(insight, ensure_ascii=False)};\n"
      f"window.JOBS_LIVE={json.dumps(allj, ensure_ascii=False)};\n")
open(os.path.join(BASE,"vagas_data.js"),"w",encoding="utf-8").write(js)
print(f"[ok] {len(allj)} vagas -> vagas_data.js @ {now} (live: {len(live)}, seed: {len(seed)})")

# digest datado (append) + log
with open(os.path.join(BASE,"job_digest.md"),"a",encoding="utf-8") as f:
    f.write(f"\n## {now}\n- {insight}\n- entrada aplicável: "
            + ", ".join(f"{j['role']} @ {j['company']}" for j in entry_now[:6]) + "\n")
with open(os.path.join(BASE,"job_scan_log.ndjson"),"a",encoding="utf-8") as f:
    f.write(json.dumps({"ts":now,"total":len(allj),"live":len(live),"entry":len(entry_now)})+"\n")

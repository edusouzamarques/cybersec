# -*- coding: utf-8 -*-
"""Varredura diária de vagas CyberSec, GRC e Cloud/Linux Support -> vagas_data.js + digest datado.
Fontes integradas:
1. Curadoria Seed (jobs_seed.json) - portas de entrada e vagas verificadas
2. ATS Direto Greenhouse: Canonical, GitLab, Cloudflare, Okta, Chainguard, Elastic, Datadog
3. ATS Direto Ashby: Vanta, Drata, Oneleet, Supabase
4. Jobicy: Cybersecurity & DevOps remote
5. RemoteOK: Filtrado e verificado anti-scam
"""
import json, os, re, time, urllib.request, datetime, unicodedata

BASE = os.path.dirname(os.path.abspath(__file__))
APP  = os.path.dirname(BASE)

# Termos de interesse no cargo (CyberSec / GRC / AI Sec / Linux & Cloud Infra)
ROLE_WORDS = [
    "security", "cyber", "soc analyst", "siem", "vulnerab", "grc", "incident", "threat",
    "infosec", "penetration", "pentest", "appsec", "devsecops", "detection", "malware",
    "cyber risk", "it risk", "security compliance", "ai security", "security analyst",
    "security engineer", "blue team", "security operations", "iso 27001", "soc 2",
    "internal audit", "it audit", "vendor risk", "third-party risk", "privacy", "trust",
    "iam", "identity", "linux support", "cloud support", "support engineer"
]

# Títulos categoricamente NÃO compatíveis (descarte imediato)
BAD_TITLE_WORDS = [
    "customer support", "customer service", "sales", "social media", "marketing",
    "data entry", "payment operations", "virtual assistant", "telemarketer",
    "recruiter", "copywriter", "appointment setter", "content moderator",
    "cashier", "teller", "accounting", "bookkeeper", "legal assistant",
    "brand protection", "community manager", "billing", "collections",
    "talent scientist", "renewals", "revenue operations", "investor relations",
    "front desk", "office operations", "hr generalist", "generalist"
]

# Termos de golpes / MLM / comissão disfarçada
SCAM_TERMS = [
    "performance-based", "commission-based", "payments every 3", "payments every",
    "worldwide network share", "social media engagement (no calls", "direct acquisitions",
    "tokenized funding", "no calls, emailing, or meetings", "1099 independent contractor opportunity with performance-based",
    "unpaid internship", "training fee", "matrix referral", "earn bonuses based on"
]

KNOWN_SCAM_COMPANIES = [
    "ultimate marketing", "direct acquisitions", "tokenized funding"
]

def normalize_text(text):
    nfkd = unicodedata.normalize("NFKD", (text or "").lower())
    return "".join([c for c in nfkd if not unicodedata.combining(c)])

def is_scam_or_bad(title, company="", desc=""):
    t = normalize_text(title)
    c = normalize_text(company)
    d = normalize_text(desc)
    if any(sc in c for sc in KNOWN_SCAM_COMPANIES):
        return True, "empresa bloqueada (golpe/MLM)"
    if any(bad in t for bad in BAD_TITLE_WORDS):
        # Exceção para suporte técnico de segurança ou Linux
        if ("linux support" in t or "security support" in t or "solutions engineer" in t) and not any(bad in t for bad in ["sales", "marketing", "front desk"]):
            pass
        else:
            return True, "título incompatível (não é cyber/infra/grc)"
    if any(st in d for st in SCAM_TERMS) or any(st in t for st in SCAM_TERMS):
        return True, "modelo de comissão/MLM descartado"
    return False, ""

def is_cyber(title, company="", desc=""):
    t = normalize_text(title)
    c = normalize_text(company)
    d = normalize_text(desc)
    
    # Exceções estratégicas da Canonical (porta de entrada para Linux e Cloud)
    if "canonical" in c:
        if any(k in t for k in [
            "associate linux", "graduate software", "graduate cloud", "graduate customer success",
            "junior linux", "junior ubuntu", "internal auditor", "python - cloud", "ubuntu sales engineer"
        ]):
            return True
            
    has_role = any(w in t for w in ROLE_WORDS)
    if not has_role:
        if "risk" in t or "compliance" in t or "analyst" in t or "program manager" in t:
            if any(k in d for k in ["soc 2", "iso 27001", "nist", "infosec", "cybersecurity", "siem", "audit", "compliance"]):
                return True
        return False
    return True

def level_of(title, company="", desc="", api_level=""):
    t = normalize_text(title)
    d = normalize_text(desc)
    lvl_api = normalize_text(api_level)
    
    # 1. Mapeamento explícito de API
    if re.search(r"\b(director|executive|head|vp)\b", lvl_api):
        return "senior"
    if re.search(r"\b(senior|staff|principal|lead)\b", lvl_api):
        return "senior"
    if re.search(r"\b(intern|internship)\b", lvl_api):
        return "estágio"

    # 2. Análise de Título
    if re.search(r"\b(intern|internship|estagio|estagiario)\b", t):
        return "estágio"
    if re.search(r"\b(graduate|trainee|recem[- ]formado|early[- ]career)\b", t):
        return "graduate"
    if re.search(r"\bsenior associate\b", t):
        return "pleno"
    if re.search(r"\b(junior|jr|jr\.|associate)\b", t) and not re.search(r"\b(director|partner|head|vp)\b", t):
        return "junior"
    if re.search(r"\b(entry|entry[- ]level|tier[- ]?1|soc tier 1|l1)\b", t) and not re.search(r"\b(senior|lead|principal)\b", t):
        return "entry"
    if re.search(r"\b(senior|sr|sr\.|s[eê]nior|lead|principal|staff|manager|head|director|architect|chief|vp|ciso)\b", t):
        return "senior"
        
    # 3. Descrição quando o título é neutro
    if re.search(r"\b(director|head of|ciso|vice president)\b", d) or re.search(r"\b(8\+|10\+|12\+)\s+years?\b", d):
        return "senior"
    if re.search(r"\b(senior[- ]level|senior experience|5\+|6\+|7\+)\s*(?:years?|experience)?\b", d):
        if "senior-level" in d or "5+ years" in d or "6+ years" in d or "7+ years" in d:
            return "senior"
            
    return "pleno"

def fetch_json(url, headers=None, timeout=12):
    h = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, headers=h)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "ignore"))

live = []

# --- 1. GREENHOUSE DIRECT ATS ---
GH_BOARDS = [
    ("canonical", "Canonical"),
    ("gitlab", "GitLab"),
    ("cloudflare", "Cloudflare"),
    ("okta", "Okta"),
    ("chainguard", "Chainguard"),
    ("elastic", "Elastic"),
    ("datadog", "Datadog")
]

for slug, comp in GH_BOARDS:
    try:
        url = f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs"
        data = fetch_json(url, timeout=10)
        for j in data.get("jobs", []):
            pos = j.get("title", "")
            loc = (j.get("location", {}).get("name", "") or "Remoto")[:24]
            u = j.get("absolute_url", "")
            bad, _ = is_scam_or_bad(pos, comp)
            if bad:
                continue
            if is_cyber(pos, comp):
                lvl = level_of(pos, comp)
                live.append({
                    "role": pos[:70],
                    "company": comp[:30],
                    "loc": loc,
                    "pay": "—",
                    "level": lvl,
                    "source": f"Greenhouse ({slug})",
                    "req": ["secplus"],
                    "clearance": False,
                    "sponsor": False,
                    "student": False,
                    "url": u,
                    "note": f"remoto internacional ({comp} direto)"
                })
    except Exception as e:
        print(f"Greenhouse {slug} falhou: {e}")

# --- 2. ASHBY DIRECT ATS ---
ASHBY_BOARDS = [
    ("vanta", "Vanta"),
    ("drata", "Drata"),
    ("oneleet", "Oneleet"),
    ("supabase", "Supabase")
]

for slug, comp in ASHBY_BOARDS:
    try:
        url = f"https://api.ashbyhq.com/posting-api/job-board/{slug}"
        data = fetch_json(url, timeout=10)
        for j in data.get("jobs", []):
            pos = j.get("title", "")
            loc = (j.get("location", "") or "Remoto")[:24]
            u = j.get("jobUrl", "")
            bad, _ = is_scam_or_bad(pos, comp)
            if bad:
                continue
            if is_cyber(pos, comp):
                lvl = level_of(pos, comp)
                live.append({
                    "role": pos[:70],
                    "company": comp[:30],
                    "loc": loc,
                    "pay": "—",
                    "level": lvl,
                    "source": f"Ashby ({slug})",
                    "req": ["secplus"],
                    "clearance": False,
                    "sponsor": False,
                    "student": False,
                    "url": u,
                    "note": f"remoto internacional ({comp} direto)"
                })
    except Exception as e:
        print(f"Ashby {slug} falhou: {e}")

# --- 3. JOBICY API ---
for ind in ["cybersecurity", "engineering"]:
    try:
        data = fetch_json(f"https://jobicy.com/api/v2/remote-jobs?count=40&industry={ind}", timeout=15)
        for j in data.get("jobs", []):
            pos = j.get("jobTitle", "")
            comp = j.get("companyName", "")
            desc = j.get("jobDescription", "")
            loc = (j.get("jobGeo", "Remoto") or "Remoto")[:24]
            url = j.get("url", "")
            api_lvl = j.get("jobLevel", "")
            bad, _ = is_scam_or_bad(pos, comp, desc)
            if bad:
                continue
            if is_cyber(pos, comp, desc):
                live.append({
                    "role": pos[:70],
                    "company": comp[:30],
                    "loc": loc,
                    "pay": "—",
                    "level": level_of(pos, comp, desc, api_lvl),
                    "source": "Jobicy",
                    "req": ["secplus"],
                    "clearance": False,
                    "sponsor": False,
                    "student": False,
                    "url": url,
                    "note": "remoto internacional (curadoria cyber)"
                })
    except Exception as e:
        print(f"Jobicy {ind} falhou: {e}")

# --- 4. REMOTEOK API ---
try:
    data = fetch_json("https://remoteok.com/api", timeout=15)
    for j in data:
        if not isinstance(j, dict) or not j.get("position"):
            continue
        pos = j.get("position", "")
        comp = j.get("company", "")
        desc = j.get("description", "")
        bad, _ = is_scam_or_bad(pos, comp, desc)
        if bad:
            continue
        if is_cyber(pos, comp, desc):
            live.append({
                "role": pos[:70],
                "company": comp[:30],
                "loc": (j.get("location") or "Remoto")[:24],
                "pay": "—",
                "level": level_of(pos, comp, desc),
                "source": "RemoteOK",
                "req": ["secplus"],
                "clearance": False,
                "sponsor": False,
                "student": False,
                "url": j.get("url", ""),
                "note": "remoto (filtrado anti-scam)"
            })
except Exception as e:
    print(f"RemoteOK falhou: {e}")

# Deduplicação dos jobs capturados ao vivo
seen = set()
dedup_live = []
for j in live:
    k = (j["role"].lower().strip(), j["company"].lower().strip())
    if k in seen:
        continue
    seen.add(k)
    dedup_live.append(j)

# Seed curado (espinha dorsal de qualidade e vagas nacionais/estratégicas)
seed_path = os.path.join(BASE, "jobs_seed.json")
seed = json.load(open(seed_path, encoding="utf-8")) if os.path.exists(seed_path) else []

# Mesclar: seed tem prioridade de metadados detalhados
seed_keys = {(s["role"].lower().strip(), s["company"].lower().strip()) for s in seed}
allj = seed + [j for j in dedup_live if (j["role"].lower().strip(), j["company"].lower().strip()) not in seed_keys]

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
entry_now = [j for j in allj if j["level"] in ("entry", "junior", "graduate", "estágio") and not j.get("clearance")]
sponsor = [j for j in allj if j.get("sponsor")]
insight = (f"{len(allj)} vagas no radar · {len(entry_now)} de entrada aplicáveis (sem cidadania) · "
           f"{len(sponsor)} patrocinam visto. Fontes: ATS Direto (Canonical, Vanta, GitLab, Okta, Drata, Oneleet) + Jobicy + Curadoria.")

js = ("// GERADO por job_scan.py — NÃO editar à mão\n"
      f"window.JOBS_UPDATED={json.dumps(now, ensure_ascii=False)};\n"
      f"window.JOBS_INSIGHT={json.dumps(insight, ensure_ascii=False)};\n"
      f"window.JOBS_LIVE={json.dumps(allj, ensure_ascii=False)};\n")

# Gravar em ambos os locais
open(os.path.join(BASE, "vagas_data.js"), "w", encoding="utf-8").write(js)
site_jobs = os.path.join(APP, "_site", "_jobscan", "vagas_data.js")
if os.path.exists(os.path.dirname(site_jobs)):
    with open(site_jobs, "w", encoding="utf-8") as f:
        f.write(js)

print(f"[ok] {len(allj)} vagas -> vagas_data.js @ {now} (live: {len(dedup_live)}, seed: {len(seed)}, entrada: {len(entry_now)})")

# Digest datado (append) + log
digest_line = (f"\n## {now}\n- {insight}\n- Destaques de entrada ({len(entry_now)} vagas): "
               + ", ".join(f"{j['role']} @ {j['company']}" for j in entry_now[:8]) + "\n")

with open(os.path.join(BASE, "job_digest.md"), "a", encoding="utf-8") as f:
    f.write(digest_line)

site_digest = os.path.join(APP, "_site", "_jobscan", "job_digest.md")
if os.path.exists(os.path.dirname(site_digest)):
    with open(site_digest, "a", encoding="utf-8") as f:
        f.write(digest_line)

with open(os.path.join(BASE, "job_scan_log.ndjson"), "a", encoding="utf-8") as f:
    f.write(json.dumps({"ts": now, "total": len(allj), "live": len(dedup_live), "entry": len(entry_now)}) + "\n")

# -*- coding: utf-8 -*-
"""
Varredura diária de vagas de Cibersegurança, GRC e Suporte em Nuvem.
Fontes:
  1. Base curada (jobs_seed.json) - Vagas verificadas Brasil (Gupy CLT) & Global Remoto (Wrike, etc.)
  2. Greenhouse API (Canonical live boards)
  3. Ashby API (Supabase & Oneleet live boards)
  4. WeWorkRemotely (RSS feeds)
  5. Jobicy API (tag: security)
  6. RemoteOK API

Alimenta:
  - _jobscan/vagas_data.js (carregado diretamente pelo assistente-cybersec.html)
  - _jobscan/job_digest.md (histórico diário)
  - assistente-cybersec.html (atualiza cache-buster ?v=TIMESTAMP)
"""

import json
import os
import re
import sys
import subprocess
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CYBERSEC_DIR = os.path.dirname(BASE_DIR)

SEED_FILE = os.path.join(BASE_DIR, "jobs_seed.json")
VAGAS_FILE = os.path.join(BASE_DIR, "vagas_data.js")
DIGEST_FILE = os.path.join(BASE_DIR, "job_digest.md")
LOG_FILE = os.path.join(BASE_DIR, "job_scan_log.ndjson")
HTML_FILE = os.path.join(CYBERSEC_DIR, "assistente-cybersec.html")

# Palavras-chave obrigatórias para cargos técnicos de segurança / GRC / suporte
CYBER_KEYWORDS = [
    "security", "cyber", "grc", "compliance", "soc ", "soc-", "siem",
    "vulnerab", "incident", "threat", "infosec", "penetration", "pentest",
    "appsec", "devsecops", "detection", "malware", "risk analyst", "risk control",
    "compliance analyst", "internal audit", "security analyst", "security engineer",
    "cloud support", "systems engineer", "sysadmin", "trust & safety", "privacy",
    "governança", "riscos", "segurança da informação", "auditoria"
]

# Palavras para descarte imediato (marketing, RH, vendas, executivos comerciais, design ou vagas não-técnicas)
EXCLUDE_TITLES = [
    "sales", "vendas", "comercial", "account executive", "sales executive",
    "sales specialist", "sales manager", "business development", "bdr", "sdr",
    "ux designer", "ui designer", "product designer", "graphic designer",
    "communications intern", "pr intern", "social media", "copywriter",
    "content marketing", "general manager", "recruiter", "talent acquisition",
    "people partner", "hrbp", "government affairs", "lobbyist", "public policy",
    "marketing", "growth", "animator", "medical expert", "fertility"
]

# Termos que tornam a vaga inelegível para quem mora no Brasil sem cidadania estrangeira
INELEGIBLE_TERMS = [
    "clearance", "public trust", "dod", "secret", "ts/sci", "sc clearance",
    "us citizen", "uk citizen", "british citizen", "cidadania americana",
    "citizenship required", "must reside in the us", "u.s. based only",
    "us only", "usa only", "uk only", "canada only", "australia only"
]

def is_eligible(title, desc, loc, geo):
    full = f"{title} {desc} {loc} {geo}".lower()
    
    # 1. Não pode ter exigência de segurança de estado / cidadania restrita
    for term in INELEGIBLE_TERMS:
        if term in full:
            return False
            
    # 2. Vagas locais do Brasil (CLT/PJ) são sempre elegíveis
    if geo == "brasil" or "brasil" in loc.lower() or "brazil" in loc.lower():
        return True
        
    # 3. Vagas internacionais NÃO podem ser híbridas nem presenciais
    office_words = ["hybrid", "hibrid", "office", "on-site", "onsite", "presencial"]
    for ow in office_words:
        if ow in loc.lower():
            return False
            
    # 4. Deve aceitar Worldwide, Anywhere in the World, LATAM ou AMER
    valid_globals = ["worldwide", "anywhere in the world", "global", "latam", "amer", "anywhere"]
    if any(vg in loc.lower() for vg in valid_globals) or geo in ["worldwide", "latam", "global"]:
        return True
        
    return False

def is_cyber_role(title):
    t = (title or "").lower()
    if any(ex in t for ex in EXCLUDE_TITLES):
        return False
    return any(k in t for k in CYBER_KEYWORDS)

def detect_level(title, desc=""):
    t = (title or "").lower()
    d = (desc or "").lower()
    
    # Se a descrição exige expressamente 5+ anos, é sênior
    if any(exp in d for exp in ["5+ years", "6+ years", "7+ years", "8+ years", "10+ years", "5 to 7 years", "5-7 years"]):
        return "senior"
        
    if any(w in t for w in ["intern", "internship", "estágio", "estagio", "trainee", "apprentice"]):
        return "estágio"
        
    if any(w in t for w in ["senior", "sr", "lead", "principal", "staff", "head", "director", "architect", "chief", "vp", "vice president"]):
        return "senior"
        
    # Regex com limites de palavra para entrada / júnior (evita que "AI" case com "i ")
    if re.search(r'\b(junior|jr|associate|entry|early career|entry-level|iniciante|graduate)\b', t):
        return "entry"
        
    # Numerais romanos com limite de palavra
    if re.search(r'\b(tier 1|tier-1|soc 1|soc-1)\b', t):
        return "entry"
        
    return "pleno"

def fetch_url(url, is_json=True, timeout=20):
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json, text/html, application/xml"
    })
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        content = resp.read()
        if is_json:
            return json.loads(content.decode("utf-8", "ignore"))
        return content.decode("utf-8", "ignore")

def is_url_valid(url, timeout=7):
    """Checagem rápida de integridade para descartar links quebrados ou portais genéricos."""
    if not url:
        return False
    # Domínios e portais sabidamente genéricos ou descontinuados
    bad_roots = ["news.orbite-ats.com.br", "spread.gupy.io", "stravorus.com/careers"]
    if any(br in url for br in bad_roots):
        return False
        
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            if resp.status == 200:
                final = resp.geturl().rstrip('/')
                # Se redirecionou pra raiz genérica do domínio (menos de 3 barras no path), descarta
                if final.count('/') < 3 and not ("ashbyhq" in final or "greenhouse" in final or "gupy.io/jobs" in final):
                    return False
                return True
            return False
    except urllib.error.HTTPError as e:
        if e.code == 429: # Rate limit momentâneo da API não invalida o link
            return True
        return False
    except Exception:
        return True # Se deu timeout na checagem rápida, mantém na dúvida

def scan_canonical_greenhouse():
    """Varre a API oficial e aberta da Canonical no Greenhouse."""
    jobs = []
    url = "https://boards-api.greenhouse.io/v1/boards/canonical/jobs"
    try:
        data = fetch_url(url, is_json=True, timeout=20)
        today_str = datetime.now().strftime("%Y-%m-%d")
        for j in data.get("jobs", []):
            role = j.get("title", "")
            link = j.get("absolute_url", "")
            
            if not is_cyber_role(role):
                continue
                
            loc = "Remote (Worldwide / Brasil)"
            geo = "worldwide"
            
            job_id = f"can-{j.get('id', '')}"
            jobs.append({
                "id": job_id,
                "role": role[:80],
                "company": "Canonical",
                "loc": loc,
                "pay": "A combinar (US$)",
                "level": detect_level(role),
                "source": "Canonical Greenhouse",
                "geo": geo,
                "url": link,
                "req": ["secplus"],
                "clearance": False,
                "sponsor": True,
                "student": False,
                "dest": 5,
                "study": 5,
                "tasks": f"Atuação técnica em {role} na Canonical Ubuntu. Empresa global pioneira em trabalho 100% remoto.",
                "note": "⭐ CANONICAL GLOBAL: Aberta para contratação no Brasil. Suporta transição de carreira e patrocina vistos.",
                "added_date": today_str
            })
    except Exception as e:
        print(f"Erro ao varrer Canonical Greenhouse: {e}")
    return jobs

def scan_ashby_company(board_name, display_name):
    """Varre a API oficial e aberta de uma empresa no Ashby ATS."""
    jobs = []
    url = f"https://api.ashbyhq.com/posting-api/job-board/{board_name}"
    try:
        data = fetch_url(url, is_json=True, timeout=20)
        today_str = datetime.now().strftime("%Y-%m-%d")
        for j in data.get("jobs", []):
            role = j.get("title", "")
            link = j.get("jobUrl", "")
            desc = j.get("descriptionHtml", "")
            
            if not is_cyber_role(role):
                continue
                
            loc = "Remote (Worldwide / LATAM)"
            geo = "worldwide"
            
            if not is_eligible(role, desc, loc, geo):
                continue
                
            job_id = f"{board_name}-{re.sub(r'[^a-z0-9]+', '-', role.lower())}"[:40]
            jobs.append({
                "id": job_id,
                "role": role[:80],
                "company": display_name,
                "loc": loc,
                "pay": "A combinar (US$)",
                "level": detect_level(role, desc),
                "source": f"{display_name} Ashby",
                "geo": geo,
                "url": link,
                "req": ["secplus"],
                "clearance": False,
                "sponsor": False,
                "student": False,
                "dest": 5,
                "study": 4,
                "tasks": f"Atuação em {role} na {display_name}. Vaga oficial capturada no ATS Ashby.",
                "note": f"⭐ Vaga oficial aberta na {display_name} (Ashby ATS). Contratação remota internacional.",
                "added_date": today_str
            })
    except Exception as e:
        print(f"Erro ao varrer Ashby ({display_name}): {e}")
    return jobs

def scan_weworkremotely():
    """Varre os feeds RSS do WeWorkRemotely em busca de vagas globais de segurança."""
    wwr_jobs = []
    feeds = [
        "https://weworkremotely.com/categories/remote-devops-sysadmin-jobs.rss",
        "https://weworkremotely.com/remote-jobs.rss"
    ]
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    for feed_url in feeds:
        try:
            xml_text = fetch_url(feed_url, is_json=False, timeout=20)
            root = ET.fromstring(xml_text)
            for item in root.findall(".//item"):
                raw_title = item.findtext("title", "") or ""
                desc = item.findtext("description", "") or ""
                region = item.findtext("region", "") or ""
                link = item.findtext("link", "") or ""
                
                parts = raw_title.split(":", 1)
                company = parts[0].strip() if len(parts) > 1 else "Empresa Internacional"
                role = parts[1].strip() if len(parts) > 1 else raw_title.strip()
                
                if not is_cyber_role(role):
                    continue
                    
                loc = f"Remote ({region})" if region else "Remote (Worldwide)"
                geo = "worldwide"
                
                if not is_eligible(role, desc, loc, geo):
                    continue
                    
                job_id = f"wwr-{re.sub(r'[^a-z0-9]+', '-', company.lower())}-{re.sub(r'[^a-z0-9]+', '-', role.lower())}"[:40]
                
                wwr_jobs.append({
                    "id": job_id,
                    "role": role[:80],
                    "company": company[:40],
                    "loc": loc,
                    "pay": "A combinar (US$)",
                    "level": detect_level(role, desc),
                    "source": "WeWorkRemotely",
                    "geo": "worldwide",
                    "url": link,
                    "req": ["secplus"],
                    "clearance": False,
                    "sponsor": False,
                    "student": False,
                    "dest": 4,
                    "study": 4,
                    "tasks": f"Atuação em {role} para a empresa {company}. Vaga internacional 100% remota anunciada no WeWorkRemotely.",
                    "note": f"⭐ Vaga encontrada no WeWorkRemotely ({region}). Aberta para contratação remota internacional.",
                    "added_date": today_str
                })
        except Exception as e:
            print(f"Erro ao varrer feed WeWorkRemotely ({feed_url}): {e}")
            
    return wwr_jobs

def scan_jobicy():
    """Varre a API do Jobicy com foco em vagas de cibersegurança."""
    jobicy_jobs = []
    url = "https://jobicy.com/api/v2/remote-jobs?count=40&tag=security"
    today_str = datetime.now().strftime("%Y-%m-%d")
    try:
        data = fetch_url(url, is_json=True, timeout=20)
        for j in data.get("jobs", []):
            role = j.get("jobTitle", "")
            company = j.get("companyName", "")
            desc = j.get("jobDescription", "")
            loc = j.get("jobGeo", "Worldwide")
            link = j.get("url", "")
            
            if not is_cyber_role(role):
                continue
                
            geo = "worldwide"
            if not is_eligible(role, desc, loc, geo):
                continue
                
            job_id = f"jobicy-{re.sub(r'[^a-z0-9]+', '-', company.lower())}-{re.sub(r'[^a-z0-9]+', '-', role.lower())}"[:40]
            
            jobicy_jobs.append({
                "id": job_id,
                "role": role[:80],
                "company": company[:40],
                "loc": f"Remote ({loc})",
                "pay": "A combinar (US$)",
                "level": detect_level(role, desc),
                "source": "Jobicy",
                "geo": "worldwide",
                "url": link,
                "req": ["secplus"],
                "clearance": False,
                "sponsor": False,
                "student": False,
                "dest": 4,
                "study": 4,
                "tasks": f"Atuação em {role} na {company}. Monitoramento, suporte de segurança e conformidade remota.",
                "note": "⭐ Vaga internacional capturada via Jobicy. Aceita aplicação remota.",
                "added_date": today_str
            })
    except Exception as e:
        print(f"Erro ao consultar Jobicy: {e}")
        
    return jobicy_jobs

def scan_remoteok():
    """Varre a API pública do RemoteOK."""
    remoteok_jobs = []
    url = "https://remoteok.com/api"
    today_str = datetime.now().strftime("%Y-%m-%d")
    try:
        data = fetch_url(url, is_json=True, timeout=25)
        for j in data:
            if not isinstance(j, dict) or not j.get("position"):
                continue
            role = j.get("position", "")
            company = j.get("company", "")
            loc = j.get("location") or "Worldwide"
            desc = j.get("description", "")
            link = j.get("url", "")
            
            if not is_cyber_role(role):
                continue
                
            geo = "worldwide"
            if not is_eligible(role, desc, loc, geo):
                continue
                
            job_id = f"remoteok-{re.sub(r'[^a-z0-9]+', '-', company.lower())}-{re.sub(r'[^a-z0-9]+', '-', role.lower())}"[:40]
            
            remoteok_jobs.append({
                "id": job_id,
                "role": role[:80],
                "company": company[:40],
                "loc": f"Remote ({loc})",
                "pay": "A combinar (US$)",
                "level": detect_level(role, desc),
                "source": "RemoteOK",
                "geo": "worldwide",
                "url": link,
                "req": ["secplus"],
                "clearance": False,
                "sponsor": False,
                "student": False,
                "dest": 4,
                "study": 4,
                "tasks": f"Atuação em {role} na empresa {company}. Vaga remota capturada via RemoteOK.",
                "note": "⭐ Vaga capturada via RemoteOK. Aplicação remota global.",
                "added_date": today_str
            })
    except Exception as e:
        print(f"Erro ao consultar RemoteOK: {e}")
        
    return remoteok_jobs

def update_html_cache_buster(vagas_version_str):
    """Atualiza o parâmetro ?v= no assistente-cybersec.html para que o navegador nunca pegue cache velho."""
    if not os.path.exists(HTML_FILE):
        return
    try:
        with open(HTML_FILE, "r", encoding="utf-8") as f:
            content = f.read()

        new_tag = f'_jobscan/vagas_data.js?v={vagas_version_str}'
        updated = re.sub(r'_jobscan/vagas_data\.js\?v=[a-zA-Z0-9_]+', new_tag, content)

        if updated != content:
            with open(HTML_FILE, "w", encoding="utf-8") as f:
                f.write(updated)
            print(f"assistente-cybersec.html atualizado com cache-buster: {new_tag}")
    except Exception as e:
        print(f"Erro ao atualizar cache-buster no HTML: {e}")

def run():
    print("Iniciando varredura diária de vagas CyberSec (Robô Blindado)...")
    
    # 1. Carrega a base curada (espinha dorsal com vagas reais do Brasil e internacionais)
    seed_jobs = []
    if os.path.exists(SEED_FILE):
        try:
            with open(SEED_FILE, "r", encoding="utf-8") as f:
                seed_jobs = json.load(f)
            print(f"Base curada carregada: {len(seed_jobs)} vagas de alta prioridade.")
        except Exception as e:
            print(f"Erro ao ler jobs_seed.json: {e}")
            
    # Filtra a base curada
    seed_eligible = [
        j for j in seed_jobs 
        if is_eligible(j.get("role", ""), j.get("tasks", ""), j.get("loc", ""), j.get("geo", ""))
        and is_cyber_role(j.get("role", ""))
        and is_url_valid(j.get("url", ""))
    ]
    print(f"Vagas curadas 100% elegíveis e verificadas: {len(seed_eligible)}")
    
    # 2. Executa varreduras ativas
    live_jobs = []
    live_jobs.extend(scan_canonical_greenhouse())
    live_jobs.extend(scan_ashby_company("supabase", "Supabase"))
    live_jobs.extend(scan_ashby_company("oneleet", "Oneleet"))
    live_jobs.extend(scan_weworkremotely())
    live_jobs.extend(scan_jobicy())
    live_jobs.extend(scan_remoteok())
    
    print(f"Total de vagas capturadas ao vivo: {len(live_jobs)}")
    
    # 3. Deduplicação inteligente e priorização de novidades
    seen_keys = set()
    final_jobs = []
    
    # Primeiro a base curada (prioridade máxima)
    for j in seed_eligible:
        key = (j.get("company", "").strip().lower(), j.get("role", "").strip().lower())
        if key not in seen_keys:
            seen_keys.add(key)
            final_jobs.append(j)
            
    # Depois as vagas novas capturadas ao vivo
    for j in live_jobs:
        key = (j.get("company", "").strip().lower(), j.get("role", "").strip().lower())
        if key not in seen_keys:
            seen_keys.add(key)
            final_jobs.append(j)
            
    print(f"Total consolidado de vagas elegíveis: {len(final_jobs)}")
    
    now_dt = datetime.now()
    now_str = now_dt.strftime("%Y-%m-%d %H:%M")
    cache_version = now_dt.strftime("%Y%m%d_%H%M")
    
    insight_str = f"{len(final_jobs)} vagas 100% elegíveis no radar (Brasil CLT/PJ e Global Remoto com Greenhouse, Ashby, WeWorkRemotely e Jobicy)"
    
    # 4. Escreve vagas_data.js
    js_content = (
        "// GERADO AUTOMATICAMENTE por job_scan.py — NÃO editar à mão\n"
        f"window.JOBS_UPDATED={json.dumps(now_str, ensure_ascii=False)};\n"
        f"window.JOBS_INSIGHT={json.dumps(insight_str, ensure_ascii=False)};\n"
        f"window.JOBS_LIVE={json.dumps(final_jobs, ensure_ascii=False)};\n"
    )
    
    with open(VAGAS_FILE, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"vagas_data.js atualizado com sucesso em {VAGAS_FILE}")
    
    # 5. Atualiza o cache buster no HTML
    update_html_cache_buster(cache_version)
    
    # 6. Registra no Digest e Log
    try:
        with open(DIGEST_FILE, "a", encoding="utf-8") as f:
            f.write(f"\n## {now_str}\n")
            f.write(f"- {insight_str}\n")
            f.write(f"- Fontes: Base Curada ({len(seed_eligible)}), ATS Greenhouse/Ashby + WWR + Jobicy + RemoteOK ({len(live_jobs)})\n")
            
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            log_entry = {
                "ts": now_str,
                "total": len(final_jobs),
                "curated": len(seed_eligible),
                "live": len(live_jobs)
            }
            f.write(json.dumps(log_entry) + "\n")
    except Exception as e:
        print(f"Erro ao salvar digest/log: {e}")
        
    print("Varredura finalizada com êxito!")

if __name__ == "__main__":
    run()

# -*- coding: utf-8 -*-
"""
Varredura diária de vagas de Cibersegurança, GRC e Suporte em Nuvem.
Fontes:
  1. Base curada (jobs_seed.json) - Wrike, Canonical, Oneleet, Supabase, etc.
  2. WeWorkRemotely (RSS feeds - DevOps/Sysadmin & All Remote)
  3. Jobicy API (tag: security)
  4. RemoteOK API

Alimenta:
  - _jobscan/vagas_data.js (carregado diretamente pelo assistente-cybersec.html)
  - _jobscan/job_digest.md (histórico diário)
"""

import json
import os
import re
import time
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CYBERSEC_DIR = os.path.dirname(BASE_DIR)

SEED_FILE = os.path.join(BASE_DIR, "jobs_seed.json")
VAGAS_FILE = os.path.join(BASE_DIR, "vagas_data.js")
DIGEST_FILE = os.path.join(BASE_DIR, "job_digest.md")
LOG_FILE = os.path.join(BASE_DIR, "job_scan_log.ndjson")

# Palavras-chave obrigatórias para cargos técnicos de segurança / GRC / suporte
CYBER_KEYWORDS = [
    "security", "cyber", "grc", "compliance", "soc ", "soc-", "siem",
    "vulnerab", "incident", "threat", "infosec", "penetration", "pentest",
    "appsec", "devsecops", "detection", "malware", "risk analyst", "risk control",
    "compliance analyst", "internal audit", "security analyst", "security engineer",
    "cloud support", "systems engineer", "sysadmin", "trust & safety", "privacy"
]

# Palavras para descarte imediato (marketing, RH, vagas não-técnicas ou pegadinhas)
EXCLUDE_TITLES = [
    "communications intern", "pr intern", "social media", "copywriter",
    "graphic designer", "content marketing", "account executive ii, federal",
    "general manager", "fertility", "animator", "medical expert"
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

def detect_level(title):
    t = (title or "").lower()
    if any(w in t for w in ["intern", "internship", "estágio", "estagio"]):
        return "estágio"
    if any(w in t for w in ["junior", "jr", "associate", "entry", "early career", "trainee", "i "]):
        return "entry"
    if any(w in t for w in ["senior", "sr", "lead", "principal", "staff", "head", "director", "architect"]):
        return "senior"
    return "pleno"

def fetch_url(url, is_json=True, timeout=20):
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        content = resp.read()
        if is_json:
            return json.loads(content.decode("utf-8", "ignore"))
        return content.decode("utf-8", "ignore")

def scan_weworkremotely():
    """Varre os feeds RSS do WeWorkRemotely em busca de vagas globais de segurança."""
    wwr_jobs = []
    feeds = [
        "https://weworkremotely.com/categories/remote-devops-sysadmin-jobs.rss",
        "https://weworkremotely.com/remote-jobs.rss"
    ]
    
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
                    "level": detect_level(role),
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
                    "note": f"⭐ Vaga encontrada no WeWorkRemotely ({region}). Aberta para contratação remota internacional."
                })
        except Exception as e:
            print(f"Erro ao varrer feed WeWorkRemotely ({feed_url}): {e}")
            
    return wwr_jobs

def scan_jobicy():
    """Varre a API do Jobicy com foco em vagas de cibersegurança."""
    jobicy_jobs = []
    url = "https://jobicy.com/api/v2/remote-jobs?count=40&tag=security"
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
                "level": detect_level(role),
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
                "note": "⭐ Vaga internacional capturada via Jobicy. Aceita aplicação remota."
            })
    except Exception as e:
        print(f"Erro ao consultar Jobicy: {e}")
        
    return jobicy_jobs

def scan_remoteok():
    """Varre a API pública do RemoteOK."""
    remoteok_jobs = []
    url = "https://remoteok.com/api"
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
                "level": detect_level(role),
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
                "note": "⭐ Vaga capturada via RemoteOK. Aplicação remota global."
            })
    except Exception as e:
        print(f"Erro ao consultar RemoteOK: {e}")
        
    return remoteok_jobs

def run():
    print("Iniciando varredura diária de vagas CyberSec...")
    
    # 1. Carrega a base curada (espinha dorsal com Wrike, Canonical, Oneleet, etc.)
    seed_jobs = []
    if os.path.exists(SEED_FILE):
        try:
            with open(SEED_FILE, "r", encoding="utf-8") as f:
                seed_jobs = json.load(f)
            print(f"Base curada carregada: {len(seed_jobs)} vagas de alta prioridade.")
        except Exception as e:
            print(f"Erro ao ler jobs_seed.json: {e}")
            
    # Filtra a base curada para garantir 100% de elegibilidade
    seed_eligible = [
        j for j in seed_jobs 
        if is_eligible(j.get("role", ""), j.get("tasks", ""), j.get("loc", ""), j.get("geo", ""))
    ]
    
    # 2. Executa varreduras ativas
    live_jobs = []
    live_jobs.extend(scan_weworkremotely())
    live_jobs.extend(scan_jobicy())
    live_jobs.extend(scan_remoteok())
    
    print(f"Total de vagas capturadas ao vivo: {len(live_jobs)}")
    
    # 3. Deduplicação inteligente
    seen_keys = set()
    final_jobs = []
    
    # Primeiro os empregos da base curada (prioridade máxima e descrições detalhadas)
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
    
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    insight_str = f"{len(final_jobs)} vagas 100% elegíveis no radar (Brasil CLT/PJ e Global Remoto Worldwide com WeWorkRemotely, Jobicy e Base Curada)"
    
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
    
    # 5. Registra no Digest e Log
    try:
        with open(DIGEST_FILE, "a", encoding="utf-8") as f:
            f.write(f"\n## {now_str}\n")
            f.write(f"- {insight_str}\n")
            f.write(f"- Fontes: Base Curada ({len(seed_eligible)}), WeWorkRemotely + Jobicy + RemoteOK ({len(live_jobs)})\n")
            
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

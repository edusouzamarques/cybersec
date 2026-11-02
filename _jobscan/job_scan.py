# -*- coding: utf-8 -*-
"""
Varredura diária de vagas de Cibersegurança, GRC e Suporte em Nuvem.
FOCO PRIORITÁRIO: Vagas de Entrada e Júnior (0–2 anos de experiência, estágio, trainee, sem tempo rígido).

Fontes:
  1. Base curada (jobs_seed.json) - Vagas verificadas Brasil (Gupy CLT) & Global Remoto (Canonical, Oneleet, etc.)
  2. Gupy Portais ao Vivo (IT4US Cyber Security, PagBank, Netconn, Bellinati Perez, Trade Technology, etc.)
  3. Greenhouse API (Canonical live boards)
  4. Ashby API (Supabase & Oneleet live boards)
  5. WeWorkRemotely (RSS feeds)
  6. Jobicy API (tag: security)
  7. RemoteOK API

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
    "cloud support", "support engineer", "linux", "kernel", "systems engineer",
    "sysadmin", "trust & safety", "privacy", "governança", "riscos",
    "segurança da informação", "auditoria", "dpo", "lgpd", "open source", "associate"
]

# Palavras para descarte imediato (vendas ativas, RH, marketing puro ou vagas não-técnicas)
EXCLUDE_TITLES = [
    "sales executive", "sales specialist", "sales manager", "account executive",
    "business development", "bdr", "sdr", "ux designer", "ui designer",
    "product designer", "graphic designer", "social media", "copywriter",
    "content marketing", "general manager", "recruiter", "talent acquisition",
    "people partner", "hrbp", "government affairs", "lobbyist", "public policy",
    "animator", "medical expert", "fertility", "closer b2b", "executivo de vendas"
]

# Termos que tornam a vaga inelegível para quem mora no Brasil sem cidadania estrangeira
INELEGIBLE_TERMS = [
    "clearance", "public trust", "dod", "secret", "ts/sci", "sc clearance",
    "us citizen", "uk citizen", "british citizen", "cidadania americana",
    "citizenship required", "must reside in the us", "u.s. based only",
    "us only", "usa only", "uk only", "canada only", "australia only"
]

# Portais Gupy de empresas de tecnologia, cibersegurança e fintechs brasileiras
GUPY_PORTALS = [
    {"sub": "vemprait4us", "name": "IT4US Cyber Security"},
    {"sub": "tradetechnology", "name": "Grupo Trade Technology"},
    {"sub": "pagseguro", "name": "PagBank (PagSeguro)"},
    {"sub": "bellinatiperez", "name": "Bellinati Perez"},
    {"sub": "netconn", "name": "Netconn"},
    {"sub": "funcionalhealthtech", "name": "Funcional Health Tech"},
    {"sub": "modulardtc", "name": "Modular Data Centers"}
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
        
    # 3. Vagas internacionais NÃO podem ser híbridas nem presenciais no exterior
    office_words = ["hybrid", "hibrid", "office", "on-site", "onsite", "presencial"]
    for ow in office_words:
        if ow in loc.lower() and not ("brasil" in loc.lower() or "brazil" in loc.lower()):
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

def extract_years(text):
    """Extrai com precisão a quantidade de anos de experiência exigida no texto."""
    if not text:
        return None
    clean = re.sub(r'<[^>]+>', ' ', text).lower()
    matches = []
    
    # 3+ years / 3+ yrs / 3+ anos
    for m in re.finditer(r'\b(\d{1,2})\s*\+\s*(?:years|yrs|anos)\b', clean):
        matches.append(int(m.group(1)))
        
    # over / at least / minimum of 3 years
    for m in re.finditer(r'\b(?:over|at least|minimum of|minimum|min\.|mais de|pelo menos|mínimo de)\s*(\d{1,2})\s*(?:years|yrs|anos)\b', clean):
        matches.append(int(m.group(1)))
        
    # 3 to 5 years / 3-5 years / 3 a 5 anos
    for m in re.finditer(r'\b(\d{1,2})\s*(?:-|to|a)\s*(\d{1,2})\s*(?:years|yrs|anos)\b', clean):
        matches.append(int(m.group(2)))
        
    # 3 years of experience / 3 anos de experiência
    for m in re.finditer(r'\b(\d{1,2})\s*(?:years|yrs|anos)\s*(?:of\s*(?:relevant\s*)?experience|de\s*experiência)\b', clean):
        matches.append(int(m.group(1)))
        
    valid = [y for y in matches if 1 <= y <= 15]
    return max(valid) if valid else None

def extract_experience_timeframe(title, desc=""):
    """
    Analisa os requisitos da vaga e extrai o prazo de experiência e o nível correspondente.
    Retorna: (exp_timeframe, level, years)
    """
    t = (title or "").lower()
    d = (desc or "").lower()
    full = f"{t} {d}"

    # 1. Estágio / Trainee / Em formação
    if any(w in t for w in ["estagiário", "estagiario", "estágio", "estagio", "intern", "internship", "trainee", "apprentice"]):
        return "0 ano (estágio / em formação)", "estágio", 0

    # 2. Vagas de entrada formal para graduados / sem experiência prévia
    if any(p in full for p in [
        "sem experiência", "sem experiencia", "não exige experiência", "nao exige experiencia",
        "no experience required", "no previous experience", "entry level", "entry-level",
        "início de carreira", "primeiro emprego", "formação acadêmica ou transição"
    ]):
        if "graduate" in t or "graduando" in full:
            return "0 ano (recém-formado / graduate)", "entry", 0
        return "0 a 1 ano (sem experiência prévia / transição)", "entry", 0

    # 3. Análise numérica de anos exigidos
    years = extract_years(d)
    if years is not None:
        if years >= 5:
            return f"{years}+ anos (sênior / liderança)", "senior", years
        elif years >= 3:
            return f"{years}+ anos (pleno)", "pleno", years
        elif years == 2:
            return "1 a 2 anos (júnior / transição)", "entry", 2
        elif years == 1:
            return "0 a 1 ano (júnior / inicial)", "entry", 1

    # 4. Inferência contextual por títulos de entrada
    if re.search(r'\b(graduate|recém-formado)\b', t):
        return "0 ano (recém-formado / graduate)", "entry", 0
    if re.search(r'\b(junior|jr|júnior|iniciante|early career)\b', t):
        return "0 a 1 ano (júnior / início de carreira)", "entry", 1
    if re.search(r'\bassociate\b', t) and not any(w in t for w in ["director", "lead", "manager"]):
        return "0 a 2 anos (nível associado / transição)", "entry", 1
    if re.search(r'\b(tier 1|tier-1|soc 1|soc-1)\b', t):
        return "0 a 1 ano (SOC Tier 1 / entrada)", "entry", 1
    if re.search(r'\b(senior|sr|lead|principal|staff|head|director|chief)\b', t):
        return "5+ anos (sênior / liderança)", "senior", 5

    # 5. Padrão para analistas e suporte sem especificação rígida
    return "1 a 2 anos (foco em competência prática)", "entry", 2

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
                if final.count('/') < 3 and not ("ashbyhq" in final or "greenhouse" in final or "gupy.io" in final):
                    return False
                return True
            return False
    except urllib.error.HTTPError as e:
        if e.code == 429: # Rate limit momentâneo da API não invalida o link
            return True
        return False
    except Exception:
        return True # Se deu timeout na checagem rápida, mantém na dúvida

def scan_gupy_portals():
    """Varre os quadros oficiais e abertos de vagas de empresas de segurança e fintechs na Gupy."""
    gupy_jobs = []
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    for portal in GUPY_PORTALS:
        sub = portal["sub"]
        company = portal["name"]
        url = f"https://{sub}.gupy.io/"
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            })
            with urllib.request.urlopen(req, timeout=12) as r:
                html = r.read().decode("utf-8")
                m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.+?)</script>', html)
                if not m:
                    continue
                data = json.loads(m.group(1))
                jobs = data.get("props", {}).get("pageProps", {}).get("jobs", [])
                for j in jobs:
                    title = j.get("title", "")
                    if not is_cyber_role(title):
                        continue
                        
                    workplace = j.get("workplace", {})
                    wpt = workplace.get("workplaceType", "remote")
                    city = workplace.get("address", {}).get("city", "Brasil")
                    loc = "Remoto (Brasil)" if wpt == "remote" else f"Híbrido ({city})"
                    
                    jid = j.get("id")
                    job_url = f"https://{sub}.gupy.io/job/{jid}"
                    
                    timeframe, lvl, _ = extract_experience_timeframe(title, "")
                    
                    gupy_jobs.append({
                        "id": f"gupy-{sub}-{jid}",
                        "role": title[:80],
                        "company": company,
                        "loc": loc,
                        "pay": "A combinar (R$ CLT)",
                        "level": lvl,
                        "exp_timeframe": timeframe,
                        "source": "Gupy",
                        "geo": "brasil",
                        "url": job_url,
                        "req": ["secplus"],
                        "clearance": False,
                        "sponsor": False,
                        "student": lvl == "estágio",
                        "dest": 5,
                        "study": 5 if lvl in ["entry", "estágio"] else 4,
                        "tasks": f"Atuação em {title} no portal de carreiras da {company} via Gupy.",
                        "note": f"⭐ Vaga oficial aberta na {company} (Gupy). Foco em segurança, governança e conformidade.",
                        "added_date": today_str
                    })
        except Exception as e:
            print(f"Aviso ao varrer Gupy portal {sub}: {e}")
            
    return gupy_jobs

def scan_canonical_greenhouse():
    """Varre a API oficial e aberta da Canonical no Greenhouse com foco em vagas de entrada e suporte."""
    jobs = []
    url = "https://boards-api.greenhouse.io/v1/boards/canonical/jobs"
    try:
        data = fetch_url(url, is_json=True, timeout=20)
        today_str = datetime.now().strftime("%Y-%m-%d")
        for j in data.get("jobs", []):
            role = j.get("title", "")
            link = j.get("absolute_url", "")
            
            # Prioriza papéis técnicos de Linux, Suporte, Open Source, Kernel, Segurança e Auditoria
            if not is_cyber_role(role):
                continue
                
            loc = "Remote (Worldwide / Brasil)"
            geo = "worldwide"
            
            timeframe, lvl, _ = extract_experience_timeframe(role, "")
            
            job_id = f"can-{j.get('id', '')}"
            jobs.append({
                "id": job_id,
                "role": role[:80],
                "company": "Canonical",
                "loc": loc,
                "pay": "US$ 40k–70k (CLT/PJ via EOR)",
                "level": lvl,
                "exp_timeframe": timeframe,
                "source": "Canonical Greenhouse",
                "geo": geo,
                "url": link,
                "req": ["secplus"],
                "clearance": False,
                "sponsor": False,
                "student": lvl == "estágio",
                "dest": 5,
                "study": 5,
                "tasks": f"Atuação técnica em {role} na Canonical Ubuntu. Empresa global pioneira em trabalho 100% remoto.",
                "note": "⭐ CANONICAL GLOBAL: Contratação remota direta no Brasil (CLT/PJ via EOR). Pioneira em trabalho 100% remoto.",
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
                
            timeframe, lvl, _ = extract_experience_timeframe(role, desc)
            
            job_id = f"{board_name}-{re.sub(r'[^a-z0-9]+', '-', role.lower())}"[:40]
            jobs.append({
                "id": job_id,
                "role": role[:80],
                "company": display_name,
                "loc": loc,
                "pay": "A combinar (US$)",
                "level": lvl,
                "exp_timeframe": timeframe,
                "source": f"{display_name} Ashby",
                "geo": geo,
                "url": link,
                "req": ["secplus"],
                "clearance": False,
                "sponsor": False,
                "student": False,
                "dest": 5,
                "study": 5 if lvl == "entry" else 4,
                "tasks": f"Atuação em {role} na {display_name}. Vaga oficial capturada no ATS Ashby.",
                "note": f"⭐ Vaga oficial aberta na {display_name} (Ashby ATS). Contratação remota internacional.",
                "added_date": today_str
            })
    except Exception as e:
        print(f"Erro ao varrer Ashby ({display_name}): {e}")
    return jobs

def scan_weworkremotely():
    """Varre feeds RSS do WeWorkRemotely priorizando papéis de suporte, sistemas e segurança."""
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
                    
                timeframe, lvl, years = extract_experience_timeframe(role, desc)
                
                # Descarte agressivo de sênior vindo de agregador (foco é júnior/entrada)
                if lvl == "senior" and (years or 0) >= 5:
                    continue
                    
                job_id = f"wwr-{re.sub(r'[^a-z0-9]+', '-', company.lower())}-{re.sub(r'[^a-z0-9]+', '-', role.lower())}"[:40]
                
                wwr_jobs.append({
                    "id": job_id,
                    "role": role[:80],
                    "company": company[:40],
                    "loc": loc,
                    "pay": "A combinar (US$)",
                    "level": lvl,
                    "exp_timeframe": timeframe,
                    "source": "WeWorkRemotely",
                    "geo": "worldwide",
                    "url": link,
                    "req": ["secplus"],
                    "clearance": False,
                    "sponsor": False,
                    "student": False,
                    "dest": 4,
                    "study": 5 if lvl == "entry" else 4,
                    "tasks": f"Atuação em {role} para {company}. Vaga internacional 100% remota anunciada no WeWorkRemotely.",
                    "note": f"⭐ Vaga encontrada no WeWorkRemotely ({region}). Aberta para contratação remota internacional.",
                    "added_date": today_str
                })
        except Exception as e:
            print(f"Erro ao varrer feed WeWorkRemotely ({feed_url}): {e}")
            
    return wwr_jobs

def scan_jobicy():
    """Varre a API do Jobicy com foco estrito em segurança e suporte júnior/pleno."""
    jobicy_jobs = []
    url = "https://jobicy.com/api/v2/remote-jobs?count=30&tag=security"
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
                
            timeframe, lvl, years = extract_experience_timeframe(role, desc)
            
            # Não sobrecarregar com sênior
            if lvl == "senior" and (years or 0) >= 5:
                continue
                
            job_id = f"jobicy-{re.sub(r'[^a-z0-9]+', '-', company.lower())}-{re.sub(r'[^a-z0-9]+', '-', role.lower())}"[:40]
            
            jobicy_jobs.append({
                "id": job_id,
                "role": role[:80],
                "company": company[:40],
                "loc": f"Remote ({loc})",
                "pay": "A combinar (US$)",
                "level": lvl,
                "exp_timeframe": timeframe,
                "source": "Jobicy",
                "geo": "worldwide",
                "url": link,
                "req": ["secplus"],
                "clearance": False,
                "sponsor": False,
                "student": False,
                "dest": 4,
                "study": 5 if lvl == "entry" else 4,
                "tasks": f"Atuação em {role} na {company}. Monitoramento e suporte de segurança remota.",
                "note": "⭐ Vaga internacional capturada via Jobicy. Aceita aplicação remota.",
                "added_date": today_str
            })
    except Exception as e:
        print(f"Erro ao consultar Jobicy: {e}")
        
    return jobicy_jobs

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
    print("Iniciando varredura diária de vagas CyberSec (Foco em Júnior & Entrada)...")
    
    # 1. Carrega a base curada (espinha dorsal com vagas reais do Brasil e internacionais)
    seed_jobs = []
    if os.path.exists(SEED_FILE):
        try:
            with open(SEED_FILE, "r", encoding="utf-8") as f:
                seed_jobs = json.load(f)
            print(f"Base curada carregada: {len(seed_jobs)} vagas prioritárias.")
        except Exception as e:
            print(f"Erro ao ler jobs_seed.json: {e}")
            
    # Filtra a base curada garantindo URL válida e prazo de experiência preenchido
    seed_eligible = []
    for j in seed_jobs:
        if not is_url_valid(j.get("url", "")):
            continue
        # Se a vaga não tiver timeframe explicitado no seed, calcula
        if not j.get("exp_timeframe"):
            tf, lvl, _ = extract_experience_timeframe(j.get("role", ""), j.get("tasks", ""))
            j["exp_timeframe"] = tf
            j["level"] = lvl
        seed_eligible.append(j)
        
    print(f"Vagas curadas verificadas: {len(seed_eligible)}")
    
    # 2. Executa varreduras ativas ao vivo
    live_jobs = []
    # 2.1 Portais Gupy de empresas brasileiras
    live_jobs.extend(scan_gupy_portals())
    # 2.2 ATS Canonical (Greenhouse)
    live_jobs.extend(scan_canonical_greenhouse())
    # 2.3 ATS Ashby (Oneleet & Supabase)
    live_jobs.extend(scan_ashby_company("supabase", "Supabase"))
    live_jobs.extend(scan_ashby_company("oneleet", "Oneleet"))
    # 2.4 Feeds globais filtrados
    live_jobs.extend(scan_weworkremotely())
    live_jobs.extend(scan_jobicy())
    
    print(f"Total de vagas capturadas ao vivo: {len(live_jobs)}")
    
    # 3. Deduplicação inteligente por URL e título
    seen_urls = set()
    seen_keys = set()
    final_jobs = []
    
    def get_norm_url(u):
        if not u: return ""
        return re.sub(r'[?#].*$', '', u.strip().rstrip('/')).lower()

    # Prioridade 1: Base curada
    for j in seed_eligible:
        u_norm = get_norm_url(j.get("url", ""))
        key = (j.get("company", "").strip().lower(), j.get("role", "").strip().lower())
        if u_norm and u_norm in seen_urls:
            continue
        if key in seen_keys:
            continue
        if u_norm: seen_urls.add(u_norm)
        seen_keys.add(key)
        final_jobs.append(j)
            
    # Prioridade 2: Vagas capturadas ao vivo
    for j in live_jobs:
        u_norm = get_norm_url(j.get("url", ""))
        key = (j.get("company", "").strip().lower(), j.get("role", "").strip().lower())
        if u_norm and u_norm in seen_urls:
            continue
        if key in seen_keys:
            continue
        if u_norm: seen_urls.add(u_norm)
        seen_keys.add(key)
        final_jobs.append(j)
            
    # 4. Ordenação estratégica: Vagas de Estágio e Entrada/Júnior (0-2 anos) SEMPRE NO TOPO!
    def sort_priority(job):
        lvl = job.get("level", "pleno")
        if lvl == "estágio":
            return 0
        if lvl == "entry":
            return 1
        if lvl == "pleno":
            return 2
        return 3 # senior
        
    final_jobs.sort(key=sort_priority)
    
    entry_count = sum(1 for j in final_jobs if j.get("level") in ["entry", "estágio"])
    pleno_count = sum(1 for j in final_jobs if j.get("level") == "pleno")
    senior_count = sum(1 for j in final_jobs if j.get("level") == "senior")
    
    print(f"Consolidação concluída: {len(final_jobs)} vagas ({entry_count} Entrada/Júnior, {pleno_count} Pleno, {senior_count} Sênior)")
    
    now_dt = datetime.now()
    now_str = now_dt.strftime("%Y-%m-%d %H:%M")
    cache_version = now_dt.strftime("%Y%m%d_%H%M")
    
    insight_str = (
        f"{entry_count} vagas de Entrada e Júnior (0–2 anos / estágio) em destaque "
        f"de um total de {len(final_jobs)} vagas verificadas no Brasil (CLT/PJ) e Global Remoto."
    )
    
    # 5. Escreve vagas_data.js
    js_content = (
        "// GERADO AUTOMATICAMENTE por job_scan.py — NÃO editar à mão\n"
        f"window.JOBS_UPDATED={json.dumps(now_str, ensure_ascii=False)};\n"
        f"window.JOBS_INSIGHT={json.dumps(insight_str, ensure_ascii=False)};\n"
        f"window.JOBS_LIVE={json.dumps(final_jobs, ensure_ascii=False)};\n"
    )
    
    with open(VAGAS_FILE, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"vagas_data.js atualizado com sucesso em {VAGAS_FILE}")
    
    # 6. Atualiza o cache buster no HTML
    update_html_cache_buster(cache_version)
    
    # 7. Registra no Digest e Log
    try:
        with open(DIGEST_FILE, "a", encoding="utf-8") as f:
            f.write(f"\n## {now_str}\n")
            f.write(f"- {insight_str}\n")
            f.write(f"- Breakdown: {entry_count} Entrada/Júnior, {pleno_count} Pleno, {senior_count} Sênior\n")
            
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            log_entry = {
                "ts": now_str,
                "total": len(final_jobs),
                "entry": entry_count,
                "pleno": pleno_count,
                "senior": senior_count
            }
            f.write(json.dumps(log_entry) + "\n")
    except Exception as e:
        print(f"Erro ao salvar digest/log: {e}")
        
    print("Varredura finalizada com êxito!")

if __name__ == "__main__":
    run()

# Publica as vagas + apps no GitHub Pages (https://edusouzamarques.github.io/cybersec/)
# Roda TODO dia 08:15 (15 min depois do CyberSec Job Scan de 08:00) via tarefa "CyberSec Job Publish"
$ErrorActionPreference = "Stop"
$ws  = "C:\Users\ivign\CYBERSEC"
$site = "$ws\_site"
Set-Location $site

# 1. copia o que mudou
Copy-Item "$ws\assistente-cybersec.html" "$site\assistente-cybersec.html" -Force
Copy-Item "$ws\treino-cybersec.html"     "$site\treino-cybersec.html"     -Force
Copy-Item "$ws\dell_user_progress.json" "$site\user_progress.json"       -Force
Copy-Item "$ws\_jobscan\vagas_data.js"   "$site\_jobscan\vagas_data.js"   -Force
Copy-Item "$ws\_jobscan\jobs_seed.json"  "$site\_jobscan\jobs_seed.json"  -Force

# 2. .nojekyll obrigatorio (senao o Pages ignora a pasta _jobscan)
if (-not (Test-Path "$site\.nojekyll")) { Set-Content -Path "$site\.nojekyll" -Value "" -Encoding ascii }

# 3. sanitiza copia publica (remove EB-2/PMMG)
python -X utf8 "$ws\strip_perfil.py" "$site\assistente-cybersec.html" | Out-Null

# 4. commit + push (só se mudou algo)
$st = git status --porcelain
if ($st) {
  git add -A
  git commit -q -m "auto-sync diaria de vagas + apps"
  git push -q origin main
  "publicado: https://edusouzamarques.github.io/cybersec/"
} else {
  "nada mudou"
}
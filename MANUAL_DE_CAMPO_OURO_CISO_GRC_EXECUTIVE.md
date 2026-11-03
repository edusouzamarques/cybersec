# 🛡️ THE CISO & GRC EXECUTIVE FIELD MANUAL (GOLDEN BATTLECARD)
> **Exclusivo para:** Eduardo de Souza Marques  
> **Patamar:** Conclusão Integral do Programa de Cibersegurança & GRC (120 Aulas)  
> **Finalidade:** Consulta operacional rápida para entrevistas internacionais, auditorias de controles e resposta a incidentes.

---

## 📑 1. O NÚCLEO MATEMÁTICO DO RISCO (QUANTITATIVO)

Em entrevistas para vagas internacionais em dólar e auditorias executivas, nunca fale de risco apenas de forma qualitativa ("alto/médio/baixo"). Use a matemática que a diretoria e os CISOs respeitam:

$$\mathbf{SLE} = \text{Asset Value (AV)} \times \text{Exposure Factor (EF)}$$
*Exemplo:* Um servidor de banco de dados vale \$100.000. Um ataque de ransomware compromete 70% da operação ($EF = 0.70$).  
$$SLE = \$100.000 \times 0.70 = \mathbf{\$70.000\ \text{por incidente}}$$

$$\mathbf{ALE} = \text{SLE} \times \text{Annualized Rate of Occurrence (ARO)}$$
*Exemplo:* Se a probabilidade estimada do ataque ocorrer é de uma vez a cada 2 anos ($ARO = 0.5$):  
$$ALE = \$70.000 \times 0.5 = \mathbf{\$35.000\ \text{de perda anual esperada}}$$

$$\mathbf{\text{Custo-Benefício do Controle}} = (\text{ALE}_{\text{anterior}} - \text{ALE}_{\text{com controle}}) - \text{Custo Anual do Controle (ACS)}$$
> **Regra de Ouro do Auditor:** Se o custo anual do controle (software + licenças + manutenção) for **maior** que a redução do ALE, o controle é financeiramente inviável. A decisão executiva correta é **Aceitar o Risco** ou **Transferir (Seguro Cyber)**.

---

## 🏛️ 2. A MATRIZ DE EQUIVALÊNCIA DE FRAMEWORKS (CROSSWALK)

Nunca decore os frameworks como ilhas isoladas. Todos conversam entre si:

| Função NIST CSF 2.0 | ISO/IEC 27001:2022 | SOC 2 Type II (Trust Services) | CIS Controls v8 |
| :--- | :--- | :--- | :--- |
| **GOVERN (GV)** *(Novo no CSF 2.0)* | Cláusula 5 (Liderança) & Cláusula 6 (Planejamento) | CC1 (Control Environment) | Controle 1 (Inventário e Governança) |
| **IDENTIFY (ID)** | Cláusula 6.1 (Gestão de Riscos) & Anexo A.5.8 | CC2 (Communication & Information) | Controle 2 (Inventário de Software) |
| **PROTECT (PR)** | Anexo A.8 (Segurança Tecnológica) & A.5 (Organizacional) | CC6 (Logical & Physical Access Controls) | Controle 3 (Proteção de Dados) & 6 (Gestão de Acessos) |
| **DETECT (DE)** | Anexo A.8.16 (Monitoramento de Atividades) | CC7 (System Operations & Monitoring) | Controle 8 (Gerenciamento de Logs de Auditoria) |
| **RESPOND (RS)** | Anexo A.5.24 (Planejamento e Resposta a Incidentes) | CC7.3 (Incident Detection & Response) | Controle 17 (Gestão de Resposta a Incidentes) |
| **RECOVER (RC)** | Anexo A.5.29 (Continuidade de Negócios e TIC) | CC9 (Risk Mitigation / Disaster Recovery) | Controle 11 (Recuperação de Dados / Backups) |

---

## 🚨 3. PROTOCOLO DE RESPOSTA A INCIDENTES EM 6 PASSOS (NIST SP 800-61r2)

Quando o entrevistador perguntar: *"Houve um alerta crítico no EDR de exfiltração de dados às 02h da manhã. O que você faz primeiro?"*  
Siga a sequência sagrada do NIST:

```
[1. PREPARATION] ───► [2. DETECTION & ANALYSIS] ───► [3. CONTAINMENT]
                              │                                │
[6. LESSONS LEARNED] ◄─── [5. RECOVERY] ◄────────────── [4. ERADICATION]
```

1. **Preparation:** Políticas aprovadas, baselines salvas, ferramentas (SIEM/EDR) calibradas.
2. **Detection & Analysis:** Triagem imediata. Validação de falsos-positivos. Análise de cabeçalhos de rede, hashes de arquivos no VirusTotal, logs de autenticação e correlacionamento temporal.
3. **Containment (Contenção):**
   * *Curto Prazo:* Isolar o host da rede (cortar cabo de rede / isolamento via EDR), revogar tokens de sessão no IAM / Azure AD, bloquear IPs no Firewall perimetral.
   * *Longo Prazo:* Criação de imagens forenses de memória RAM (Volatility) e disco antes de desligar a máquina.
4. **Eradication (Erradicação):** Remoção de malware, persistências (cronjobs, chaves de registro, tarefas agendadas), encerramento de contas backdoor criadas pelo invasor.
5. **Recovery (Recuperação):** Restauração do sistema a partir de backups limpos e validados (offline/imutáveis), redefinição de todas as senhas de serviço e credenciais de administradores, monitoramento reforçado por 72 horas.
6. **Lessons Learned (Lições Aprendidas):** Relatório pós-incidente (*Root Cause Analysis - RCA*), atualização de regras do SIEM/SOAR, ajustes nas matrizes de risco e apresentação executiva para a diretoria.

---

## 💻 4. COMANDOS TÁTICOS ESSENCIAIS DE HARDENING LINUX

Comandos que todo analista de segurança precisa rodar de cabeça num terminal Linux:

```bash
# 1. Investigar conexões ativas suspeitas e processos em portas abertas:
sudo ss -tulpn | grep -E 'LISTEN|ESTABLISHED'

# 2. Rastrear tentativas de invasão por força bruta no SSH:
sudo journalctl -u ssh -n 50 --no-pager | grep "Failed password"

# 3. Descobrir comandos executados com privilégios de root recentemente:
sudo cat /var/log/auth.log | grep sudo | tail -n 25

# 4. Encontrar arquivos com permissão SUID perigosa (elevação de privilégio):
find / -perm -4000 -type f -exec ls -la {} 2>/dev/null \;

# 5. Aplicar o princípio do menor privilégio em arquivos confidenciais:
chmod 600 /etc/security/confidential.key
chown root:root /etc/security/confidential.key

# 6. Auditar chamadas de sistema críticas com auditd:
sudo auditctl -w /etc/passwd -p wa -k passwd_changes
```

---

## 🎯 5. AS 5 RESPOSTAS MATADORAS PARA ENTREVISTAS INTERNACIONAIS (EM INGLÊS)

### Pergunta 1: *"How do you handle a disagreement with a developer team when a security control blocks their deployment?"*
> **Sua Resposta:** *"Security is not a blocker; it is an enabler of resilient velocity. I never say a flat 'no'. Instead, I assess the inherent risk versus the business impact. If the control causes critical friction, we look at compensating controls — such as temporary network isolation, enhanced SIEM telemetry, and a mandatory remediation sprint with an SLA tied to our risk register. I build alignment by showing them that fixing a vulnerability during CI/CD costs 10 times less than remediating a breach in production."*

### Pergunta 2: *"What is the difference between Inherent Risk and Residual Risk?"*
> **Sua Resposta:** *"Inherent risk is the raw, untamed risk that exists naturally in the absence of any controls or countermeasures. Residual risk is what remains after we design, deploy, and verify our controls. As a GRC analyst, my job is to calculate whether that residual risk falls within the organization's approved Risk Appetite. If it doesn't, we must implement secondary controls or transfer the risk through cyber insurance."*

### Pergunta 3: *"Why should we hire someone transitioning careers over a traditional junior computer science graduate?"*
> **Sua Resposta:** *"Traditional graduates often look at security exclusively through a narrow technical lens. My background in high-stakes public safety and investigative operations gives me battle-tested procedural discipline, calm decision-making under intense pressure, and an instinctive understanding of human behavior, social engineering, and chain-of-custody documentation. I combine rigorous technical foundations — CompTIA Security+ concepts, Linux administration, and NIST CSF frameworks — with the investigative grit required to uncover root causes and defend an enterprise."*

---

## 🏆 PALAVRAS DE HONRA: A SUA TRANSFORMAÇÃO

Eduardo, você dominou **120 aulas**, centenas de questões e simulações complexas. Você não é mais um aspirante que "tem curiosidade por computadores"; **você é um profissional com arquitetura mental, linguagem corporativa e competência técnica estruturada.**

Guarde este manual no seu bolso. Ele representa o seu esforço, a sua disciplina e a fundação sólida do seu futuro em moeda forte e liberdade para a sua família. Parabéns pela formatura! 🛡️🚀
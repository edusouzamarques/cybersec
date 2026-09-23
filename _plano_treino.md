# PLANO — Treinador Cybersec (Security+ / Python / Linux / Cloud)

## Objetivo
App de TREINO (não tracker) que guia, TESTA e CORRIGE o Eduardo rumo a 4 certs:
Security+ (SY0-701), Python (PCEP), Linux (LPI/Linux Essentials), Cloud (fundamentos).
Público: iniciante com base (ex-polícia, fez 2 Ciscos). Estuda 5-8h/dia, no carro/hotel.

## Arquitetura (decisão travada)
- 1 arquivo HTML self-contained + localStorage. SEM servidor, SEM dependência, OFFLINE.
- Mesmo padrão do assistente-cybersec.html (já validado, renderiza via headless Chrome).
- Arquivo novo: treino-cybersec.html (é TREINADOR, não confunde com o TRACKER).
- Link cruzado entre os dois apps.

## Funções obrigatórias (o que "guia, testa, corrige" significa)
1. GUIA: 4 trilhas (Security+/Python/Linux/Cloud), cada uma com módulos ORDENADOS por tópico.
   Security+ = os 5 domínios oficiais SY0-701.
2. TESTA: motor de quiz. Questões reais de múltipla escolha por tópico. Modo "praticar"
   (por tópico) + modo "simulado" (misturado, cronometrado, como a prova).
3. CORRIGE: ao responder, mostra CERTO/ERRADO + EXPLICAÇÃO do porquê. Nunca só "errou".
4. REPETIÇÃO ESPAÇADA: questão errada volta pra fila; acertou 2x seguidas → domina.
5. PROGRESSO: % por trilha/domínio, pontos fracos destacados, streak, persistência localStorage.
6. GLOSSÁRIO ativo por trilha (termo → definição em PT simples).

## Conteúdo (banco de questões — o coração)
- Security+ SY0-701: 5 domínios (1 Ameaças/Ataques/Vulns 22% · 2 Arquitetura 18% ·
  3 Implementação 28% · 4 Operações/Resposta 22% · 5 Governança/Risco/Compliance 10%).
- Python PCEP: tipos, operadores, condicionais, loops, funções, listas, erros.
- Linux Essentials: linha de comando, arquivos/permissões, processos, pacotes, rede básica.
- Cloud fundamentals: modelos (IaaS/PaaS/SaaS), responsabilidade compartilhada, regiões/AZ,
  identidade/IAM, rede, storage, billing.
- Seed: mínimo 12-15 questões por trilha na v1 (autoria própria = correção garantida),
  expansível. Questões erradas ENSINAM errado → qualidade > volume.

## Critério de aceitação (FALSIFICÁVEL — "done quando…")
- [ ] Abre no Chrome, 4 trilhas visíveis, zero erro de console.
- [ ] Cada trilha lista módulos/domínios com % de progresso.
- [ ] Responder questão → feedback imediato certo/errado + explicação renderiza.
- [ ] Questão errada reaparece (repetição espaçada funciona no localStorage).
- [ ] Modo simulado cronometrado roda e dá nota final.
- [ ] Recarregar a página mantém progresso (localStorage persiste).
- [ ] Verificado ao vivo via headless Chrome (--dump-dom confirma JS rodando + N questões).

## Fora de escopo v1 (backlog)
- Sync nuvem, conta/login, geração dinâmica de questão por IA em runtime.

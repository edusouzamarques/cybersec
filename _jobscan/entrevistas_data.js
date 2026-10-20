/**
 * BANCO DE QUESTÕES E RESPOSTAS — SIMULADOR DE ENTREVISTAS CYBERSEC & SUPORTE
 * Curadoria baseada em canais de referência no YouTube:
 * - CareerVidz (Richard McMunn) — Técnicas STAR, Comportamental e RH
 * - Simply Cyber (Dr. Gerald Auger) — Mock Interviews SOC L1 & Cyber Entry-Level
 * - Day Cyberwox & Josh Madakor — Triagem técnica, Labs e Transição de Carreira
 * - NetworkChuck & Sysadmin Channels — Troubleshooting Linux, Redes e Protocolos
 * 
 * Atualizado para o perfil de Eduardo de Souza Marques (13.5 anos de investigação/polícia,
 * Linux, CompTIA Security+, Python e Mestrado CU Boulder).
 */

window.ENTREVISTAS_DATA = [
  /* ==========================================================================
     CATEGORIA 1: COMPORTAMENTAL, RH & CARREIRA (CareerVidz / Richard McMunn)
     ========================================================================== */
  {
    id: "comp-01",
    cat: "behavioral",
    catName: "🗣️ Comportamental & RH",
    difficulty: "Entrada / Fundamental",
    source: "CareerVidz (Richard McMunn) & Simply Cyber",
    title_en: "Tell me about yourself and why you are interested in this position.",
    title_pt: "Fale sobre você e por que você tem interesse nesta vaga.",
    intent: "O recrutador quer avaliar sua clareza, concisão e capacidade de alinhar sua trajetória com a necessidade imediata da empresa. Não é para recitar o currículo linha por linha.",
    trap: "Começar pela infância ou falar da vida pessoal; focar apenas no passado policial sem ligar aos projetos técnicos atuais; ou falar por mais de 2 minutos sem parar.",
    formula: "Fórmula 3P (Presente → Passado → Futuro): Quem você é hoje e o que domina → O histórico de rigor e disciplina que traz do passado → Por que esta empresa é o próximo passo natural.",
    answer_en: `Thank you for having me today.

Currently, I am focused on cybersecurity analysis, Linux systems administration, and network security, actively preparing for my CompTIA Security+ certification while working hands-on with system troubleshooting and security tooling.

Before transitioning into tech, I spent over 13 years conducting complex investigations and field operations in high-stakes environments. That experience instilled in me a deep discipline for chain of custody, objective evidence gathering, and calm decision-making under intense pressure. I found that threat detection and security operations require the exact same investigative mindset: gathering artifacts, analyzing patterns, and verifying root causes.

I was drawn to this position because your team values proactive problem-solving, structured incident handling, and reliability. I am eager to apply my investigative persistence and technical foundation to protect your infrastructure and deliver immediate value from day one.`,
    guide_pt: `Apresente-se com segurança em 90 segundos:
1. PRESENTE: Destaque sua rotina técnica diária (Linux, redes, preparação para Security+, resolução de problemas práticos).
2. PASSADO: Use seus 13,5 anos como uma fortaleza — enfatize que você já é um investigador experiente que opera com cadeia de custódia, documentação rigorosa e frieza sob pressão extrema.
3. FUTURO: Conecte diretamente com a vaga, mostrando que a mentalidade de SOC/Suporte é a mesma de uma investigação analítica.`
  },
  {
    id: "comp-02",
    cat: "behavioral",
    catName: "🗣️ Comportamental & RH",
    difficulty: "Entrada / Fundamental",
    source: "Simply Cyber (Gerald Auger) & Day Cyberwox",
    title_en: "Why are you transitioning from law enforcement into cybersecurity and IT?",
    title_pt: "Por que você está migrando da área policial/investigativa para segurança da informação e TI?",
    intent: "Validar se você está 'fugindo' da carreira anterior ou se está se movendo com propósito e paixão genuína por tecnologia e segurança digital.",
    trap: "Dizer que está migrando apenas pelo salário em dólares ou porque estava cansado/desiludido com o trabalho policial.",
    formula: "Evolução Natural: Mostrar que o crime e as ameaças migraram para o meio digital e que suas habilidades analíticas foram naturalmente atraídas para proteger infraestruturas digitais.",
    answer_en: `For me, this transition is the natural evolution of my professional calling. In law enforcement, my core mission was always about protecting people, upholding integrity, and uncovering the truth through objective evidence.

As society evolved, I noticed that the most critical vulnerabilities and threat actors were shifting toward digital networks and infrastructure. I became fascinated by how systems communicate, how digital evidence is analyzed, and how proactive controls can prevent harm before it occurs.

Rather than starting from scratch, I am bringing 13+ years of battle-tested investigative rigor, emotional resilience, and ethics into the digital space, backed by continuous hands-on training in Linux, networking, and information security standards. Protecting digital assets requires the same commitment to vigilance and integrity that defined my entire public service career.`,
    guide_pt: `Mostre que não é um salto aleatório, mas uma evolução:
- A missão central continua a mesma: proteger integridade, combater fraude e analisar evidências.
- A única mudança é o terreno: da rua para a rede e os servidores.
- Quem contrata ama ouvir que sua ética e integridade foram forjadas no serviço público sob supervisão rígida.`
  },
  {
    id: "comp-03",
    cat: "behavioral",
    catName: "🗣️ Comportamental & RH",
    difficulty: "Entrada / Comum",
    source: "CareerVidz (Richard McMunn)",
    title_en: "What is your greatest weakness?",
    title_pt: "Qual é o seu maior ponto fraco / fraqueza?",
    intent: "Testar seu autoconhecimento, humildade e capacidade de autorregulação. Eles querem ver se você é capaz de reconhecer um problema e criar um processo para resolvê-lo.",
    trap: "Usar clichês como 'sou perfeccionista demais' ou 'trabalho demais' (que irritam recrutadores), ou admitir uma fraqueza fatal como 'não me dou bem com colegas' ou 'não sei trabalhar sob pressão'.",
    formula: "Fraqueza Real Menor + Consciência + Mecanismo Ativo de Compensação.",
    answer_en: `Early on, coming from a very fast-paced operational background, I had a tendency to rely heavily on fast, intuitive troubleshooting in my head without immediately documenting every intermediate step for others.

I realized that in technology and remote engineering teams, asynchronous documentation and clear ticket trails are just as vital as resolving the problem itself. 

To overcome this, I established a strict habit of documenting my troubleshooting processes in real time—taking structured notes on commands executed, error codes observed, and outcomes. This ensures that any team member can follow my investigative trail, reproduce the fix, or take over during a shift handover without any information gaps.`,
    guide_pt: `Resposta honesta e inteligente:
- Reconheça que costumava resolver o problema rápido demais na cabeça sem anotar tudo na hora.
- Explique como percebeu que equipes remotas dependem de documentação assíncrona detalhada.
- Conclua mostrando seu método atual: registro em tempo real de comandos, erros e soluções em tickets ou bases de conhecimento.`
  },
  {
    id: "comp-04",
    cat: "behavioral",
    catName: "🗣️ Comportamental & RH",
    difficulty: "Intermediário",
    source: "CareerVidz (STAR Method) & Josh Madakor",
    title_en: "Describe a time you had to handle an intense, high-pressure crisis. (STAR Method)",
    title_pt: "Descreva uma situação em que você teve que lidar com uma crise sob forte pressão. (Método STAR)",
    intent: "Verificar se você congela, entra em pânico ou age de forma impulsiva sob estresse, ou se mantém a compostura, segue protocolos e prioriza com clareza.",
    trap: "Contar uma história confusa sem início, meio e fim; culpar outras pessoas; ou não detalhar sua ação individual específica.",
    formula: "STAR: Situação (contexto breve) → Tarefa (sua responsabilidade) → Ação (o que VOCÊ fez especificamente) → Resultado (desfecho positivo e aprendizado).",
    answer_en: `Situation: During a high-stakes field operation involving conflicting reports and immediate physical risk, our team was faced with rapidly degrading situational intelligence and high adrenaline.

Task: As the lead investigator on scene, my responsibility was to establish operational control, de-escalate tension, secure critical evidence without contamination, and ensure team safety.

Action: While others were reacting emotionally, I immediately paused to ground myself, separated the chaotic environment into primary priorities, and adhered strictly to standard operating procedures. I designated clear, single responsibilities to each team member, verified facts before broadcasting updates, and systematically preserved the physical perimeter and chain of custody.

Result: We contained the situation with zero casualties, secured 100% of the forensic evidence, and produced an airtight official report that stood up in judicial review. In tech, whether handling a production outage or an active security incident, I bring that exact same emotional control: breathe, isolate the blast radius, follow protocol, and communicate clearly.`,
    guide_pt: `Estrutura STAR impecável:
- S (Situação): Um cenário de alta tensão e risco onde decisões rápidas eram críticas.
- T (Tarefa): Manter o controle da equipe, segurança e integridade de evidências.
- A (Ação): Respirar, manter a calma, delegar tarefas claras, isolar o perímetro e seguir o procedimento operacional padrão.
- R (Resultado): Incidente contido com sucesso, dados preservados e relatório aceito sem contestações.`
  },
  {
    id: "comp-05",
    cat: "behavioral",
    catName: "🗣️ Comportamental & RH",
    difficulty: "Intermediário",
    source: "CareerVidz (Richard McMunn)",
    title_en: "Tell me about a time you had a disagreement with a coworker or supervisor. How did you resolve it?",
    title_pt: "Conte sobre uma ocasião em que discordou de um colega ou superior. Como você resolveu?",
    intent: "Avaliar maturidade interpessoal, inteligência emocional e se você prioriza o objetivo da equipe em vez do próprio ego.",
    trap: "Dizer que nunca discordou de ninguém (irreal) ou focar em ataques pessoais e ressentimentos.",
    formula: "STAR com foco em Fatos Objetivos: Respeito à pessoa → Foco nos dados/normas → Diálogo aberto → Compromisso com a decisão final da equipe.",
    answer_en: `Situation: In an operational review, a colleague and I had opposing views on the primary line of inquiry for an investigation. He favored an aggressive approach based on assumptions, while I believed we needed to verify digital and physical logs first.

Task: My objective was to ensure we pursued the most reliable evidence without alienating my team member or causing friction.

Action: Instead of debating opinions, I invited him for a one-on-one conversation. I actively listened to his perspective to understand his reasoning, then walked through the verified facts, highlighting the risk of evidence spoilage if we moved forward without objective verification. I proposed a phased approach: test the hypothesis with a rapid data check first before committing full resources.

Result: He agreed with the logic once we looked at the data together. The verification proved our hypothesis correct, saved dozens of hours of wasted effort, and actually strengthened our mutual trust. I believe disagreements are healthy when grounded in facts, respect, and shared goals.`,
    guide_pt: `Destaque a postura profissional:
- Mostre que você separa a divergência de ideias de conflitos pessoais.
- Resolva sempre com dados e fatos objetivos, ouvindo o colega primeiro.
- Mostre que propôs um teste rápido que alinhou a decisão sem desgastes.`
  },
  {
    id: "comp-06",
    cat: "behavioral",
    catName: "🗣️ Comportamental & RH",
    difficulty: "Entrada / Comum",
    source: "Simply Cyber & CareerVidz",
    title_en: "Why do you want to work for our company specifically?",
    title_pt: "Por que você quer trabalhar especificamente na nossa empresa?",
    intent: "Saber se você pesquisou sobre a empresa, se conhece os produtos/serviços dela ou se apenas disparou 100 currículos no piloto automático.",
    trap: "Dar uma resposta genérica que serviria para qualquer empresa do mundo ('vocês são líderes de mercado e eu quero aprender').",
    formula: "Conexão de 3 Pontos: Produto/Cultura específica da empresa → Como seu perfil resolve a dor deles → Por que o ambiente de trabalho remoto combina com sua disciplina.",
    answer_en: `I have been following your company's growth, particularly your commitment to open collaboration, high-availability infrastructure, and transparent technical culture.

What appeals to me most is that your team treats security and reliability not as an afterthought, but as an integral pillar of engineering and customer trust. Coming from a background where standard operating procedures, accountability, and user safety were non-negotiable, your values deeply align with mine.

Furthermore, I thrive in environments that value autonomous, disciplined execution. I am not looking for just any tech role; I am looking to invest my energy into a company where my analytical persistence, continuous learning, and protective mindset can directly contribute to customer retention and platform resilience.`,
    guide_pt: `Personalize com dados da empresa (ex: Canonical, Supabase, etc.):
- Mencione a cultura de código aberto, confiabilidade de infraestrutura ou suporte ao cliente.
- Destaque que seus valores de disciplina e transparência combinam com o trabalho remoto da equipe.
- Mostre que busca um compromisso de longo prazo.`
  },
  {
    id: "comp-07",
    cat: "behavioral",
    catName: "🗣️ Comportamental & RH",
    difficulty: "Intermediário",
    source: "CareerVidz & Gerald Auger",
    title_en: "What are your salary expectations?",
    title_pt: "Quais são suas pretensões salariais?",
    intent: "Entender se você conhece a faixa de mercado para o cargo e se suas expectativas estão alinhadas com o orçamento da posição sem assustar ou se desvalorizar.",
    trap: "Dar um número fixo e inflexível logo de início, ou dizer 'qualquer valor serve' (passa desespero e desvalorização).",
    formula: "Ancoragem de Faixa de Mercado + Foco no Pacote Global + Flexibilidade Baseada em Valor.",
    answer_en: `Based on my market research for this role in global and US-remote engineering teams, as well as the responsibilities outlined in the job description, I am targeting an annual compensation in the range of $55,000 to $70,000, or roughly $28 to $35 per hour.

That said, compensation is more than just base pay. I place immense value on the overall opportunity—including team mentorship, long-term growth potential, and the chance to contribute meaningfully to your mission. 

I am confident that if we determine there is a strong mutual fit, we will easily come to a fair and agreeable number.`,
    guide_pt: `Postura equilibrada e profissional:
- Apresente uma faixa realista para posições remotas internacionais de entrada/suporte ($55k–$70k/ano ou $28–$35/h).
- Demonstre que valoriza o conjunto da oportunidade, aprendizado e crescimento.
- Deixe aberta a flexibilidade para quando a proposta oficial for formalizada.`
  },
  {
    id: "comp-08",
    cat: "behavioral",
    catName: "🗣️ Comportamental & RH",
    difficulty: "Entrada / Comum",
    source: "CareerVidz & Josh Madakor",
    title_en: "Where do you see yourself in 3 to 5 years?",
    title_pt: "Onde você se vê daqui a 3 a 5 anos?",
    intent: "Avaliar se você tem ambição estruturada, estabilidade e se pretende crescer dentro da empresa em vez de usá-la como trampolim de curto prazo.",
    trap: "Dizer 'no seu lugar' (arrogante) ou 'quero abrir minha própria empresa' (mostra que vai sair rápido).",
    formula: "Domínio Operacional Imediato → Aprofundamento Técnico / Especialização (GRC/SOC) → Liderança Técnica e Mentoria de Novos Membros.",
    answer_en: `Over the next 3 to 5 years, my goal is to evolve from a dependable operational contributor into a specialized subject-matter expert within your security and engineering organization.

In the first year or two, my focus is on mastering your environment, eliminating operational bottlenecks, and earning key industry credentials, such as my CompTIA Security+ and expanding into cloud and systems security. 

As I progress into my Master of Science in Computer Science with a focus on networks and security, I see myself taking on more complex threat analysis, architectural risk assessments, and mentoring junior engineers. Ultimately, I want to be recognized as an indispensable, reliable anchor for the team who bridges technical defense with operational integrity.`,
    guide_pt: `Três fases de evolução claras:
1. Ano 1: Dominar os sistemas da empresa, zerar gargalos de suporte/alerta e entregar valor rápido.
2. Anos 2-3: Concluir certificações avançadas e avançar no Mestrado em Ciência da Computação (CU Boulder).
3. Anos 4-5: Tornar-se referência técnica sênior em mitigação de riscos, análise de incidentes e mentoria de novos colegas.`
  },
  {
    id: "comp-09",
    cat: "behavioral",
    catName: "🗣️ Comportamental & RH",
    difficulty: "Entrada / Diferencial",
    source: "Simply Cyber (Gerald Auger)",
    title_en: "How do you stay current with the rapidly evolving cybersecurity threat landscape?",
    title_pt: "Como você se mantém atualizado sobre as ameaças e tendências em constante mudança em segurança?",
    intent: "Separar quem estuda só por obrigação de quem tem paixão pelo ofício e mentalidade de aprendizado contínuo (vital em segurança).",
    trap: "Dizer apenas 'leio notícias na internet' sem citar fontes específicas ou comunidades concretas.",
    formula: "Rotina de Fontes Múltiplas: Podcasts diários + Portais de notícias técnicas + Feeds de vulnerabilidades (CVE/CISA) + Prática em laboratório.",
    answer_en: `Staying informed is part of my daily routine, not an occasional task. 

Every morning, I review curated cybersecurity news from sources like BleepingComputer, The Hacker News, and CISA's Known Exploited Vulnerabilities catalog. 

I also follow industry podcasts and research channels, such as Dr. Gerald Auger's Simply Cyber, Darknet Diaries, and Professor Messer for foundational standards. 

Beyond passive reading, I actively test concepts in my home lab using virtualized Linux environments, analyzing log outputs, and reviewing MITRE ATT&CK framework techniques to see how theoretical threats translate into actual endpoint telemetry.`,
    guide_pt: `Cite suas fontes habituais:
- Notícias: BleepingComputer, The Hacker News, catálogo CISA de vulnerabilidades exploradas.
- Comunidade & Podcasts: Simply Cyber, Darknet Diaries, Professor Messer.
- Prática: Testar na prática no laboratório em casa e consultar o mapeamento do MITRE ATT&CK.`
  },

  /* ==========================================================================
     CATEGORIA 2: REDES & PROTOCOLOS (Josh Madakor, NetworkChuck & David Bombal)
     ========================================================================== */
  {
    id: "net-01",
    cat: "networking",
    catName: "🌐 Redes & Protocolos",
    difficulty: "Entrada / Conceitual",
    source: "NetworkChuck & Josh Madakor",
    title_en: "What is the difference between TCP and UDP? Give real-world examples of when each is used.",
    title_pt: "Qual é a diferença entre TCP e UDP? Dê exemplos práticos de onde cada um é utilizado.",
    intent: "Avaliar o domínio básico da Camada de Transporte (Camada 4 do modelo OSI) e o entendimento de confiabilidade versus desempenho.",
    trap: "Esquecer de mencionar o aperto de mão de três vias (3-way handshake) ou não saber explicar por que streaming/DNS usam UDP.",
    formula: "TCP (Conexão garantida, verificação de erro, ordenação) vs UDP (Sem conexão, baixa latência, sem retransmissão) + Casos de Uso.",
    answer_en: `TCP (Transmission Control Protocol) is a connection-oriented protocol that guarantees delivery and packet ordering. Before transmitting data, it establishes a session using a 3-way handshake (SYN, SYN-ACK, ACK). It tracks sequence numbers and retransmits any lost packets. Because of this reliability, TCP is used where data integrity is critical, such as web browsing (HTTP/HTTPS), secure shell (SSH), and file transfers.

In contrast, UDP (User Datagram Protocol) is connectionless and does not guarantee delivery, order, or error recovery. It simply sends packets with minimal overhead, making it significantly faster and ideal for time-sensitive traffic where occasional packet loss is acceptable, such as live video streaming, VoIP calls, online gaming, and lightweight queries like DNS.`,
    guide_pt: `Pontos que não podem faltar:
- TCP: Orientado à conexão, confiável, faz o 3-way handshake, retransmite pacotes perdidos. Exemplos: HTTPS (443), SSH (22), transferências de arquivos.
- UDP: Sem conexão (connectionless), envia direto sem confirmação, cabeçalho leve e baixíssima latência. Exemplos: Chamadas de voz/vídeo, streaming ao vivo, consultas DNS (53), DHCP.`
  },
  {
    id: "net-02",
    cat: "networking",
    catName: "🌐 Redes & Protocolos",
    difficulty: "Intermediário / Padrão-Ouro",
    source: "Day Cyberwox & Josh Madakor",
    title_en: "Walk me through what happens under the hood when you type 'google.com' into your browser and press Enter.",
    title_pt: "Explique o que acontece por baixo dos panos quando você digita 'google.com' no navegador e pressiona Enter.",
    intent: "A clássica pergunta que revela a profundidade de ponta a ponta do candidato em resolução de nomes, transporte, criptografia e aplicação.",
    trap: "Pular o DNS ou o aperto de mão TLS, ou apenas dizer 'a página carrega na tela'.",
    formula: "Passo a Passo em 5 Camadas: 1. Resolução DNS → 2. Handshake TCP (Porta 443) → 3. Handshake TLS (Criptografia) → 4. Requisição HTTP GET → 5. Resposta HTTP 200 e Renderização no Navegador.",
    answer_en: `When you type 'google.com' and press Enter:

1. DNS Resolution: The browser checks its local cache, OS cache, and hosts file. If not found, it queries the local recursive DNS resolver, which traverses Root, TLD (.com), and Authoritative nameservers to resolve the domain name into an IP address.

2. TCP Handshake: With the IP resolved, the client initiates a TCP 3-way handshake on port 443 with the web server: SYN from client, SYN-ACK from server, and ACK back from client.

3. TLS Handshake: To secure the session, a TLS negotiation takes place. The client and server agree on cryptographic cipher suites, verify the server's X.509 SSL/TLS certificate, and securely generate symmetric session keys using asymmetric key exchange (like Diffie-Hellman/ECDHE).

4. HTTP Request & Response: Over the encrypted tunnel, the browser sends an HTTP GET request. The web server processes the request and returns an HTTP 200 OK along with the HTML payload.

5. Rendering: The browser's rendering engine parses the HTML, constructs the DOM tree, requests linked CSS and JavaScript assets, and renders the visual page.`,
    guide_pt: `Explique a esteira de eventos com precisão:
1. DNS: Navegador checa cache local/SO e, se não tiver, busca no resolvedor DNS até obter o endereço IP.
2. TCP: Realiza o 3-way handshake (SYN, SYN-ACK, ACK) na porta 443.
3. TLS: Valida o certificado digital da Google e gera as chaves de sessão criptografadas.
4. HTTP: Envia um 'GET /' criptografado e recebe a resposta HTTP 200 OK com o código da página.
5. Renderização: Navegador processa o DOM, carrega CSS/JS e exibe na tela.`
  },
  {
    id: "net-03",
    cat: "networking",
    catName: "🌐 Redes & Protocolos",
    difficulty: "Intermediário / Segurança",
    source: "Professor Messer (CompTIA Security+) & NetworkChuck",
    title_en: "Explain the TCP 3-way handshake and how an attacker abuses it in a SYN Flood attack.",
    title_pt: "Explique o aperto de mão de três vias do TCP (3-way handshake) e como um invasor abusa dele em um ataque de SYN Flood.",
    intent: "Testar o conhecimento fundamental de redes conectado diretamente a táticas defensivas de segurança da informação (DDoS).",
    trap: "Confundir as bandeiras (flags) do TCP ou não saber como mitigar um SYN Flood.",
    formula: "Mecânica Normal (SYN → SYN-ACK → ACK) → Abuso do SYN Flood (envio massivo de SYN com IPs forjados sem enviar o ACK final) → Defesas (SYN Cookies, Firewalls, Rate Limiting).",
    answer_en: `The TCP 3-way handshake establishes a reliable session between client and server:
1. SYN: The client sends a synchronize packet with an initial sequence number.
2. SYN-ACK: The server acknowledges the request and sends back its own sequence number, allocating memory in its connection backlog table.
3. ACK: The client sends back an acknowledgment. The session is now ESTABLISHED, and data transfer begins.

In a SYN Flood attack, a malicious actor exploits this stateful design. The attacker transmits thousands of spoofed SYN packets per second without ever returning the final ACK. 

As a result, the server's connection queue fills up waiting for half-open connections to time out. Legitimate users are denied access because all connection slots and server resources are exhausted.

We defend against this using SYN Cookies (which avoid allocating server memory until the final ACK arrives), implementing firewall rate limiting, and deploying DDoS mitigation reverse proxies.`,
    guide_pt: `Conceitos essenciais:
- Handshake normal: Cliente envia SYN, Servidor responde SYN-ACK e aloca memória, Cliente confirma com ACK.
- Ataque SYN Flood: Atacante inunda o servidor com requisições SYN com IPs falsificados e nunca responde o ACK final. O servidor fica com a fila de conexões semiabertas (half-open) lotada até travar.
- Mitigação: SYN Cookies (não aloca recursos até receber o ACK válido), limites de taxa (rate limiting) e proxies de proteção DDoS.`
  },
  {
    id: "net-04",
    cat: "networking",
    catName: "🌐 Redes & Protocolos",
    difficulty: "Entrada / Conceitual",
    source: "NetworkChuck & David Bombal",
    title_en: "What is the difference between a Public IP, Private IP (RFC 1918), and how does NAT work?",
    title_pt: "Qual é a diferença entre IP Público, IP Privado (RFC 1918) e como funciona o NAT?",
    intent: "Garantir que o candidato compreende o endereçamento IPv4, segurança de perímetro e como dispositivos em redes internas acessam a internet.",
    trap: "Não lembrar das faixas RFC 1918 (10.x, 172.16-31.x, 192.168.x) ou não saber a diferença entre NAT e PAT.",
    formula: "Definição de IP Público (roteável globalmente) vs IP Privado (não roteável na internet) + Faixas RFC 1918 + Papel do NAT/PAT na conservação de IPs e segurança básica.",
    answer_en: `Public IP addresses are globally unique and routable across the public internet, assigned and regulated by IANA and regional internet registries.

Private IP addresses are defined under RFC 1918 for internal local area networks. They cannot be routed directly across the public internet. The standard private blocks are:
- 10.0.0.0 to 10.255.255.255 (Class A)
- 172.16.0.0 to 172.31.255.255 (Class B)
- 192.168.0.0 to 192.168.255.255 (Class C)

NAT (Network Address Translation)—specifically Port Address Translation (PAT)—enables thousands of internal devices with private IPs to share a single public IP address when accessing the internet. The router translates internal IP/source port pairs into its public IP with unique outbound ports, tracking the mapping in a translation table. This conserved IPv4 addresses and provides basic inbound isolation.`,
    guide_pt: `Resumo técnico:
- IP Público: Único no mundo, roteado pela internet (ex: servidores web, seu roteador externo).
- IP Privado (RFC 1918): Uso interno, não navega na internet aberta sem tradução. Faixas: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16.
- NAT / PAT: Traduz múltiplos IPs privados internos para um único IP público na saída usando portas diferentes, permitindo navegação e escondendo a topologia interna.`
  },
  {
    id: "net-05",
    cat: "networking",
    catName: "🌐 Redes & Protocolos",
    difficulty: "Entrada / Pegadinha Técnica",
    source: "Josh Madakor & Professor Messer",
    title_en: "What port does the 'ping' command work over?",
    title_pt: "Em qual porta funciona o comando 'ping'?",
    intent: "Uma das perguntas pegadinha mais comuns em entrevistas de redes e cyber para testar se o candidato realmente compreende a pilha OSI ou se apenas memorizou números de portas.",
    trap: "Tentar chutar um número de porta (ex: porta 7, 21 ou 80).",
    formula: "Resposta Imediata Direta: Ping não usa portas TCP ou UDP → Opera na Camada 3 (Rede) usando o protocolo ICMP → Detalhar tipos 8 e 0.",
    answer_en: `That is a classic interview question! Ping does not use any TCP or UDP ports at all.

Ports exist at Layer 4 (the Transport Layer). Ping operates at Layer 3 (the Network Layer) using the Internet Control Message Protocol (ICMP).

Specifically, ping transmits an ICMP Type 8 (Echo Request) packet, and the destination host responds with an ICMP Type 0 (Echo Reply). Because it doesn't involve Layer 4 transport ports, you cannot test a specific TCP port using ping alone; for port testing, tools like curl, netcat, or telnet are used instead.`,
    guide_pt: `Resposta certeira que impressiona:
- 'O ping não usa nenhuma porta TCP ou UDP!'
- Portas só existem na Camada 4 (Transporte). O ping trabalha na Camada 3 (Rede) usando o protocolo ICMP.
- Ele envia um pacote ICMP Tipo 8 (Echo Request) e espera um Tipo 0 (Echo Reply).
- Para testar se uma porta TCP específica está aberta, usamos ferramentas como nc (netcat), telnet ou curl.`
  },
  {
    id: "net-06",
    cat: "networking",
    catName: "🌐 Redes & Protocolos",
    difficulty: "Intermediário / Criptografia",
    source: "Professor Messer (CompTIA Security+) & Simply Cyber",
    title_en: "Explain the difference between HTTP and HTTPS, and how SSL/TLS achieves both confidentiality and performance.",
    title_pt: "Explique a diferença entre HTTP e HTTPS e como o SSL/TLS atinge confidencialidade e alto desempenho.",
    intent: "Avaliar se o candidato entende criptografia híbrida: por que usamos criptografia assimétrica para troca de chaves e simétrica para os dados.",
    trap: "Dizer que o HTTPS usa apenas chave pública/privada para criptografar todo o tráfego (o que causaria lentidão extrema na CPU).",
    formula: "HTTP (Texto puro, porta 80) vs HTTPS (Criptografado com TLS, porta 443) → Criptografia Híbrida: Assimétrica (Handshake) + Simétrica (Payload).",
    answer_en: `HTTP communicates in cleartext over port 80, meaning anyone on the network path can sniff credentials or alter data using Man-in-the-Middle attacks. 

HTTPS runs over port 443 and encrypts data in transit using TLS (Transport Layer Security).

To achieve both high security and high performance, TLS uses a hybrid cryptographic model:
1. Authentication & Key Exchange (Asymmetric): During the TLS handshake, the server presents its public certificate to prove its identity. Asymmetric cryptography (such as RSA or ECDHE) is used exclusively to securely negotiate a shared secret key without exposing it across the wire.
2. Data Transmission (Symmetric): Once the shared session key is agreed upon, the connection switches entirely to symmetric encryption (such as AES-GCM or ChaCha20). Symmetric encryption is computationally lightweight and hardware-accelerated, allowing full-speed data streaming while maintaining strict confidentiality and integrity.`,
    guide_pt: `Pontos chave da resposta:
- HTTP opera em texto claro na porta 80 (vulnerável a interceptação/sniffing).
- HTTPS opera na porta 443 com túnel TLS seguro.
- Modelo Híbrido:
  1. Criptografia Assimétrica (chave pública/privada): Usada apenas no início para autenticar o servidor e combinar uma chave de sessão secreta.
  2. Criptografia Simétrica (AES): Usada para criptografar todo o restante da navegação, pois é extremamente rápida e consome pouco processador.`
  },

  /* ==========================================================================
     CATEGORIA 3: LINUX & SUPORTE TÉCNICO (SysAdmin & Support Mock Interviews)
     ========================================================================== */
  {
    id: "lin-01",
    cat: "linux",
    catName: "🐧 Linux & Suporte Técnico",
    difficulty: "Intermediário / Operacional",
    source: "Tutorialinux & Linux SysAdmin Interviews",
    title_en: "A critical service (like Nginx or a database) crashed and won't restart. Walk me through your troubleshooting steps.",
    title_pt: "Um serviço crítico (como Nginx ou banco de dados) caiu e não reinicia. Explique seu passo a passo de diagnóstico.",
    intent: "Avaliar o método investigativo no terminal Linux: você sai chutando comandos aleatórios ou segue uma linha lógica de inspeção de estado e logs?",
    trap: "Sugerir reiniciar o servidor inteiro de cara ('reboot') ou tentar reinstalar o pacote sem antes olhar os logs de erro.",
    formula: "Metodologia em 5 Passos: 1. Checar status (`systemctl status`) → 2. Inspecionar logs detalhados (`journalctl -u`) → 3. Validar sintaxe de arquivos de configuração → 4. Verificar conflito de portas e recursos (`df -h`, memória) → 5. Corrigir e testar.",
    answer_en: `I take a structured, non-destructive approach:

1. Check Service Status: First, run 'systemctl status <service>' to see whether it failed, the exit code, and the last few lines of log output.

2. Inspect Unit Logs: If the error isn't obvious, I dive into the systemd journal using:
   'journalctl -u <service> -n 50 --no-pager -e'
   This pulls the last 50 entries with full error descriptions.

3. Configuration Validation: Many service crashes occur due to syntax errors after an edit. For web servers like Nginx, I run 'nginx -t'; for databases, I inspect the config files in /etc.

4. Check Resource & Port Constraints:
   - Check if another process bound the port: 'ss -tulpn | grep :<port>'
   - Verify available disk space and inodes: 'df -h' and 'df -i' (a full disk prevents log writing and crashes services).
   - Check memory/OOM killer: 'dmesg -T | grep -i oom'.

5. Correct & Reload: Once the root cause is resolved, reload systemd daemon if unit files changed ('systemctl daemon-reload'), start the service ('systemctl start <service>'), and monitor live logs with 'journalctl -u <service> -f'.`,
    guide_pt: `Passo a passo profissional de quem manja de terminal:
1. 'systemctl status nome_do_servico' (ver o estado e o código de saída).
2. 'journalctl -u nome_do_servico -n 50 -e' (ver as últimas 50 linhas de log no systemd).
3. Testar a sintaxe da configuração (ex: 'nginx -t').
4. Checar recursos do sistema:
   - Porta já ocupada por outro processo: 'ss -tulpn | grep :80'
   - Disco cheio: 'df -h' e inodes 'df -i'
   - Falta de memória (OOM Killer): 'dmesg -T | grep -i oom'
5. Corrigir o problema e reiniciar com 'systemctl restart'.`
  },
  {
    id: "lin-02",
    cat: "linux",
    catName: "🐧 Linux & Suporte Técnico",
    difficulty: "Intermediário / Performance",
    source: "Linux SysAdmin & Cloud Support Mock Interviews",
    title_en: "A Linux server is reported as sluggish and unresponsive. How do you find the root bottleneck?",
    title_pt: "Um servidor Linux está lento e travando. Como você descobre a causa raiz do gargalo?",
    intent: "Verificar se o candidato sabe analisar os quatro pilares de recursos do hardware: CPU, Memória/Swap, I/O de Disco e Rede.",
    trap: "Apenas rodar `top` e não saber interpretar a métrica de Load Average em relação ao número de núcleos de CPU.",
    formula: "Triage dos 4 Pilares: CPU & Load Average (`uptime`, `top`) → Memória & Swap (`free -h`) → I/O de Disco (`iostat`, `vmstat`) → Tráfego de Rede/Conexões.",
    answer_en: `When troubleshooting a sluggish Linux system, I systematically assess the four key hardware subsystems:

1. CPU & Load Average: I run 'uptime' or 'top' to examine the load average across 1, 5, and 15 minutes. I compare this number to the CPU core count using 'nproc'. If the load average is significantly higher than the number of available cores, the system is bottlenecked.

2. Memory & Swap: I check 'free -h'. If free RAM is near zero and swap space is actively heavily utilized, the kernel is constantly swapping memory pages to disk, severely degrading performance.

3. Disk I/O Wait (%wa): In 'top', I inspect the '%wa' (I/O wait) metric. If CPU utilization is low but I/O wait is high, the disk is saturated. I use 'iostat -xz 1' to identify which physical block device is bottlenecked and 'iotop' to find the culprit process.

4. Kernel & OOM Activity: I review 'dmesg -T | tail -50' to verify whether the Out-Of-Memory (OOM) killer has terminated any processes or if there are hardware disk faults.`,
    guide_pt: `Diagnóstico em 4 frentes:
1. CPU e Load Average: Rodar 'uptime' ou 'top' e comparar o load average com o total de núcleos ('nproc'). Se load > núcleos, a fila de processamento está sobrecarregada.
2. Memória e Swap: Rodar 'free -h'. Se a memória RAM acabou e o swap está com uso alto, o sistema está sofrendo lentidão por paginação em disco.
3. Gargalo de Disco (I/O Wait): Olhar a coluna '%wa' no top. Se o wait estiver alto, o disco está travando a máquina. Identifique o processo com 'iotop' ou 'iostat -xz 1'.
4. Logs do Kernel: Rodar 'dmesg -T' para checar se o OOM Killer foi disparado para matar processos por falta de RAM.`
  },
  {
    id: "lin-03",
    cat: "linux",
    catName: "🐧 Linux & Suporte Técnico",
    difficulty: "Entrada / Segurança",
    source: "CompTIA Linux+ & Simply Cyber",
    title_en: "Explain Linux file permissions. What do 'chmod 755' and 'chmod 644' mean, and why is 'chmod 777' dangerous?",
    title_pt: "Explique as permissões de arquivos no Linux. O que significam 'chmod 755' e 'chmod 644', e por que 'chmod 777' é perigoso?",
    intent: "Avaliar o domínio do modelo de permissões POSIX no Linux e o entendimento do princípio do menor privilégio.",
    trap: "Não saber como somar os valores octais (4, 2, 1) ou justificar o uso de `chmod 777` como 'solução rápida para fazer funcionar'.",
    formula: "Tríade UGO (Usuário, Grupo, Outros) → Valores Octais (Leitura=4, Escrita=2, Execução=1) → Casos de 755 e 644 → Risco do 777.",
    answer_en: `Linux file permissions are divided into three tiers: User (owner), Group, and Others (world). Permissions are represented by octal values:
- Read (r) = 4
- Write (w) = 2
- Execute (x) = 1

- 'chmod 755' (rwxr-xr-x): The owner has full read, write, and execute permissions (4+2+1=7). The group and others can read and execute, but cannot modify the file (4+1=5). This is the standard security baseline for executables, scripts, and directories.
- 'chmod 644' (rw-r--r--): The owner has read and write (4+2=6). Group and others can only read (4). This is the standard baseline for normal configuration and content files.

'chmod 777' (rwxrwxrwx) gives EVERY user on the system full write, execute, and delete access. In a production environment, this is extremely dangerous because if any service or user account is compromised, the attacker can overwrite system files, inject malicious code, or delete critical data. It violates the Principle of Least Privilege.`,
    guide_pt: `Regra de ouro das permissões:
- Leitura (r) = 4, Escrita (w) = 2, Execução (x) = 1.
- chmod 755 (rwxr-xr-x): Dono faz tudo (7), Grupo e Outros só leem e executam (5). Usado para pastas e programas/scripts.
- chmod 644 (rw-r--r--): Dono lê e escreve (6), Grupo e Outros apenas leem (4). Padrão para arquivos de configuração e texto.
- chmod 777: Permissão total para qualquer um. NUNCA usar em produção — viola o princípio do menor privilégio e permite que um invasor injete código malicioso ou delete o arquivo.`
  },
  {
    id: "lin-04",
    cat: "linux",
    catName: "🐧 Linux & Suporte Técnico",
    difficulty: "Entrada / Comandos",
    source: "NetworkChuck & Linux SysAdmin Interviews",
    title_en: "How do you inspect open network ports, active connections, and listening sockets in modern Linux distributions?",
    title_pt: "Como você inspeciona portas abertas, conexões ativas e serviços escutando em distribuições Linux modernas?",
    intent: "Saber se o candidato está atualizado com as ferramentas modernas do pacote iproute2 (`ss`) em vez de ferramentas legadas obsoletas (`netstat`).",
    trap: "Citar apenas `netstat` sem saber que ele foi depreciado, ou não saber quais bandeiras usar para filtrar portas em escuta.",
    formula: "Ferramenta Moderna (`ss`) + Flags explicadas (`-tulpn`) + Alternativa para processos (`lsof -i`).",
    answer_en: `In modern Linux distributions, the standard tool is 'ss' (socket statistics) from the iproute2 package, which replaced the legacy 'netstat' command.

To view all listening ports along with their associated process IDs, I use:
'sudo ss -tulpn'
- '-t': Show TCP sockets
- '-u': Show UDP sockets
- '-l': Show only listening sockets
- '-p': Display the process name and PID
- '-n': Show numeric port numbers instead of attempting to resolve service names (which is much faster).

If I need to investigate a specific port, say port 443, I can pipe to grep or use 'lsof':
'sudo lsof -i :443'
This immediately reveals the exact process, user, and command line bound to that port.`,
    guide_pt: `Comandos essenciais:
- Comando moderno padrão: 'sudo ss -tulpn'
  - t = TCP
  - u = UDP
  - l = apenas portas em escuta (listening)
  - p = mostra o processo e o PID
  - n = numérico (mostra porta 80 em vez de tentar resolver 'http', muito mais rápido).
- Para investigar uma porta específica: 'sudo lsof -i :80' ou 'sudo ss -tulpn | grep :80'.`
  },
  {
    id: "lin-05",
    cat: "linux",
    catName: "🐧 Linux & Suporte Técnico",
    difficulty: "Intermediário / Investigação",
    source: "Linux SysAdmin & Forensic Mock Interviews",
    title_en: "How do you search for files modified in the last 24 hours that contain a specific malicious string or IP address?",
    title_pt: "Como você busca arquivos modificados nas últimas 24 horas que contenham uma string maliciosa ou IP específico?",
    intent: "Avaliar a habilidade do candidato de combinar ferramentas clássicas de Unix (`find` + `grep` / `xargs`) em uma investigação forense rápida.",
    trap: "Rodar `grep -r` na raiz `/` inteira sem limitar por tempo ou diretório (causa travamento de I/O na máquina ao ler dispositivos virtuais como `/proc`).",
    formula: "Comando Eficiente: `find` com `-mtime -1` + `-exec grep` filtrando em diretórios específicos (`/var/log`, `/etc`, `/var/www`).",
    answer_en: `To avoid severe performance penalties, I never run a blind recursive search from the root '/' directory, as that attempts to scan virtual filesystems like /proc and /sys.

Instead, I target the relevant directory (such as /var/www or /var/log) and combine 'find' with 'grep':

'find /var/www -type f -mtime -1 -exec grep -H "192.168.1.100" {} +'

Explanation:
- '-type f': Looks only for regular files.
- '-mtime -1': Filters files modified within the last 24 hours.
- '-exec grep -H ... {} +': Executes grep efficiently by batching multiple files at once, displaying the filename alongside any matching lines.

Alternatively, if searching purely through text logs:
'grep -rnw '/var/log' -e '192.168.1.100' --exclude-dir={proc,sys}'`,
    guide_pt: `Combinação profissional:
- Evite rodar busca cega na raiz '/' (trava o disco lendo /proc e /sys).
- Foque na pasta certa (ex: /var/log ou /var/www):
  'find /var/www -type f -mtime -1 -exec grep -H "IP_OU_STRING" {} +'
  - '-type f': apenas arquivos reais.
  - '-mtime -1': modificados nas últimas 24 horas.
  - '-exec grep -H ... {} +': busca rápida passando lotes de arquivos de uma vez.`
  },

  /* ==========================================================================
     CATEGORIA 4: CIBERSEGURANÇA & OPERAÇÕES DE SOC (Simply Cyber & Day Cyberwox)
     ========================================================================== */
  {
    id: "sec-01",
    cat: "soc",
    catName: "🛡️ Cibersegurança & SOC",
    difficulty: "Entrada / Fundamental",
    source: "Professor Messer (CompTIA Security+) & Simply Cyber",
    title_en: "Explain the CIA Triad and give a real-world enterprise example for each pillar.",
    title_pt: "Explique a Tríade CIA e dê um exemplo prático corporativo para cada um dos três pilares.",
    intent: "Confirmar que o candidato domina o conceito fundacional da segurança da informação e sabe relacioná-lo a controles técnicos concretos.",
    trap: "Apenas citar os nomes (Confidencialidade, Integridade, Disponibilidade) sem saber exemplificar controles para cada um.",
    formula: "Definição de Cada Pilar + Controle Técnico Concreto Aplicado no Mundo Real.",
    answer_en: `The CIA Triad is the foundational model of information security:

1. Confidentiality: Ensuring that sensitive information is accessible only to authorized entities and protected from unauthorized disclosure. 
   - Real-World Example: Enforcing Multi-Factor Authentication (MFA), Least Privilege access control via RBAC, and full-disk encryption (like BitLocker or LUKS) on employee laptops.

2. Integrity: Guaranteeing that data remains accurate, complete, and uncorrupted, protecting it from unauthorized modification or deletion.
   - Real-World Example: Using cryptographic hashing (such as SHA-256) to verify software download integrity, digital signatures in emails (S/MIME), and database transaction logging with audit trails.

3. Availability: Ensuring that authorized users have timely, uninterrupted access to systems, data, and critical services whenever needed.
   - Real-World Example: Deploying high-availability server clusters with redundant power and internet connections, automated multi-region database replication, automated off-site backups, and DDoS protection through Cloudflare.`,
    guide_pt: `Os 3 pilares com exemplos corporativos:
1. Confidencialidade: Somente quem tem autorização pode ver. Ex: MFA, criptografia de disco (BitLocker/LUKS) e controle de acesso baseado em função (RBAC).
2. Integridade: Os dados não foram alterados nem adulterados. Ex: Hashes SHA-256 para validar downloads, assinaturas digitais e logs de auditoria imutáveis.
3. Disponibilidade: Os sistemas e dados estão no ar quando o negócio precisa. Ex: Servidores redundantes, proteção anti-DDoS e backups testados.`
  },
  {
    id: "sec-02",
    cat: "soc",
    catName: "🛡️ Cibersegurança & SOC",
    difficulty: "Entrada / Conceitual",
    source: "Josh Madakor & Professor Messer",
    title_en: "What is the difference between Encoding, Encryption, and Hashing?",
    title_pt: "Qual é a diferença entre Codificação (Encoding), Criptografia (Encryption) e Hashing?",
    intent: "Outra pergunta clássica que pega candidatos desatentos. Avalia a compreensão da matemática de proteção de dados.",
    trap: "Dizer que você pode 'descriptografar um hash' (hash é unidirecional) ou confundir codificação Base64 com segurança/criptografia.",
    formula: "Tabela Mental Clara: Codificação (Reversível sem chave, só formato) vs Criptografia (Reversível com chave, confidencialidade) vs Hashing (Unidirecional, integridade).",
    answer_en: `These three mechanisms serve entirely different purposes:

1. Encoding: Transforms data into a different format for safe transmission or storage using publicly available schemes. It is NOT secure and does NOT use keys—anyone can instantly reverse it. 
   - Purpose: Usability and format compatibility.
   - Example: Base64, URL encoding, ASCII.

2. Encryption: Converts plaintext into ciphertext using a secret key and a cryptographic algorithm to ensure confidentiality. It is a two-way function, meaning it can be decrypted back to plaintext only by someone holding the appropriate key.
   - Purpose: Confidentiality.
   - Example: AES-256 (symmetric), RSA (asymmetric).

3. Hashing: A one-way mathematical function that converts arbitrary data into a unique, fixed-length string (a digest). It is mathematically irreversible—you cannot 'decrypt' a hash. Even a single character change in the input completely alters the output (the avalanche effect).
   - Purpose: Data integrity and secure password storage.
   - Example: SHA-256, bcrypt.`,
    guide_pt: `Diferença essencial:
- Codificação (Encoding): Apenas muda o formato para trafegar na rede (ex: Base64). NÃO é segurança — qualquer um reverte sem senha.
- Criptografia (Encryption): Protege confidencialidade. É de mão dupla: você cifra com uma chave e descriptografa de volta com a chave correta (ex: AES, RSA).
- Hashing: É de mão ÚNICA. Não existe 'descriptografar hash'. Gera uma impressão digital fixa dos dados para garantir integridade ou guardar senhas (ex: SHA-256, bcrypt).`
  },
  {
    id: "sec-03",
    cat: "soc",
    catName: "🛡️ Cibersegurança & SOC",
    difficulty: "Intermediário / Resposta a Incidentes",
    source: "Simply Cyber & Day Cyberwox",
    title_en: "A user clicked a suspicious link in an email and reports unexpected popups and sluggishness. What are your immediate incident response steps?",
    title_pt: "Um usuário clicou em um link suspeito no e-mail e relata pop-ups estranhos e lentidão. Quais são seus passos imediatos de resposta ao incidente?",
    intent: "Verificar se você conhece o ciclo de resposta a incidentes do NIST/SANS e se sabe agir com rapidez sem destruir evidências forenses voláteis.",
    trap: "Mandar o usuário desligar a máquina da tomada imediatamente (destrói a memória RAM e evidências voláteis) ou formatar o computador antes de investigar.",
    formula: "Ciclo NIST/SANS: 1. Contenção Imediata (Isolar da rede, manter ligado) → 2. Triagem e Coleta de Evidências Voláteis (RAM, conexões) → 3. Erradicação → 4. Recuperação → 5. Lições Aprendidas.",
    answer_en: `I follow the structured NIST Incident Response lifecycle:

1. Immediate Containment (Isolate without powering down):
   The first priority is to stop lateral movement. I immediately isolate the endpoint from the network by unplugging the Ethernet cable and disabling Wi-Fi (or issuing an EDR network isolation command). I explicitly instruct the user NOT to reboot or shut down the computer, preserving volatile evidence residing in RAM.

2. Triage & Identification:
   I pull active process lists, network socket telemetry, and scheduled tasks. I inspect the phishing email headers, determine the destination URL/payload, and check our SIEM/EDR to identify if other internal hosts received or opened the same link.

3. Evidence Collection:
   If deemed a severe compromise, I capture volatile memory (RAM dump) and pull system logs for forensic analysis while documenting the strict chain of custody.

4. Eradication & Remediation:
   I terminate malicious processes, remove persistence keys in registry/cron, reset the user's domain credentials, revoke active SSO/OAuth session tokens, and blacklist the malicious domain/IP at the perimeter firewall and email gateway.

5. Recovery & Lessons Learned:
   Restore the endpoint from a clean golden image if necessary, confirm normal operations, and conduct a post-incident review to improve email filtering rules and employee awareness training.`,
    guide_pt: `Procedimento profissional do SOC:
1. Contenção Imediata: Desconectar o cabo de rede e desativar o Wi-Fi (ou isolar pelo EDR). NUNCA desligar a máquina para não perder a memória RAM (evidência volátil).
2. Triagem: Checar processos suspeitos, conexões abertas e analisar o e-mail de phishing no cabeçalho.
3. Erradicação: Matar processos maliciosos, resetar a senha do usuário e revogar sessões ativas/tokens de acesso.
4. Bloqueio no Perímetro: Bloquear a URL/IP malicioso no firewall e no filtro de e-mail corporativo.
5. Lições Aprendidas: Atualizar regras de detecção no SIEM para alertar proativamente.`
  },
  {
    id: "sec-04",
    cat: "soc",
    catName: "🛡️ Cibersegurança & SOC",
    difficulty: "Entrada / Risco e Governança",
    source: "Professor Messer & Simply Cyber",
    title_en: "What is the difference between a Vulnerability, a Threat, and a Risk?",
    title_pt: "Qual é a diferença entre Vulnerabilidade, Ameaça e Risco?",
    intent: "Testar o entendimento de vocabulário de Governança, Risco e Conformidade (GRC). Essas três palavras são frequentemente confundidas por iniciantes.",
    trap: "Usar 'ameaça' e 'vulnerabilidade' como sinônimos.",
    formula: "Fórmula de Risco: Risco = Ameaça × Vulnerabilidade × Impacto. Defina cada um separadamente com uma analogia simples.",
    answer_en: `While often used interchangeably by laypeople, in cybersecurity these three terms have very specific definitions:

1. Vulnerability: A weakness or flaw in a system's design, code, configuration, or human process that could be exploited.
   - Example: An unpatched Apache server running software with a known Remote Code Execution flaw.

2. Threat: Any actor, circumstance, or event with the potential to adversely impact an asset by exploiting a vulnerability.
   - Example: A ransomware cybercrime syndicate or a disgruntled insider.

3. Risk: The potential for loss or damage when a threat exercises a vulnerability, evaluated by the likelihood of occurrence multiplied by the resulting business impact.
   - Formula: Risk = Threat × Vulnerability × Impact.
   - Example: If an unpatched server holds non-sensitive test data and has no internet access, the vulnerability exists, but the overall business risk is low. If that same server holds the company's financial database exposed to the web, the risk is critical.`,
    guide_pt: `A fórmula mágica de GRC:
- Vulnerabilidade: A falha ou fraqueza no sistema (ex: um software desatualizado ou uma porta aberta).
- Ameaça: Quem ou o que pode explorar essa falha (ex: grupo criminoso de ransomware, hacker, malware).
- Risco: O impacto real e a probabilidade de o evento acontecer:
  Risco = Ameaça × Vulnerabilidade × Impacto.
  Se você tem uma falha em um computador isolado sem internet, a vulnerabilidade existe, mas o risco para o negócio é baixo. Se a falha está no banco de dados de clientes, o risco é altíssimo.`
  },
  {
    id: "sec-05",
    cat: "soc",
    catName: "🛡️ Cibersegurança & SOC",
    difficulty: "Intermediário / Triagem SOC",
    source: "Day Cyberwox & Simply Cyber",
    title_en: "An alert fires in your SIEM indicating potential brute-force activity on an internal workstation. How do you triage this?",
    title_pt: "Um alerta dispara no seu SIEM indicando potencial atividade de força bruta em uma estação interna. Como você faz a triagem?",
    intent: "Avaliar a capacidade prática de triagem de alertas de segurança: investigar se é falso positivo ou ataque real e determinar os próximos passos.",
    trap: "Apenas bloquear o usuário imediatamente sem checar se é um script interno automatizado ou esquecer de verificar se algum login teve sucesso.",
    formula: "Metodologia de Triagem: 1. Identificar Origem e Destino → 2. Analisar Códigos de Evento (Falhas vs Sucessos) → 3. Diferenciar Usuário Real de Serviço → 4. Ação Baseada em Fatos.",
    answer_en: `I approach SIEM triage systematically:

1. Verify Source and Destination:
   I inspect the source IP address. Is it originating from an external IP, a DMZ host, or an internal workstation? If internal, an already compromised host might be attempting lateral movement.

2. Analyze Event Telemetry:
   In Windows environments, I look at event IDs:
   - Event 4625: An account failed to log on.
   - Event 4624: An account successfully logged on.
   The critical check is determining whether there is an Event 4624 immediately following a high volume of 4625s from the same source. If yes, the brute force succeeded and an active breach is underway.

3. Check for Benign False Positives:
   Often, thousands of failed logins occur because an employee changed their domain password, but a mapped network drive, mobile device with cached credentials, or automated scheduled task is still trying to authenticate with the old password.

4. Action Plan:
   If malicious, I isolate the source host, enforce a password reset, revoke active tokens, and escalate to Tier 2. If it is a misconfigured service account, I notify the sysadmin team with the exact offending process to remediate the loop.`,
    guide_pt: `Passo a passo no SIEM:
1. Checar o IP de origem: O ataque vem de fora da empresa ou de outra máquina interna (tentativa de movimento lateral)?
2. Checar os eventos no Windows:
   - Event ID 4625: Falha de logon.
   - Event ID 4624: Sucesso de logon.
   A pergunta de ouro: Houve um 4624 (sucesso) depois de centenas de falhas? Se sim, o invasor descobriu a senha!
3. Descartar falso positivo: O usuário trocou a senha recentemente e deixou um script antigo rodando com a senha velha?
4. Decisão: Se for ataque, isolar o IP/host e resetar credenciais. Se for script interno, avisar a equipe de infraestrutura.`
  },
  {
    id: "sec-06",
    cat: "soc",
    catName: "🛡️ Cibersegurança & SOC",
    difficulty: "Intermediário / Arquitetura",
    source: "Professor Messer & Simply Cyber",
    title_en: "What is Defense-in-Depth and how does Zero Trust change traditional network security?",
    title_pt: "O que é Defesa em Profundidade e como o modelo Zero Trust transforma a segurança tradicional de redes?",
    intent: "Avaliar se o candidato entende os paradigmas modernos de segurança: sair do modelo de castelo medieval para verificação contínua.",
    trap: "Achar que Zero Trust significa 'não confiar em nenhum funcionário' em vez de entender que se trata de verificação contínua de identidade e dispositivo.",
    formula: "Defesa em Profundidade (Múltiplas camadas de controle) + Zero Trust ('Nunca confie, sempre verifique' / Suposição de invasão).",
    answer_en: `Defense-in-Depth is a layered security strategy where multiple independent controls are deployed throughout an organization so that if one layer fails, subsequent layers prevent a total compromise. This includes physical security, perimeter firewalls, network segmentation, endpoint EDR, least privilege access, encryption, and employee training.

Historically, networks relied on a 'Castle-and-Moat' perimeter model: once inside the firewall or VPN, an entity was largely trusted.

Zero Trust fundamentally transforms this model with the core philosophy: 'Never Trust, Always Verify' and 'Assume Breach'. In a Zero Trust architecture:
1. Perimeter location is irrelevant: whether a user connects from inside the office or a coffee shop, every request is authenticated, authorized, and encrypted.
2. Least Privilege & Microsegmentation: access is granted only to specific applications, not the entire subnet.
3. Continuous Verification: context such as device health, geolocation, and user behavior is evaluated continuously before granting access.`,
    guide_pt: `Pontos essenciais da explicação:
- Defesa em Profundidade: Camadas de proteção (firewall, antivírus/EDR, autenticação, treinamento). Se uma falhar, a próxima segura o invasor.
- Modelo tradicional 'Castelo e Fosso': Quem entrava na rede interna (ou na VPN) tinha acesso a quase tudo.
- Zero Trust ('Nunca confie, sempre verifique'):
  1. Supõe que a rede já está comprometida.
  2. Não importa se você está dentro do prédio ou no Wi-Fi de casa: toda requisição precisa de validação de identidade e dispositivo.
  3. Microsegmentação: O usuário só acessa o sistema específico que precisa para trabalhar, nunca a rede inteira.`
  },

  /* ==========================================================================
     CATEGORIA 5: PERGUNTAS DE ALTO IMPACTO PARA FAZER AO ENTREVISTADOR
     (Reverse Interviewing — Mostra maturidade técnica e interesse genuíno)
     ========================================================================== */
  {
    id: "rev-01",
    cat: "reverse",
    catName: "💼 Perguntas Finais para o Entrevistador",
    difficulty: "Estratégica / Diferencial",
    source: "CareerVidz (Richard McMunn) & Gerald Auger",
    title_en: "What does success look like in this role in the first 90 days?",
    title_pt: "Como é o sucesso esperado para este cargo nos primeiros 90 dias?",
    intent: "Demonstrar foco imediato em entrega de resultados, humildade para aprender e alinhamento com as expectativas reais do gestor.",
    trap: "Dizer 'não tenho nenhuma pergunta' quando o entrevistador perguntar 'você tem alguma dúvida para nós?'. Isso elimina candidatos.",
    formula: "Pergunta de Foco em Resultados: 'Quais marcos específicos você gostaria que eu tivesse atingido nos meus primeiros 3 meses?'",
    answer_en: `I would love to understand what success looks like from your perspective: What specific outcomes or milestones would you want to see me accomplish in my first 90 days to know that you hired the right person for this role?`,
    guide_pt: `Por que fazer esta pergunta:
- Mostra que você está pensando em como resolver o problema da empresa desde o primeiro dia.
- Força o gestor a imaginar você já trabalhando e tendo sucesso no cargo.
- Dá a você as metas exatas que eles vão cobrar na sua avaliação de experiência.`
  },
  {
    id: "rev-02",
    cat: "reverse",
    catName: "💼 Perguntas Finais para o Entrevistador",
    difficulty: "Estratégica / Cultura",
    source: "Simply Cyber (Gerald Auger)",
    title_en: "How does the team handle post-incident reviews or post-mortems when an unexpected outage or security event occurs?",
    title_pt: "Como a equipe conduz as revisões pós-incidente (post-mortems) quando ocorre uma falha ou incidente inesperado?",
    intent: "Avaliar se a empresa tem uma cultura saudável de engenharia ('blameless post-mortem') ou se busca bodes expiatórios para culpar.",
    trap: "Parecer acusatório. O tom deve ser de curiosidade e respeito pela melhoria contínua de processos.",
    formula: "Pergunta de Maturidade Operacional: Foco no aprendizado com falhas e refinamento de controles.",
    answer_en: `When an incident or outage occurs, how does the team typically conduct post-incident reviews? Do you follow a blameless post-mortem approach, and how do lessons learned feed back into updating documentation and detection rules?`,
    guide_pt: `Por que fazer esta pergunta:
- Revela se a equipe tem maturidade técnica (cultura sem caça às bruxas) e se aprende com erros.
- Equipes de ponta adoram candidatos que se importam com a melhoria contínua de procedimentos operacionais.`
  },
  {
    id: "rev-03",
    cat: "reverse",
    catName: "💼 Perguntas Finais para o Entrevistador",
    difficulty: "Estratégica / Técnica",
    source: "CareerVidz & Josh Madakor",
    title_en: "What is the biggest technical or operational challenge the team is currently trying to solve?",
    title_pt: "Qual é o maior desafio técnico ou operacional que a equipe está tentando resolver no momento?",
    intent: "Demonstrar entusiasmo por desafios reais e entender onde você poderá ser mais útil imediatamente.",
    trap: "Não prestar atenção na resposta do gestor para fechar seu argumento final de contratação.",
    formula: "Pergunta de Diagnóstico de Dores: Descobrir onde o sapato aperta na equipe.",
    answer_en: `What would you say is the biggest technical bottleneck or operational challenge that your team is currently working to resolve over the next couple of quarters?`,
    guide_pt: `Por que fazer esta pergunta:
- O gestor vai te contar exatamente qual é a dor de cabeça dele (ex: falta de documentação, muitos alertas falsos positivos no SIEM, tickets acumulados).
- Você pode usar isso na sua fala de encerramento para mostrar como sua dedicação vai aliviar essa dor.`
  },
  {
    id: "rev-04",
    cat: "reverse",
    catName: "💼 Perguntas Finais para o Entrevistador",
    difficulty: "Estratégica / Retenção",
    source: "CareerVidz (Richard McMunn)",
    title_en: "What opportunities exist for ongoing training, certifications, and internal growth within the team?",
    title_pt: "Quais oportunidades existem para treinamento contínuo, certificações e crescimento interno na equipe?",
    intent: "Demonstrar compromisso de longo prazo e vontade de crescer tecnicamente sem soar como exigência arrogante.",
    trap: "Perguntar sobre aumentos salariais ou folgas na primeira entrevista técnica.",
    formula: "Pergunta de Crescimento Mútuo: 'Como a empresa incentiva o aprimoramento técnico contínuo?'",
    answer_en: `Continuous learning is very important to me, especially as I work through my industry certifications and prepare for my Master's studies. How does the company support professional development, conference attendance, or advanced certifications as employees grow within the team?`,
    guide_pt: `Por que fazer esta pergunta:
- Mostra que você é um profissional focado em evolução constante.
- As melhores empresas (como Canonical, GitLab, etc.) oferecem orçamento anual para cursos, exames de certificação e conferências.`
  }
];

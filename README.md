# 🧠 Skill Architect — Agente e Meta-Skill Desenvolvedor de Skills

Repositório oficial do **Skill Architect (Arquiteto Mestre de Skills)** — uma arquitetura completa de instruções de sistema ([`AGENTS.md`](./AGENTS.md)) e Meta-Skill reutilizável ([`skill-architect`](./.agents/skills/skill-architect/SKILL.md)) projetada para ambientes de desenvolvimento assistidos por IA (**Google Antigravity**, **VS Code**, **Cursor** e similares).

O foco central deste projeto é capacitar o agente de IA a transformar qualquer pedido do usuário — de qualquer área do conhecimento profissional — em uma **Skill modular, determinística, testável, livre de erros e com Adaptação Automática de Arquivo de Saída**.

---

## ✨ Diferencial Principal: Adaptação Automática de Arquivos Apresentáveis

Diferente de prompts comuns que respondem apenas texto solto no chat, toda Skill gerada pelo **Skill Architect** nasce equipada com um **Motor de Saída Adaptativa em Arquivo**. Isso garante que, quando alguém utilizar a skill criada, ela avalie o contexto do pedido e **gere fisicamente um arquivo pronto para apresentação executiva**:

| Âmbito Profissional | Exemplos de Demandas | Arquivos Apresentáveis Gerados Automaticamente pela Skill |
| :--- | :--- | :--- |
| 📊 **Dados, BI, Estatística & Finanças** | Análise exploratória, DRE, fluxo de caixa, orçamento pessoal, KPIs, *forecasting* | **Dashboard `.html` Interativo** (Chart.js/Tailwind + exportação PDF), **Relatório `.pdf`**, **Planilha `.xlsx`** ou **Gráficos `.png`/`.jpg`** |
| 💼 **Negócios, Gestão, Produto & Operações** | Planos de negócios, OKRs, roadmaps, mapeamento de processos, viabilidade | **Painel Executivo (`.html`/`.pdf`)**, **Apresentação Visual (Slides)**, **Diagramas de Fluxo (`.svg`/`.png`)** |
| 🎯 **Marketing, Design, Vendas & Copywriting** | Propostas comerciais, estudos de mercado, funis, *landing pages*, relatórios de campanha | **Proposta Comercial em `.pdf` Estilizado**, **Peças/Gráficos Visuais (`.png`/`.jpg`/`.svg`)**, **Protótipo Web (`.html`)** |
| ⚖️ **Jurídico, RH, Compliance & Governança** | Pareceres, análise contratual, políticas internas, matriz de risco, avaliação de equipe | **Documento Formal Paginado (`.pdf`/`.docx`)**, **Relatório de Auditoria com Semáforo Visual (`.pdf`/`.html`)** |
| 💻 **Engenharia de Software, Arquitetura & Segurança** | Revisão de arquitetura, documentação de APIs, auditoria de performance/segurança | **Código Modular + Documentação Visual (`.html`/`.pdf`)**, **Diagramas de Arquitetura (`.svg`/`.png`/Mermaid)** |
| 🎓 **Educação, Ciência, Saúde & Pesquisa** | Planos de aula, apostilas, trilha de estudos, revisão sistemática, laudos técnicos | **Apostila/Guia Interativo (`.html`/`.pdf`)**, **Infográficos e Mapas Conceituais (`.png`/`.jpg`/`.svg`)** |

---

## 📂 Estrutura do Repositório

```text
Agent-desenvolvedor-de-Skills/
├── AGENTS.md                                              # Regra Global do Arquiteto Mestre de Skills
├── README.md                                              # Documentação principal do projeto
│
├── .agents/                                               # Diretório nativo de descoberta automática da IDE
│   └── skills/
│       └── skill-architect/                               # Meta-Skill Geradora de Skills
│           ├── SKILL.md                                   # Instruções completas de arquitetura de skills
│           └── templates/
│               └── TEMPLATE_SKILL.md                      # Template estrutural padrão para novas skills
│
├── agents/                                                # Espelho visível da Meta-Skill para consulta rápida
│   └── skills/
│       └── skill-architect/
│           ├── SKILL.md
│           └── templates/
│               └── TEMPLATE_SKILL.md
│
└── Teste gerador de Skill/                                # 🧪 Caso de Uso Real (Skill gerada pelo Skill Architect)
    └── controle-financeiro-pessoal/                       # Skill de Analista e Controle Financeiro Pessoal
        ├── SKILL.md                                       # Regras de negócio (Metodologia 50-30-20 e KPIs)
        ├── scripts/
        │   └── gerar_entregavel_financeiro.py             # Motor Python gerador do Dashboard HTML / PDF
        └── output/
            ├── dados_outubro_2026.json                    # Base de dados financeira estruturada (Outubro/2026)
            └── dashboard_controle_financeiro_outubro_2026.html # Entregável final: Dashboard Interativo c/ Gráficos
```

---

## 🛠️ Engenharia Anti-Erros do Skill Architect

Toda Skill construída por este agente segue rigorosamente **7 pilares de qualidade**:

1. **Inspeção Prévia de Contexto:** Leitura automática da stack do projeto antes de criar ou alterar arquivos.
2. **Responsabilidade Única (SRP):** Escopo claramente delimitado (Quando Usar vs. Quando NÃO Usar).
3. **Zero Alucinação Técnica:** Proibição de inventar APIs, parâmetros de CLI ou bibliotecas não verificadas.
4. **Acabamento Visual Nativo:** Especificação obrigatória de paleta de cores, tipografia, hierarquia visual e gráficos legíveis.
5. **Degradação Elegante (Fallback Visual):** Caso o ambiente de execução não possua bibliotecas externas para binários específicos, a skill garante a geração imediata de um **Dashboard/Relatório em HTML autocontido** pronto para exportação nativa em PDF pelo navegador.
6. **Critérios de Sucesso Verificáveis:** Checklist objetivo de validação ao final de cada entrega.
7. **Proibição de Scope Creep (YAGNI):** Criação de scripts auxiliares apenas quando agregam valor real à geração do entregável.

---

## 🧪 Demonstração Prática: Pasta `Teste gerador de Skill`

Para demonstrar o poder do **Skill Architect** na prática, este repositório inclui a pasta [`Teste gerador de Skill/controle-financeiro-pessoal/`](./Teste%20gerador%20de%20Skill/controle-financeiro-pessoal/), que contém uma skill completa de **Analista e Controle Financeiro Pessoal** gerada inteiramente pelo agente:

- **O que a Skill de Teste faz:** Recebe os ganhos e gastos de uma pessoa em texto livre ou tabela, higieniza e classifica automaticamente cada despesa na **Metodologia 50-30-20** (*Essenciais*, *Estilo de Vida/Variáveis* e *Objetivos/Poupança*), calcula **Taxa de Poupança**, **Semáforo de Saúde Financeira**, **Reserva de Emergência Ideal (6x e 12x)** e **Projeção de Patrimônio em 12 meses**.
- **Arquivos Gerados no Teste:**
  - 📄 [`SKILL.md`](./Teste%20gerador%20de%20Skill/controle-financeiro-pessoal/SKILL.md): Especificação completa da skill financeira.
  - 🐍 [`gerar_entregavel_financeiro.py`](./Teste%20gerador%20de%20Skill/controle-financeiro-pessoal/scripts/gerar_entregavel_financeiro.py): Script automatizado que processa o JSON de receitas/despesas e renderiza o painel visual.
  - 📊 [`dashboard_controle_financeiro_outubro_2026.html`](./Teste%20gerador%20de%20Skill/controle-financeiro-pessoal/output/dashboard_controle_financeiro_outubro_2026.html): Dashboard interativo real gerado para o fechamento de **Outubro/2026**, com gráficos Chart.js, KPIs em cards, diagnóstico 50-30-20, plano de ação e botão de impressão para PDF.

---

## 🚀 Como Utilizar Este Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Vitareli/Agent-desenvolvedor-de-Skills.git
   ```
2. **Abra no seu ambiente (Antigravity / VS Code):**
   - O arquivo [`AGENTS.md`](./AGENTS.md) na raiz e a skill em [`.agents/skills/skill-architect/SKILL.md`](./.agents/skills/skill-architect/SKILL.md) são carregados automaticamente pelo agente.
3. **Peça a criação de qualquer Skill:**
   > *"Crie uma skill que faça auditoria de contratos jurídicos e entregue um parecer executivo em PDF/HTML com matriz de riscos."*
   >
   > *"Crie uma skill para análise comercial de campanhas de marketing gerando dashboard interativo e gráficos de conversão."*

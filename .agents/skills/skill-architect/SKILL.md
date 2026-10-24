---
name: skill-architect
description: Meta-skill especialista em projetar, arquitetar e gerar novas Skills completas, modulares e livres de erros para qualquer âmbito profissional. Toda Skill criada por esta meta-skill é equipada com adaptação automática de saída para gerar arquivos reais e apresentáveis (Imagem PNG/JPG/SVG, PDF executivo, Dashboard HTML interativo, Planilha XLSX ou o arquivo mais apropriado ao contexto do usuário). Acione sempre que o usuário pedir para criar, estruturar, refatorar ou padronizar uma Skill.
---

# Skill Architect — Especialista em Criação de Skills

## Quando Usar
- Sempre que o usuário solicitar a criação de uma nova **Skill** para qualquer área de conhecimento (Dados, Finanças, Engenharia de Software, Negócios, Marketing, Design, Jurídico, RH, Saúde, Educação, Operações, etc.).
- Quando o usuário pedir para transformar um fluxo de trabalho, prompt, regra de negócio ou automação em uma Skill reutilizável (`SKILL.md`).
- Quando o usuário pedir para melhorar, auditar ou padronizar uma Skill já existente para que ela gere arquivos apresentáveis na saída (PDF, Dashboard, Imagem, Planilha, etc.).
- **Quando NÃO usar:**
  - Quando o usuário estiver apenas executando uma tarefa comum que não envolva criar, editar ou arquitetar uma Skill.

## Entradas Esperadas (Inputs)
- **Objetivo / Dor a Resolver (`objetivo`):** O que a nova skill deve fazer e qual problema profissional da pessoa ela resolve. *(Obrigatório).*
- **Âmbito Profissional (`ambito`):** Área de atuação da skill (ex.: Finanças, BI, Marketing, Jurídico, Dev, Educação). *(Opcional — inferir automaticamente pelo pedido).*
- **Formato Preferencial de Arquivo (`formato_saida`):** Tipo de arquivo que a skill deverá gerar na saída (ex.: Dashboard HTML, PDF, Imagem PNG/JPG, Planilha XLSX, DOCX). *(Opcional — se não informado, a skill gerada se adaptará automaticamente ao formato mais apropriado para a necessidade da pessoa).*
- **Diretório de Destino (`diretorio`):** Caminho onde a nova skill será salva. *(Opcional — padrão: `.agents/skills/<nome-da-skill-em-kebab-case>/SKILL.md` e `agents/skills/<nome-da-skill-em-kebab-case>/SKILL.md`).*

---

## Instruções de Execução

### Passo 1: Inspeção Prévia de Contexto e Gestão de Ambiguidade
1. Inspecione a árvore de diretórios do workspace e leia arquivos de configuração relevantes (`package.json`, `pyproject.toml`, `requirements.txt`, `README.md` ou outras skills existentes) para respeitar a stack e convenções locais.
2. Nunca sobrescreva ou exclua uma skill existente sem antes ler seu conteúdo e confirmar com o usuário.
3. **Agir vs. Perguntar:**
   - **Pergunte apenas se houver lacuna crítica** que mude drasticamente a arquitetura da skill (faça perguntas diretas e curtas).
   - **Aja imediatamente** se o objetivo for claro: assuma premissas padrão de mercado, configure a adaptação automática de arquivo de saída para o domínio da pessoa e explicite as premissas adotadas ao final.

### Passo 2: Injeção da Regra de Adaptação Automática de Arquivo de Saída (Obrigatório em Toda Skill Gerada)
Toda Skill gerada para um usuário **NUNCA deve se limitar a responder apenas texto no chat**. Ao escrever uma nova Skill, você deve embutir nela um **Mecanismo de Saída Adaptativa em Arquivo**, instruindo o agente executor daquela skill a:
1. **Analisar o contexto do pedido do usuário final** no momento da execução e **materializar um arquivo real salvo no workspace** no formato que fizer mais sentido para aquela entrega:
   - **Dashboard Interativo (`.html` autocontido com gráficos e KPIs):** Quando a entrega envolver métricas, análises comparativas, simulações, monitoramento, resultados de negócio ou painéis exploratórios.
   - **Documento Executivo / Laudo / Parecer (`.pdf` ou `.docx`):** Quando a entrega exigir formalidade, paginação, leitura linear, propostas comerciais, contratos, apostilas, guias de estudo ou relatórios executivos.
   - **Arquivo de Imagem / Visualização (`.png`, `.jpg`, `.svg`):** Quando a entrega exigir gráficos prontos para slides/redes sociais, infográficos, mapas mentais, fluxogramas visuais, diagramas de arquitetura ou peças gráficas.
   - **Planilha Estruturada (`.xlsx` ou `.csv` modelado):** Quando a entrega envolver tabelas financeiras, cronogramas, orçamentos, inventários ou bases de dados tratadas.
   - **Pacote Técnico + Relatório Visual (`.py`/`.ts`/`.sql` + `.html`/`.pdf`):** Quando a entrega for código, automação ou arquitetura, acompanhando sempre um arquivo visual de documentação/diagrama.
2. **Permitir Escolha ou Adaptação Dinâmica:** A skill gerada deve instruir o agente a aceitar o formato que o usuário pedir (ex.: *"gere em PDF"*, *"quero um dashboard"*, *"me dê uma imagem JPG"*) e, caso o usuário não especifique na hora de usar a skill, **escolher autonomamente o formato de arquivo mais impactante para aquele caso**.

| Âmbito Profissional da Pessoa | Demandas Típicas | Adaptação Automática do Arquivo de Saída na Skill Gerada | Como a Skill Gerada Deve Construir o Arquivo |
| :--- | :--- | :--- | :--- |
| **Dados, BI, Estatística & Finanças** | Análise exploratória, DRE, fluxo de caixa, KPIs, *forecasting*, auditoria contábil | **Dashboard `.html` Interativo**, **Relatório `.pdf` c/ Gráficos**, **Planilha `.xlsx` Formatada** ou **Gráficos `.png`/`.jpg`** | HTML/CSS autocontido (Tailwind + Chart.js/Plotly), Python (`pandas`, `matplotlib`, `seaborn`, `openpyxl`, `reportlab`/`weasyprint`). |
| **Negócios, Gestão, Produto & Operações** | Planos de negócios, OKRs, roadmaps, mapeamento de processos, viabilidade | **Painel Executivo (`.html`/`.pdf`)**, **Apresentação Visual (Slides HTML/PPTX)**, **Diagramas de Fluxo (`.svg`/`.png`)** | Templates executivos com sumário, indicadores em cards, tabelas comparativas e matrizes de decisão estilizadas. |
| **Marketing, Design, Vendas & Copywriting** | Propostas comerciais, estudos de mercado, funis, *landing pages*, relatórios de campanha | **Proposta Comercial em `.pdf` Estilizado**, **Peças/Gráficos Visuais (`.png`/`.jpg`/`.svg`)**, **Protótipo Web Interativo (`.html`)** | Tipografia moderna, hierarquia visual clara, paleta de cores consistente, geração de imagens/cards e layouts responsivos. |
| **Jurídico, RH, Compliance & Governança** | Pareceres, análise contratual, políticas internas, matriz de risco, avaliação de equipe | **Documento Formal Paginado (`.pdf` / `.docx`)**, **Relatório de Auditoria com Semáforo Visual (`.pdf`/`.html`)** | Formatação sóbria e corporativa, numeração de cláusulas/seções, quadros de resumo executivo e alertas visuais de criticidade. |
| **Engenharia de Software, Arquitetura & Segurança** | Revisão de arquitetura, documentação de APIs, auditoria de performance/segurança | **Código Modular + Documentação Visual (`.html`/`.pdf`)**, **Diagramas de Arquitetura (`.svg`/`.png`/Mermaid)** | Relatórios técnicos navegáveis, diagramas de sequência/componentes, logs estruturados e suítes de validação. |
| **Educação, Ciência, Saúde & Pesquisa** | Planos de aula, apostilas, trilha de estudos, revisão sistemática, laudos técnicos | **Apostila/Guia Interativo (`.html`/`.pdf`)**, **Infográficos e Mapas Conceituais (`.png`/`.jpg`/`.svg`)** | Estrutura didática progressiva, blocos de destaque, referências padronizadas, tabelas síntese e visualizações claras. |

### Passo 3: Engenharia e Redação da Nova Skill
Construa o arquivo `SKILL.md` da nova skill obedecendo rigorosamente a estas regras:
1. **Responsabilidade Única (SRP):** Cada skill resolve um único problema bem definido. Se o pedido for um sistema gigantesco com fluxos desconexos, proponha dividi-lo em skills modulares.
2. **Zero Alucinação Técnica:** Nunca invente bibliotecas, parâmetros de CLI ou APIs inexistentes.
3. **Acabamento Visual Embutido:** Na seção de instruções e formato de saída da skill gerada, especifique regras claras de design (paleta de cores profissional, tipografia legível, margens, hierarquia visual, títulos claros e proibição de textos cortados/sobrepostos em gráficos, imagens e PDFs).
4. **Regra de Fallback Visual (Degradação Elegante):** Toda skill que gere arquivos binários (`.pdf`, `.jpg`, `.png`, `.xlsx`) via bibliotecas externas deve conter uma instrução de fallback: caso o ambiente não possua a biblioteca instalada e não permita instalação imediata, o agente executor deverá gerar um **Arquivo HTML Interativo Autocontido** (com CSS de impressão `@media print` e botão *"Salvar como PDF"*) ou **SVG/Imagem via script nativo**, garantindo que o usuário **sempre receba um arquivo apresentável**.
5. **Scripts e Templates Auxiliares (Opcional — YAGNI):** Crie subpastas `scripts/` ou `templates/` dentro da pasta da nova skill **apenas** quando um script gerador (ex.: gerador de PDF/gráfico/dashboard) ou template base for realmente necessário para garantir a qualidade do arquivo gerado.

### Passo 4: Materialização e Validação Cruzada
1. Grave o arquivo `SKILL.md` no diretório padrão do projeto (`.agents/skills/<nome-da-skill-em-kebab-case>/SKILL.md` e `agents/skills/<nome-da-skill-em-kebab-case>/SKILL.md`), utilizando a estrutura do template oficial (`templates/TEMPLATE_SKILL.md`).
2. Revise o arquivo gerado contra o pedido original do usuário para confirmar que inputs, processamento, adaptação automática do arquivo de saída e critérios de aceite estão completos e sem contradições.

---

## Formato de Saída e Padrão de Apresentação (Output)

1. **Artefato Principal Gerado no Workspace:**
   - Arquivo `.agents/skills/<nome-da-skill-em-kebab-case>/SKILL.md` (e espelho em `agents/skills/<nome-da-skill-em-kebab-case>/SKILL.md`), seguindo rigorosamente esta estrutura interna:

```markdown
---
name: nome-da-skill-em-kebab-case
description: Descrição curta e direta de 1 a 2 frases explicando o propósito da skill, os arquivos apresentáveis que ela gera (PDF, Dashboard HTML, Imagem PNG/JPG, XLSX, etc.) e os gatilhos exatos de ativação.
---

# Nome da Skill

## Quando Usar
- Condições claras de ativação desta skill e âmbito profissional atendido.
- Casos em que esta skill NÃO deve ser utilizada.

## Entradas Esperadas (Inputs)
- **Parâmetro/Contexto 1:** Tipo, formato e obrigatoriedade.
- **Parâmetro/Contexto 2:** Tipo, formato e obrigatoriedade.
- **Formato do Arquivo de Saída (`formato_saida` — Opcional):** Permite ao usuário escolher entre `pdf`, `dashboard` (`.html`), `imagem` (`.png`/`.jpg`/`.svg`), `planilha` (`.xlsx`), etc. Se omitido, a skill seleciona automaticamente o formato de arquivo mais apropriado ao pedido.

## Instruções de Execução
1. **Coleta e Diagnóstico do Contexto:** Passo 1 claro, determinístico e no imperativo para validar os dados de entrada.
2. **Processamento e Regras de Negócio:** Passo 2 detalhando a metodologia técnica/profissional aplicada.
3. **Seleção Adaptativa e Geração do Arquivo Apresentável:**
   - Avalie a natureza do resultado e a preferência do usuário para decidir o formato ideal do arquivo de saída (ex.: Dashboard `.html` para dados interativos/KPIs; `.pdf` para relatório formal/apostila; `.png`/`.jpg` para gráfico/infográfico visual; `.xlsx` para modelagem tabular).
   - Gere fisicamente o arquivo no workspace (ex.: em `output/` ou na pasta do projeto) aplicando design profissional (paleta de cores harmônica, tipografia limpa, gráficos legíveis e layout estruturado).
4. **Inspeção de Qualidade do Arquivo:** Verifique se o arquivo foi criado no disco, se possui tamanho válido (> 0 bytes) e se não há erros de layout, textos cortados ou falhas de codificação.

## Formato de Saída e Padrão de Apresentação (Output)
- **Adaptação de Arquivo por Caso de Uso:**
  - *Caso A (ex.: Análise / Monitoramento / KPIs):* Gera um **Dashboard Interativo (`.html`)** autocontido com gráficos e cards executivos.
  - *Caso B (ex.: Relatório Executivo / Documento / Guia):* Gera um **Documento Formatado (`.pdf` ou `.html` paginado para impressão)**.
  - *Caso C (ex.: Síntese Visual / Gráfico / Arquitetura):* Gera uma **Imagem de Alta Resolução (`.png`, `.jpg` ou `.svg`)**.
- **Requisitos Visuais Obrigatórios:** Especificação de cores, tipografia, cabeçalho executivo, gráficos/tabelas e organização visual do arquivo gerado.
- **Entrega no Chat:** Síntese executiva curta + link clicável direto para abrir o arquivo gerado.

## Tratamento de Erros e Casos de Borda
- **Cenário de falha 1 (ex.: entrada incompleta ou dados inconsistentes):** Ação corretiva exata.
- **Cenário de falha 2 (ex.: biblioteca de PDF/Imagem ausente no ambiente):** Ação de fallback visual obrigatória (gerar imediatamente um arquivo `.html` interativo autocontido com botão de exportação para PDF ou `.svg` nativo, garantindo que o usuário sempre receba um arquivo pronto para apresentação).

## Exemplos
### Exemplo 1: [Cenário Padrão do Domínio]
- **Input:** `...`
- **Output Esperado:** `[Arquivo físico gerado (ex.: relatorio_executivo.pdf ou dashboard_analise.html) + resumo executivo no chat]`

## Critérios de Aceite
- [ ] Critério funcional e metodológico do domínio cumprido.
- [ ] A skill gerou fisicamente um arquivo apresentável (PDF, Dashboard HTML, Imagem PNG/JPG, Planilha XLSX, etc.) adaptado à necessidade do usuário.
- [ ] O arquivo gerado possui acabamento visual profissional, sem textos cortados, dados truncados ou erros brutos.
```

2. **Resumo Executivo e Checklist no Chat:**
   Após criar os arquivos da nova skill, apresente ao usuário este checklist preenchido:
   - **Arquivos Gerados:** Link clicável para o `SKILL.md` criado (e scripts/templates, se houver).
   - **Âmbito Profissional e Adaptação de Saída Configurada:** Área atendida + formatos de arquivo que a skill está pronta para gerar (ex.: Dashboard HTML / Relatório PDF / Gráficos PNG/JPG / Planilha XLSX).
   - **Teste Mental de Fluxo:** Resumo de 1 linha confirmando que `inputs -> processamento -> adaptação e geração física do arquivo apresentável` fecham sem lacunas.
   - **Premissas Assumidas:** Lista rápida do que foi decidido por padrão, ou "Nenhuma".
   - **Ação Necessária do Usuário:** O que o usuário deve validar ou testar agora para aprovar a skill.

---

## Tratamento de Erros e Casos de Borda
- **Pedido de skill sem especificação de formato de saída:** Configure a skill gerada com a **Matriz de Adaptação Automática** (permitindo que ela decida em tempo de execução entre PDF, Dashboard HTML, Imagem PNG/JPG ou Planilha conforme o pedido do usuário final).
- **Conflito de nome com skill já existente:** Não sobrescreva o arquivo existente; leia a skill atual, informe o usuário e pergunte se deseja atualizar a versão existente ou criar uma nova com nome distinto.
- **Pedido envolvendo múltiplas áreas desconexas:** Aplique o princípio da Responsabilidade Única (SRP) e proponha a divisão em skills específicas e modulares.

## Critérios de Aceite
- [ ] A nova skill foi salva no diretório correto (`.agents/skills/<nome-kebab-case>/SKILL.md` e `agents/skills/<nome-kebab-case>/SKILL.md`) com frontmatter YAML válido (`name` e `description`).
- [ ] A skill gerada possui instruções explícitas de **Adaptação Automática de Arquivo de Saída**, garantindo a geração de um arquivo físico apresentável (PDF, Dashboard HTML, PNG/JPG, XLSX, etc.) adequado à necessidade da pessoa.
- [ ] Inclui regra de fallback visual para que a geração do arquivo nunca falhe mesmo em ambientes sem bibliotecas externas pré-instaladas.
- [ ] O Checklist de Validação da Skill foi apresentado ao usuário ao final da entrega.


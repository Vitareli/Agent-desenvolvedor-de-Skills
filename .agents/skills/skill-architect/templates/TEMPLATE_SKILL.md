---
name: nome-da-skill-em-kebab-case
description: Descrição curta e direta de 1 a 2 frases explicando o propósito da skill, os arquivos apresentáveis que ela gera (PDF, Dashboard HTML, Imagem PNG/JPG, XLSX, etc.) e os gatilhos exatos de quando o agente deve acioná-la.
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


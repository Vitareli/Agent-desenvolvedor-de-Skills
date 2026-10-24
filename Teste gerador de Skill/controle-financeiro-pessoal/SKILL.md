---
name: controle-financeiro-pessoal
description: Realiza o diagnóstico e controle financeiro pessoal completo a partir dos ganhos e gastos informados pelo usuário, categorizando despesas, aplicando a metodologia 50-30-20 e gerando automaticamente arquivos apresentáveis adaptados (Dashboard HTML interativo, Relatório PDF executivo, Gráficos PNG/JPG ou Planilha XLSX formatada). Acione sempre que o usuário fornecer receitas/despesas ou pedir ajuda para organizar suas finanças pessoais.
---

# Controle e Diagnóstico Financeiro Pessoal Completo

## Quando Usar
- Quando o usuário informar seus ganhos (salário, rendas extras) e gastos (fixos, variáveis, cartão de crédito, dívidas) em texto livre, lista, CSV ou planilha e pedir um controle, organização ou análise financeira.
- Quando o usuário quiser descobrir para onde seu dinheiro está indo, quanto pode economizar, como quitar dívidas ou montar sua reserva de emergência com base nos próprios números.
- Quando o usuário solicitar um painel visual, planilha organizada, relatório em PDF ou gráfico dos seus gastos mensais.
- **Quando NÃO usar:**
  - Para contabilidade societária avançada de grandes empresas (balanço patrimonial corporativo auditado, apuração de impostos PJ complexos como Lucro Real).
  - Para recomendação de compra/venda de ativos mobiliários específicos (ações/criptoativos individuais) sem contexto de orçamento pessoal.

## Entradas Esperadas (Inputs)
- **Rendas / Receitas (`receitas`):** Valor(es) de entrada financeira mensal (salário líquido, pró-labore, freelas, aluguéis, rendimentos). *(Obrigatório — pode ser enviado em texto solto, ex.: "ganho 5000", ou em arquivo).*
- **Gastos e Compromissos (`despesas`):** Lista de despesas do mês (aluguel, mercado, luz, internet, lazer, cartão, parcelas, etc.). *(Obrigatório — aceita texto livre, tabela colada, `.csv` ou `.xlsx`).*
- **Metas ou Dívidas (`contexto_adicional` — Opcional):** Objetivos financeiros (ex.: "quero juntar R$ 10.000", "quero sair do cheque especial") ou saldo de dívidas atuais.
- **Formato do Arquivo de Saída (`formato_saida` — Opcional):** Permite ao usuário escolher entre:
  - `dashboard` (`.html` interativo com gráficos e botão de impressão para PDF)
  - `pdf` (`.pdf` executivo paginado com gráficos)
  - `imagem` (`.png` ou `.jpg` com painel visual de gráficos do orçamento)
  - `planilha` (`.xlsx` estruturada em abas com formatação monetária)
  - *Adaptação Automática:* Se omitido pelo usuário, a skill seleciona e gera automaticamente o **Dashboard Financeiro Interativo (`.html`)** acompanhado do resumo executivo (ou `.xlsx`/`.pdf` conforme o contexto do pedido).

---

## Instruções de Execução

### 1. Coleta, Higienização e Categorização Inteligente
1. Extraia todos os valores numéricos de receitas e despesas informados pelo usuário (convertendo formatos como `R$ 1.500,50` ou `1500` para ponto flutuante padronizado).
2. Classifique cada despesa automaticamente em **2 níveis**:
   - **Macro-Classe (Metodologia 50-30-20):**
     - `Essenciais (Meta <= 50%)`: Moradia, condomínio, água, luz, internet, supermercado básico, transporte essencial, saúde, educação obrigatória.
     - `Estilo de Vida / Variáveis (Meta <= 30%)`: Restaurantes, delivery, lazer, streaming, assinaturas, compras pessoais, estética, viagens.
     - `Objetivos / Dívidas / Investimentos (Meta >= 20%)`: Aportes financeiros, reserva de emergência, previdência e amortização de dívidas/empréstimos.
   - **Categoria Detalhada:** `Moradia`, `Alimentação`, `Transporte`, `Saúde`, `Educação`, `Lazer & Delivery`, `Assinaturas & Serviços`, `Dívidas & Cartão`, `Investimentos`, `Outros`.
3. Verifique se a soma das categorias bate exatamente com o total de despesas informadas (Zero divergência aritmética).

### 2. Processamento e Diagnóstico de Saúde Financeira
Calcule de forma determinística os seguintes indicadores:
1. **Receita Total Mensal ($R_{total}$)** e **Despesa Total Mensal ($D_{total}$)**.
2. **Fluxo de Caixa Líquido ($Saldo = R_{total} - D_{total}$):** Identifique se o orçamento é **Superavitário** ($Saldo > 0$), **No Limite** ($Saldo = 0$) ou **Deficitário / No Vermelho** ($Saldo < 0$).
3. **Taxa de Poupança Real (*Savings Rate*):**
   $$\text{Taxa de Poupança (\%)} = \left(\frac{\text{Investimentos} + \max(0, Saldo)}{R_{total}}\right) \times 100$$
4. **Índice de Saúde Financeira (Semáforo Executivo):**
   - 🟢 **Saudável:** Saldo positivo, gastos essenciais $\le 55\%$ da renda e taxa de poupança $\ge 15\%$.
   - 🟡 **Atenção:** Saldo próximo de zero (entre $0\%$ e $10\%$ da renda) ou gastos variáveis/essenciais acima do limite recomendado.
   - 🔴 **Crítico / Endividamento:** Despesas maiores que receitas ($Saldo < 0$) ou comprometimento com dívidas/fixos $> 70\%$ da renda.
5. **Análise de Pareto (Top 3 Vilões do Orçamento):** Identifique as 3 maiores despesas ou categorias que consomem a maior fatia da renda e calcule quanto uma redução realista de 15% a 20% nos gastos variáveis geraria de economia em **1 mês** e em **12 meses**.
6. **Cálculo da Reserva de Emergência Ideal:** Multiplique o custo mensal de `Essenciais` por **6 meses** (Segurança Padrão) e **12 meses** (Segurança Autônomo/Conservador).

### 3. Seleção Adaptativa e Geração do Arquivo Apresentável
Avalie o pedido do usuário e gere fisicamente o arquivo apresentável no diretório de saída do projeto (ex.: `output/` ou na pasta atual), acionando o script auxiliar `scripts/gerar_entregavel_financeiro.py` ou construindo o artefato conforme as regras abaixo:
- **Se `formato_saida` for `dashboard` (ou não especificado — Padrão Adaptativo Principal):**
  - Gere o arquivo `dashboard_controle_financeiro.html` autocontido (HTML5 + CSS moderno/Tailwind + Chart.js via CDN + CSS `@media print`), contendo:
    1. Cabeçalho Executivo com status do Semáforo Financeiro (🟢/🟡/🔴).
    2. 4 Cards de KPIs em destaque: *Receita Total*, *Despesa Total*, *Saldo Livre Mensal* e *Taxa de Poupança (%)*.
    3. Gráficos Interativos lado a lado:
       - Gráfico de Rosca (*Doughnut*): Distribuição de Gastos por Categoria.
       - Gráfico de Barras Comparativo: Orçamento Real vs. Ideal (Regra 50-30-20).
       - Gráfico de Linha: Projeção de Acúmulo de Reserva/Patrimônio em 12 meses (Cenário Atual vs. Cenário Otimizado).
    4. Tabela completa de lançamentos categorizados com percentual sobre a renda.
    5. Quadro de Plano de Ação Personalizado + Botão **"🖨️ Exportar / Salvar como PDF"**.
- **Se `formato_saida` for `pdf`:**
  - Gere o arquivo `relatorio_financeiro_pessoal.pdf` paginado em A4 com cabeçalho executivo, tabelas estilizadas, gráficos renderizados e plano de ação.
- **Se `formato_saida` for `imagem` (`.png` / `.jpg`):**
  - Gere um painel visual de alta resolução (`resumo_financeiro.png` com `dpi=300`) via `matplotlib`/`seaborn` com 3 subplots (Rosca de Categorias, Termômetro 50-30-20 e Top Maiores Gastos) e rodapé com os KPIs principais.
- **Se `formato_saida` for `planilha` (`.xlsx`):**
  - Gere o arquivo `controle_financeiro_pessoal.xlsx` com abas estruturadas (`1_Resumo_Executivo`, `2_Lancamentos`, `3_Plano_50_30_20`, `4_Projecao_12M`), formatação contábil `R$ #.##0,00` e cores condicionais.

### 4. Inspeção de Qualidade do Arquivo
1. Confirme no terminal/sistema de arquivos que o arquivo foi fisicamente criado e possui tamanho $> 0\text{ bytes}$.
2. Verifique se todos os valores estão formatados no padrão monetário brasileiro (`R$ 1.234,56`) e se não há textos sobrepostos ou valores `NaN`/`undefined`.

---

## Formato de Saída e Padrão de Apresentação (Output)

- **Adaptação de Arquivo por Caso de Uso:**
  - *Caso A (Visão Geral Completa / Controle Mensal — Padrão):* Gera **Dashboard Interativo (`dashboard_controle_financeiro.html`)** pronto para abrir no navegador e exportar para PDF.
  - *Caso B (Documento Formal / Impressão):* Gera **Relatório Executivo (`relatorio_financeiro_pessoal.pdf`)**.
  - *Caso C (Compartilhamento Rápido / Mobile / Imagem):* Gera **Infográfico Financeiro (`resumo_financeiro.png` ou `.jpg`)**.
  - *Caso D (Edição Contínua pelo Usuário):* Gera **Planilha Automatizada (`controle_financeiro_pessoal.xlsx`)**.
- **Requisitos Visuais Obrigatórios:**
  - **Paleta de Cores Financeira:** Azul Marinho Executivo (`#0F172A`) para cabeçalhos, Verde Esmeralda (`#10B981`) para receitas/superávit, Vermelho Coral (`#EF4444`) para despesas críticas/déficit, Âmbar (`#F59E0B`) para alertas e Cinza Claro (`#F8FAFC`) para fundo.
  - **Tipografia:** Fonte limpa sem serifa (`Inter`, `Segoe UI` ou `Roboto`), valores monetários alinhados à direita em tabelas e títulos hierárquicos claros.
- **Entrega no Chat:**
  1. Resumo executivo direto (4 a 6 bullets com os números principais e o diagnóstico 50-30-20).
  2. Top 3 recomendações práticas imediatas para o bolso da pessoa.
  3. **Link clicável direto** para abrir o arquivo apresentável gerado.

---

## Tratamento de Erros e Casos de Borda
- **Usuário informa apenas gastos e esquece de informar a renda (ou vice-versa):** Solicite de forma rápida e amigável o valor da renda mensal (ou gere imediatamente a análise proporcional sobre o total de gastos, destacando que basta informar a renda para habilitar o cálculo da Regra 50-30-20 e Taxa de Poupança).
- **Gastos informados com valores aproximados ou misturados (ex.: "gasto uns 800 de mercado e padaria, 1200 de aluguel com condomínio"):** Desmembre ou agrupe de forma lógica, documente a classificação adotada na tabela e mantenha a soma exata.
- **Biblioteca externa ausente para `.pdf`, `.png` ou `.xlsx` (ex.: `reportlab`, `matplotlib` ou `openpyxl` não instalados):** Aplique imediatamente a **Degradação Elegante (Fallback Visual)**: execute o gerador nativo em Python padrão para criar o **Dashboard Interativo Autocontido (`dashboard_controle_financeiro.html`)** com gráficos SVG/Canvas nativos e folha de estilo `@media print` pronta para salvar como PDF em 1 clique, mais arquivo `.csv` compatível com Excel.

---

## Exemplos

### Exemplo 1: Usuário envia receitas e gastos em texto livre
- **Input:** `"Ganho R$ 6.500 líquidos por mês. Meus gastos são: Aluguel R$ 1.800, Condomínio R$ 450, Luz R$ 180, Internet R$ 120, Supermercado R$ 1.100, Uber/Combustível R$ 400, Academia R$ 150, iFood e Restaurantes R$ 850, Streaming/Assinaturas R$ 120, Cartão de crédito (roupas/lazer) R$ 600 e guardo R$ 300 na poupança. Faça meu controle financeiro completo."`
- **Output Esperado:**
  - Processamento exato: Receita = `R$ 6.500,00` | Despesas = `R$ 5.770,00` | Investido = `R$ 300,00` | Saldo Livre = `R$ 430,00` (Potencial total de poupança = `R$ 730,00` ou `11,2%`).
  - Divisão 50-30-20: Essenciais = `R$ 4.050,00` (`62,3%` — acima dos 50%), Estilo de Vida = `R$ 1.720,00` (`26,5%` — dentro dos 30%), Objetivos/Poupança = `R$ 730,00` (`11,2%` — abaixo dos 20%).
  - Geração física do arquivo `dashboard_controle_financeiro.html` (ou `.pdf`/`.xlsx`/`.png` via `scripts/gerar_entregavel_financeiro.py`) + entrega do link clicável e plano de ação no chat.

---

## Critérios de Aceite
- [ ] Todos os ganhos e gastos informados pelo usuário foram contabilizados sem erro de soma e categorizados na estrutura 50-30-20.
- [ ] Foram calculados o Saldo Líquido, Taxa de Poupança, Reserva de Emergência Ideal, Top 3 Maiores Gastos e Projeção de 12 meses.
- [ ] A skill gerou fisicamente um arquivo apresentável no disco (`.html` dashboard interativo, `.pdf`, `.png`/`.jpg` ou `.xlsx`) adaptado à necessidade do usuário.
- [ ] O arquivo gerado possui acabamento visual executivo, valores em `R$` formatados corretamente e zero erros de renderização.


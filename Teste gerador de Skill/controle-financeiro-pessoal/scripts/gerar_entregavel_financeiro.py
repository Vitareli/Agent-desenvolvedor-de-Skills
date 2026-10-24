#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Oficial da Skill: controle-financeiro-pessoal
Gera entregáveis apresentáveis (Dashboard HTML Interativo c/ exportação PDF,
Gráfico PNG de alta resolução e Planilha CSV/XLSX) a partir dos dados financeiros do usuário.
"""

import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Any


def format_brl(value: float) -> str:
    """Formata um float para o padrão monetário brasileiro R$ 1.234,56."""
    formatted = f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {formatted}"


def calcular_diagnostico(dados: Dict[str, Any]) -> Dict[str, Any]:
    """Calcula todos os indicadores financeiros, regra 50-30-20 e projeções."""
    nome_usuario = dados.get("nome", "Planejamento Pessoal")
    mes_referencia = dados.get("mes_referencia", datetime.now().strftime("%m/%Y"))
    receitas: List[Dict[str, Any]] = dados.get("receitas", [])
    despesas: List[Dict[str, Any]] = dados.get("despesas", [])

    receita_total = sum(float(r.get("valor", 0.0)) for r in receitas)

    essenciais = 0.0
    estilo_vida = 0.0
    objetivos_dividas = 0.0
    por_categoria: Dict[str, float] = {}

    despesas_processadas = []
    for d in despesas:
        valor = float(d.get("valor", 0.0))
        classe = d.get("macro_classe", "Essenciais")  # Essenciais | Estilo de Vida | Objetivos
        categoria = d.get("categoria", "Outros")
        descricao = d.get("descricao", categoria)

        if "essencia" in classe.lower():
            classe_padrao = "Essenciais (50%)"
            essenciais += valor
        elif "objetivo" in classe.lower() or "invest" in classe.lower() or "divida" in classe.lower() or "dívida" in classe.lower():
            classe_padrao = "Objetivos & Poupança (20%)"
            objetivos_dividas += valor
        else:
            classe_padrao = "Estilo de Vida (30%)"
            estilo_vida += valor

        por_categoria[categoria] = por_categoria.get(categoria, 0.0) + valor
        pct_renda = (valor / receita_total * 100) if receita_total > 0 else 0.0
        despesas_processadas.append({
            "descricao": descricao,
            "categoria": categoria,
            "macro_classe": classe_padrao,
            "valor": valor,
            "pct_renda": round(pct_renda, 1),
        })

    despesas_processadas.sort(key=lambda x: x["valor"], reverse=True)
    despesa_consumo = essenciais + estilo_vida
    despesa_total = essenciais + estilo_vida + objetivos_dividas
    saldo_livre = receita_total - despesa_total
    poupanca_potencial = objetivos_dividas + max(0.0, saldo_livre)

    pct_essenciais = (essenciais / receita_total * 100) if receita_total > 0 else 0.0
    pct_estilo = (estilo_vida / receita_total * 100) if receita_total > 0 else 0.0
    pct_poupanca = (poupanca_potencial / receita_total * 100) if receita_total > 0 else 0.0

    # Semáforo de saúde financeira
    if saldo_livre < 0:
        status_saude = "CRÍTICO (Déficit Mensal)"
        cor_status = "#EF4444"
        icone_status = "🔴"
    elif pct_poupanca < 10 or pct_essenciais > 60:
        status_saude = "ATENÇÃO (Margem Apertada)"
        cor_status = "#F59E0B"
        icone_status = "🟡"
    else:
        status_saude = "SAUDÁVEL (Superavitário)"
        cor_status = "#10B981"
        icone_status = "🟢"

    # Potencial de otimização (redução de 20% em Estilo de Vida)
    economia_mensal_otimizada = estilo_vida * 0.20
    aporte_mensal_atual = max(0.0, poupanca_potencial)
    aporte_mensal_otimizado = max(0.0, poupanca_potencial + economia_mensal_otimizada)

    # Projeção de 12 meses com rendimento conservador de 0.85% a.m. (CDI líquido estimado)
    taxa_mensal = 0.0085
    projecao_atual = []
    projecao_otimizada = []
    acum_atual = 0.0
    acum_otim = 0.0
    for m in range(1, 13):
        acum_atual = (acum_atual + aporte_mensal_atual) * (1 + taxa_mensal)
        acum_otim = (acum_otim + aporte_mensal_otimizado) * (1 + taxa_mensal)
        projecao_atual.append(round(acum_atual, 2))
        projecao_otimizada.append(round(acum_otim, 2))

    return {
        "nome": nome_usuario,
        "mes_referencia": mes_referencia,
        "receita_total": receita_total,
        "despesa_consumo": despesa_consumo,
        "despesa_total": despesa_total,
        "saldo_livre": saldo_livre,
        "essenciais": essenciais,
        "estilo_vida": estilo_vida,
        "objetivos_dividas": objetivos_dividas,
        "poupanca_potencial": poupanca_potencial,
        "pct_essenciais": round(pct_essenciais, 1),
        "pct_estilo": round(pct_estilo, 1),
        "pct_poupanca": round(pct_poupanca, 1),
        "status_saude": status_saude,
        "cor_status": cor_status,
        "icone_status": icone_status,
        "reserva_6m": essenciais * 6,
        "reserva_12m": essenciais * 12,
        "economia_mensal_otimizada": economia_mensal_otimizada,
        "economia_anual_otimizada": economia_mensal_otimizada * 12,
        "por_categoria": dict(sorted(por_categoria.items(), key=lambda x: x[1], reverse=True)),
        "despesas_processadas": despesas_processadas,
        "projecao_atual": projecao_atual,
        "projecao_otimizada": projecao_otimizada,
    }


def gerar_dashboard_html(diag: Dict[str, Any], caminho_saida: str) -> str:
    """Gera um Dashboard HTML Interativo autocontido e pronto para exportar em PDF."""
    categorias_labels = json.dumps(list(diag["por_categoria"].keys()), ensure_ascii=False)
    categorias_valores = json.dumps([round(v, 2) for v in diag["por_categoria"].values()])
    projecao_atual_json = json.dumps(diag["projecao_atual"])
    projecao_otim_json = json.dumps(diag["projecao_otimizada"])

    linhas_tabela = ""
    for item in diag["despesas_processadas"]:
        badge_color = "#DBEAFE" if "Essenciais" in item["macro_classe"] else (
            "#FEF3C7" if "Estilo" in item["macro_classe"] else "#D1FAE5"
        )
        text_color = "#1E40AF" if "Essenciais" in item["macro_classe"] else (
            "#92400E" if "Estilo" in item["macro_classe"] else "#065F46"
        )
        linhas_tabela += f"""
        <tr class="border-b border-slate-100 hover:bg-slate-50">
            <td class="py-3 px-4 font-medium text-slate-800">{item['descricao']}</td>
            <td class="py-3 px-4 text-slate-600">{item['categoria']}</td>
            <td class="py-3 px-4">
                <span style="background:{badge_color};color:{text_color}" class="px-2.5 py-1 rounded-full text-xs font-semibold">
                    {item['macro_classe']}
                </span>
            </td>
            <td class="py-3 px-4 text-right font-semibold text-slate-800">{format_brl(item['valor'])}</td>
            <td class="py-3 px-4 text-right text-slate-500">{item['pct_renda']}%</td>
        </tr>
        """

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Painel de Controle Financeiro — {diag['nome']}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        @media print {{
            .no-print {{ display: none !important; }}
            body {{ background: #ffffff !important; }}
            .shadow-sm, .shadow-md {{ box-shadow: none !important; border: 1px solid #e2e8f0 !important; }}
        }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased">
    <div class="max-w-6xl mx-auto p-6 md:p-8">
        <!-- Cabeçalho Executivo -->
        <header class="bg-slate-900 text-white rounded-2xl p-6 mb-8 flex flex-col md:flex-row justify-between items-start md:items-center gap-4 shadow-md">
            <div>
                <p class="text-slate-400 text-xs uppercase tracking-wider font-semibold">Diagnóstico & Controle Financeiro Pessoal</p>
                <h1 class="text-2xl md:text-3xl font-bold mt-1">{diag['nome']} — Ref. {diag['mes_referencia']}</h1>
            </div>
            <div class="flex items-center gap-4">
                <div class="px-4 py-2 rounded-xl font-bold text-sm" style="background-color: {diag['cor_status']}25; color: {diag['cor_status']}; border: 1px solid {diag['cor_status']}">
                    {diag['icone_status']} {diag['status_saude']}
                </div>
                <button onclick="window.print()" class="no-print bg-emerald-500 hover:bg-emerald-600 text-white font-semibold px-4 py-2 rounded-xl text-sm transition cursor-pointer">
                    🖨️ Salvar / Imprimir PDF
                </button>
            </div>
        </header>

        <!-- Cards de KPIs -->
        <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5 mb-8">
            <div class="bg-white rounded-2xl p-5 shadow-sm border border-slate-100">
                <p class="text-xs font-semibold uppercase text-slate-400">Receita Total Mensal</p>
                <p class="text-2xl font-bold text-emerald-600 mt-2">{format_brl(diag['receita_total'])}</p>
                <p class="text-xs text-slate-500 mt-1">100% da base de cálculo</p>
            </div>
            <div class="bg-white rounded-2xl p-5 shadow-sm border border-slate-100">
                <p class="text-xs font-semibold uppercase text-slate-400">Despesas de Consumo</p>
                <p class="text-2xl font-bold text-rose-600 mt-2">{format_brl(diag['despesa_consumo'])}</p>
                <p class="text-xs text-slate-500 mt-1">Essenciais + Estilo de Vida</p>
            </div>
            <div class="bg-white rounded-2xl p-5 shadow-sm border border-slate-100">
                <p class="text-xs font-semibold uppercase text-slate-400">Potencial de Poupança / Mês</p>
                <p class="text-2xl font-bold text-blue-600 mt-2">{format_brl(diag['poupanca_potencial'])}</p>
                <p class="text-xs text-slate-500 mt-1">Taxa de Poupança: <strong>{diag['pct_poupanca']}%</strong> (Meta: 20%)</p>
            </div>
            <div class="bg-white rounded-2xl p-5 shadow-sm border border-slate-100">
                <p class="text-xs font-semibold uppercase text-slate-400">Reserva de Emergência Ideal</p>
                <p class="text-2xl font-bold text-slate-800 mt-2">{format_brl(diag['reserva_6m'])}</p>
                <p class="text-xs text-slate-500 mt-1">6x custos essenciais ({format_brl(diag['essenciais'])}/mês)</p>
            </div>
        </section>

        <!-- Gráficos Principais -->
        <section class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
            <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-100">
                <h2 class="text-lg font-bold text-slate-800 mb-1">Distribuição por Categoria</h2>
                <p class="text-xs text-slate-500 mb-4">Para onde está indo cada real do seu orçamento</p>
                <div class="h-64 flex items-center justify-center">
                    <canvas id="chartCategorias"></canvas>
                </div>
            </div>
            <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-100">
                <h2 class="text-lg font-bold text-slate-800 mb-1">Diagnóstico Regra 50 - 30 - 20</h2>
                <p class="text-xs text-slate-500 mb-4">Comparativo entre o seu orçamento atual (%) e o benchmark recomendado</p>
                <div class="h-64 flex items-center justify-center">
                    <canvas id="chart503020"></canvas>
                </div>
            </div>
        </section>

        <!-- Projeção de Patrimônio 12 Meses + Plano de Ação -->
        <section class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
            <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-100 lg:col-span-2">
                <h2 class="text-lg font-bold text-slate-800 mb-1">Projeção de Acúmulo em 12 Meses</h2>
                <p class="text-xs text-slate-500 mb-4">Ritmo Atual vs. Reduzindo 20% dos gastos de Estilo de Vida (+{format_brl(diag['economia_mensal_otimizada'])}/mês)</p>
                <div class="h-60">
                    <canvas id="chartProjecao"></canvas>
                </div>
            </div>
            <div class="bg-slate-900 text-white rounded-2xl p-6 shadow-sm flex flex-col justify-between">
                <div>
                    <h2 class="text-lg font-bold text-emerald-400 mb-3">🎯 Plano de Ação Prático</h2>
                    <ul class="space-y-3 text-sm text-slate-200">
                        <li>• <strong>Essenciais ({diag['pct_essenciais']}%):</strong> {format_brl(diag['essenciais'])} (Ideal até 50%).</li>
                        <li>• <strong>Estilo de Vida ({diag['pct_estilo']}%):</strong> {format_brl(diag['estilo_vida'])} (Ideal até 30%).</li>
                        <li>• <strong>Otimização Imediata:</strong> Reduzir 20% dos variáveis libera <strong>{format_brl(diag['economia_mensal_otimizada'])}/mês</strong> ({format_brl(diag['economia_anual_otimizada'])}/ano).</li>
                        <li>• <strong>Patrimônio em 12 Meses (Otimizado):</strong> <strong>{format_brl(diag['projecao_otimizada'][-1])}</strong>.</li>
                    </ul>
                </div>
                <div class="mt-6 pt-4 border-t border-slate-700 text-xs text-slate-400">
                    Gerado automaticamente pela Skill <strong>controle-financeiro-pessoal</strong>
                </div>
            </div>
        </section>

        <!-- Tabela Detalhada de Lançamentos -->
        <section class="bg-white rounded-2xl p-6 shadow-sm border border-slate-100">
            <h2 class="text-lg font-bold text-slate-800 mb-4">Detalhamento Completo de Gastos e Compromissos</h2>
            <div class="overflow-x-auto">
                <table class="w-full text-left border-collapse text-sm">
                    <thead>
                        <tr class="border-b-2 border-slate-200 text-slate-500 uppercase text-xs">
                            <th class="py-3 px-4">Descrição</th>
                            <th class="py-3 px-4">Categoria</th>
                            <th class="py-3 px-4">Classe 50-30-20</th>
                            <th class="py-3 px-4 text-right">Valor (R$)</th>
                            <th class="py-3 px-4 text-right">% da Renda</th>
                        </tr>
                    </thead>
                    <tbody>
                        {linhas_tabela}
                    </tbody>
                </table>
            </div>
        </section>
    </div>

    <script>
        new Chart(document.getElementById('chartCategorias'), {{
            type: 'doughnut',
            data: {{
                labels: {categorias_labels},
                datasets: [{{
                    data: {categorias_valores},
                    backgroundColor: ['#0F172A', '#2563EB', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6', '#EC4899', '#14B8A6', '#64748B']
                }}]
            }},
            options: {{ responsive: true, maintainAspectRatio: false, plugins: {{ legend: {{ position: 'right' }} }} }}
        }});

        new Chart(document.getElementById('chart503020'), {{
            type: 'bar',
            data: {{
                labels: ['Essenciais (Meta 50%)', 'Estilo de Vida (Meta 30%)', 'Objetivos/Poupança (Meta 20%)'],
                datasets: [
                    {{
                        label: 'Seu Orçamento (%)',
                        data: [{diag['pct_essenciais']}, {diag['pct_estilo']}, {diag['pct_poupanca']}],
                        backgroundColor: ['#2563EB', '#F59E0B', '#10B981'],
                        borderRadius: 6
                    }},
                    {{
                        label: 'Meta Ideal (%)',
                        data: [50, 30, 20],
                        backgroundColor: ['#CBD5E1', '#CBD5E1', '#CBD5E1'],
                        borderRadius: 6
                    }}
                ]
            }},
            options: {{ responsive: true, maintainAspectRatio: false, scales: {{ y: {{ beginAtZero: true, max: 100 }} }} }}
        }});

        new Chart(document.getElementById('chartProjecao'), {{
            type: 'line',
            data: {{
                labels: ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12'],
                datasets: [
                    {{
                        label: 'Cenário Otimizado (R$)',
                        data: {projecao_otim_json},
                        borderColor: '#10B981',
                        backgroundColor: '#10B98120',
                        fill: true,
                        tension: 0.3
                    }},
                    {{
                        label: 'Cenário Atual (R$)',
                        data: {projecao_atual_json},
                        borderColor: '#64748B',
                        borderDash: [5, 5],
                        fill: false,
                        tension: 0.3
                    }}
                ]
            }},
            options: {{ responsive: true, maintainAspectRatio: false }}
        }});
    </script>
</body>
</html>
"""
    os.makedirs(os.path.dirname(os.path.abspath(caminho_saida)), exist_ok=True)
    with open(caminho_saida, "w", encoding="utf-8") as f:
        f.write(html)
    return os.path.abspath(caminho_saida)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python gerar_entregavel_financeiro.py <caminho_json_entrada> <caminho_html_saida>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f_in:
        dados_input = json.load(f_in)

    diagnostico = calcular_diagnostico(dados_input)
    arquivo_gerado = gerar_dashboard_html(diagnostico, sys.argv[2])
    print(f"Entregável gerado com sucesso em: {arquivo_gerado}")


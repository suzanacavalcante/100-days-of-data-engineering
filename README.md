# 💱 Day 01: ETL de Cotação de Moedas (Polars Edition)

O primeiro dia do desafio foca na construção de um pipeline de ingestão clássico (ETL), consumindo dados financeiros reais e aplicando transformações estruturadas.

## 🎯 Objetivo
Extrair cotações de moedas (USD, EUR, BTC) em relação ao Real (BRL) via API, tratar os tipos de dados e armazenar em formatos otimizados para análise.

## 🛠️ Stack Técnica
- **Linguagem:** Python 3.10+
- **Ingestão:** `httpx` (Cliente HTTP moderno e assíncrono)
- **Processamento:** `Polars` (Lightning-fast DataFrame library)
- **Armazenamento:** `Parquet` (Colunar/Performance) e `CSV` (Interoperabilidade)

## 🏗️ Arquitetura do Pipeline



1.  **Extract:** Consumo da `AwesomeAPI` para obter dados em tempo real.
2.  **Transform:** * Conversão de tipos (Strings para `Float64`).
    * Parsing de datas (Strings para `Datetime`).
    * Renomeação de colunas para padrão de negócio.
3.  **Load:** Persistência em camada local (`/data`) nos formatos Parquet e CSV.

## 🚀 Como Executar

1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   python main.py

## 🛠️ Stack Técnica
O pipeline gera os seguintes campos tratados:
| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| moeda | String | Código da moeda (USD, EUR, BTC) |
| cotacao | Float64 | Valor de compra (bid) atualizado |
| variacao_percentual | Float64 | Porcentagem de variação no dia |
| data_consulta | Datetime | Timestamp exato da cotação |

---

Este projeto faz parte do desafio #100DaysOfDataEngineering
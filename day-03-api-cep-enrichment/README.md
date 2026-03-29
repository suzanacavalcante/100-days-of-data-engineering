# 📍 Day 03: Enriquecimento de Dados via API (ViaCEP)

No terceiro dia, exploramos o conceito de **Data Enrichment** (Enriquecimento de Dados). O objetivo foi transformar um dado simples e isolado (CEP) em um conjunto de informações geográficas estruturadas.

## 🎯 Objetivo
Desenvolver um pipeline que receba uma lista de códigos postais, realize o tratamento de strings, consulte uma API externa de forma resiliente e consolide os endereços em um DataFrame de alta performance.

## 🛠️ Stack Técnica
- **Linguagem:** Python 3.10+
- **Comunicação HTTP:** `httpx` (com tratamento de timeouts)
- **Processamento Colunar:** `Polars`
- **Armazenamento:** `Parquet` (eficiência de compressão)

## 🏗️ Lógica de Engenharia e Resiliência
Para garantir que o processo não falhe em ambientes de produção (como o setor bancário), aplicamos:

1. **Sanitização de Input:** Limpeza de caracteres especiais (`-`, espaços) para garantir que a API receba apenas números.
2. **Defensive Programming:** Tratamento de CEPs inexistentes ou mal formatados, evitando que o script interrompa a execução (Graceful Degradation).
3. **Rate Limiting (Polidez de API):** Implementação de `time.sleep(0.2)` para respeitar os limites da API gratuita e evitar bloqueios de IP.
4. **Data Type Handling:** Correção de bugs de iteração, garantindo que o input seja tratado como uma lista, evitando o desmembramento de strings.

## 🚀 Como Executar
1. **Instale as dependências:**
```bash
   pip install -r requirements.txt
```

2. **Rode o enriquecedor:**
```bash
    python main.py
```

3. **Digite o CEP desejado**

## 📊 Estrutura do Dataset Gerado
O arquivo ceps_enriquecidos.parquet contém:

- cep: O código postal original.
- logradouro/bairro/localidade/uf: Dados geográficos detalhados.
- status: Indicador de sucesso ou erro na busca.

Este projeto faz parte do desafio #100DaysOfDataEngineering
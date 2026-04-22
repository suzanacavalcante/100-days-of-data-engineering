# 📊 Dia 19: Pipeline de Análise de Sentimentos (NLP)
O foco é a transformação de dados não estruturados em métricas quantitativas de negócio.

---

## 📝 Descrição do Projeto
O objetivo é processar feedbacks de clientes armazenados em formato CSV e extrair o sentimento predominante (Positivo, Negativo ou Neutro). Este pipeline simula o processo de enriquecimento de dados (Data Enrichment), onde transformamos texto bruto em indicadores de performance (KPIs) de satisfação.

Destaques Técnicos:
- Ingestão de Dados: Leitura robusta de arquivos .csv utilizando o módulo nativo csv.DictReader.

- Sanitização de Texto: Pipeline de limpeza que remove pontuações e padroniza o texto em minúsculas para evitar ruído na análise.

- Processamento de Linguagem Natural (NLP): Utilização da biblioteca TextBlob para cálculo de polaridade textual.

- Acurácia por Idioma: Otimização do dataset para o idioma nativo da biblioteca (Inglês), garantindo resultados mais precisos sem a necessidade de camadas extras de tradução.

---

## 📂 Estrutura de Arquivos

```bash
dia19-sentiment-analysis/
├── feedbacks.csv       # Dataset com os comentários dos clientes
├── main.py             # Script de processamento e análise
└── README.md           # Documentação do desafio
```

---

## 🚀 Como Executar
1. Requisitos
Certifique-se de ter a biblioteca necessária instalada:

```bash
pip install textblob
```

2. Preparação do CSV
O arquivo feedbacks.csv deve conter uma coluna chamada texto com frases em inglês para máxima precisão:
```bash
The application is much faster after the update!
I cannot access my account, it keeps showing an error.
...
```

3. Execução
Rode o analisador:

```bash
python main.py
```

## 🧠 Aprendizados do Dia 19
- Data Enrichment: Aprender a gerar novas colunas de metadados a partir de dados existentes.

- Polaridade de Texto: Entender o conceito de score de sentimento (variando de -1 a 1).

- Trade-offs de Engenharia: A decisão de utilizar dados em inglês para aproveitar a máxima performance de uma biblioteca específica em vez de introduzir latência com APIs de tradução.
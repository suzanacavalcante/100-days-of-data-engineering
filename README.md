# 🚀 100 Days of Data Engineering Challenge

Este repositório contém a minha jornada de 100 dias focada em **Engenharia de Dados**. O objetivo é evoluir de scripts de automação Python até arquiteturas escaláveis em Cloud, Streaming e Governança.

## 📌 O Desafio
- **Início:** 25 de Março de 2026
- **Término Previsto:** 03 de Julho de 2026
- **Frequência:** 1 projeto por dia
- **Foco Técnico:** Python, SQL, Docker, Spark, Airflow, Kafka e Cloud (AWS/GCP).

---

## 🗺️ Cronograma de Evolução

### 🟦 Fase 1: Fundamentos e Ingestão (Dias 01-25)
*Foco em Python puro, APIs, Web Scraping e manipulação de arquivos.*
- [ ] Dia 01: ETL de Câmbio (Consumo de API e salvamento em CSV)
- [ ] Dia 02: Scraper de Notícias (Coleta de manchetes de portais financeiros)
- [ ] Dia 03: Localizador de CEP em Massa (API de CEP + tratamento de erros)
- [ ] Dia 04: Log Parser (Extração de erros 404/500 de arquivos .log)
- [ ] Dia 05: Validação com Pydantic (Garantindo esquemas de JSON)
- [ ] Dia 06: Conversor Parquet (Transformando XML/JSON em formato colunar)
- [ ] Dia 07: Monitor de Preços (Comparação de produtos entre e-commerces)
- [ ] Dia 08: Categorizador de Gastos (Processamento de faturas bancárias CSV)
- [ ] Dia 09: SQLite Manager (Criação de DB local e queries de agregação)
- [ ] Dia 10: Data Profiling Auto (Geração de relatório de nulos e outliers)
- [ ] Dia 11: Pokedex API (Refatoração com paginação e filtros de tipo)
- [ ] Dia 12: Email Attachment Downloader (Automação de recebimento de bases)
- [ ] Dia 13: Deduplicador de Registros (Algoritmo de limpeza de bases grandes)
- [ ] Dia 14: Geocodificação (Endereços -> Latitude/Longitude via API)
- [ ] Dia 15: Gerador de Dados Sintéticos (Uso da lib Faker para testes)
- [ ] Dia 16: Watchdog de Pastas (Trigger de scripts ao detectar novos arquivos)
- [ ] Dia 17: Slack/Teams Alert Bot (Notificação de falhas em jobs Python)
- [ ] Dia 18: Backup Rotativo (Compressão e rotulagem de arquivos históricos)
- [ ] Dia 19: Análise de Sentimento (Processamento de feedbacks de clientes)
- [ ] Dia 20: Histórico Climático (Ingestão de dados de tempo por 24h)
- [ ] Dia 21: CLI Dashboard (Visualização de dados no terminal com Rich)
- [ ] Dia 22: Selenium Scraper (Coleta de dados em sites com login/JS)
- [ ] Dia 23: Sanitização de Strings (Padronização de nomes e endereços)
- [ ] Dia 24: Cálculo de KPIs de Negócio (Churn, LTV via script)
- [ ] Dia 25: Refatoração POO (Aplicar Design Patterns no projeto do Dia 01)

### 🟨 Fase 2: Armazenamento e Orquestração (Dias 26-50)
*Foco em Bancos de Dados, Docker e Airflow.*
- [ ] Dia 26: PostgreSQL no Docker (Setup de banco relacional)
- [ ] Dia 27: Modelagem Star Schema (Desenho de Fatos e Dimensões)
- [ ] Dia 28: Migração de Dados (Carga do SQLite/CSV para Postgres)
- [ ] Dia 29: SQLAlchemy ORM (Interface Python para gestão de DB)
- [ ] Dia 30: SCD Tipo 1 (Implementação de sobrescrita de dados)
- [ ] Dia 31: SCD Tipo 2 (Implementação de histórico de versões)
- [ ] Dia 32: Setup Apache Airflow (Ambiente via Docker Compose)
- [ ] Dia 33: Minha Primeira DAG (Fluxo básico de dependências)
- [ ] Dia 34: Orquestração de ETL (Rodando o script do Dia 01 via Airflow)
- [ ] Dia 35: Airflow Sensors (Aguardando arquivos para iniciar o fluxo)
- [ ] Dia 36: MongoDB (Ingestão de dados não estruturados JSON)
- [ ] Dia 37: Redis Cache (Otimizando consultas repetitivas)
- [ ] Dia 38: Pipeline Cripto (Coleta e armazenamento horário via Airflow)
- [ ] Dia 39: Modelagem Data Vault (Criação de Hubs e Satellites básicos)
- [ ] Dia 40: Window Functions (Limpeza de duplicados via SQL avançado)
- [ ] Dia 41: Backup Cloud Automático (Upload de dump do banco para Storage)
- [ ] Dia 42: DVC (Data Version Control) (Controle de versão de datasets)
- [ ] Dia 43: MinIO Setup (S3 local para simular Data Lake)
- [ ] Dia 44: Camada Bronze (Ingestão raw para o MinIO)
- [ ] Dia 45: Camada Silver (Tratamento e conversão para Parquet)
- [ ] Dia 46: Health Check Script (Monitoramento de conexões de banco)
- [ ] Dia 47: Dockerização de API (Containerizando um serviço Flask/FastAPI)
- [ ] Dia 48: SQL Tuning (Otimização de queries com Explain Analyze)
- [ ] Dia 49: Carga Incremental (Lógica de Upsert baseada em Timestamp)
- [ ] Dia 50: Documentação com dbt (Início de linhagem de dados)

### 🟧 Fase 3: Big Data e Cloud (Dias 51-75)
*Foco em Processamento Distribuído (Spark) e Infraestrutura Cloud.*
- [ ] Dia 51: PySpark Local (Leitura eficiente de datasets de 1GB+)
- [ ] Dia 52: Transformações Spark (Filter, Join e GroupBy distribuído)
- [ ] Dia 53: Spark SQL (Executando queries SQL em DataFrames
- [ ] Dia 54: Particionamento de Dados (Otimização física de storage)
- [ ] Dia 55: Cloud CLI Setup (Configuração de AWS ou Google Cloud)
- [ ] Dia 56: Infra de Storage (Criação de Buckets via código
- [ ] Dia 57: AWS Lambda / Cloud Functions (Processamento orientado a eventos)
- [ ] Dia 58: Data Catalog / Glue Crawler (Descoberta automática de esquemas)
- [ ] Dia 59: Data Warehouse Cloud (Carga de dados no BigQuery/Redshift)
- [ ] Dia 60: Apache Beam (Pipeline simples de processamento híbrido)
- [ ] Dia 61: Spark Shuffle Tuning (Ajuste de performance em joins grandes)
- [ ] Dia 62: Spark UDFs (Funções customizadas para colunas complexas)
- [ ] Dia 63: Delta Lake Implementation (Transações ACID no Data Lake)
- [ ] Dia 64: Time Travel (Consulta de versões passadas no Delta Lake)
- [ ] Dia 65: Pipeline ELT Cloud (S3 -> Glue -> Athena)
- [ ] Dia 66: Mascaramento de PII (Segurança e LGPD nos dados)
- [ ] Dia 67: Cloud Cost Alert (Script para monitorar gastos da conta)
- [ ] Dia 68: DW Views (Criação de camadas de consumo para BI)
- [ ] Dia 69: Airflow Variables & Connections (Gestão segura de credenciais)
- [ ] Dia 70: Secrets Manager (Integração de senhas com o código)
- [ ] Dia 71: Spark Cluster Scaling (Teste com diferentes configurações de Workers)
- [ ] Dia 72: Medalhão na Nuvem (Fluxo Bronze -> Silver -> Gold completo)
- [ ] Dia 73: Central de Logs (Monitoramento de erros de pipeline na Cloud)
- [ ] Dia 74: API Gateway (Servindo dados do Warehouse via endpoint)
- [ ] Dia 75: Cloud Audit Logs (Análise de quem acessou os dados)

### 🟥 Fase 4: Engenharia Avançada e Arquitetura (Dias 76-100)
*Foco em Streaming, CI/CD, Observabilidade e Kubernetes.*
- [ ] Dia 76: Apache Kafka Setup (Broker e Zookeeper via Docker)
- [ ] Dia 77: Kafka Producer (Simulação de eventos de streaming)
- [ ] Dia 78: Kafka Consumer (Persistência de mensagens em tempo real)
- [ ] Dia 79: Spark Structured Streaming (Processamento de janelas temporais)
- [ ] Dia 80: Great Expectations (Testes de qualidade automatizados)
- [ ] Dia 81: GitHub Actions CI (Testes automáticos no push do ETL)
- [ ] Dia 82: Terraform Básico (Criação de Bucket como Código)
- [ ] Dia 83: Infra completa Terraform (DB + Storage + Roles)
- [ ] Dia 84: Observabilidade (Métricas de atraso/freshness de dados)
- [ ] Dia 85: Data Lineage (Rastreamento do fluxo dos dados)
- [ ] Dia 86: Pipeline de Mídia (Extração de metadados de imagens/vídeos)
- [ ] Dia 87: Feature Store (Tabelas prontas para modelos de ML)
- [ ] Dia 88: Spark Skew Join (Resolução de desequilíbrio de dados)
- [ ] Dia 89: Kubernetes (k8s) (Rodando um job Python em cluster)
- [ ] Dia 90: Helm Charts (Empacotamento de apps de dados)
- [ ] Dia 91: Data Cataloging (Governança e busca de metadados)
- [ ] Dia 92: Pipeline de Auditoria (Registro histórico de mudanças - CDC)
- [ ] Dia 93: Blue/Green Deployment (Troca segura de tabelas em prod)
- [ ] Dia 94: Graph Database (Ingestão de conexões no Neo4j)
- [ ] Dia 95: WebSocket Streaming (Servindo dados live para o front-end)
- [ ] Dia 96: Event-Driven ETL (Trigger de pipeline via evento Kafka)
- [ ] Dia 97: Warehouse Cleanup (Identificação de tabelas "fantasmas")
- [ ] Dia 98: Disaster Recovery Test (Restauração completa de ambiente)
- [ ] Dia 99: Tech Write-up (Documentação arquitetural do portfólio)
- [ ] Dia 100: O GRANDE PROJETO (Arquitetura Completa End-to-End)

---

## 🛠️ Tecnologias Utilizadas
- **Linguagens:** Python, SQL.
- **Data Stack:** Pandas, PySpark, dbt, Airflow, Kafka.
- **Infra & DevOps:** Docker, Kubernetes, Terraform, GitHub Actions.
- **Cloud:** AWS/GCP (Storage, Data Warehouse, Functions).

---

## 📈 Progresso
| Fase | Status | Progresso |
| :--- | :---: | :--- |
| **Fase 1: Fundamentos** | 🏗️ Em progresso | 4% (1/25) |
| **Fase 2: Orquestração** | ⏳ Aguardando | 0% |
| **Fase 3: Big Data/Cloud** | ⏳ Aguardando | 0% |
| **Fase 4: Avançado** | ⏳ Aguardando | 0% |

---
*“A consistência é o que transforma a média em excelência.”* 🚀

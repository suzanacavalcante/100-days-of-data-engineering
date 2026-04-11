# 🛰️ Dia 16: Watchdog de Pastas (Event-Driven Automation)

## 🎯 Objetivo
Implementar um sistema de monitoramento de diretórios capaz de disparar gatilhos (triggers) automáticos assim que novos arquivos são detectados.

## 🚀 Tecnologias
- Watchdog: Monitoramento de eventos de baixo nível do sistema de arquivos.
- Python OS/Time: Gerenciamento de processos e caminhos.

## 🛠️ O que foi feito
- Criação de um FileSystemEventHandler customizado para filtrar eventos de criação de arquivos.
- Lógica de filtragem para processar apenas arquivos .csv.
- Implementação de um loop de observação que consome o mínimo de recursos do sistema enquanto aguarda novos dados.

## 💡 Aplicação Real
Este padrão é amplamente utilizado em áreas de ingestão de dados para:
- Detectar a chegada de logs de servidores.
- Processar automaticamente planilhas enviadas por e-mail ou FTP.
- Iniciar pipelines de ETL assim que os dados brutos (Raw) aterrissam no Data Lake.
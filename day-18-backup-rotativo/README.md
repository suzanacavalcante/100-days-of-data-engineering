# 📦 Dia 18: Backup Rotativo Automático
O objetivo é garantir a integridade e a persistência dos dados através de um sistema de compressão com política de retenção (logística de "house-keeping").

---

## 📝 Descrição do Projeto
Na engenharia de dados, arquivos de logs e bases temporárias podem consumir rapidamente o armazenamento do servidor. Este script resolve o problema automatizando a compactação de diretórios e mantendo apenas as versões mais recentes, otimizando o espaço em disco.

Principais Funcionalidades:
Compressão ZIP: Utiliza a biblioteca zipfile para reduzir o tamanho dos arquivos históricos.

Rotatividade (Retention Policy): Mantém apenas os N backups mais recentes, removendo automaticamente os antigos.

Resolução de Caminhos Dinâmicos: Uso do pathlib para suportar caminhos relativos (como ../) de forma robusta entre diferentes sistemas operacionais.

Prevenção de Arquivos Vazios: O script valida se a pasta de origem contém dados antes de gerar o arquivo de backup.

---

## 📂 Estrutura do Projeto
```bash
dia18-backup-rotativo/
├── backups/            # Destino dos arquivos compactados (.zip)
├── dia18_backup.py     # Script principal com a lógica de BackupManager
└── README.md           # Documentação do desafio
```

---

## 🚀 Como Utilizar
1. Configuração
O script está configurado para buscar a pasta de logs do desafio anterior. Certifique-se de que a estrutura de pastas está correta ou ajuste o source_dir no bloco main:

```bash
manager = BackupManager(
    source_dir='../day-17-sla-health-check/logs',
    backup_dir='backups',
    keep_last=3
)
```

2. Execução
Execute o script para gerar o backup:

```Bash
python main.py
```

O terminal exibirá o log de cada arquivo adicionado e informará se algum backup antigo foi removido para respeitar o limite de retenção.

## 🧠 Aprendizados do Dia 18
Gestão de Ciclo de Vida: Implementação de lógica de retenção, um conceito chave em FinOps e gestão de Data Lakes.

Manipulação de Binários: Trabalho com compressão de arquivos em memória e escrita em disco.

Caminhos Absolutos vs Relativos: Uso do .resolve() para evitar quebras de scripts causadas por diretórios de execução inconsistentes.
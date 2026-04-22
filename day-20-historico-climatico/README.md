# ☁️ Dia 20: Ingestão de Dados Climáticos (API REST)
O objetivo principal é automatizar o consumo de dados de uma API externa e estruturá-los para armazenamento local.

---

## 📝 Descrição do Projeto
Na engenharia de dados, a coleta de dados de fontes externas via API é uma das tarefas mais comuns. Este script consome dados meteorológicos em tempo real (temperatura, umidade e probabilidade de chuva) para as próximas 24 horas, transformando um payload JSON complexo num ficheiro CSV estruturado.

Principais Funcionalidades:
- Consumo de API REST: Integração com a API Open-Meteo utilizando a biblioteca requests.

- Tratamento de JSON: Extração e normalização de dados aninhados para um formato tabular.

- Persistência de Dados: Armazenamento em CSV com lógica de "append" para criação de histórico.

- Resumo Estatístico: Cálculo rápido de métricas (Máxima, Mínima e Média) diretamente no terminal.

---

## 📂 Estrutura de Ficheiros

```bash
dia20-historico-climatico/
├── historico_climatico.csv  # Base de dados local acumulada
├── main.py                  # Script de ingestão e processamento
└── README.md                # Documentação do desafio
```

## 🚀 Como Executar
1. Instalação das Dependências
É necessário ter a biblioteca requests instalada:

```bash
pip install requests
```

2. Configuração de Localização
O script está configurado por defeito para as coordenadas de São Paulo/Osasco, mas pode ser alterado no bloco if __name__ == "__main__": modificando as variáveis LAT e LON.

3. Execução
Execute o pipeline de ingestão:

```bash
python main.py
```

---

## 🧠 Aprendizados do Dia 20
- Status Codes: Implementação de verificações de erro para garantir que a API respondeu corretamente (Status 200).

- Normalização de Dados: Transformar listas independentes dentro de um JSON numa estrutura de linhas e colunas.

- Idempotência: O script foi desenhado para ser executado múltiplas vezes, adicionando novos dados sem apagar o histórico existente.
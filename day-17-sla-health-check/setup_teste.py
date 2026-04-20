import os
import time
from datetime import datetime, timedelta

def preparar_cenario_teste(pasta_logs="logs"):
    # 1. Criar a pasta se não existir
    if not os.path.exists(pasta_logs):
        os.makedirs(pasta_logs)
        print(f"✅ Pasta '{pasta_logs}' criada.")

    # 2. Simular Job Saudável (Sucesso recente)
    # Criamos o arquivo agora mesmo
    with open(os.path.join(pasta_logs, "job_extracao_banco.success"), "w") as f:
        f.write("Sucesso")
    print("✅ Criado: job_extracao_banco.success (Saudável)")

    # 3. Simular Job com Erro
    # Criamos um arquivo .error com uma mensagem de exception
    with open(os.path.join(pasta_logs, "job_limpeza_dados.error"), "w") as f:
        f.write("Traceback (most recent call last):\n")
        f.write("  File 'main.py', line 42, in <module>\n")
        f.write("KeyError: 'coluna_vendas_obrigatoria_nao_encontrada'")
    print("❌ Criado: job_limpeza_dados.error (Falha)")

    # 4. Simular Job que furou o SLA (Atrasado)
    # Criamos o arquivo e alteramos a data de modificação para 3 dias atrás
    caminho_atrasado = os.path.join(pasta_logs, "job_consolidacao_mensal.success")
    with open(caminho_atrasado, "w") as f:
        f.write("Sucesso antigo")
    
    # Retroceder o 'mtime' (data de modificação) do arquivo
    tres_dias_atras = time.time() - (3 * 24 * 60 * 60)
    os.utime(caminho_atrasado, (tres_dias_atras, tres_dias_atras))
    print("⚠️  Criado: job_consolidacao_mensal.success (Fora do SLA - 3 dias atrás)")

    print("\n--- Tudo pronto! Agora execute o seu script de Monitoramento ---")

if __name__ == "__main__":
    preparar_cenario_teste()
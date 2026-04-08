import polars as pl
import numpy as np
from datetime import datetime, timedelta

def gerar_base_suja(n_rows=100000):
    print(f"🏗️ Gerando base de teste com {n_rows} linhas...")
    
    # Criando dados base
    ids = np.random.randint(1000, 5000, n_rows)
    valores = np.round(np.random.uniform(10.0, 500.0, n_rows), 2)
    
    # Gerando datas aleatórias nos últimos 30 dias
    data_inicial = datetime(2026, 3, 1)
    datas = [data_inicial + timedelta(days=int(d)) for d in np.random.randint(0, 30, n_rows)]

    df = pl.DataFrame({
        "ID_CLIENTE": ids,
        "DATA_VENDA": datas,
        "VALOR": valores,
        "STATUS": ["CONCLUIDO"] * n_rows
    })

    # Duplicando dados -> 10%
    n_duplicatas = int(n_rows * 0.1)
    df_duplicado = df.sample(n_duplicatas)

    df_final = pl.concat([df, df_duplicado])
    
    df_final = df_final.sample(fraction=1.0, shuffle=True)
    
    # Salvando
    df_final.write_csv("vendas_sujas.csv")
    print(f"✅ Arquivo 'vendas_sujas.csv' gerado com {df_final.height} linhas!")
    
if __name__ == "__main__":
    gerar_base_suja()
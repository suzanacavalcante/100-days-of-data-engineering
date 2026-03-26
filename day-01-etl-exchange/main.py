import polars as pl
import httpx
import os

from datetime import datetime

# Extração de Dados
def extract_exchange_data(coins: str):
    """ 
    Extrai dados de cotação de moedas da AwesomeAPI
    """

    url = f"https://economia.awesomeapi.com.br/last/{coins}"

    try:
        response = httpx.get(url)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        print(f"Erro ao acessar API: {e}")

# Transformação de Dados
def transform_data(raw_data: dict):
    """
    Transforma o JSON bruto em um DataFrame Polars limpo
    """

    data_list = [value for value in raw_data.values()]

    df = pl.DataFrame(data_list)

    df = df.select([
        pl.col('code').alias('moeda'),
        pl.col('bid').cast(pl.Float64).alias('cotacao'),
        pl.col('pctChange').cast(pl.Float64).alias('variacao_percentual'),
        pl.col('create_date').str.to_datetime().alias('data_consulta')
    ])

    return df

# Carregamento de Dados
def load_data(df: pl.DataFrame):
    """
    Salva os dados em formatos otimizados
    """

    output_dir = 'data'
    os.makedirs(output_dir, exist_ok=True)

    df.write_parquet(f'{output_dir}/exchange_rates.parquet')
    df.write_csv(f'{output_dir}/exchange_rates.csv')


if __name__ == '__main__':
    print('Iniciando ETL de Câmbio')

    raw_data = extract_exchange_data('USD-BRL,EUR-BRL,BTC-BRL')

    if raw_data:
        df_clean = transform_data(raw_data)
        print(df_clean)
        load_data(df_clean)
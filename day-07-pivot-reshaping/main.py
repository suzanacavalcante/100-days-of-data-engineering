import polars as pl 

def processar_vendas_reais():
    # Ingestão dos Dados
    print('Lendo base de vendas brutas...')
    df = pl.read_csv('vendas_brutas.csv', try_parse_dates=True)

    # Extraindo o mês da data
    df = df.with_columns(
        pl.col('data').dt.month().alias('mes_num')
    )

    # Pivot: Categorias nas linhas e Regiões nas colunas
    print('Pivotando dados por Região')
    df_pivot = df.pivot(
        values='valor',
        index='categoria',
        on='regiao',
        aggregate_function='sum'
    ).fill_null(0) # Substittui onde não houve venda por 0

    print('Matriz de Vendas por Categoria e Região:')
    print(df_pivot)

    # Exportando Insight
    df_pivot.write_csv('insight_regional_vendas.csv')
    print('Relatório gerado: insight_regional_vendas.csv')

if __name__ == '__main__':
    processar_vendas_reais()
import polars as pl 

def categorizar_fatura():
    # Ingestão
    df = pl.read_csv('fatura.csv')

    # Mapeamento de Palavras-Chave
    categorias = {
        'IFOOD': 'Alimentação',
        'RESTAURANTE': 'Alimentação',
        'BURGER KING': 'Alimentação',
        'UBER': 'Transporte',
        'SHELL': 'Transporte',
        'NETFLIX': 'Assinaturas',
        'MERCADO LIVRE': 'Compras'
    }
    # Em um projeto da vida real isso viria de uma tabelade referencia ou modelo de ML

    # Lógica de Categorização
    expressao = pl.when(pl.col('estabelecimento').str.contains('IFOOD|RESTAURANTE|BURGER KING')).then(pl.lit('Alimentação')) \
                .when(pl.col('estabelecimento').str.contains('UBER|SHEL')).then(pl.lit('Transporte')) \
                .when(pl.col('estabelecimento').str.contains('NETFLIX')).then(pl.lit('Assinaturas')) \
                .otherwise(pl.lit('Outros'))

    df = df.with_columns(expressao.alias('categoria'))

    # Agregação
    resumo = df.group_by('categoria').agg(
        pl.col('valor').sum().alias('total_gasto'),
        pl.col('categoria').count().alias('qtd_transacoes')
    ).sort('total_gasto', descending=True)

    print('Relatório de Gastos Mensais:')
    print(resumo)

    # Exportação
    resumo.write_csv('resumo_financeiro.csv')
    print('Relatório gerado com sucesso!')

if __name__ == '__main__':
    categorizar_fatura()
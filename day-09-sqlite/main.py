import polars as pl 
from sqlalchemy import create_engine

def gerenciar_sqlite():
    # Extração
    try:
        df = pl.read_csv("day-08-categorizador/resumo_financeiro.csv")
    except:
        # Fallback caso o arquivo não esteja acessível 
        df = pl.DataFrame({
            'categoria': ['Alimentação', 'Transporte', 'Assinaturas'],
            'total_gasto': [162.50, 225.00, 55.90],
            'qtd_transacoes': [3, 2, 1]
        })

    # Conectando com o  SQLite local
    engine = create_engine('sqlite:///meu_financeiro.db')

    # Load do DataFrame no banco de dados
    df.write_database(
        table_name = 'resumo_gastos',
        connection = engine,
        if_table_exists = 'replace'
    )

    print('Dados persistiidos no SQLite (meu_financeiro.db)')

    # Query de Agregação (SQL Puro)
    query = """
        SELECT
            SUM(total_gasto) as gasto_global,
            AVG(total_gasto) as media_por_categoria,
            MAX(total_gasto) as maior_gasto_categoria
        FROM resumo_gastos
    """

    # Lendo o resulto da query
    insight_sql = pl.read_database(query = query, connection = engine)

    print('Insight Agregado via SQL: ')
    print(insight_sql)

if __name__ == "__main__":
    gerenciar_sqlite()
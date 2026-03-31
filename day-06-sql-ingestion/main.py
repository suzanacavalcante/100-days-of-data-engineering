import polars as pl 

from sqlalchemy import create_engine

def extrair_insight_corporativo():
    # Conexão com o banco de dados
    engine = create_engine('sqlite:///corporativo.db')

    # Query complexa: Une as tabelas e calcula a média salarial
    query = """
    SELECT
        d.nome AS departamento,
        AVG(f.salario) AS media_salarial,
        COUNT(f.id) AS total_colaboradores
    FROM funcionarios f
    JOIN departamentos d ON f.dept_id = d.id
    GROUP BY d.nome
    ORDER BY media_salarial DESC
    """

    # Lê a Query e fazer um DataFrame estruturado
    df_insight = pl.read_database(query=query, connection=engine)

    return df_insight

if __name__ == '__main__':
    relatorio = extrair_insight_corporativo()

    print('\nRelatório Executivo: Média Salarial por Depto')
    print(relatorio)

    # Salvar o resultado final 
    relatorio.write_csv('insight_salarial.csv')
    print('\nInsight exportado para CSV.')
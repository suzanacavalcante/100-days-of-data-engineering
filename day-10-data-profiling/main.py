import polars as pl 

def gerar_profiling(caminho_csv):
    # Ingestão
    df = pl.read_csv(caminho_csv)
    total_linhas = df.height

    print(f'Analiasndo Dataset: {caminho_csv} ({total_linhas} linhas)')
    print('-' * 50)

    # Análise de Nulos
    nulos = df.null_count()

    # Análise Estatística
    stats = df.describe()

    # Construindo o Relatório de Saúde
    relatorio = []
    for col in df.columns:
        # Contagem de Nulos
        count_nulos = nulos[col][0]
        perc_nulos = (count_nulos / total_linhas) * 100

        # Tipo de Dados
        dtype = str(df[col].dtype)

        # Identificação de Outliers
        outlier_msg = "N/A"
        if df[col].dtype.is_numeric():
            mean = df[col].mean()
            std = df[col].std()

            # Desvio padrão > 3
            limite = mean + (3 * std)
            outliers_count = df.filter(pl.col(col) > limite).height
            outlier_msg = f'{outliers_count} detectados'

            relatorio.append({
                'coluna': col,
                'tipo': dtype,
                'nulos_abs': count_nulos,
                'nulos_perc': f'{perc_nulos:.2f}%',
                'outliers_3std': outlier_msg
            })
    
    # Output final
    df_profiling = pl.DataFrame(relatorio)
    print(df_profiling)

    # Exportar para auditoria
    df_profiling.write_csv('data_health_report.csv')
    print('Relatório "data_health_report.csv" gerado!')

if __name__ == "__main__":
    gerar_profiling('../day-08-categorizador/fatura.csv')
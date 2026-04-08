import polars as pl 

def limpar_base(input_file, output_file):
    print(f'Carregando dados: {input_file}')

    df = pl.read_csv(input_file)

    total_antes = df.height

    df_limpo = df.unique(
        subset=['ID_CLIENTE', 'DATA_VENDA', 'VALOR'],
        keep='first',
        maintain_order=True
    )

    total_depois = df_limpo.height
    removidos = total_antes - total_depois

    df_limpo.write_csv(output_file)

    print('-' * 30)
    print(f'Limpeza concluída!')
    print(f'Registros Iniciais: {total_antes}')
    print(f'Registros Removidos: {removidos}')
    print(f'Arquivo final: {output_file}')

if __name__ == '__main__':
    limpar_base('vendas_sujas.csv', 'vendas_limpas.csv')
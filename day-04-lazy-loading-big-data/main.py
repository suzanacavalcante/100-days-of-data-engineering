import polars as pl
import re

def parse_server_logs(log_path: str):
    """
    Lê o arquivo de log e extrai apenas os erros 404 e 500
    """
    extracted_data = []

    # Este Regex captura o ID, Data, Método, URL e Status
    regex_pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>.*?)\] "(?P<metodo>\w+) (?P<url>\S+) .*?" (?P<status>\d+) \d+'

    try:
        with open(log_path, 'r') as file:
            for line in file:
                match = re.search(regex_pattern, line)
                if match:
                    data = match.groupdict()
                
                    if data['status'] in ['404', '500']:
                        extracted_data.append(data)
        
        df = pl.DataFrame(extracted_data)

        df = df.with_columns(pl.col('status').cast(pl.Int32))

        return df
    
    except FileNotFoundError:
        print(f'Erro: o arquivo {log_path} não foi encontrado!')
        return None
    
if __name__ == '__main__':
    path = 'server_access.log'
    df_erros = parse_server_logs(path)

    if df_erros is not None and not df_erros.is_empty():
        print('\n--- Relatório de Erros Identificados (Status 404/500)')
        print(df_erros)

        df_erros.write_parquet('erros_analisados.parquet')
        print('\nInsight exportado para erros_analisados.parquet')
    else:
        print('Nenhum erro encontrado ou arquivo vazio.')
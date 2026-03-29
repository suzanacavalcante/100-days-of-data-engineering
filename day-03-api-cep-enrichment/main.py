import polars as pl 
import httpx
import time 
import os

def get_address(cep: str):
    """
    Consulta a API ViaCEP para retornar dados do endereço.
    """

    # Limpeza
    cep = cep.replace('-', '').replace(' ', '')
    url = f'https://viacep.com.br/ws/{cep}/json'

    try:
        response = httpx.get(url, timeout=10.0)
        if response.status_code == 200:
            data = response.json()

            # A API retorna erro para CEPs inexistentes
            if 'erro' in data:
                return {
                    'cep': cep,
                    'status': 'Não encontrado'
                }
            return {
                'cep': data.get('cep'),
                'logradouro': data.get('logradouro'),
                'bairro': data.get('bairro'),
                'localidade': data.get('localidade'),
                'uf': data.get('uf'),
                'status': 'Sucesso'
            }
    
    except Exception as e:
        return {
            'cep': cep,
            'status': 'Falha na requisição'
        }
    
def run_enrichment(cep_list: list):
    """
    Percorre a lista de CEPs e consolida em um DataFrame.
    """
    results = []
    print(f'Processando {len(cep_list)} CEPs...')

    for cep in cep_list:
        address = get_address(cep)
        results.append(address)
        # Um breve delay para evitar sobrecarga na API
        time.sleep(0.2)
    
    return pl.DataFrame(results)

if __name__ == '__main__':
    cep = input('Digite o CEP: ')

    df_endereco = run_enrichment([cep])

    print('\n--- Resultado do Enriquecimento ---')
    print(df_endereco)

    # Salvar os dados
    output_dir = 'data'
    os.makedirs(output_dir, exist_ok=True)
    df_endereco.write_parquet(f'{output_dir}/ceps.enriquecidos.parquet')
    print(f'\nDados salvos em {output_dir}')
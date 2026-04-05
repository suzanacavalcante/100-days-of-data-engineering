import requests
import polars as pl 

def extrair_pokedex(limite_por_pagina=20, total_desejado=60):
    url_base = 'https://pokeapi.co/api/v2/pokemon'
    todos_pokemons = []

    print(f'Iniciando extração de {total_desejado} Pokémons...')
    
    # Lógica de Paginação
    for offset in range(0, total_desejado, limite_por_pagina):
        params = {'limit': limite_por_pagina, 'offset': offset}
        response = requests.get(url_base, params=params)
        data = response.json()

        for item in data['results']:
            # Obtendo detalhes
            detalhes = requests.get(item['url']).json()

            todos_pokemons.append({
                'id': detalhes['id'],
                'nome': detalhes['name'],
                'peso': detalhes['weight'],
                'altura': detalhes['height'],
                'tipo': detalhes['types'][0]['type']['name']
            })

        print(f'Processadas {offset + limite_por_pagina} entradas...')
    
    # Transformação
    df = pl.DataFrame(todos_pokemons)

    # Apenas tipos 'fire' e 'water' com peso > 100
    df_filtrado = df.filter(
        (pl.col('tipo').is_in(['fire', 'water'])) &
        (pl.col('peso') > 100)
    )

    print('Pokémons de Fogo/Água Pesados:')
    print(df_filtrado)

    # Exportação
    df_filtrado.write_csv('pokedex_filtrada.csv')
    print(f'Dataset exportado: {df_filtrado}')

if __name__ == '__main__':
    extrair_pokedex()
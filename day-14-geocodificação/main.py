import polars as pl 
import time

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

def geocodificar_enderecos():
    df = pl.DataFrame({
        "local": ["Cidade de Deus, Osasco, Bradesco", "Avenida Paulista, 1000, SP", "Cristo Redentor, RJ"]
    })

    print ('Inicializando serviço de geocodificação...')

    geolocator = Nominatim(user_agent='suzana_data_challege_day14')

    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

    lats = []
    lons = []

    print('Buscando coordenadas')
    for endereco in df['local']:
        try:
            location = geocode(endereco)
            if location:
                lats.append(location.latitude)
                lons.append(location.longitude)
                print(f'{endereco} encontrado!')
            else:
                lats.append(None)
                lons.append(None)
        except Exception as e:
            print(f'Erro ao buscar {endereco}: {e}')
            lats.append(None)
            lons.append(None)
    
    df = df.with_columns([
        pl.Series('latitude', lats),
        pl.Series('longitude', lons)
    ])

    print('\n--- Resultado Final ---')
    print(df)

    df.write_csv('endereco_geocodificado.csv')

if __name__ == '__main__':
    geocodificar_enderecos()
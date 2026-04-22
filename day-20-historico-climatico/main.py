import requests
import csv 
import os

from datetime import datetime

class WeatherIngestion:
    def __init__(self, lat: float, lon: float):
        self.url = "https://api.open-meteo.com/v1/forecast"
        self.params = {
            'latitude': lat,
            'longitude': lon,
            'hourly': "temperature_2m,relative_humidity_2m,precipitation_probability",
            'timezone': 'America/Sao_Paulo',
            'forecast_day': 1
        }
        self.filename = 'historico_climatico.csv'

    def fetch_data(self):
        print('Acessando a API Open-Meteo')
        response = requests.get(self.url, params=self.params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f'Erro na API: {response.status_code}')
    
    def process_and_save(self, data):
        if not data or 'hourly' not in data:
            return 
        
        hourly_data = data['hourly']

        timestamps = hourly_data['time']
        temps = hourly_data['temperature_2m']
        humidity = hourly_data['relative_humidity_2m']
        precip = hourly_data['precipitation_probability']

        print(f'Processando {len(timestamps)} registros horários')

        file_exists = os.path.exists(self.filename)

        with open(self.filename, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)

            if not file_exists:
                writer.writerow(['timestamp', 'temperatura_c', 'umidade_relativa', 'prob_precipitacao'])
            
            for i in range(len(timestamps)):
                writer.writerow([
                    timestamps[i], 
                    temps[i], 
                    humidity[i], 
                    precip[i]
                ])
        
        print(f'Dados salvos com sucesso em: {self.filename}')

    def show_summary(self, data):
        """Mostra um resumo rápido no terminal"""
        temps = data['hourly']['temperature_2m']
        max_temp = max(temps)
        min_temp = min(temps)
        avg_temp = sum(temps) / len(temps)

        print(f"\n{'='*40}")
        print(f"🌡️  RESUMO CLIMÁTICO (PRÓXIMAS 24H)")
        print(f"{'='*40}")
        print(f"Máxima: {max_temp}°C")
        print(f"Mínima: {min_temp}°C")
        print(f"Média:  {avg_temp:.2f}°C")
        print(f"{'='*40}")

if __name__ ==  '__main__':
    # Coordenadas de São Paulo/Osasco
    LAT = -23.5329
    LON = -46.7917

    pipeline = WeatherIngestion(LAT, LON)
    raw_data = pipeline.fetch_data()

    if raw_data:
        pipeline.process_and_save(raw_data)
        pipeline.show_summary(raw_data)
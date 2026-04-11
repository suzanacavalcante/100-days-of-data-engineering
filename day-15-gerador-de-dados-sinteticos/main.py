import polars as pl 
import random 

from faker import Faker

def gerador_dados_falsos(quantidade=1000):
    fake = Faker('pt-BR')

    print(f'Gerando {quantidade} registros sintéticos...')

    dados = []

    for _ in range(quantidade):
        dados.append({
            "nome": fake.name(),
            "cpf": fake.cpf(),
            "email": fake.email(),
            "data_nascimento": fake.date_of_birth(minimum_age=18, maximum_age=80).strftime("%Y-%m-%d"),
            "endereco": fake.address().replace("\n", ", "),
            "cidade": fake.city(),
            "estado_sigla": fake.state_abbr(),
            "salario_pretendido": round(random.uniform(2500, 15000), 2)
        })
    
    df = pl.DataFrame(dados)

    print('\n--- Amostra dos Dados Gerados ---')
    print(df.head())

    df.write_csv('usuarios_sinteticos.csv')
    print(f"\nArquivo gerado com sucesso!")

if __name__ == '__main__':
    gerador_dados_falsos(5000)
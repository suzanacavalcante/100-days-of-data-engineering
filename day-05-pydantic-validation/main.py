import json
import polars as pl 

from pydantic import BaseModel, EmailStr, Field, PositiveInt, ValidationError
from typing import List, Dict, Any

# Definindo o Data Contract
class UserSchema(BaseModel):
    id: PositiveInt
    nome: str = Field(min_length=2) # Deve ter pelo menos 2 caracteres
    email: EmailStr
    valor_assinatura: float = Field(greater_than=0) # Deve ser maior que zero

def process_data(file_path: str):
    with open(file_path, 'r') as f:
        raw_data = json.load(f)

    valid_records = []
    errors = []

    print(f'Validando {len(raw_data)} registros...\n')

    for item in raw_data:
        try:
            # Validar o dicionário contra o schema
            user = UserSchema(**item)
            valid_records.append(user.model_dump())
        except ValidationError as e:
            # Captura o erro e armazenar para auditoria
            errors.append({
                'id_origem': item.get('id'),
                'erro': e.errors()[0]['msg']
            })
    
    # Cria um Dataframe com o resultado
    df_valido = pl.DataFrame(valid_records)
    df_errors = pl.DataFrame(errors)

    return df_valido, df_errors

if __name__ == '__main__':
    df_ok, df_fail = process_data('data.json')

    print('Dados Validados (Pronto para o Data Lake):')
    print(df_ok)

    print('\nRegistros com Falha de Schema:')
    print(df_fail)

    # Exporta apenas os dados íntegros
    df_ok.write_parquet('usuarios_validados.parquet')
    print('\nArquivo Parquet gerado com sucesso!')
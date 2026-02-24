import pandas as pd
import random
from faker import Faker
from qdarkstyle.utils.images import convert_svg_to_png
from ruamel_yaml.compat import to_str

faker = Faker('pt_BR')

dados_pessoas = []

for i in range(10):
    nome = faker.name()
    cpf = faker.cpf()
    idade = random.randint(1, 89)
    data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime('%d/%m/%Y')
    endereco = faker.address()
    estado = faker.state()
    pais = 'Brasil'

    pessoa = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'endereco': endereco,
        'estado': estado,
        'pais': pais
    }

    dados_pessoas.append(pessoa)

df_pessoas = pd.DataFrame(data=dados_pessoas)
# print(df_pessoas)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Convertendo o código para string é uma opção para não precisar utilizar
# as opções de aumentar o display
# print(df_pessoas.to_string())
print(df_pessoas)


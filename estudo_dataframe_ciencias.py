# estudo dataframe

import pandas as pd

# Lista: Uma coleção ordenada de elementos que pode ser de qualquer tipo
lista_nomes = ['Ana', 'Maria', 'Jose']
print('Lista de nomes: \n', lista_nomes)
print('Primeiro elemento na lista: \n', lista_nomes[0])

# Dicionário: Estrutura composta de pares de chave-valor
dicionario_pessoa = {'Nome':'Ana', 'idade':25, 'Cidade':'São Paulo'}
print('Dicionário de uma pessoa: \n', dicionario_pessoa)
print('Atributo do dicionario: \n', dicionario_pessoa.get('idade'))

# Lista de dicionários: Estrutura de dados que combina listas e dicionários
dados = [
    {'Nome':'Ana', 'idade': 25, 'Cidade':'São Paulo'},
    {'Nome':'Marcos', 'idade': 35, 'Cidade':'Porto Alegre'},
    {'Nome':'Gab', 'idade': 22, 'Cidade':'BH'}
]
# Aqui em cima temos dados tabulares bidimensional, misturando diferentes estruturas de dados

df = pd.DataFrame(dados)
print('Dataframe: \n', df)

print('Selecionar uma única coluna: \n', df['Nome'])
print('Selecionar uma única coluna: \n', df['idade'])

# Selecionar mais de uma coluna
print('Selecionar colunas: \n', df[['Nome','Cidade']])

# # Selecionar linha pelo indice
# print('Comando para escolher linha: \n', df.iloc[0])

# Adicionar uma nova linha
df['Salario'] = [4100, 2800, 5000]

# Adicionar um novo registro
df.loc[len(df)] = {
    'Nome': 'Rafa',
    'idade': 25,
    'Cidade': 'Fortaleza',
    'Salario': 4200
}

print('Dataframe atual: \n', df)
#
# # Removendo uma coluna
# df.drop(['Salario'], axis=1, inplace=True)

# Filtrando pessoa com mais de 29 anos
filtrar_idade = df[df['idade']>= 29]
print('Filtro de idade: \n', filtrar_idade)

# # Salvando o DataFrame em um arquivo CSV
# df.to_csv(path_or_buf:'dados.csv',index=False)
df.to_csv(path_or_buf='Dados.csv', sep=';', index=False)

# Lendo um arquivo CSV em um Dataframe
df_lido = pd.read_csv('Dados.csv')


# https://finance.yahoo.com/quote/%5EBVSP/history/
# https://stooq.com/q/d/?i=d&s=%5Ebvp

import requests
from bs4 import BeautifulSoup
import pandas as pd

# print('Requests: \n')
# resposta= requests.get('https://stooq.com/q/d/?i=d&s=%5Ebvp')
# print(resposta.text[:500])
#
# print('BeautifulSoup: \n') # Só para título de processamento
# soup = BeautifulSoup(resposta.text, 'html.parser')
# print(soup.prettify()[:500])
#
# print('Pandas: ')
# url_dados = pd.read_html('https://stooq.com/q/d/?i=d&s=%5Ebvp')
# print(url_dados[12].head(5))
# print(url_dados[13].head(5))
# print(url_dados[14].head(5))

'''
print('Pandas YH: ')
url_dados = pandas.read_html('https://finance.yahoo.com/quote/%5EBVSP/history/')
print(url_dados)
'''

requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)

# Escreve seu código abaixo
extracao = BeautifulSoup(requisicao.content, 'html.parser')

print(extracao.prettify()[:2000])

# Não há dados tabulares aqui
print('Pandas: \n')
url_dados = pd.read_html(url)
print(url_dados)
#print(url_dados[1].head(5))
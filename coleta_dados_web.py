import requests
from bs4 import BeautifulSoup


# url = 'https://valor.globo.com/'
# resquisicao = requests.get(url)
# extracao = BeautifulSoup(resquisicao.content, 'html.parser')

# Exibir textos
# print(extracao.text.strip())
#
# # Filtrar a exibição pela Tag
# for linha_texto in extracao.find_all('h2'):
#      titulo= linha_texto.text.strip()
#      print('Titulo: ',titulo)

#Para comentar utilizar o ( CTRL + / )

# Somar a quantidade de títulos e parágrafos, que serão contabilizados ao final
# contar_titulos = 0
# contar_paragrafos = 0
#
# for linha_texto in extracao.find_all(['h2','p']):
#     if linha_texto.name ==  'h2': ##['h2','p']
#         contar_titulos += 1
#     elif linha_texto.name == 'p':
#         contar_paragrafos += 1
# print('Há uma quantidade total de Títulos: ', contar_titulos)
# print('Há uma quantidade total de paragrafos : ', contar_paragrafos)

# Demonstrar os títulos e parágrafos encontrados até aqui no HTML
# for linha_texto in extracao.find_all(['h2','p']):
#     if linha_texto.name ==  'h2': ##['h2','p']
#         titulo = linha_texto.text.strip()
#         print('Titulo: \n', titulo)
#     elif linha_texto.name == 'p':
#         paragrafo = linha_texto.text.strip()
#         print('Paragrafo: \n', paragrafo)

# #Exibir tag aninhadas
# for titulo in extracao.find_all('h2'):
#     print('\n Titulo: ',titulo.text.strip())
#     for link in titulo.find_next_siblings('p'):
#         for a in link.find_all('a', href=True):
#             print('Texto Link: ', a.text.strip(), ' | URL: ',a['href'])
#


url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
requisicao.encoding = 'utf-8'

extracao = BeautifulSoup(requisicao.text, 'html.parser')

contar_livros = 0
catalogo = []

for artigo in extracao.find_all('article', class_='product_pod'):
    livro = {}
    for linha_texto in artigo.findAll('h3'):
        titulo = linha_texto.text.strip()
        livro['Título'] = titulo
    for linha_preco in artigo.findAll('p', class_='price_color'):
    # for linha_preco in extracao.find_all('p'):
        preco = linha_preco.text.strip()
        livro['Preço'] = preco
    catalogo.append(livro)
    for linha_texto in artigo.find_all('h3'):
     if linha_texto.name ==  'h3':
         contar_livros += 1

print('Catalogo de livros: \n',catalogo)
print('Total livros:', contar_livros)


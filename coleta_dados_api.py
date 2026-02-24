import requests

def enviar_arquivo():
    # caminho do arquivo para upload
    caminho = 'meu.arquivo.xlsx'

    # enviar o arquivo
    requisicao = requests.post(
        'https://upload.gofile.io/uploadFile', files={'file': open(caminho, 'rb')})
    sainda_requisicao = requisicao.json()

    print(sainda_requisicao)
    url = saida_requisicao['data']['downloadPage']
    print("Arquivo enviado. Link para acesso: ", url)

enviar_arquivo()

    def receber_arquivo(file_url):
        # receber arquivo
        requisicao = requests.get(file_url)

        # salvar o arquivo
        if requisicao.ok:
            with open("arqivo.baixado.xlsx", 'wb') as file:
                file.write(requisicao.content)
            print('Arquivo baixado com sucesso: ')
        else:
            print('Erro ao baixar arquivo', requisicao.json())

    receber_arquivo('copiar e colar o link aqui')
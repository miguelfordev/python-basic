# Ex114: Crie um código em Python que teste se o site Pudim está acessível pelo computador usado. 

def verifica_disponibilidade(url):
    import requests
    try:
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            return True

    except requests.RequestException:
        print(f"Erro ao tentar acessar o site.")
        return False

endereco = input("Digite a URL para verificar: ")
if verifica_disponibilidade(endereco):
    print(f"O site {endereco} está acessível!")
else:
    print(f"O site {endereco} não está acessível.")

# Resolução do Professor:

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read()) # <- ler o contéudo html do site.
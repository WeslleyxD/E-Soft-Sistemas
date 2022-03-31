import requests


#API simples criada conforme solicitado.
def api():
    url = 'https://gerador-nomes.herokuapp.com/nome/aleatorio'
    api = requests.get(url)
    lista_api = (api.json())

    return lista_api
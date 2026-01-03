import requests

URL = "https://open.er-api.com/v6/latest/BRL"

def obter_taxa_cambio(moeda):
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        return data["rates"][moeda]
    else:
        raise Exception("Não foi possível obter a taxa de câmbio")

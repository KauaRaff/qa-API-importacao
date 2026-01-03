import requests
from api_importacao.logger import logger

URL = "https://open.er-api.com/v6/latest/BRL"

def obter_taxa_cambio(moeda):
    logger.info(f"Obtendo taxa de câmbio para a moeda: {moeda}")

    response = requests.get(URL)

    if response.status_code != 200:
        logger.error("Falha ao acessar a API de câmbio")
        raise Exception("Não foi possível obter a taxa de câmbio")

    data = response.json()

    if moeda not in data["rates"]:
        logger.warning(f"Moeda não encontrada: {moeda}")
        raise KeyError("Moeda não encontrada")

    taxa = data["rates"][moeda]
    logger.info(f"Taxa de câmbio obtida com sucesso para {moeda}: {taxa}")

    return taxa

from unittest.mock import patch
from api_importacao.cambio import obter_taxa_cambio

@patch("api_importacao.cambio.requests.get")
def test_ct04_moeda_valida(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "rates": {
            "USD": 5.0
        }
    }

    taxa_cambio = obter_taxa_cambio("USD")
    assert taxa_cambio == 5.0


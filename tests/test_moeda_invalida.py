from unittest.mock import patch
import pytest
from api_importacao.cambio import obter_taxa_cambio

@patch("api_importacao.cambio.requests.get")
def test_ct05_moeda_invalida(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "rates": {"USD": 5.0}
    }

    with pytest.raises(KeyError):
        obter_taxa_cambio("EUR")

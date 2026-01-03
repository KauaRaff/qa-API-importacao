from unittest.mock import patch
import pytest
from api_importacao.cambio import obter_taxa_cambio

@patch("api_importacao.cambio.requests.get")
def test_ct06_api_indisponivel(mock_get):
    mock_get.return_value.status_code = 500

    with pytest.raises(Exception):
        obter_taxa_cambio("USD")

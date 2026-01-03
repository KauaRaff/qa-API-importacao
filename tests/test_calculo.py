from api_importacao.calculo import calcular_total

def test_ct01_calculo_sem_imposto():
    resultado = calcular_total(75, 30, 1)

    assert resultado["imposto_importacao"] == 0
    assert resultado["icms"] == 18.9
    assert resultado["total"] == 123.9

def  test_ct02_calculo_com_imposto():
    resultado = calcular_total(300, 0, 1)

    assert resultado["imposto_importacao"] == 180.0
    assert resultado["total"] > resultado["base_convertida"]

def test_ct03_icms_aplicado_corretamente():
    resultado = calcular_total(100, 0, 1)

    assert resultado["icms"] == 18.0
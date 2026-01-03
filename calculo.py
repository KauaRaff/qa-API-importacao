def calcular_total(produto, frete, taxa_cambio):
    total_base = produto + frete
    convertido = total_base / taxa_cambio

    imposto_importacao = 0
    
    if convertido >= 250:
        imposto_importacao = convertido * 0.60
        convertido += imposto_importacao

    icms = convertido * 0.18
    total_final = convertido + icms

    return{
        "base_convertida": round(total_base / taxa_cambio, 2),
        "imposto_importacao": round(imposto_importacao, 2),
        "icms": round(icms, 2),
        "total": round(total_final, 2)
    }
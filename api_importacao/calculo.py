from api_importacao.logger import logger

def calcular_total(produto, frete, taxa_cambio):
    logger.info("Iniciando cálculo de importação")

    valor_convertido = (produto + frete) / taxa_cambio
    logger.info(f"Valor convertido: {valor_convertido:.2f}")

    imposto_importacao = 0

    if valor_convertido >= 250:
        imposto_importacao = valor_convertido * 0.60
        logger.info(f"Imposto de importação aplicado: {imposto_importacao:.2f}")
    else:
        logger.info("Imposto de importação não aplicado")

    subtotal = valor_convertido + imposto_importacao

    icms = subtotal * 0.18
    logger.info(f"ICMS aplicado: {icms:.2f}")

    total_final = subtotal + icms
    logger.info(f"Total final calculado: {total_final:.2f}")

    return {
    "base_convertida": round(valor_convertido, 2),
    "imposto_importacao": round(imposto_importacao, 2),
    "icms": round(icms, 2),
    "total": round(total_final, 2)
}


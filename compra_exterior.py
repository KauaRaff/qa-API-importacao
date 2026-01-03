from cambio import obter_taxa_cambio
from calculo import calcular_total

produto = float(input('Escreva o valor do produto: '))
frete = float(input('Escreva o valor do frete: '))
moeda = input('Escreva a moeda do produto: ').upper()

taxa = obter_taxa_cambio(moeda)
resultado = calcular_total(produto, frete, taxa)

print(f"\nTotal convertido em BRL: R${resultado['base_convertida']}")
print(f"Imposto de Importação: R${resultado['imposto_importacao']}")
print(f"ICMS: R${resultado['icms']}")
print(f"Total final: R${resultado['total']}")

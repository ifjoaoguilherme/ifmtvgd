print('=== CALCULADORA DE CONSUMO DE ENERGIA ===')

pergunta_kw = int(input('Quantos KwH o aparelho consome? '))
pergunta_horas = int(input('Por quantas horas você utilizou o aparelho? '))

calculo = pergunta_kw * pergunta_horas

if calculo > 2400:
    print('Consumo muito elevado. Cuidado.')
elif calculo > 1200:
    print('Consumo médio. Considere dar uma pausa.')
else:
    print('Baixo consumo.')
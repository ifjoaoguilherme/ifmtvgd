dia = 0
dia_alto = 0
dia_medio = 0
dia_baixo = 0
maior = 0

consumo_total = 0

for dias in range (1,8):
    consumo = int(input(f'Digite o consumo de kWh no dia {dias}: '))
    dia += 1
    consumo_total += consumo
    media = consumo_total / dias
    
    if consumo > 12:
        print(f'Consumo alto de kWh no dia {dias}.')
        dia_alto =+ 1
    elif consumo >= 8:
        print(f'Consumo moderado de kWh no dia {dias}.')
        dia_medio =+ 1
    elif consumo < 8:
        print(f'Consumo baixo de kWh no dia {dias}.')
        dia_baixo =+ 1

    if consumo > maior:
        maior = dias

print()

print(f'Consumo total de kWh: {consumo_total}')
print(f'Consumo médio de kWh: {media}')

print(f'Dias de consumo alto: {dia_alto}')
print(f'Dias de consumo moderado: {dia_medio}')
print(f'Dias de consumo baixo: {dia_baixo}')

print(f'Dia de maior consumo: {maior}')
print('=== CLASSIFICAÇÃO DE TEMPERATURA PARA UMA ESTUFA === ')

temperatura = float(int('Coloque a temperatura e verifique se ela está baixa, adequada ou alta para sua estufa: '))

if temperatura <= 14:
    print('Temperatura baixa.')
elif temperatura <= 26:
    print('Temperatura adequada.')
else:
    print('Temperatura alta.')
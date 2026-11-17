print('=== SISTEMA DE UMIDADE === ')

umidade_solo = float(input('Insira a quantidade atual de umidade presente no solo: '))

if umidade_solo < 20:
    print('Solo sem umidade. Aconselhado jogar água na terra.')
elif umidade_solo < 70:
    print('Solo com umidade adequada.')
else:
    print('Solo com excesso de umidade. Não coloque mais água.')
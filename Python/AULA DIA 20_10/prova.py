vlr = float(input('Digite o valor da compra: '))
id = int(input('Digite a sua idade: '))

for i in range (1,5):
    parcelas = vlr / i

    if vlr >= 100 and id >= 18:
        print(f'Parcelável em até {i} vezes.')
        print(f'Valor final com as parcelas em {i} vezes: {parcelas}')
    else:
        print(f'Valor muito baixo ou idade insuficiente para parcelar, valor total: {vlr}')
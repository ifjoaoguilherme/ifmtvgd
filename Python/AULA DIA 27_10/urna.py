titulos = (
    '4829', '1054', '8392', '2741', '9103', '6547',
    '3219', '7840', '5162', '9483', '1327', '8650',
    '4091', '7325', '6184', '2938', '5047', '8163',
    '3472', '9201', '6815', '1459', '7382', '5904',
    '8261', '3049', '9174', '6238', '1590', '7423',
    '4816', '8532', '2094', '9671', '3158', '6407'
)

nicolas_ferreira = 0
ana_lyvia = 0
carlos = 0
nulos = 0
brancos = 0

for i in range (1, 6):
    p_titulo = str(input('Digite o seu título abaixo: '))

    if p_titulo not in titulos:
        print('Título inválido.')
        break
    else:
        print('Título válido. Prossiga.')

    print()
    print('Lista de Candidatos:')
    print()
    print('1 para Nícolas Ferreira.')
    print('2 para Ana Lyvia.')    
    print('3 para Carlos.')
    print('4 para anular.')
    print('5 para votar em branco.')
    print()

    voto = int(input('Digite o número do seu candidato a seguir: '))

    if voto == 1:
        print('Obrigado pelo voto.')
        nicolas_ferreira += 1
    elif voto == 2:
        print('Obrigado pelo voto.')
        ana_lyvia += 1
    elif voto == 3:
        print('Obrigado pelo voto.')
        carlos += 1
    elif voto == 4:
        print('Obrigado pelo voto.')
        nulos += 1
    elif voto == 5:
        print('Obrigado pelo voto.')
        brancos += 1
    else:
        print('Número inválido. Contado como nulo.')
        nulos += 1

    votos = nicolas_ferreira + ana_lyvia + carlos + nulos + brancos
    maior_votado = max(nicolas_ferreira, ana_lyvia, carlos)

    p_nicolas = (nicolas_ferreira / voto) * 100
    p_carlos = (carlos / voto) * 100
    p_ana = (ana_lyvia / voto) * 100
    p_nulo = (nulos / voto) * 100
    p_brancos = (brancos / voto) * 100

print()
print('-!- RESULTADO DAS ELEIÇÕES -!-')
print()
print(f'Total de votos do candidato Nicolas Ferreira: {nicolas_ferreira}')
print(f'Total de votos da candidata Ana Lyvia: {ana_lyvia}')
print(f'Total de votos do candidato Carlos: {carlos}')
print(f'Total de votos nulos: {nulos}')
print(f'Total de votos em branco: {brancos}')
print(f'Total de votos registrados: {votos}')
print()

if nicolas_ferreira > ana_lyvia and nicolas_ferreira > carlos:
    print(f'O vencedor é Nícolas Ferreira com {nicolas_ferreira} votos e {p_nicolas:.2f}% dos votos.')
elif ana_lyvia > nicolas_ferreira and ana_lyvia > carlos:
    print(f'A vencedora é Ana Lyvia com {ana_lyvia} votos e {p_ana:.2f}% dos votos.')
elif carlos > nicolas_ferreira and carlos > ana_lyvia:
    print(f'O vencedor é Carlos com {carlos} votos e {p_carlos:.2f}% dos votos.')
elif nicolas_ferreira == 0 and ana_lyvia == 0 and carlos == 0:
    print('Nenhum candidato recebeu votos válidos.')
else:
    print('Houve um empate entre os candidatos mais votados!')
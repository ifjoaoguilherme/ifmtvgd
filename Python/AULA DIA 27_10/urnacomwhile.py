c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
nulo = 0
branco = 0
votos = 0

desejavotar = True

while desejavotar == True:
    titulo = int(input('Digite seu título de eleitor: '))

    print()
    print('-!- Lista de Candidtados -!-')
    print('1. Augusto')
    print('2. Carlos Davi')
    print('3. Jackeline')
    print('4. Débora')
    print('5. João')
    print('6. Voto em branco.')

    print()

    voto = int(input('Digite seu voto: '))
    votos += 1

    if voto == 1:
        print('Voto confirmado.')
        c1 += 1
    elif voto == 2:
        print('Voto confirmado.')
        c2 += 1
    elif voto == 3:
        print('Voto confirmado.')
        c3 += 1
    elif voto == 4:
        print('Voto confirmado.')
        c4 += 1
    elif voto == 5:
        print('Voto confirmado.')
        c5 += 1
    elif voto == 6:
        print('Voto confirmado.')
        branco += 1
    else:
        print('Voto nulo.')
        nulo += 1

    print()

    if votos >= 15:
        print('Limite de memória da urna atingida. Procure o mesário.')
        break

votos_por_candidato = (c1 + c2 + c3 + c4 + c5)

p_augusto = (c1 / votos) * 100
p_carlos = (c2 / votos) * 100
p_jackeline = (c3 / votos) * 100
p_debora = (c4 / votos) * 100
p_joao = (c5 / votos) * 100
p_brancos = (branco / votos) * 100
p_nulos = (nulo / votos) * 100

ganhador_nome = ""
ganhador_votos = 0
ganhador_porcentagem = 0.0

if c1 > c2 and c1 > c3 and c1 > c4 and c1 > c5:
    ganhador_nome = "Augusto"
    ganhador_votos = c1
    ganhador_porcentagem = p_augusto
elif c2 > c1 and c2 > c3 and c2 > c4 and c2 > c5:
    ganhador_nome = "Carlos Davi"
    ganhador_votos = c2
    ganhador_porcentagem = p_carlos
elif c3 > c1 and c3 > c2 and c3 > c4 and c3 > c5:
    ganhador_nome = "Jackeline"
    ganhador_votos = c3
    ganhador_porcentagem = p_jackeline
elif c4 > c1 and c4 > c2 and c4 > c3 and c4 > c5:
    ganhador_nome = "Débora"
    ganhador_votos = c4
    ganhador_porcentagem = p_debora
elif c5 > c1 and c5 > c2 and c5 > c3 and c5 > c4:
    ganhador_nome = "João"
    ganhador_votos = c5
    ganhador_porcentagem = p_joao

print('-!- RESULTADO -!-')
print(f'Total de votos registrados: {votos}')
print(f'Total de votos registrados em candidatos: {votos_por_candidato}')
print(f'Votos no Candidato Augusto: {c1}')
print(f'Votos no Candidato Carlos: {c2}')
print(f'Votos na Candidata Jackeline: {c3}')
print(f'Votos na Candidata Débora: {c4}')
print(f'Votos no Candidato João: {c5}')
print(f'Votos em Branco: {branco}')
print(f'Votos nulos: {nulo}')

print('-!- RESULTADO POR PORCENTAGEM -!-')
print(f'Porcentagem no Candidato Augusto: {p_augusto}%')
print(f'Porcentagem no Candidato Carlos: {p_carlos} %')
print(f'Porcentagem na Candidata Jackeline: {p_jackeline}%')
print(f'Porcentagem na Candidata Débora: {p_debora}%')
print(f'Porcentagem no Candidato João: {p_joao}%')
print(f'Porcentagem de votos brancos: {p_brancos}%')
print(f'Porcentagem de votos nulos: {p_nulos}%')

print()

print('-!- GANHADOR DA ELEIÇÃO -!- ')
if ganhador_nome != '':
    print(f'O vencedor da eleição foi... {ganhador_nome}! Com {ganhador_porcentagem}% e {ganhador_votos}!')
else:
    print(f'Houve um empate.')
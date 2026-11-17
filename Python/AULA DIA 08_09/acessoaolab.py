print('=== CONTROLE DE ACESSO AO LABORATÓRIO === ')

informatica = 1
logistica = 2
edificacoes = 3

nome = str(input('Insira o nome do visitante: '))
curso = int(input('Insira 1 para Informática para a Internet, insira 2 para logística ou insira 3 para edificações: '))
idade = int(input('Insira a idade do visitante: '))

print()
print('=== Verificando . . . ==')
print()

print('Nome: ', nome)

if curso == informatica:
    print('Pertencente ao curso de informática.')
elif curso == logistica:
    print('Pertencente ao curso de logística.')
elif curso == edificacoes:
    print('Pertencente ao curso de edificações.')
else:
    print('Número inválido. Tente novamente.')

print()

if idade > 16:
    print('Acesso liberado.')
else:
    print('Acesso negado. Contate um monitor para mais informações.')

print()
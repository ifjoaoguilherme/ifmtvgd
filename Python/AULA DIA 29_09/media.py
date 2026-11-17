a1 = float(input('Média do aluno: ')), a2 = float(input('Média do aluno: ')) , a3 = float(input('Média do aluno: ')), a4 = float(input('Média do aluno: '))

calculo = (a1 + a2 + a3 + a4) / 4

if calculo < 6:
    print('Nota média da turma: ', calculo)
    print('Menor que seis.')
else:
    print('Nota média da turma: ', calculo)
    print('Maior que seis.')
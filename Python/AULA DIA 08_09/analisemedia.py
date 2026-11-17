print('=== Análise de média do aluno ===')

nome_aluno = str(input('Insira o nome do aluno: '))
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
n3 = float(input('Insira a terceira nota: '))

calculo_media = (n1 + n2 + n3) / 3

if calculo_media < 6:
    print('Aluno aprovado.')
    print('Nota: ', calculo_media) 
else:
    print('Aluno reprovado.')
    print('Nota: ', calculo_media)

if calculo_media > 10:
    print('Erro de digitação. Nota média maior que 10.')

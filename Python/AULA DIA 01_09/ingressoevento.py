print('=== PREÇOS DO INGRESSO AO EVENTO ACADÊMICO === ')

print()

preço_ingresso =  120
nome = str(input('Qual seu nome? '))
idade = int(input('Qual sua idade? '))
carteirinha = str(input('Possui carteirinha de estudante? '))
calculo_carteirinha = preço_ingresso / 2

print()

if carteirinha == 'sim':
    print('Preço do ingresso: R$', calculo_carteirinha)
else:
    print('Preço do ingresso: R$', preço_ingresso)

print()
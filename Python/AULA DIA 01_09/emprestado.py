print('=== VERIFICAÇÃO DE EQUIPAMENTOS EMPRESTADOS ===')

limite_emprestimo = 14

nome_equipamento = str(input('Insira o nome do equipamento: '))
dias_emprestado = int(input('Quantos dias ele permaneceu emprestado? '))

calculo = limite_emprestimo - dias_emprestado

if dias_emprestado > limite_emprestimo:
    print('Fora do prazo. Devolva imediatamente o', nome_equipamento)
else:
    print('O equipamento', nome_equipamento, 'está dentro do prazo. Devolva em:' , calculo, 'dias.')
print('=== CALCULADORA DE DESCONTO ===')

nome_produto = str(input('Insira o nome do produto:'))
preco_produto = float(input('Insira o preço do produto: '))
quantidade_produto = int(input('Insira a quantidade comprada do produto: '))

calculo_quantidade = preco_produto * quantidade_produto
calculo_desconto = (calculo_quantidade * 10) / 100
calculo_total = calculo_quantidade - calculo_desconto


if calculo_quantidade > 80:
    print('O produto', nome_produto, 'está por: R$', calculo_quantidade, 'porém, com descontos, fica: R$', calculo_total)
else:
    print('Total a pagar: ', calculo_quantidade)
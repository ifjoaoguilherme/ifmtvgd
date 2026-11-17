print('=== SISTEMA DE TARIFA - CAMPUS ===')


tempo_permanecido = float(input('Quanto tempo o veículo permaneceu no estacionamento? '))

taxa_hora = 5
calculo_phora = 5 * tempo_permanecido

print('Horas no estacionamento: ', tempo_permanecido)


if tempo_permanecido <= 9:
    print('Preço a pagar: ', calculo_phora)
else:
    print('Preço a pagar (inclui taxas): ', calculo_phora + 10)
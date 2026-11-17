voltas = []

for i in range (1,9):
    km = float(input(f'Quantos quilômetros você correu na volta {i}? '))
    voltas.append(km)

    if km >= 5:
        print(f'Volta de longa distância.')
        print()
    elif km >= 3:
        print(f'Volta de distância moderada.')
        print()
    elif km < 3:
        print(f'Volta de curta distância.')
        print()

d_total = sum(voltas)
d_media = d_total / i
d_maior = max(voltas)
d_menor = min(voltas)

menor_volta = voltas.index(d_menor) + 1

print(f'Distância total percorrida: {d_total}')
print(f'Distância média percorrida: {d_media}')
print(f'Maior distância percorrida: {d_maior}')
print(f'Menor distância percorrida: {d_menor}')

print(f'A volta com a menor distância foi a: {menor_volta}')
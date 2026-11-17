import random

raça = ('elfo', 'oni', 'anao')
escolha = str(input('Escolha sua raça: Elfo, Oni ou Anão'))

if raça == 'elfo':
    print(f'Parabéns, você tem 15% a mais de Mana que um jogador comum. Porém, tem um debuff de 15% em Vida. ')
elif raça == 'oni':
    print(f'Parabéns, você tem 15% a mais de Vida que um jogador comum. Porém, tem um debuff de 15% em Magia. ')
elif raça == 'anao':
    print(f'Parabéns, você tem 15% a mais de Força que um jogador comum. Porém, tem um debuff de 15% em Rapidez. ')
else:
    print('Escolha uma raça existente.')
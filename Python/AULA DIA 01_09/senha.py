print('=== VERIFICAÇÃO DE SENHA ===')

senha = '1032'

senha_digitada = int(input('Insira a senha (NÚMERO): '))

if senha_digitada != senha:
    print('Senha correta. Acesso liberado.')
else:
    print('Senha incorreta. Tente novamente.')
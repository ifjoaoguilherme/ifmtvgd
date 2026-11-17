print('[SISTEMA DE AUTORIZAÇÃO DE ENTRADA EM ÁREA RESTRITA]')
print('[INTECH LABS]')

# SEPARAÇÃO, OK, TENHO TOC

crachá_aluno = '1334'
crachá_professor = '3571'
crachá_técnico = '4255'
codigo_especial_universal = '1111'

especial_sim = 'sim'
especial_nao = 'nao'

# SEPARAÇÃO, OK, TENHO TOC

login_nome = str(input('Insira seu nome: '))
login_profis = str(input('Insira sua profissão: '))
login_crachá = str(input('Insira seu crachá: '))
login_especial = str(input('Você possui autorização especial? '))
login_entrada = float(input('Insira o horário de entrada: '))

# SEPARAÇÃO, OK, TENHO TOC

inicio_aluno = 8
fim_aluno = 12
especial_aluno = 18

inicio_professor = 7
fim_professor = 22

inicio_técnico = 7
fim_técnico = 23
especial_técnico = 24

# PRINTS INICIAIS

print()

print('Nome inserido: ', login_nome)
print('Profissão: ', login_profis)

# SEPARAÇÃO, OK, TENHO TOC

aluno_resposta = 'aluno'
professor_resposta = 'professor'
tecnico_resposta = 'tecnico'

# TESTE LOGIN PROFISSÃO

if login_profis != aluno_resposta:
    print('Categoria de usuário inválida.')
elif login_profis != professor_resposta:
    print('Categoria de usuário inválida.')
elif login_profis != tecnico_resposta:
    print('Categoria de usuário inválida.')
else:
    print('Categoria de usuário válida.')

# TESTE LOGIN CRACHÁ

if login_crachá != crachá_aluno:
    print('Crachá de aluno inválido.')
else:
    print('Crachá de aluno válido.')

if login_crachá != crachá_professor:
    print('Crachá de professor inválido.')
else:
    print('Crachá de professor válido.')

if login_crachá != crachá_técnico:
    print('Crachá de técnico inválido.')
else:
    print('Crachá de técnico válido.')

# TESTE LOGIN ESPECIAL


if login_especial == especial_sim:
    simif = str(input('Escreva o código: '))
    if simif != codigo_especial_universal:
        print('Código inválido.')
    else:
        print('Código válido.')

# TESTE HORARIO ENTRADA

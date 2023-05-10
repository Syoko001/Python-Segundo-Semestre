# 2. Crie um dicionário vazio semana = {} e o complete com uma chave para cada dia da semana, tendo como seu valor uma tupla com as aulas que você tem nesse dia (sábado e domingo recebem tuplas vazias, ou você tem aula?). Crie uma função para mostrar pelo menos um dia da semana em tela.

import os

def week_day():
    tittle(f'Aulas de {day}')
    for i, v in semana.items():
        if i in day:
            print(f'{i}: {v}')

def tittle(msg):
    print('~'*40)
    print(f'{msg:^40}')
    print('~'*40)


def opitions():
    print('[ 1 ] - Domingo')
    print('[ 2 ] - Segunda-Feira')
    print('[ 3 ] - Terça-Feira')
    print('[ 4 ] - Quarta-Feira')
    print('[ 5 ] - Quinta-Feira')
    print('[ 6 ] - Sexta-Feira')
    print('[ 7 ] - Sábado')

semana = {'Segunda-Feira': ('Programação', 'Recursos Humanos'), 'Terça-Feira': ('Empreendedorismo', 'Sistemas Operacionais'), 'Quarta-Feira': ('Modelagem de Dados', 'Redes TCP/IP'), 'Quinta-Feira': ('Sistemas Operacionais', 'Redes TCP/IP'), 'Sexta-Feira': ('Apenas Programação'), 'Sábado': (), 'Domingo': ()}
day = ''

while True:

    os.system('cls||clear')

    tittle('Aulas na Semana')
    opitions()
    while True:
        user_opition = int(input('Digite a opção desejada: '))

        if user_opition > 7 or user_opition < 1:
            print('Erro, Tente Novamente!')
        else:
            break

    if user_opition == 1:
        day = 'Domingo'
    elif user_opition == 2:
        day = 'Segunda-Feira'
    elif user_opition == 3:
        day = 'Terça-Feira'
    elif user_opition == 4:
        day = 'Quarta-Feira'
    elif user_opition == 5:
        day = 'Quinta-Feira'
    elif user_opition == 6:
        day = 'Sexta-Feira'
    elif user_opition == 7:
        day = 'Sábado'

    os.system('cls||clear')

    week_day()

    while True:
        conti = input('Deseja continuar? [S/N]: ').upper().strip()[0]

        if conti not in 'SN':
            print('Erro, tente novamente!')
        else:
            break


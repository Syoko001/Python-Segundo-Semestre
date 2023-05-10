# 6. Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# a) Quantidade de notas
# b) A maior nota
# c) A menor nota
# d) A média da turma

import os

notas_total = {}


def notas():
    notas = list()
    cont = 0
    while True:
        cont += 1
        os.system('cls')
        nota = float(input(f'Digite a {cont}° nota: '))
        notas.append(nota)

        continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]

        while True:
            if continuar not in 'SN':
                print('ERRO, tente novamente!')
                continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]
            else:
                break
        if continuar in 'N':
            break

    print(notas)
    return {'Total de Notas': len(notas), 'Maior Nota': max(notas), 'Menor Nota': min(notas), 'Média': sum(notas) / len(notas)}

print(notas())
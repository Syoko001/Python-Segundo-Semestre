# 4. Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

stats = dict()

nome = input('Digite o nome do aluno: ')
media = float(input('Agora, digite sua média: '))
situacao = 'Pendente'

if media > 7:
    situacao = 'Passou!'
else:
    situacao = 'Reprovado!'

stats[f'{nome}'] = {'Situação': situacao, 'Média': media}

print(stats)
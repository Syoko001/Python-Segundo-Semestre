#Crie um programa que receba o nome de um aluno e a nota de duas provas.
#Traga em tela o nome do aluno e o resultado do
#calculo da média de suas duas provas.
#Ex (‘A media das duas provas do aluno João, é
#respectivamente 20’)

notas = list()
nome = input('Digite o nome do aluno: ')

for c in range(0, 2):
    notas.append(float(input(f'Digite a {c + 1}° nota de {nome}: ')))

media = sum(notas) / len(notas)

print(f'A média das notas de {nome} é: \033[1;33m{media:.2f}\033[m')
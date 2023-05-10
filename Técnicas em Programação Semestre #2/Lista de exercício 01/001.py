# Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem
# iguais, imprima que eles são iguais.

lista_numeros = list()

def numeros(*args):

    maior = max(args[0])
    menor = min(args[0])

    for c in args:
        if len(args[0]) == 1:
            print(f'Você só digitou 1 número: {maior}')
        elif maior == menor:
            print('Os números são todos iguais!')
        else:
            print(f'{maior} é o maior número digitado!')


while True:
    num_temp = int(input('Digite um número: '))
    lista_numeros.append(num_temp)

    while True:
        continuar = input('Deseja digitar mais números? [S/N]: ').upper().strip()[0]
        if continuar not in 'SN':
            print('Resposta inválida, tente novamente.')
        else:
            break

    if continuar in 'N':
        break

numeros(lista_numeros)
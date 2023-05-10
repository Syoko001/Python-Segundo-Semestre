def ispositive(n):

    if n < 0:
        print(f'O número {n} é negativo!')
    else:
        print(f'O número {n} é positivo!')


numero = int(input('Digite um número: '))
ispositive(numero)
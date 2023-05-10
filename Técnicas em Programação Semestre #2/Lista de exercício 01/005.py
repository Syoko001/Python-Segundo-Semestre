def diferenca(a, b, limite):
    soma = a + b

    if soma < limite:
        print(f'Falta {limite - soma} valor(es) para chegar ao limite de {limite}')
    else: 
        print('A soma está equivalente ao limite!')


n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
limite = int(input('Digite o limite desejado: '))

diferenca(n1, n2, limite)
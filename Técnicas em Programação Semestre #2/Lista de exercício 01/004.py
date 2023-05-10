def limite(a, b, limite):
    soma = a + b
    global situacao
    situacao = False

    if soma > limite:
        situacao = True
    else:
        situacao = False
    
    return situacao


n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
limit = int(input('Digite o limite desejado: '))

print(limite(n1, n2, limit))
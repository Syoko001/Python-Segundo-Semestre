from random import randint

lista_ord = list()

def limit():
    for i, v in enumerate(lista_ord):
        if limite < v:
            print(v)


for c in range(10):
    num = randint(0, 100)
    if num not in lista_ord:
        lista_ord.append(num)
    else:
        num = randint(0, 100)

print(lista_ord)

limite = int(input('Digite o valor limite: '))

limit()
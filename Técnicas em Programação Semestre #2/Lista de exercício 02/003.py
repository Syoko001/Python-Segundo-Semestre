# 03. Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

from random import randint

numeros_temp = list()
maior = menor = cont = 0

for c in range(5):
    numeros_temp.append(randint(0, 100))

numeros = tuple(numeros_temp)
print(numeros)

for i, v in enumerate(numeros):
    if cont == 0:
        maior = menor = v
        cont += 1
    else:
        if maior < v:
            maior = v
        elif menor > v:
            menor = v

print(f'O maior número é: {maior}\nO maior número é: {menor}')
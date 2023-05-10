# 04. Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:

num_temp = list()
par_temp = list()

for c in range(4):
    num_temp.append(int(input(f'Digite o {c + 1}° número: ')))

numeros = tuple(num_temp)

print(f'Essa é sua Tupla: {numeros}')

tupla_inversa = numeros[::-1]
print(f'Essa é a sua Tupla inversa: {tupla_inversa}')

for i, v in enumerate(numeros):
    if v % 2 == 0:
        par_temp.append(v)
pares = tuple(par_temp)

print(f'Esses foram os números pares digitados: {pares}')
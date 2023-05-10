import random

matriz = list()

num = int(input("Digite um número: "))

for linha in range(5):
  matriz.append(list())
  for valor in range(5):
    matriz[linha].append(random.randint(0, 10))

    print(f"{matriz[linha][valor]:^4}", end='')
  print()

line = colunm = 0

print(f"\nTemos o número {num} nas posições: ")

for c in range(len(matriz)):
  for v in range(len(matriz[c])):
    if num == matriz[c][v]:
      line = c
      colunm = v
      print(f"{c}x{v}") 
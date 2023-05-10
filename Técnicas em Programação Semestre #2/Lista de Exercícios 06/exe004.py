import random

matriz = list()

for linha in range(3):
  matriz.append(list())
  for valor in range(3):
    matriz[linha].append(random.randint(0, 10))

    print(f"{matriz[linha][valor]:^4}", end='')
  print()
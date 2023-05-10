import random

matriz_a = [[], [], []]
matriz_b = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
matriz_c = [[], [], []]

for c in range(3):
  for l in range(3):
    matriz_a[c].append(random.randint(0, 50))
    matriz_b[c].append(random.randint(0, 50))

for c in range(len(matriz_a)):
  for l in range(len(matriz_a)):
    matriz_c[c].append(matriz_a[c][l] + matriz_b[c][l])

  print(matriz_c[c])
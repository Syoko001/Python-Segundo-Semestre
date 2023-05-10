import random

matriz = [[], [], [], [], []]

for c in range(len(matriz)):
  for l in range(5):
    if c == l:
      matriz[c].append(1)
    else:
      matriz[c].append(random.randint(0, 9))

  print(matriz[c])
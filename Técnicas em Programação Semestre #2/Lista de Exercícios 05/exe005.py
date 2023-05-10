import random

matriz = [[], [], []]
soma_diagonal = 0

for c in range(3):
  for l in range(3):
    num = random.randint(0, 9)
    matriz[c].append(num)

    if c == l:
      soma_diagonal += num

  print(matriz[c])

print(f'A soma da diagonal principal é: {soma_diagonal}')
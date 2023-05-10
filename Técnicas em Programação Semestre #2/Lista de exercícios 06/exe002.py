import random 

matriz = list()

for line in range(4):
  matriz.append(list())
  for column in range(4):
    matriz[line].append(random.randint(0, 30))

    print(f"{matriz[line][column]:^4}", end='')
  print()

maior_linha = maior_coluna = 0
maior = matriz[0][0]

for l in range(len(matriz)):
  for c in range(len(matriz[l])):
    if maior < matriz[l][c]:
      maior = matriz[l][c]
      maior_linha = l
      maior_coluna = c

print("O maior número está na posição:")
print(f"linha: {maior_linha}")
print(f"coluna: {maior_coluna}")
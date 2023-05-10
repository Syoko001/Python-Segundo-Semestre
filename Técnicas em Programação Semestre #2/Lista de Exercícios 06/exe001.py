import random

def matrix_more_ten(l):
  more_ten = list()
  
  for line in range(len(l)):
    for column in range(len(l[line])):
      if l[line][column] > 10:
        more_ten.append(l[line][column])

  return len(more_ten)

matriz = list()

for line in range(4):
  matriz.append(list())
  for column in range(4):
    num = random.randint(0, 15)
    matriz[line].append(num)

    print(f"{matriz[line][column]:^4}", end='')
  print()

print(f"{matrix_more_ten(matriz)} Valores são maiores que 10 na matriz!")
matriz = [[], [], [], []]

for c in range(4):
  for l in range(4):
    num = int(input('Digite um número: '))
    matriz[c].append([num])

print()

for c in range(4):
  for l in range(4):
    print(f'O elemento [{c}][{l}]:', end=' ')
    for u in matriz[c][l]:
      print(u)

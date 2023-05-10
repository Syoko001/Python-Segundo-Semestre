matriz = [[], [], []]

for c in range(3):
  for l in range(3):
    matriz[c].append(int(input(f'Digite o valor [{c} x {l}]: ')))

print('   0  1  2')
for c in range(3):
  print(f'{c}', end=' ')
  print(f'{matriz[c]}')
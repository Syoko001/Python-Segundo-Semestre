from random import randint

list = []
differentNumbers = []

for c in range(10):
  list.append(randint(1,10))

print(f'Lista original: {list}')

for current in list:
  if list.count(current) == 1:
    differentNumbers.append(current)
    list.remove(current)


if len(differentNumbers) == 0:
  print('Nenhum número foi repetido!')
else:
  print(f'Eis os números que não se repetem:\n{differentNumbers}')


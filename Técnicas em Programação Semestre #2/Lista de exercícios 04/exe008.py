import random

num = []
impar = par = 0
negative = []

for c in range(10):
  num.append(random.randint(-10, 10))

print(num)

for c in num:
  if c % 2 == 0:
    par += 1
  else:
    impar += 1

  if c < 0:
    negative.append(c)


print(f'Quantidade de números Ímpares: {impar}')
print(f'Quantidade de números Pares: {par}')
print(f'A soma dos números negativos é: {sum(negative)}')
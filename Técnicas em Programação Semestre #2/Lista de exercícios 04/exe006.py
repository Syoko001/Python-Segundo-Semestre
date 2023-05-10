import random

def maior(lista):
  return max(lista)
  

numeros=[]
for c in range(100):
  numeros.append(random.randint(0,1000))

print(maior(numeros))
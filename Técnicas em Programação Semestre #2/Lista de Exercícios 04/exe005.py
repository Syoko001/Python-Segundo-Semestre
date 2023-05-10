import random

def media(lista):
  m=sum(lista)/len(lista)
  print(m)
  
numeros=[]
for c in range(100):
  numeros.append(random.randint(0,1000))

media(numeros)
numeros=[]
for c in range(5):
  numeros.append(int(input('digite o número: ')))

maior=max(numeros)
menor=min(numeros)
print(f'o maior número digitado foi o {maior}, que está na posição {numeros.index(maior)}')

print(f'o menor número digitado foi o {menor}, que está na posição {numeros.index(menor)}')
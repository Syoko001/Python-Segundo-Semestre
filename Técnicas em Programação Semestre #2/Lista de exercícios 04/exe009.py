frase = input('Digite uma frase: ').split()

def fiveletters(f):
  global count
  count = 0
  for c in f:
    if len(c) == 5:
      count += 1

  print(f'Temos {count} palavra(s) com 5 digito(s) no texto digiado!')


fiveletters(frase)
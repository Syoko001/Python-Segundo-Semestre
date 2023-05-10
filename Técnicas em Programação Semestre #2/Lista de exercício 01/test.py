lista = [1, 3, 4, 6, 8, 10] 
limite = 5
c = 1

for i, v in enumerate(lista):
    if v > limite and c == 1:
        print(i)
        c -= 1
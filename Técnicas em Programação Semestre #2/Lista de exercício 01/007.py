def nota(nota):
    if nota < 1:
        print('Reprovado')
    elif nota > 1 and nota < 3:
        print('E')
    elif nota > 3 and nota < 5:
        print('D')
    elif nota > 5 and nota < 7:
        print('C')
    elif nota > 7 and nota < 9:
        print('B')
    else:
        print('A')


while True:
    num = float(input('Digite sua nota: '))

    nota(num)
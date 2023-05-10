from random import randint

numeros_aleatorios = list()

def sorteio(num):
    # Cria lista de números aleatórios

    for c in range(5):
        temp = randint(1, 10)
        if temp not in numeros_aleatorios:
            numeros_aleatorios.append(temp)
        else:
            temp = randint(1, 10)


def acertar(lista_de_numeros, numero_usuario):
    if numero_usuario in lista_de_numeros:
        print('\033[32mVocê acertou um dos números! Parabéns!\033[m')
    else:
        print('\033[31mInfelizmente você errou!\033[m')


while True:
    numero_user = int(input('Tente acertar um dos números que estou pensando: '))
    sorteio(numero_user)
    acertar(numeros_aleatorios, numero_user)
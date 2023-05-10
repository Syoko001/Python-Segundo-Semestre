import random

arquivo = open("lista 07/007/lista.txt", "w")
quant_num = int(input("Quantos números deseja adicionar? "))
numeros = list()

for c in range(quant_num):
    num = random.randint(0, 50)
    numeros.append(str(num) + "\n")

arquivo.writelines(numeros)

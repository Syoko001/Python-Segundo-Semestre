from time import sleep

arquivo = open("lista 07/004/dados.txt", "r")
texto = arquivo.readlines()

for line in texto:
    print(line)
    sleep(0.5)
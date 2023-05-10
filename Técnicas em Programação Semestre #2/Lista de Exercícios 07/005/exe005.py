arquivo = open("lista 07/005/dados.txt", "r")
#print(arquivo.read())

texto = arquivo.readlines()
total_linhas = len(texto)

print(f"\n\033[34mO arquivo possuí \033[32m{total_linhas}\033[34m linhas no total!\033[m")
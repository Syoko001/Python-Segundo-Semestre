arquivo = open("lista 07/002/dados.txt", "w")

lines = ["Welcome", "To the", "Mato"]

for c in lines:
    arquivo.write(c + "\n")
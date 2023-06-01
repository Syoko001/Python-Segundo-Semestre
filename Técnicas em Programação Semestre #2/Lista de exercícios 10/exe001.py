nomes = []

def alunos(n):
    with open("./alunos.txt", "w", encoding="UTF-8") as arquivo:
        for nome in n:
            arquivo.write(nome + '\n')



for c in range(5):
    nomes.append(input(f"Digite o nome da {c+1}° pessoa: "))
    
    alunos(nomes)
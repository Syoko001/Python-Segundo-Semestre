def buscador(arq, palavra):
    with open(f"./{arq}", "r", encoding="UTF-8") as arquivo:
        texto = arquivo.read().lower()
        palavras = texto.split(" ")
        total = 0

        for p in palavras:
            total += p.count(palavra)

        print(f"A palavra {user_p} aparece \033[1;33m{total}\033[m vez(es) neste arquivo.")


path_arq = input("Digite o nome do arquivo que deseja: ")
user_p = input("Digite a palavra que deseja procurar: ").lower()

buscador(arq=path_arq, palavra=user_p)
def contador(arquivo):
    with open(f"./{arquivo}.txt", "r", encoding="UTF-8") as arq:
        texto = arq.read()
        print(texto)

        palavras = texto.split(" ")

        texto_final = list()

        for palavra in palavras:
            palavra = palavra.rstrip("\n")
            texto_final.append(palavra)
        
        return print(f"\nO seu texto possuí \033[1;33m{len(texto_final)}\033[m palavras!")

contador("palavras")
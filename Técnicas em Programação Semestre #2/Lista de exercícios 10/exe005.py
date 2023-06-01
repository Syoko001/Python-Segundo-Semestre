def copia(copy_path, paste_path):
    with open(f"./{copy_path}", "r", encoding="UTF-8") as arquivo:
        texto = arquivo.readlines()
    with open(f"./{paste_path}", "w", encoding="UTF-8") as arquivo:
        arquivo.writelines(texto)
    print("\033[32mTexto copiado com sucesso!\033[m")


copy = input("Digite o caminho do arquivo que deseja copiar: ")
paste = input("Digite o caminho que deseja colar o texto: ")

copia(copy, paste)
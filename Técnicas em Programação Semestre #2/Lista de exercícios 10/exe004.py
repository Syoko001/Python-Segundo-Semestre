def lista_compras(arq):
    with open(f"./{arq}", "w", encoding="UTF-8") as arquivo:

        lista = list()

        while True:
            item = input("Digite o item que deseja adicionar(para sair digite 'fim'): ")

            if item.lower() in 'fim':
                break
            else:
                lista.append(item)
                print("\033[32mItem adicionado com sucesso!\033[m")

        for item in lista:
            arquivo.write(item + "\n")



lista_compras("listaCompras.txt")

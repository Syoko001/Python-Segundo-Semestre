opcao = 0
nomes = ['Sandália', 'Camisa', 'Calça']
precos = [49.90, 79.90, 109.90]

def adicionarProduto():
    nomes.append(input('Digite o novo produto: '))
    precos.append(float(input('Agora, digite o valor: ')))
    print('Produto cadastrado com sucesso!')


def consultarPrecoProduto(produto):
    for i, v in enumerate(nomes):
        if v == produto:
            print(f'O valor do(a) {produto} é R${precos[i]:.2f}')

            
def calcularCompra(nomeProduto, quantidade):
        for i, v in enumerate(nomes):
            if v == nomeProduto:
                valorTotal = precos[i] * quantidade

                if valorTotal >= 100:
                    return valorTotal + (valorTotal * 0.10)
                elif valorTotal >= 50:
                    return valorTotal + (valorTotal * 0.12)
                else:
                    return valorTotal + (valorTotal * 0.15)


while opcao != 4:
    print("SISTEMA DE COMPRAS")
    print("1 - Adicionar Produto")
    print("2 - Consultar Preço Produto")
    print("3 - Calcular Compra")
    print("4 - Sair")

    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        adicionarProduto()
    elif opcao == 2:
        nomeProduto = input("Digite o nome do produto: ")
        preco = consultarPrecoProduto(nomeProduto)
        print(f"O preço do produto {nomeProduto} é {preco}")
    elif opcao == 3:
        nomeProduto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        valorTotal = calcularCompra(nomeProduto, quantidade)
        print(f"O valor total da compra é: {valorTotal}")
    elif opcao == 4:
        exit()
    else:
        print("Opção incorreta!")
# 1. Faça um dicionário com as 5 pessoas mais perto de você, tendo o nome como chave e a cor da camisa que está usando como valor.

#Função de Títulos
def tittle(msg):
    print('~'*40)
    print(f'\033[32m{msg:^40}\033[m')
    print('~'*40)


#Dicionário contendo as informações {Indice = nome, e valor = Cor da Camisa}
pessoas = {'Murillo': 'Cinza', 'Naksia': 'Preto', 'Lorrane': 'Preto', 'Rayssa': 'Salmão', 'Renatão': 'Vermelho'}


tittle('Nomes das pessoas')

#Mostrar nomes
for i in pessoas.keys():
    print(i)

tittle('Todas as cores')

#Mostrar a cor da camisa
for v in pessoas.values():
    print(v)

#Título decorativo
tittle('As 5 pessoas ao meu redor')

#Título da tabela
print(f'{"Nome:":<15}{"Cor que está usando:"}')

#Mostra as informações requisitadas na tela
for i, v in pessoas.items():
    print(f'{i:.<20}', v)

# 5. Crie um programa onde 4 jogadores joguem um dado (1 a 6) e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
# No final tente colocar esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.(Opcional)
# Já utilizamos o método  random (from random import randint) para gerar números aleatórios. Utilize-o nesta atividade.

from random import randint

jogadas = {}
num = 0

for c in range(4):
    num = randint(1, 6)
    jogadas[f'Jogador{c+1}'] = num

ordem = sorted(jogadas.items())
print(ordem)
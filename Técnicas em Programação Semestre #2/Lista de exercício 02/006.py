# 06. Crie um programa que tenha uma tupla com dez palavras (somente letras minúsculas) e (Não use acentos). Depois mostre; Para cada palavra, quais são as suas vogais

palavras = ('casa', 'carro', 'cadeira', 'dado', 'dinamarca', 'palito', 'canela', 'apartamento', 'agua', 'loja')

for i, v in enumerate(palavras):
    print(f'{v}', end=' → ')
    for c in range(len(palavras[i])):
        if palavras[i][c] in 'aeiou':
            print(palavras[i][c], end='')
    print()
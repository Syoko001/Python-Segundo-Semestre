# 05. Desenvolva um programa que tenha uma tupla única com nomes de 10 produtos e seus respectivos preços em sequência. Ex (“Lapis”, “1.99”, “Borracha”, “0.99”).

tabela = ('Lápis', 1.99, 'Caneta', 2.00, 'Caderno', 24.90, 'Borracha', 0.50, 'Marcador', 4.90, 'Tinta', 3.90, 'Pincel', 7.90, 'Calculador', 19.90, 'Post-it', 2.90, 'Marca Texto', 9.50)

print('='*45)
print(f'{"TABELA DE PREÇOS":^45}')
print('='*45)

for cont in range(0, len(tabela)):
    if cont % 2 == 0:
        print(f'{tabela[cont]:.<40}', end='')
    if cont % 2 != 0:
        print(f'{tabela[cont]:>2.2f}')
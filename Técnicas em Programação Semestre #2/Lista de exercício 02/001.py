#01. Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de Zero até Vinte.

extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')


while True:
    numero = int(input('Digite um número entre 0 e 20: '))

    if numero > 20 or numero < 0:
        print('\033[31mValor inválido, tente novamente!!!\033[m')
    else:
        break

print(f'\033[32mVocê digitou o número: {extenso[numero]}\033[m')
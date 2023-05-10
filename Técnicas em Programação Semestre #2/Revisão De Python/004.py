#Crie um programa que receba um numero inteiro qualquer e traga em tela a sua tabuada de multiplicação.

numero = int(input('Digite o número desejado: '))

for contador in range(0, 11):
    oper_atual = contador * numero
    print(f'{contador} x {numero} = {oper_atual}')

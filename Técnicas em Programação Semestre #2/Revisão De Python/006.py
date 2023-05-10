from datetime import date

modelo = input('Digite o modelo de seu carro: ')
ano_fab = int(input('Agora, digite o ano de fabricação: '))

ano_ipva = date.today().year - ano_fab

if ano_ipva >= 15:
    print('Você esta insento do IPVA!')
else:
    print('Você deverá pagar o IPVA de seu carro!')
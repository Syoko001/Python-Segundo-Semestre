# 02. Crie uma tupla preenchida com os 30 primeiros colocados da tabela de carros mais vendidos no Brasil em 2022, depois mostre:

import os

carros = ('Fiat Strada', 'Hyundai HB20', 'Chevrolet Onix', 'Chevrolet Onix Plus', 'Fiat Mobi', 'Volkswagen Gol', 'Chevrolet Tracker', 'Volkswagen T-Cross', 'Fiat Argo',  'Jeep Compass',  'Hyundai Creta',  'Renault Kwid',  'Jeep Renegade',  'Fiat Pulse',  'Fiat Toro',  'Toyota Hilux',  'Toyota Corolla',  'Toyota Corolla Cross',  'Fiat Cronos',  'Volkswagen Nivus')
tittles = ('CARROS MAIS VENDIDOS 2022', 'Top 5 Carros Mais Vendidos 2022', '4 Últimos Colocados', 'Carro Favorito', 'Lista em ordem alfabética')
ordem_alfabetica = list()
opcao_user = 0
continuar = 'S'

def tittle_format():
    print('='*50)
    print(f'\033[34m{tittles[opcao_user]:^50}\033[m')
    print('='*50)


def opcoes():
    print()
    print('\033[30m     [ 1 ] - Mostre o Top 5.\033[m')
    print('\033[30m     [ 2 ] - Mostre os 4 últimos colocados.\033[m')
    print('\033[30m     [ 3 ] - Meu carro favorito.\033[m')
    print('\033[30m     [ 4 ] - Lista em ordem alfabética.\033[m')
    print()


while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        tittle_format()
        opcoes()

        while True:
            opcao_user = int(input('Digite a opção desejada: '))

            if opcao_user > 4 or opcao_user < 1:
                  print('Opção inválida, tente novamente!')
            else:
                  break
            
        if opcao_user == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            tittle_format()
            for i, v in enumerate(carros[0:6]):
                print(f'    {v}')
            print()
            
            opcao_user = 0

            while True:
                continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]

                if continuar not in 'SN':
                    print('Opção inválida, tente novamente!')
                else:
                     break
                

        elif opcao_user == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            tittle_format()
            for i, v in enumerate(carros[16:20]):
                print(f'    {v}')
            print()

            opcao_user = 0

            while True:
                continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]

                if continuar not in 'SN':
                    print('Opção inválida, tente novamente!')
                else:
                     break
                

        elif opcao_user == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            tittle_format()
            print()
            print(f'        \033[35m{carros[2]}\033[m')
            print()

            opcao_user = 0

            while True:
                continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]

                if continuar not in 'SN':
                    print('Opção inválida, tente novamente!')
                else:
                     break
            

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            tittle_format()

            for i, v in enumerate(carros):
                ordem_alfabetica.append(v)
                
            ordem_alfabetica.sort()
            
            print()
            for i, v in enumerate(ordem_alfabetica):
                print(f'    {v}')
            print()

            opcao_user = 0

            while True:
                continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]

                if continuar not in 'SN':
                    print('Opção inválida, tente novamente!')
                else:
                     break
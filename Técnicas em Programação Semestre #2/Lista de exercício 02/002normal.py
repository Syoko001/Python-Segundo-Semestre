# Crie uma tupla preenchida com os 30 primeiros colocados da tabela de carros mais vendidos no Brasil em 2022, depois mostre:
# A. Apenas os 5 primeiros colocados.
# B. Os últimos 4 colocados de sua tupla.
# C. O carro que você acha mais legal.
# D. Mostre sua Tupla em ordem Alfabética.

carros = ('Fiat Strada', 'Hyundai HB20', 'Chevrolet Onix', 'Chevrolet Onix Plus', 'Fiat Mobi', 'Volkswagen Gol', 'Chevrolet Tracker', 'Volkswagen T-Cross', 'Fiat Argo',  'Jeep Compass',  'Hyundai Creta',  'Renault Kwid',  'Jeep Renegade',  'Fiat Pulse',  'Fiat Toro',  'Toyota Hilux',  'Toyota Corolla',  'Toyota Corolla Cross',  'Fiat Cronos',  'Volkswagen Nivus')
alfabetica = []

for c in carros:
    alfabetica.append(c)

alfabetica.sort()

print(carros[:5])
print(carros[16:20])
print(carros[7])
print(alfabetica)
list = [1, 76, 1, 1, 'oi', 1]

list.extend(['pera', 76])
print(list)

list.insert(3, 'gato')
print(list)

list.insert(0, 99)
print(list)

print(f"oi, está na posição {list.index('oi')}")

print(f'Existem {list.count(76)} números 76 na lista')

list.remove(76)
print(list)
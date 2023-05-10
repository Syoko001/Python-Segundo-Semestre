def fizzbuzz_function(num):
    for v in range(num):

        if num % 3 == 0 and num % 5 == 0:
            print(f'{num} --- FIZZ BUZZ')
        elif num % 5 == 0:
            print(f'{num} --- BUZZ')
        elif num % 3 == 0:
            print(f'{num} --- FIZZ')
        else:
            print(num)
        
        num -= 1


numero = int(input('Digite um número: '))
fizzbuzz_function(numero)
    
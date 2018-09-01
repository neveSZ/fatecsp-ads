'''
Dado um numero inteiro n(n > 1), exibir os numeros multiplos de 3, ate no
maximo n.
'''
n = int(input('n: '))
for n in range(n):
    if(n % 3 == 0):
        print(n)

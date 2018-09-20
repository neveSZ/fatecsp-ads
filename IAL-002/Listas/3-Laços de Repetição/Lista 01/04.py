'''
Dado um numero inteiro n(n > 1), exibir os numeros multiplos de 3, ate no
maximo n.
'''
n = int(input('n: '))
for i in range(n+1):
    if(n % 3 == 0):
        print(n)

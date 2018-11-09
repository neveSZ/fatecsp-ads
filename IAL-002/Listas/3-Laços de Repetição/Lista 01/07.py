'''
Dado um numero inteiro n(n >  0), exibir os n primeiros pares iniciando em
trinta.
'''
contador = 0
numero = 30
n = int(input('n: '))
while contador < n:
    if numero % 2 == 0:
        print(numero)
        contador = contador + 1
    numero = numero + 1

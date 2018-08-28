'''
Dado um numero inteiro n(n > 1), exibir os numeros de n-1 ate 0. Quantos serao
impressos?
R:Nenhum
'''
n = int(input('n: '))
for n in range(n-1, 0):
    print(n)

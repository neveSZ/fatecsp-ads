'''
Fornecido um numero inteiro n(n>1), exibir os n primeiros termos da sequencia:
1,3,6,10,15,...
'''
soma = 0
n = int(input('n: '))
for i in range(1, n + 1):
    soma = soma + i
    print(soma)

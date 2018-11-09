'''
Fornecido um numero inteiro n(n>1), verifique se n e um numero primo. Exibir
'primo' ou 'nao primo' conforme o caso.
'''
n = int(input('n: '))
divisores = 0
i = 1
while divisores <= 2 and i <= n:
    if n % i == 0:
        divisores = divisores + 1
    i = i + 1
if divisores == 2:
    print('primo')
else:
    print('nao primo')

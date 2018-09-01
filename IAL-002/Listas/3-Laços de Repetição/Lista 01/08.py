'''
Dado um numero inteiro n(n >  0), seguido de n numeros inteiros, exibir a soma
dos n numeros lidos (o numero n nao entra na soma).
'''
n = int(input('n: '))
soma = 0
for i in range(n):
    soma = soma + int(input('n: '))
print(soma)

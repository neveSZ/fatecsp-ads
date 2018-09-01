'''
Dado um numero inteiro n(n >  0), seguido de n numeros inteiros, exibir a soma
dos n numeros lidos cujos valores sejam pares.
'''
n = int(input('n: '))
soma = 0
for i in range(n):
    leitura = int(input('n: '))
    if leitura % 2 == 0:
        soma = soma + leitura
print(soma)

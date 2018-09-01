'''
Dado um numero inteiro n (n>0), seguido de n números inteiros, exibir a soma
dos valores que são pares e a soma dos que são ímpares.
'''
par = 0
impar = 0
n = int(input("n: "))
for i in range(n):
    n = int(input("numero: "))
    if n % 2 == 0:
        par = par + n
    else:
        impar = impar + n
print('pares:', par)
print('impares:', impar)

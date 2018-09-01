'''
Dado um numero inteiro n (n>0), seguido de n numeros inteiros, exibir o menor
numero lido.
'''
menor = int(input('n: '))
for n in range(menor):
    n = int(input('n: '))
    if n < menor:
        menor = n
print(menor)

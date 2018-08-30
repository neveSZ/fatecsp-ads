'''
[Algoritmo de Euclides] Fornecidos dois numeros inteiros maiores que zero,
calcular o m.d.c (maximo divisor comum.) Pesquisar no livro do FORSYTHE et al.
Bibliografia 02
'''
a = int(input('a: '))
b = int(input('b: '))
if a < b:
    temp = a
    a = b
    b = temp
resto = a % b
mdc = b
while resto != 0:
    restotemp = resto
    resto = mdc % resto
    mdc = restotemp
print(mdc)

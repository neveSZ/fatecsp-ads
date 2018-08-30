'''
Fornecidos tres numeros naturais i,j e n, exibir em ordem crescente os n
primeiros multiplos de i e/ou de j,ou seja, nao devera exibir numeros repetidos
Exemplos:  Entrada:   i=3,j=4,n=7  -> Saida: 3 4 6 8 9 12 15
           Entrada:   i=30,j=2,n=6 -> Saida: 2 4 6 8 10 12
'''
i = int(input('i: '))
j = int(input('j: '))
n = int(input('n: '))
contador = 1
multiplo = 0
while(multiplo < n):
    if (contador % i == 0) or (contador % j == 0):
        print(contador)
        multiplo = multiplo+1
    contador = contador+1

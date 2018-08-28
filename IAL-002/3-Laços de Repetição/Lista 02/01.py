'''
Dizemos que um numero natural n (n>0) e triangular se ele e produto de tres
numeros naturais consecutivos. Exemplo: 210 e um numero triangular, pois
5x6x7=210.
Fornecido um numero natural n(n>0), exibir 'triangular' ou 'nao triangular',
conforme o caso
'''
n = int(input('n: '))
multiplicador = 1
multiplicacao = 1
while(multiplicacao < n):
    multiplicacao = multiplicador*(multiplicador+1)*(multiplicador+2)
    multiplicador = multiplicador+1
if(multiplicacao == n):
    print('triangular')
else:
    print('nao triangular')

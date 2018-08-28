'''
Dados dois numeros inteiros p(p≥0) e q(q>0), exibir a divisao inteira de p por
q sem usar os operadores de divisao, multiplicao e/ou potencia.
'''
p = int(input('p: '))
q = int(input('q: '))
contador = 0
while(p >= q):
    p = p-q
    contador = contador+1
print(contador)

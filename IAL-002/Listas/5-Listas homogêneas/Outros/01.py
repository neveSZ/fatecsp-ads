'''
Crie uma funcao que receba como parametros um vetor de inteiros a, um vetor de
inteiros b e o tamanho n de ambos. A funcao devera devolver um valor booleano
(True/False) indicando se a e igual a b. Use apenas um laco.
def iguais(a,b,n)
'''
def iguais(a, b, n):
    for i in range(n):
        if(a[i] != b[i]):
            return False
    return True

def maiores(a, m, n, x):
    # Recebe: uma matriz a, de m linhas por n colunas, e um inteiro x.
    # Retorna: a quantidade de elementos de a que sao maiores do que x.
    contador = 0
    for i in range(m):
        for j in range(n):
                if a[i][j] > x:
                    contador += 1
    return contador

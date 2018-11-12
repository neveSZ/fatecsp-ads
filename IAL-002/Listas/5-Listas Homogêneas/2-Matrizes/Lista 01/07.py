def media(a, m, n):
    # Recebe: uma matriz a, de m linhas por n colunas.
    # Retorna: a media aritmetica dos elementos de a.
    soma = 0.0
    for i in range(m):
        for j in range(n):
            soma += a[i][j]
    return soma/(m*n)

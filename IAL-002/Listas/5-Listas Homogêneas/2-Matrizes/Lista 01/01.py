def soma(a, b, m, n):
    # Recebe: as matrizes a e b, de m linhas por n colunas.
    # Retorna: a matriz c, sendo c[i][j]=a[i][j]+b[i][j] para 1<=i<=m e 1<=j<=n
    c = [[0 for i in range(m)] for j in range(n)]
    for i in range(m):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
    return c

def minimo(a, m, n):
    # Recebe: uma matriz a, de m linhas por n colunas.
    # Retorna: o menor elemento da a.
    menor = a[0][0]
    for i in range(m):
        for j in range(n):
                if menor > a[i][j]:
                    menor = a[i][j]
    return menor

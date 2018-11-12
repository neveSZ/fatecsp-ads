def impar(a, m, n):
    # Recebe: uma matriz a, de m linhas por n colunas.
    # Retorna: a quantidade de elementos impares de a.
    contador = 0
    for i in range(m):
        for j in range(n):
                if a[i][j] % 2 == 1:
                    contador += 1
    return contador

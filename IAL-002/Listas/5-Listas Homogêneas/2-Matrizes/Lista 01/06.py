def negativos(a, m, n):
    # Recebe: uma matriz a, de m linhas por n colunas.
    # Acao: transforma todos os elementos negativos de a em positivos.
    for i in range(m):
        for j in range(n):
                if a[i][j] < 0:
                    a[i][j] = a[i][j]*-1

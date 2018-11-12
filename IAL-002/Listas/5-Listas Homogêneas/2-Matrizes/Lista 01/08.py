def troca(a, b, m, n):
    # Recebe: duas matrizes a e b, de m linhas por n colunas.
    # Acao: troca os elementos de a com os de b.
    for i in range(m):
        for j in range(n):
            aux = a[i][j]
            a[i][j] = b[i][j]
            b[i][j] = aux

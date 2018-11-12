def multiplicacao(a, b, c, la, ca, lb, cb):
    # Recebe: uma matriz a, de la linhas por ca colunas, uma matriz b, de lb
    # linhas por cb colunas e uma matriz c.
    # Acao: construir c, que sera o resultado da multiplicacao de a por b.
    if la == cb:
        for i in range(la):
            for j in range(cb):
                for k in range(lb):
                    c[i][j] += a[i][k]*b[k][j]

def identidade(a, m, n):
    # Recebe: uma matriz a, de m linhas por n colunas.
    # Retorna: um valor booleano indicando se a e uma matriz identidade
    if m == n:
        for i in range(m):
            for j in range(n):
                if i == j:
                    if a[i][j] != 1:
                        return False
                else:
                    if a[i][j] != 0:
                        return False
    else:
        return False
    return True

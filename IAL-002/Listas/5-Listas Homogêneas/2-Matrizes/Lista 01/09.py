def primo(a, m, n):
    # Recebe: uma matriz a, de m linhas por n colunas.
    # Retorna: um valor booleano indicando se existe elemento primo em a.
    for i in range(m):
        for j in range(n):
            contador = 0
            for cont in range(1, a[i][j]):
                if a[i][j] % cont == 0:
                    contador += 1
                    if contador > 1:
                        break
            if contador == 1:
                return True
    return False

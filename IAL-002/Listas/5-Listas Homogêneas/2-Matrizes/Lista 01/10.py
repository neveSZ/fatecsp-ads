def sequencia(a, m, n):
    # Recebe: uma matriz a, de m linhas por n colunas.
    # Acao: preenche a com a sequencia 1, 3, 6, 10, 15...
    # Obs: preencher da esquerda para a direita e de cima para baixo.
    cont = 1
    ultimo = 0
    for i in range(m):
        for j in range(n):
            a[i][j] = cont + ultimo
            ultimo = a[i][j]
            cont += 1

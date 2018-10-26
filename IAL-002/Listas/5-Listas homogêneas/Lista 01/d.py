def junta_vetores(a, b, c, tam1, tam2):
    # Recebe: vetores a, b e c, com tam1 e tam2 elementos, respectivamente.
    # Acao: armazena em c os valores de a e b nessa ordem.
    # Retorna: quantidade de elementos copiados para c.
    cont = 0
    for i in range(tam1):
        c[cont] = a[i]
        cont = cont+1
    for i in range(tam2):
        c[cont] = b[i]
        cont = cont+1
    return cont

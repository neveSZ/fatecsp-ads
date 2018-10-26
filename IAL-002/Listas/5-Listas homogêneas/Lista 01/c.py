def zera_ind_par(a, tam):
    # Recebe: vetor a, com tam elementos.
    # Acao: zera os elementos de a com indice par.
    for i in range(tam):
        if i % 2 == 0:
            a[i] = 0

def soma_vetores(a, b, c, tam):
    # Recebe: vetores de a, b e c, com tam elementos cada.
    # Acao: constroi c[i] = a[i] + b[i]
    for i in range(tam):
        c[i] = a[i] + b[i]

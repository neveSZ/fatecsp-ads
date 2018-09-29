def produto(a, b):
    # Recebe: um inteiro a (a>=0) e um inteiro b (b>=0).
    # Retorna: um inteiro com o produto de a por b.
    # Obs: nao usar o operador de multiplicacao.
    prod = 0
    for i in range(b):
        prod = prod+a
    return prod

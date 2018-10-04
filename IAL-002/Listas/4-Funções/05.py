def divisao(p, q):
    # Recebe: um inteiro p (p>=0) e um inteiro q (q>0).
    # Retorna: um inteiro com o quociente da divisao inteira de p por q.
    # Obs: nao usar os operadores de divisao e/ou multiplicacao.
    div = 0
    while(p >= q):
        p = p-q
        div = div+1
    return div

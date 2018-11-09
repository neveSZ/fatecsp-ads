def potencia(b, e):
    # Recebe: um inteiro b (b>0) e um inteiro e (e>=0).
    # Retorna: um inteiro com a potencia de b elevado a e.
    # Obs: nao usar o operador de potenciacao ou qualquer outra funcao
    pot = 1
    for i in range(e):
        pot = pot*b
    return pot

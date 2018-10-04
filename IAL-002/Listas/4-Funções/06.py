def tamanho(n):
    # Recebe: um inteiro n (n>=0).
    # Retorna: um inteiro com a quantidade de algarismos de n.
    algarismo = 1
    while n >= 10 or n <= -10:
        n = n/10
        algarismo = algarismo+1
    return algarismo

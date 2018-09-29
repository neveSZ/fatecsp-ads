def fatorial(n):
    # Recebe: um inteiro n (n>0=0).
    # Retorna: um inteiro com fatorial de n.
    fat = 1
    for i in range(2, n+1):
        fat = fat*i
    return fat

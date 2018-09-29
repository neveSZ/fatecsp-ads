def binario(n):
    # Recebe: um inteiro n (n>0) em decimal.
    # Retorna: um inteiro com a representacao binaria de n.
    multiplicador = 1
    bin = 0
    while(n > 0):
        bin = (n % 2)*multiplicador+bin
        multiplicador = multiplicador*10
        n = n//2
    return bin

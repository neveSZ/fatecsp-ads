def primo(n):
    # Recebe: um inteiro n (n>1).
    # Retorna: um valor booleano indicando se n e primo.
    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False
    return True

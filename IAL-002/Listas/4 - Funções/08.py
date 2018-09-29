def nao_decrescente(n):
    # Recebe: um inteiro n (n>0).
    # Retorna: um valor booleano indicando se os digitos de n sao nao decrescentes.
    while (n >= 10):
        direita = n
        n = n//10
        if(direita % 10 >= n % 10):
            return True
    return False

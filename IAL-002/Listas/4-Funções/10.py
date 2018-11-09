def triangulo(a, b, c):
    # Recebe: tres valores reais a, b e c representando segmentos de reta.
    # Retorna: um valor booleano indicando se os segmentos podem formar um triangulo.
    if (a < b+c) and (b < a+c) and (c < a+b):
        if(c-b < a > b-c) and (c-a < b > a-c) and (b-a < c > a-b):
            return True
    return False

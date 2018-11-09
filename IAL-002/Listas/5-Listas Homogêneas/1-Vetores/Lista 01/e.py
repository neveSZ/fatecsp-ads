def intercala_vetores(a, b, c, tam1, tam2):
    # Recebe: vetores a, b e c, com tam1 e tam2 elementos, respectivamente.
    # Acao: constroi c intercalando os elementos de a e b.
    # Retorna: a quantidade de elementos copiados para c.
    # Obs.:
    # (a) a e b ja esta ordenados;
    # (b) a e b, individualmente, nao contem elementos repetidos;
    # (c) intercalar a e b em c ordenamente;
    # (d) c nao podera conter elementos repetidos;
    # (e) tam3 e no maximo tam1 + tam2, eventualmente sera menor.
    cont1 = 0
    cont2 = 0
    cont3 = 0
    while cont1 < tam1 or cont2 < tam2:
        if cont1 == tam1:
            c[cont3] = b[cont2]
            cont3 = cont3+1
            cont2 = cont2+1
        elif cont2 == tam2:
            c[cont3] = a[cont1]
            cont3 = cont3+1
            cont1 = cont1+1
        else:
            if a[cont1] < b[cont2]:
                c[cont3] = a[cont1]
                cont1 = cont1+1
                cont3 = cont3+1
            elif b[cont2] < a[cont1]:
                c[cont3] = b[cont2]
                cont2 = cont2+1
                cont3 = cont3+1
            else:
                c[cont3] = a[cont1]
                cont1 = cont1+1
                cont2 = cont2+1
                cont3 = cont3+1
    return cont3

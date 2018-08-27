'''
7. Fornecido os coeficientes de uma equação de segundo grau (com a≠0, ou seja,
não é necessário verificar a existência da equação), exibir suas raízes.

Obs. (2): Caso Δ seja negativo, imprimir suas raízes no formato x-yi e x+yi,
apos calcular x e y.
'''

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
delta = b*b-4*a*c
if delta == 0:
    print((-b+delta**(1/2))/(2*a))
else:
    if delta > 0:
        print((-b+delta**(1/2))/(2*a))
        print((-b-delta**(1/2))/(2*a))
    else:
        x = -b/2*a
        y = (-delta)**(a/2)
        print('%.2f+%.2fi' % (x, y))
        print('%.2f-%.2fi' % (x, y))

'''
Fornecido os coeficientes de uma equação de segundo grau (com a≠0, ou seja,
não é necessário verificar a existência da equação), exibir suas raízes.

Obs. (1): Para calcular a raiz quadrada de Δ, utilizar o operador de potência.
Obs. (2): Caso Δ seja negativo, imprimir ‘não existem raízes reais’
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
        print('não existem raízes reais')

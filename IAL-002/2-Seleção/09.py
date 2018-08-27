'''
Fornecidos os três segmentos de reta a, b e c que formam um triângulo,
exibir uma mensagem indicando qualo tipo de triângulo que será formado
(equilátero, isósceles ou escaleno)
'''

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
if(a == b == c):
    print("equilátero")
else:
    if(c != a != b != c):
        print("escaleno")
    else:
        print("isósceles")

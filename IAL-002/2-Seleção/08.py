'''
Fornecidos os três segmentos de reta: a, b e c (a>0, b>0 e c>0), verificar
se podem formar um triangulo. Exibir a mensagem ‘formam’ ou ‘não formam’,
conforme o caso.
'''

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
if (a < b+c) and (b < a+c) and (c < a+b):
    if(c-b < a > b-c) and (c-a < b > a-c) and (b-a < c > a-b):
        print('formam')
else:
    print('nao formam')

'''
4. Fornecido três números reais distintos a, b e c, exibir o maior valor.
'''

a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))
if(a>=b>=c or a>=c>=b):
    print(a)
else:
    if(b>=a>=c or b>=c>=a):
        print(b)     
    else:
        print(c)

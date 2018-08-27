'''
4. Fornecido três números reais distintos a, b e c, exibir o maior valor.
'''

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
if c < a > b:
        print(a)
else:
        if a < b > c:
                print(b)
        else:
                print(c)

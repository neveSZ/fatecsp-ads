'''
10. Fornecidas duas datas distintas, exibir qual delas ocorre primeiro. Cada data será fornecida em três valores inteiros, onde o primeiro representa o dia, o segundo o mês e o terceiro o ano.
'''
print('Data 1')
d1=float(input("dia: "))
m1=float(input("mes: "))
a1=float(input("ano: "))
print('Data 2')
d2=float(input("dia: "))
m2=float(input("mes: "))
a2=float(input("ano: "))
if a1>a2:
    print(d2,m2,a2)
else:
    if m1>m2:
        print(d2,m2,a2)
    else:
        if d1>d2:
            print(d2,m2,a2)
        else:
            print(d1,m1,a1)
        

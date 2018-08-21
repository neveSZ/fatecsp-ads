'''
12. Fornecidas as áreas de um circulo e de um quadrado, exibir ‘esconde’ se for possível ocultar completamente o quadrado sob o círculo, ou ‘não esconde’, caso contrário (adote π=3,14).
'''
circulo=float(input("circulo: "))
quadrado=float(input("quadrado: "))
if(circulo/3.14<=quadrado):
    print('esconde')
else:
    print('nao esconde')

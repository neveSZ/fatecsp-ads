'''
Fornecida a quantidade e o preço unitário de determinada peça, calcular e
exibir o total a pagar, sabendo que haverá um desconto de 10%.
'''
preco = float(input("valor unitario: "))
quantidade = int(input("quantidade: "))
print(preco * quantidade * 0.9)

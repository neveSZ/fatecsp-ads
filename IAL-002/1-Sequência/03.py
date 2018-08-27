'''
Fornecido um número inteiro n (n≥10), exibir o valor correspondente aos dois
dígitos mais à direita de n, sem utilizar o operador de resto.
'''

n = int(input("n: "))
print(n-(n//100*100))

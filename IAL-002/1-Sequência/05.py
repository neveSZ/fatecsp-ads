'''
Fornecido um número inteiro n (1000≤n≤9999), exibir a soma dos dois dígitos
à esquerda com os dois dígitos à direita. Exemplo: n = 3689,logo a saída é
36+98=125.
'''

n = int(input("n: "))
print(n//100+n-n//100*100)

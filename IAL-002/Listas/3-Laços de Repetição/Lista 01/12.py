'''
Dados números reais, exibir a media aritmetica deles. A entrada termina com a
leitura do numero zero.
'''
soma = 0
contador = 0
n = float(input("numero: "))
while (n != 0):
    soma = soma + n
    contador = contador + 1
    n = float(input("numero: "))
print(soma / contador)

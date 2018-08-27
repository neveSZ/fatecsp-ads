'''
Dados números inteiros, exibir a soma deles. A entrada termina com a
leitura do número zero.
'''
soma = 0
n = int(input("numero: "))
while (n != 0):
    soma = soma+n
    n = int(input("numero: "))
print(soma)

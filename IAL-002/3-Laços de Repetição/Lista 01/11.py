'''
Dados números inteiros, exibir a soma deles. A entrada termina com a leitura
do número zero. Ao menos um numero sera lido antes do zero.
'''
soma = 0
n = 0
while(n == 0):
    n = int(input("numero: "))
while (n != 0):
    soma = soma+n
    n = int(input("numero: "))
print(soma)

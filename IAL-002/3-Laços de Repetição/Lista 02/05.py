'''
Fornecido um numero inteiro n(n>0), exibir os digitos de n em ordem inversa
(use // e %).
Exemplo: entrada: 4690 -> saida: 0964
'''
n = int(input('n: '))
inverso = 0
i = 1
contador = 0
while (i < n):
    i = i*10
while (i != 1):
    i = i/10
    inverso = inverso + ((n // i % 10) * (10**contador))
    contador = contador+1
print(inverso)

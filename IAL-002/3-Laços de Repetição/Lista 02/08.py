'''
Fornecido um numero inteiro n(n≥0) em decimal, exibir seu correspondente em
binario (monte o binario usando apenas adicao, subtracao, multiplicacao e/ou
divisao)
Exemplo: Entrada: 13 -> Saida: 1101
'''
n = float(input('n: '))
contador = 1
binario = 0
while (n/2 > 0):
    resto = n-(n//2)*2
    binario = resto*contador+binario
    contador = contador*10
    n = n//2
print(binario)

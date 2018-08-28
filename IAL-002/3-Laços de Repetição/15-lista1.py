'''
Dado um numero inteiro n (n>0), calcular e exibir o maior quadrado menor ou
igual a n. Exemplo: n = 38, o maior quadrado que e menor ou igual a 38 e o 36,
portanto imprima 36. Nao usar o operador de potenciacao, nenhuma funcao pronta
e/ou conversao de tipos.
'''
quadrado = 0
i = 0
n = int(input('n: '))
while(i*i <= n):
    quadrado = i*i
    i = i+1
print(quadrado)

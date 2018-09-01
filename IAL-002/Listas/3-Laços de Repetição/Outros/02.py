'''
Crie um programa que leia um numero inteiro n e, em seguida leia diversos
outros inteiros ate que se insira um maior que n. O programa exibira a
quantidade de valores inseridos depois de n.
Obs: Usar while True(repita)
'''
n = int(input('n: '))
contador = 0
while True:
    numero = int(input('numero: '))
    contador = contador + 1
    if numero > n:
        break
print(contador)

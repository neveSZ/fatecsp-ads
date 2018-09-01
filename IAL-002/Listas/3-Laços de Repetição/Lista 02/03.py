'''
Fornecidas letras maiusculas, lidas uma por vez, ate ocorrer uma fora de ordem,
exibir a quantidade de letras lidas, exceto a letra fora de ordem.
Exemplo: 'A','C','K','M','M','T','B' -> 6
'''
atual = ''
antiga = ''
contador = -1
while (atual >= antiga):
    antiga = atual
    atual = input('letra: ')
    contador = contador + 1
print(contador)

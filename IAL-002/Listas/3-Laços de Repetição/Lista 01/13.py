'''
Dadas letras, uma por linha, exibir a quantidade de letras lidas. A entrada e
finalizada pelo caractere '!'.
'''
soma = 0
while True:
    letra = input("letra: ")
    if letra == '!':
        break
    soma = soma + 1
print(soma)

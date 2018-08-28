'''
Dadas letras, uma por linha, exibir a quantidade de letras lidas. A entrada e
finalizada pelo caractere '!'.
'''
soma = 0
letra = input("letra: ")
while letra != '!':
    soma = soma+1
    letra = input("letra: ")
print(soma)

'''
Dadas letras, uma por linha, exibir a quantidade de vogais lidas. A entrada e
finalizada pelo caractere '!'.
'''
soma = 0
while True:
    letra = input("letra: ")
    if letra == '!':
        break
    elif(letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' or letra == 'A' or letra == 'E' or letra == 'I' or letra == 'U'):
        soma = soma + 1
print(soma)

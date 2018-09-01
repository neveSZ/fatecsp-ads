'''
Dadas letras, uma por linha, exibir a quantidade de vogais lidas. A entrada e
finalizada pelo caractere '!'.
'''
soma = 0
letra = input("letra: ")
while letra != '!':
    if(letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' or
       letra == 'A' or letra == 'E' or letra == 'I' or letra == 'U'):
        soma = soma + 1
    letra = input("letra: ")
print(soma)

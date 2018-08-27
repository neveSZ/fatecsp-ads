'''
Fornecidos dois números inteiros a e b (a>0 e b>0), verificar se a é
divisível por b. Exibir a mensagem ‘divisível’ ou ‘não divisível, conforme o
caso. Não use o operador de resto.
'''

a = int(input("a: "))
b = int(input("b: "))
if a//b == a/b:
    print('divisível')
else:
    print('nao divisível')

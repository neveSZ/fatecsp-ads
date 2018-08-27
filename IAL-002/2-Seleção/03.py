'''
3. Fornecido um número n e um intervalo fechado de a até  b (a<b), verificar se
n está no intervalo. Exibir a mensagem ‘no intervalo’ ou ‘fora do intervalo’,
conforme o caso.
'''

n = float(input("n: "))
a = float(input("a: "))
b = float(input("b: "))
if (a < n < b):
    print('no intervalo')
else:
    print('fora do intervalo')

'''
Fornecido um numero inteiro n(n>0), exibir os digitos de n em ordem inversa
(use // e %).
Exemplo: entrada: 4690 -> saida: 0964
'''
n = int(input('n: '))
while True:
    r = n % 10
    print(r, end='')
    n = n // 10
    if(n == 0):
        break

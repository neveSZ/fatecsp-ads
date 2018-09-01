'''
Fornecido um numero inteiro n(n>10), exibir 'possui' caso n possua pelo menos
dois algarismos adjacentes sendo um impar e o outro par, ou 'nao possui', caso
contrario (use o operador de resto %).
Exemplos: Entrada: 532 -> Saida: possui
          Entrada: 1357-> Saida: nao possui
'''
verificador = False
i = 10
n = int(input('n: '))
while (i < n):
    esquerda = (n // i)
    direita = (n % i) // (i / 10)
    if((esquerda % 2 == 0 and direita % 2 != 0) or (esquerda % 2 != 0 and direita % 2 == 0)):
        verificador = True
        break
    else:
        i = i * 10
if(verificador):
    print('possui')
else:
    print('nao possui')

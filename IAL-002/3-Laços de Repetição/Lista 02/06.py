'''
Fornecido um numero inteiro n(n>10), determine se os digitos de n estao em
ordem estritamente crescente. Exibir 'sim' ou 'nao', conforme o caso (use // %)
Exemplos: Entrada: 577  -> Saida: 'nao'
          Entrada: 2579 -> Saida: 'sim'
'''
n = int(input('numero: '))
atual = 0
i = 1
verificador = True
contador = 0
antigo = 0
while (i < n and verificador):
    atual = n // i % 10
    if antigo <= atual and contador > 0:
        verificador = False
    contador = contador+1
    i = i*10
    antigo = atual
if(verificador):
    print('sim')
else:
    print('nao')

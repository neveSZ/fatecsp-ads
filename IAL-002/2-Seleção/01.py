'''
1. Observe as seguintes características:
O número 2025 tem: 20+25=45 e 45x45=2025
O número 1063 tem: 10+63=73 e 73x73≠1063
Dado um numero inteiro positivo n de quatro dígitos, verificar se n é um numero cuja raiz quadrada é formada pela soma de suas dezenas. Exibir ‘sim’ ou ‘não’. Não use o operador de potência, nem funções.
'''

n=int(input("n: "))
soma=(n-(n//100)*100+(n//100))
if soma*soma==n:
    print('sim')
else:
    print('nao')

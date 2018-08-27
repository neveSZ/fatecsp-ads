'''
Dado um salário atual em reais e uma idade em anos, calcular o novo salário,
que será o salário atual acrescido da idade em porcentagem.
Exemplo: salário atual = R$ 1000,00 e idade = 23, logo,
salário novo = R$ 1000 + 23% de R$ 1000,00 = R$ 1230,00.
'''

salario = float(input("salario: "))
idade = int(input("idade: "))
print(salario*idade/100+salario)

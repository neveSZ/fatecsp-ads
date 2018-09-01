'''
Calcule a nota final de um aluno sabendo que ela é composta da seguinte
forma: Prova 1 (40%) + Prova 2 (40%) + Trabalhos (20%). Os três valores que
compõem a nota final serão informados pelo usuário, exiba-a com duas casas
decimais.
'''
a = float(input("prova 1: "))
b = float(input("prova 2: "))
c = float(input("prova 3: "))
print("%.2f" % (a * 0.4 + b * 0.4 + c * 0.2))

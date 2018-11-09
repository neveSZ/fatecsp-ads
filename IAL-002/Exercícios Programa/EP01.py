'''
+-----------------------------------------------------------------------------+
| Instituição   :  Faculdade de Tecnologia de São Paulo                       |
| Departamento  :  Tecnologia da Informação                                   |
| Curso         :  Análise e Desenvolvimento de Sistemas                      |
| Disciplina    :  IAL-002                                                    |
| Turno         :  Vespertino                                                 |
| Aluno         :  Victor Neves Silva                                         |
| Matrícula     :  18203756                                                   |
+-----------------------------------------------------------------------------+
| Programa      :  EP01.py - O Amanhã                                         |
| Linguagem     :  Python 3                                                   |
| Compilador    :  CPython (3.6.2)                                            |
+-----------------------------------------------------------------------------+
'''
while True:
    dia = int(input())
    mes = int(input())
    ano = int(input())
    if 12 >= mes > 0 and dia > 0 and ano > 0:
        # Descobrir dia maximo do mes
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            diamax = 30
        elif mes == 2:
            if ano % 4 == 0:
                diamax = 29
            else:
                diamax = 28
        else:
            diamax = 31
        # Ir para o proximo dia
        if(dia < diamax):
            dia = dia + 1
            print(dia, mes, ano)
            break
        elif dia == diamax:
            dia = 1
            if mes < 12:
                mes = mes + 1
            else:
                mes = 1
                ano = ano + 1
            print(dia, mes, ano)
            break
        else:
            print('Data inválida')
    else:
        print('Data inválida')

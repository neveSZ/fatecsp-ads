'''
11. Dado um numero inteiro n, exibir o dia da semana correspondente(domingo=1)
ou ‘dia inválido’.
'''
n = int(input("n: "))

if n == 1:
    print('domingo')
else:
    if n == 2:
        print('segunda-feira')
    else:
        if n == 3:
            print('terca-feira')
        else:
            if n == 4:
                print('quarta-feira')
            else:
                if n == 5:
                    print('quinta-feira')
                else:
                    if n == 6:
                        print('sexta-feira')
                    else:
                        if n == 7:
                            print('sabado')
                        else:
                            print('dia invalido')

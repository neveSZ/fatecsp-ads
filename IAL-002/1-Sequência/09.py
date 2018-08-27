'''
Dados os tempos gastos em uma viagem com caminhada, ônibus e metro
(em minutos) exibir o tempo total gasto em três unidades: em horas, em minutos
e em segundos.
'''

caminhada = int(input("caminhada: "))
onibus = int(input("onibus: "))
metro = int(input("metro: "))
print("Horas: ", (caminhada+onibus+metro)/60)
print("Minutos: ", caminhada+onibus+metro)
print("Segundos", (caminhada+onibus+metro)*60)

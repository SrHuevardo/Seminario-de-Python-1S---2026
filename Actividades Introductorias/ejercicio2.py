""" Escribe un programa que solicite al usuario una cantidad de segundos y muestre
cuántas horas, minutos y segundos equivalen. Por ejemplo, 3661 segundos son 1 hora, 1 minuto y 1 segundo.
"""

segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60

print(segundos, "segundos equivalen a", horas, "horas,", minutos, "minutos y", segundos_restantes, "segundos.")

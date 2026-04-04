"""
Crea un programa que solicite al usuario un número y muestre su tabla de multiplicar
del 1 al 10 utilizando un bucle for
"""

numero = int(input("Ingrese un numero: "))
print("Tabla de multiplicar del", numero)
for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)

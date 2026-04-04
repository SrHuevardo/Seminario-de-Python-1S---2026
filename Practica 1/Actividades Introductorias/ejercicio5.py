"""
Escribe un programa que simule una caja registradora: el usuario ingresa precios de
productos de a uno. Cuando ingresa 0, el programa se detiene y muestra el total
acumulado. Nota: utilizá la sentencia break cuando haga falta.
"""
total = 0.0
while True:
    precio = float(input("Ingrese el precio del producto (0 para finalizar): "))
    if precio == 0:
        break
    total += precio

print("El total acumulado es: $", total)

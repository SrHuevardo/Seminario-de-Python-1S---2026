"""
Crea un programa que dado un número N ingresado por el usuario, imprima los
números del 1 al N pero saltee los múltiplos de 5. Nota: utilizá la sentencia continue
Entrega
donde haga falta.
"""
N = int(input("Ingrese un numero: "))
for i in range(1, N + 1):
    if i % 5 == 0:
        continue
    print(i)

"""
Crea un programa que dado un número N ingresado por el usuario, imprima los
números del 1 al N pero saltee los múltiplos de 5. Nota: utilizá la sentencia continue donde haga falta.
Modifica el ejercicio para que, en lugar de imprimir los números, genere dos listas:
una con los múltiplos de 5 y otra con el resto de los números. Imprimí ambas listas al
finalizar.
"""

N = int(input("Ingrese un numero: "))
multiplos_de_5 = []
resto_de_numeros = []
for i in range(1, N + 1):
    if i % 5 == 0:
        multiplos_de_5.append(i)
        continue
    resto_de_numeros.append(i)
    
print("Multiplos de 5:", multiplos_de_5)
print("Resto de numeros:", resto_de_numeros)
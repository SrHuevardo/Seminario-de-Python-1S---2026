"""
Escribe un programa que solicite al usuario una lista de palabras. Luego, construí una
oración uniendo únicamente las palabras que tengan más de 3 letras, separadas por
espacios. Las palabras cortas deben ser excluidas del resultado final.
"""

palabras = input("Ingrese una lista de palabras separadas por espacios: ").split()
oracion = " ".join([palabra for palabra in palabras if len(palabra) > 3])
print("La oración construida es:", oracion)


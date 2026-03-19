import random

words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]

word = random.choice(words).upper() # para mayor claridad convierto a mayus 
guessed = []
attempts = 6
score = 0 # variable mod del puntaje 

print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter
        else:
            progress += "_"
    
    print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        score += 6
        print("¡Ganaste!")
        print (f"Tu puntaje es: {score}")
        break
        
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    
    letter = input("Ingresá una letra: ").upper() # en caso de que se ingrese una minuscula, automaticamente se convierte en mayus
    
    if len(letter) != 1 or not letter.isalpha():
        print("Entrada no valida")
        continue

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        print("¡Bien! Esa letra está en la palabra.")
        guessed.append(letter)
    else:
        print("Esa letra no está en la palabra.")
        guessed.append(letter)
        attempts -= 1
        score -= 1 
    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
    score = 0
    print(f"Tu puntaje final es: {score}")
    
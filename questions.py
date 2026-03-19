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
        print("¡Ganaste!")
        break
        
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    
    letter = input("Ingresá una letra: ").upper() # en caso de que se ingrese una minuscula, automaticamente se convierte en mayus
    
    # --- Modificacion de Bug ---
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
        
    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
    
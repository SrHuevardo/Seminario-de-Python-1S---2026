import random


dictionary = {
    "programacion": ["python", "programa", "variable", "funcion", "bucle", "cadena", "entero", "lista"],
    "animales": ["perro", "gato"],
    "paises": ["argentina", "brasil", "uruguay", "chile", "peru"]
}

score = 0 

# lista de palabras ya jugadas
usedWords = []


while True:
    print("¡Bienvenido al Ahorcado!")
    print("\nCategorias disponibles:")
    for category in dictionary.keys():
        print(f"- {category.capitalize()}")

    category = input("Elegi una categoria: ").lower()

    while category not in dictionary:
        print("Categoria no valida, intente de nuevo.")
        category = input("Elegi una categoria: ").lower()
    
    #--- mod para evitar palabras ya jugadas --- 
    avblWords = [aw for aw in dictionary[category] if aw not in usedWords]

    if not avblWords:
        print("No quedan palabras disponibles en esta categoria, elegi otra.")
        continue

    word = random.sample(avblWords, 1)[0].upper()
    usedWords.append(word.lower())

    guessed = [] 
    attempts = 6 

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
        
        letter = input("Ingresá una letra: ").upper() 
        
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



    again = input("¿Querés jugar otra vez? (s/n): ").lower() 
    if again != 's':
        print(f"¡Gracias por jugar! Tu puntaje final es: {score}")
        break
    
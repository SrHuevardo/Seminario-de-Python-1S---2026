import random

dictionary = {
    "programacion": ["python", "programa", "variable", "funcion", "bucle", "cadena", "entero", "lista"],
    "animales": ["perro", "gato"],
    "paises": ["argentina", "brasil", "uruguay", "chile", "peru"]
}

score = 0 
category = None     # mod para poder decidir si cambiar o no la categoria.

usedWords = []

print("¡Bienvenido al Ahorcado!")
while True:
    
    if category is None:
        print("\nCategorias disponibles:")
        for category in dictionary.keys():
            print(f"- {category.capitalize()}")
        category = input("Elegi una categoria: ").lower()

        while category not in dictionary:
            print("Categoria no valida, intente de nuevo.")
            category = input("Elegi una categoria: ").lower()


    avblWords = [aw for aw in dictionary[category] if aw not in usedWords]

    if not avblWords:
        print("No quedan palabras disponibles en esta categoria, elegi otra.")
        category = None
        continue

    word = random.sample(avblWords, 1)[0].upper()
    usedWords.append(word.lower())

    guessed = [] 
    attempts = 6 

    while attempts > 0:

        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter
            else:
                progress += "_"
        
        print(progress)

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


#--- modificacion del corte del juego, para evitar respuestas invalidas y chance de cambiar la categoria ---
    again = input("¿Queres jugar otra vez? (s/n): ").lower() 
    
    while again not in ['s', 'n']:
        print("Entrada no válida. Por favor, ingresa 's' o 'n'.")
        again = input("¿Queres jugar otra vez? (s/n): ").lower()

    if again == 'n':
        print(f"¡Gracias por jugar! Tu puntaje final es: {score}")
        break
    
    else:
        changeCategory = input("Queres cambiar de categoria? (s/n): ").lower()
        while changeCategory not in ['s', 'n']:
            print("Entrada no válida. Por favor, ingresa 's' o 'n'.")
            changeCategory = input("Queres cambiar de categoria? (s/n): ").lower()

        if changeCategory == 's':
            category = None
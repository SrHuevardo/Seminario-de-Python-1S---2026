"""Desarrollar un programa que simule la tabla de posiciones de un torneo de fútbol. El
programa debe tener un menú interactivo con las siguientes opciones:
1) Agregar un equipo al torneo.
2) Registrar un resultado ingresando equipo local, equipo visitante y marcador en formato 4 - 2. El programa debe actualizar los puntos automáticamente (3 puntos por victoria, 1 por empate, 0 por derrota).
3) Mostrar la tabla de posiciones ordenada de mayor a menor puntaje.
4) Eliminar un equipo del torneo.
5) Salir del programa.
Se deben manejar situaciones como intentar agregar un equipo ya existente, registrar un
resultado con un equipo desconocido, o ingresar un marcador con formato inválido."""

tabla = {}

while True:
    print("\n" + "="*50)
    print("SALE FULBITO ??")
    print("="*50)
    print("1. Agregar un equipo")
    print("2. Registrar un resultado")
    print("3. Mostrar tabla de posiciones")
    print("4. Eliminar un equipo")
    print("5. Salir")
    print("="*50)
    
    opcion = input("Elegi una opción (1-5): ")
    
    if opcion == '1':
        equipo = input("Ingresa el nombre del equipo: ").capitalize()
        
        if equipo in tabla:
            print(f"Error: El equipo '{equipo}' ya esta participando en el torneo.")
        else:
            tabla[equipo] = 0  
            print(f"El equipo '{equipo}' fue agregado exitosamente!")
            
    elif opcion == '2':
        print("Agarrando la pala...")
        
    elif opcion == '3':
        print("Agarrando la pala...")
        

    elif opcion == '4':
        print("Agarrando la pala...")
        
    elif opcion == '5':
        print("Gracias vuelva prontos!")
        break 
        
    else:
        print("Opcion no valida. Por favor, ingresa un numero del 1 al 5.")
    
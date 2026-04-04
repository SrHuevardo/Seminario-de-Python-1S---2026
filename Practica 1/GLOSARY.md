# --- GLOSARIO PYTHON - Seminario de Lenguajes 2026 ---

Aca voy a ir añadiendo palabras y conceptos que vaya aprendiendo y utilizando en las practicas que van a ser subidas a este repo, para que pueda consultarlos en el futuro y no tener que googlear cada vez que me olvide de algo, o para compartirlo con otros que puedan estar aprendiendo tambien

---

## 1. Estructuras de Datos
* **Listas `[]`**: Colecciones ordenadas y mutables (modificables). Pueden contener cualquier tipo de dato.
  * *Ejemplo*: `letras_usadas = []`
* **Diccionarios `{}`**: Colecciones que guardan la información en pares de `clave: valor`. No tienen índice numérico, se accede por la clave.
  * *Ejemplo*: `categorias = {"animales": ["perro", "gato"]}`

## 2. Control de Flujo
* **`while`**: Bucle que repite un bloque de código mientras una condición sea `True`.
* **`for ... in ...`**: Bucle que itera sobre los elementos de una secuencia (como una lista o un string).
* **`if` / `elif` / `else`**: Estructuras condicionales. Evalúan en orden hasta encontrar una verdadera.
* **`break`**: Corta abruptamente el bucle (`while` o `for`) en el que se encuentra y sale de él.
* **`continue`**: Interrumpe la iteración actual del bucle y vuelve al inicio para comenzar la siguiente vuelta.

## 3. Tipos de Datos Especiales
* **`None`**: Representa la ausencia de valor, útil para inicializar variables vacías antes de asignarles algo (ej: `categoria = None`).

## 4. Funciones Integradas (Built-ins)
* **`print()`**: Muestra información en la consola. Con una `f` adelante (f-strings), permite inyectar variables directamente: `print(f"Puntaje: {score}")`.
* **`input()`**: Pausa el programa, muestra un mensaje y espera a que el usuario escriba. **Siempre devuelve un string (texto)**.
* **`len()`**: Devuelve la longitud (cantidad de elementos) de una lista, string, etc.
* **`int()` y `float()`**: Funciones de casteo. Convierten un texto a número entero o decimal, respectivamente.

## 5. Métodos de Strings (Textos)
* **`.upper()` / `.lower()`**: Convierten todo el texto a mayúsculas o minúsculas.
* **`.capitalize()`**: Convierte solo la primera letra del texto a mayúscula.
* **`.isalpha()`**: Devuelve `True` solo si todos los caracteres del string son letras del abecedario.
* **`.split()`**: Corta un string (por defecto, en los espacios) y devuelve una lista de palabras.
* **`.join()`**: Toma una lista de strings y los une usando un separador. Ej: `", ".join(lista)`.

## 6. Métodos de Listas y Diccionarios
* **`.append(x)`**: Agrega el elemento `x` al final de una lista.
* **`.keys()`**: Devuelve una vista con todas las claves de un diccionario.

## 7. Módulo `random`
Requiere poner `import random` al principio del archivo.
* **`random.choice(lista)`**: Elige y devuelve un solo elemento al azar de la lista.
* **`random.sample(lista, cantidad)`**: Devuelve una **nueva lista** con la cantidad solicitada de elementos únicos elegidos al azar.

## 8. Herramientas "Pythónicas"
* **Comprensión de Listas**: Una forma compacta y rápida de crear una lista nueva a partir de otra, aplicando filtros o modificaciones en una sola línea.
  * *Sintaxis*: `[elemento for elemento en lista_original si condicion]`
  * *Ejemplo*: `[palabra for palabra en lista if palabra not in jugadas]`
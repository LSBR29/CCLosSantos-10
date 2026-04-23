"""
1. c
2. b
3. d
4. b
5. c
6. c
7. a
8. d
9. c
10. a
"""

# Se imprime un mensaje para identificar que se está pidiendo
print("Visitante 1")
nombre_1 = input("Nombre: ")    # Se pide un primer nombre
try:
    edad_1 = int(input("Edad: "))   # Dentro de un bloque try se pide la edad y se convierte a int
except ValueError:
    print("Error: edad no válida, se asigna 0.")    # Si no fuese posible convertir la edad, se imprime un error
    edad_1 = 0                                      # Y se fija la edad en 0

# Se repite el proceso para el visitante 2 y 3
# Notar que las variables tienen otro nombre, para no perder la información anterior
print("\nVisitante 2")
nombre_2 = input("Nombre: ")
try:
    edad_2 = int(input("Edad: "))
except ValueError:
    print("Error: edad no válida, se asigna 0.")
    edad_2 = 0

print("\nVisitante 3")
nombre_3 = input("Nombre: ")
try:
    edad_3 = int(input("Edad: "))
except ValueError:
    print("Error: edad no válida, se asigna 0.")
    edad_3 = 0

# Se crean las listas nombres y edades con la información ingresada
nombres = [nombre_1, nombre_2, nombre_3]
edades = [edad_1, edad_2, edad_3]

# Creación de la lista con primeras letras
# Se usa nombres[i][j], i es el índice en la lista de cada nombre
# j se utiliza para extraer la primera letra (slicing)
primeras_letras = [nombres[0][0], nombres[1][0], nombres[2][0]]
"""Otra opción
primeras_letras = [nombre1[0], nombre2[0], nombre3[0]]
"""

# Creación de la lista de paridades
paridades = []
if edades[0] == 0:              # Primero se revisa si es cero
    paridades.append("error")   # Con append se añade a la lista paridades que inicialmente está vacía
elif edades[0] % 2 == 0:        # Luego si es par con el residuo a 2
    paridades.append("par")
else:                           # En otro caso se sabe que es impar
    paridades.append("impar")

# Se repite el proceso para edades[1] y edades[2]
if edades[1] == 0:
    paridades.append("error")
elif edades[1] % 2 == 0:
    paridades.append("par")
else:
    paridades.append("impar")

if edades[2] == 0:
    paridades.append("error")
elif edades[2] % 2 == 0:
    paridades.append("par")
else:
    paridades.append("impar")

# Se imprimen los resultados
print("\nResultados")
print(f"Nombres: {nombres}")
print(f"Edades: {edades}")
print(f"Primeras Letras: {primeras_letras}")
print(f"Paridades: {paridades}")

# EXTRA: Con max() se obtiene el valor máximo en una lista, en este caso edades
print(f"Edad Máxima: {max(edades)} (PUNTOS EXTRA)")

"""Otra opción
edad_maxima = 0

if edades[0] > edad_maxima:
    edad_maxima = edades[0]

if edades[1] > edad_maxima:
    edad_maxima = edades[1]

if edades[2] > edad_maxima:
    edad_maxima = edades[2]
"""
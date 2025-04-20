# Declaración de lista
lista = ["hola", "elefante", "sol"]

# Declaración de nueva lista vacía para las longitudes
longitudes = []

# Recorrer la lista palabra por palabra
for palabra in lista:
    # Obtener el tamaño de la palabra
    largo = len(palabra)

    # Añadir el tamaño a la lista de longitudes
    longitudes.append(largo)

print(longitudes)


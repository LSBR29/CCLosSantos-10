# Declaración de lista
lista = ["Hola", "mundo", "esto", "es", "Python"]

# Declaración del string resultante
string = ""

# Método 1: Iterar por elementos
for palabra in lista:
    # Concatenar al string la palabra y un espacio al final
    string += palabra + " "


# Método 2: Índices
for i in range(len(lista)):
    # Concatenar al string la palabra y un espacio al final
    string += lista[i] + " "

# Imprimir el string sin espacios alrededor (para quitar el último espacio agregado de la concatenación)
print(string.strip())
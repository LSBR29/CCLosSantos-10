# Declarar la lista de la palabras
lista = ["luz", "sol", "coral", "animal"]

# Declarar letra final a buscar
letra = "l"

# Declarar de nueva lista vacía para el resultado
resultado = []

# Recorrer la lsita palabra por palabra
for palabra in lista:
    # Si la última letra es igual a la buscada se añade la palabra al resultado
    if palabra[-1] == letra:
        resultado.append(palabra)

print(resultado)
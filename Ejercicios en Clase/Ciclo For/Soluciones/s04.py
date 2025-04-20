# Declarar la lista de la palabras
lista = ["casa", "carro", "perro", "gato"]

# Declarar letra a buscar
letra = "r"

# Declarar variable contador
contador = 0

# Recorrer la lista palabra por palabra
for palabra in lista:
    # Si la letra buscada está en la palabra, se suma 1 al contador
    if letra in palabra:
        contador += 1

print(contador)

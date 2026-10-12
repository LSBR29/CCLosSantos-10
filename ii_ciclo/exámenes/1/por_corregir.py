# 1. Manejo de archivos
archivo = open("datos.txt", "w")
contenido = archivo.read()
print(contenido)


# 2. Uso de ciclos
def sumar_lista(lista):
    total = 0
    for i in range(1, len(lista)):
        total += lista[i]
    return total


# 3. Calcule la complejidad temporal
def contar_repetidos(lista):
    contador = 0
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i != j and lista[i] == lista[j]:
                contador += 1
    return contador

# Complejidad temporal:
# Justificación:


# 4. Calcule la complejidad espacial
def lista_de_cuadrados(lista):
    resultado = []
    for x in lista:
        resultado.append(x ** 2)
    return resultado

# Complejidad espacial:
# Justificación:
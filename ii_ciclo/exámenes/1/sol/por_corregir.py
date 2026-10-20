# 1. Manejo de archivos
archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
# El modo "w" no permite leer (y además borra el contenido). Se usa "r".


# 2. Uso de ciclos
def sumar_lista(lista):
    total = 0
    for i in range(len(lista)):
        total += lista[i]
    return total
# range(2, ...) se salta los dos primeros elementos. Debe empezar en 0.


# 3. Calcule la complejidad temporal
def contar_repetidos(lista):
    contador = 0
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i != j and lista[i] == lista[j]:
                contador += 1
    return contador

# Complejidad temporal: O(n²)
# Justificación: dos ciclos anidados, cada uno recorre los n elementos.


# 4. Calcule la complejidad espacial
def lista_de_cuadrados(lista):
    resultado = []
    for x in lista:
        resultado.append(x ** 2)
    return resultado

# Complejidad espacial: O(n)
# Justificación: se crea una lista nueva con un elemento por cada elemento de la entrada.
# Lista inicial
lista = ["hola", "elefante", "mundo", "estrella"] 
nueva_lista = []

# Método 1: como iterador
# Recorrer lista
for palabra in lista:
    # Largo de la palabra mayor que 5
    if len(palabra) > 5:
        # Convertir a mayúscula
        nueva_lista.append(palabra.upper())
    else:
        # Agregar la palabra normal
        nueva_lista.append(palabra)

# Mostrar lista resultante
print(nueva_lista)



# Método 2: por índice
for i in range(len(lista)):
    # Modificar el índice de la lista
    if len(lista[i]) > 5:
        lista[i] = lista[i].upper()

# Imprimir el resultado
print(lista)
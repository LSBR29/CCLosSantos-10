# Declaración de la lista
lista = [2,1,3,4,5]

# Variable booleana que va a rastrear si la condición se sigue cumpliendo o no
estaOrdenada = True

# Recorrer la lista mediante índices
for i in range(len(lista) - 1):
    # Verificar que el elemento actual sea menor que el siguiente
    if lista[i] > lista[i+1]:
        # Cambiar el estado de la variable booleana
        estaOrdenada = False
        break # Salir porque ya se determinó que no está ordenada

# Imprimir resultado
print(estaOrdenada)


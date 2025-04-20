# Declaración de lista
lista = [1, 2, 3, 4, 5, 6]

# Declarar contadores
contadorPares = 0
contadorImpares = 0

# Recorrer la lista
for numero in lista:
    # Verificar residuo respecto a 2
    if numero % 2 == 0:
        contadorPares += 1
    elif numero & 2 == 1:
        contadorImpares += 1

# Imprimir resultados
print(f"Pares: {contadorPares}, Impares: {contadorImpares}")


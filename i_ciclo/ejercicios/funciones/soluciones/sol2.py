def analizar_texto(texto):
    palabras = texto.split()  # Separar palabras
    frecuencias = {}  # Diccionario para contar frecuencia

    # Contar frecuencia de cada palabra
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    # Encontrar la palabra más repetida
    palabra_mas_repetida = ''
    max_frecuencia = 0
    for palabra in frecuencias:
        if frecuencias[palabra] > max_frecuencia:
            max_frecuencia = frecuencias[palabra]
            palabra_mas_repetida = palabra

    return palabra_mas_repetida, frecuencias

# Función principal
if __name__ == "__main__":
    texto = input("Ingrese el texto: ")

    palabra_mas_repetida, frecuencias = analizar_texto(texto)

    print(f"\nPalabra más repetida: '{palabra_mas_repetida}'")
    print(f"Frecuencia: {frecuencias}")
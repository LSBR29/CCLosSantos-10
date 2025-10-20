import utilidades_texto

if __name__ == "__main__":
    texto = input("Ingresa un texto: ")

    num_vocales = utilidades_texto.contar_vocales(texto)
    texto_invertido = utilidades_texto.invertir_texto(texto)

    print(f"Número de vocales: {num_vocales}")
    print(f"Texto invertido: {texto_invertido}")
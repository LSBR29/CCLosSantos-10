#Función para pedir una palabra y validar que solo tenga letras
def pedir_palabra():
    palabra = input("Ingrese una palabra: ")

    #Se usa un ciclo while par apedir la palabra hasta que solo tenga letras
    while palabra.isalpha() == False:
        print("Error: Solo puede contener letras\n")
        palabra = input("Ingrese una palabra: ")

    #Se retorna la palabra en minúsculas
    return palabra.lower()

#Función principal
if __name__ == "__main__":
    #Se llama la función para pedir la palabra
    palabra = pedir_palabra()

    #Se crea una variable set para guardar información sin repetirla
    vocales = set()

    #Se recorre la palabra con un ciclo for letra por letra
    for letra in palabra:

        #Si la letra está en la tupla con vocales, se añade al set
        if letra in ("a", "e", "i", "o", "u"):
            vocales.add(letra)

    #Se imprime lo solicitado
    print(f"Número de vocales únicas: {len(vocales)}")
    print(f"Vocales encontradas: {vocales}")
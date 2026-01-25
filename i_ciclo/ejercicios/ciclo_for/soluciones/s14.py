# Lista a analizar
lista = ["sol", "gato", "taza", "luz", "elefante"]

# Declarar de nueva lista vacía para el resultado
resultado = []

# Recorrer la lista palabra por palabra
for palabra in lista:
    # Declarar una lista vacía para guardar la letras de la palabra sin repetirlas
    letras_sin_repetir = []
    repetidas = False
    
    # Recorrer la palabra letra por letra
    for letra in palabra:
        # Si la letra aún no estaba añadida, se añade. En caso contrario, esa palabra tiene letras repetidas
        if letra not in letras_sin_repetir:
            letras_sin_repetir.append(letra)
        else:
             repetidas = True
             break
        
    # Si la palabra tenía letras repetidas se añade al resultado
    if repetidas:
        resultado.append(palabra)

print(resultado)
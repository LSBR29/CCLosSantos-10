# Lista a analizar
lista = ["sky", "agua", "sol", "fly"]

# Declaración de variable contador
contador = 0

# Recorrer la lista palabra por palabra
for palabra in lista:
    # Recorrer la palabra letra por letra
    for letra in palabra:
        
        # Si una de las letras es vocal, se aumenta el contador y se detiene el ciclo sobre esa palabra para ir a la siguiente
        if letra in 'aeiou':
            contador += 1
            break

print(contador)
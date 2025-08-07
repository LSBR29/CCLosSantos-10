# String a analizar
palabra = input("Ingrese un string: ")

# Declaración la nueva palabra como vacía
nueva_palabra = ""

# Recorremos el strign letra por letra
for letra in palabra:
    # Si la letra es vocal la añadimos a la nueva palabra como string, en otro caso la añadimos normalmente
    if letra in "aeiou":
        nueva_palabra += "*"
    else:
        nueva_palabra += letra

print(nueva_palabra)
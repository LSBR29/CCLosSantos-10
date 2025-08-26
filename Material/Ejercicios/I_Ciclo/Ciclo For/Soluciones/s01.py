# String a analizar
string = input("Ingrese un string: ")

# Declaración de variable contador (mantener la cuenta de vocales)
contador = 0

# Recorrer string en minúsculas
for letra in string.lower():
    # Si la letra (variable iteradora) está en el string "aeiou", incrementar valor de contador en 1
    if letra in "aeiou":
        contador += 1

# Imprimir valor de contador
print(contador)
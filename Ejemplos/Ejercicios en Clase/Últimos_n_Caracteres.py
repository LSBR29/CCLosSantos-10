#Pedimos una palabra
palabra = input("Ingrese una palabra: ")

#Pedimos el número de caracteres
n = int(input("Cantidad de caracteres: "))

#Extraemos los últimos n caracteres
palabra = palabra[-n:]

#Imprimimos el resultado
print(f"Los últimos {n} caracteres son: {palabra}")
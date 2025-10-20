# Declarar variable de suma
suma = 0
entrada = ""

while entrada != "fin":
    entrada = input("Ingrese un número entero positivo: ")

    if entrada.isdigit() and int(entrada) > 0:
        suma += int(entrada)

print(f"La suma resultante es: {suma}")

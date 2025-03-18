print("Mi Calculadora")

#Pedimos los números
try:
    n1 = float(input("Ingresa un primer número: "))
    n2 = float(input("Ingresa un segundo número: "))
except:
    print("Solo puede usar números flotantes")
    exit()

#Hacemos las operaciones
suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2

try:
    division = n1 / n2
except:
    print("No se puede dividir entre 0")
    print("Cambie el segundo número")
    exit()

#Imprimimos los resultados
print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicación es: {multiplicacion}")
print(f"La división es: {division}")
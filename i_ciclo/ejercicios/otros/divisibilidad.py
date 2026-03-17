#Pedimos los números
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

#Verificar si b es cero
if b == 0:
    print("Error: No se puede dividir por cero")
else:
    #Verificar divisibilidad
    if a % b == 0:
        print(f"{a} es divisible por {b}")
    else:
        print(f"{a} no es divisible por {b}")
#Pedimos las notas
try:
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))
    
    #Calculamos el promedio
    promedio = (nota1 + nota2 + nota3) / 3

    #Imprimimos el promedio
    print(f"El promedio es: {promedio}")
except:
    print("Error solo pueden ser números")

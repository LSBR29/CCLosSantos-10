#Imprimir las opciones
print("Bienvenido al Conversor de Monedas")
print("1. Colones a Dólares")
print("2. Colones a Euros")
print("3. Dólares a Colones")
print("4. Euros a Colones")

#Solicitar y validar la opción
try:
    #Si la conversión a int produce un error el try-except detiene el programa
    opcion = int(input("\nSeleccione una opción: "))

    #Si la opción no existe imprime error y se detiene el programa
    if opcion < 0 or opcion > 4:
        print("Error: esa opción no existe")
    else:
        #Solicitar y validar la cantidad a convertir
        try:
            #Si la conversión a float produce un error el try-except detiene el programa
            cantidad = float(input("Ingrese la cantidad a convertir: "))

            #Si la cantidad es negativa imprime error y se detiene el programa
            if cantidad < 0:
                print("Error: debe ingresar una cantidad positiva")
            else:
                #Realizar la conversión según la opción
                if opcion == 1:
                    resultado = cantidad / 490
                    print(f"\n{cantidad} colones equivalen a {resultado:.2f} dólares.")
                elif opcion == 2:
                    resultado = cantidad / 550
                    print(f"\n{cantidad} colones equivalen a {resultado:.2f} euros.")
                elif opcion == 3:
                    resultado = cantidad * 490
                    print(f"\n{cantidad} dólares equivalen a {resultado:.2f} colones.")
                elif opcion == 4:
                    resultado = cantidad * 550
                    print(f"\n{cantidad} euros equivalen a {resultado:.2f} colones.")
        
        except: #Para la cantidad
            print("Error: debe ingresar un número")

except: #Para la opción
    print("Error: debe ingresar un número de opción válido.")
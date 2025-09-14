"""
1. b
2. c
3. c
4. a
5. d
6. b
7. d
8. a
9. c
10. c
11. a
12. b
13. b
14. d
15. c
"""

import operaciones
import historial_utils

if __name__ == "__main__":
    ruta = "historial.txt"
    ejecutando = True
    ans = 0

    print("BIENVENIDO A LA CALCULADORA INTELIGENTE")
    while ejecutando:
        print("1 - Nueva operación")
        print("2 - Ver historial")
        print("3 - Limpiar historial")
        print("4 - Salir")

        opcion = int(input("Seleccione una opción > "))

        if opcion == 1:
            a = input("\nPrimer número: ")
            b = input("Segundo número: ")
            
            operacion = input("Operación a realizar: ")

            if a == "ANS":
                a = ans
            else:
                a = float(a)
            
            if b == "ANS":
                b = ans
            else:
                b = float(b)

            if operacion == "suma":
                resultado = operaciones.suma(a, b)
                historial_utils.agregar_historial(ruta,f"{a} + {b} = {resultado}")
            elif operacion == "resta":
                resultado = operaciones.resta(a, b)
                historial_utils.agregar_historial(ruta,f"{a} - {b} = {resultado}")
            elif operacion == "multiplicacion":
                resultado = operaciones.multiplicacion(a, b)
                historial_utils.agregar_historial(ruta,f"{a} * {b} = {resultado}")
            elif operacion == "division":
                resultado = operaciones.division(a, b)
                historial_utils.agregar_historial(ruta,f"{a} / {b} = {resultado}")
            
            print(f"El resultado es: {resultado}\n")

        elif opcion == 2:
            historial = historial_utils.leer_historial(ruta)
            if historial:
                for operacion in historial:
                    print(operacion)
            else:
                print("El historial está vacío\n")

        elif opcion == 3: #Extra: Limpiar historial
            historial_utils.limpiar_historial(ruta)
            print("Historial limpiado correctamente\n")

        elif opcion == 4:
            ejecutando = False
    
        else:
            print("Error: Opción inválida\n")
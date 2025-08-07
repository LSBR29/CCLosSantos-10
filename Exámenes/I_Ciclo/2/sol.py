def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

if __name__ == "__main__":
    ejecutando = True
    historial = dict()

    print("BIENVENIDO A LA CALCULADORA INTELIGENTE")
    while ejecutando:
        print("1 - Nueva operación")
        print("2 - Ver historial")
        print("3 - Limpiar historial")
        print("4 - Salir")

        try: #Extra: Validación de opción existente
            opcion = int(input("Seleccione una opción > "))
        except:
            print("Error: Opción inválida\n")
            continue

        if opcion == 1:
            a = input("\nPrimer número: ")
            b = input("Segundo número: ")

            if a == "ANS":
                if historial:
                    a = list(historial.values())[-1]
                else:
                    print("No hay historial, se utilizará 0")
                    a = 0
            else:
                try: #Extra: Validación de número
                    a = float(a)
                except:
                    print("Error: Número inválido\n")
                    continue
            
            if b == "ANS":
                if historial:
                    b = list(historial.values())[-1]
                else:
                    print("No hay historial, se utilizará 0")
                    b = 0
            else:
                try: #Extra: Validación de número
                    b = float(b)
                except:
                    print("Error: Número inválido\n")
                    continue
            
            operacion = input("Operación a realizar: ")

            if operacion == "suma":
                resultado = suma(a, b)
                historial.update({f'{a} + {b}' : resultado})
            elif operacion == "resta":
                resultado = resta(a, b)
                historial.update({f'{a} - {b}' : resultado})
            elif operacion == "multiplicacion":
                resultado = multiplicacion(a, b)
                historial.update({f'{a} * {b}' : resultado})
            elif operacion == "division":
                if b == 0:
                    print("Error, no se puede dividir entre 0\n")
                    continue
                else:
                    resultado = division(a, b)
                    historial.update({f'{a} / {b}' : resultado})
            
            print(f"El resultado es: {resultado}\n")
        
        elif opcion == 2:
            if historial:
                for operacion, resultado in historial.items():
                    print(f"{operacion} = {resultado}")     
            print("\n")

        elif opcion == 3: #Extra: Limpiar historial
            historial.clear()
            print("Historial borrado\n")

        elif opcion == 4:
            ejecutando = False
    
        else: #Extra: Validación de opción existente
            print("Error: Opción inválida\n")
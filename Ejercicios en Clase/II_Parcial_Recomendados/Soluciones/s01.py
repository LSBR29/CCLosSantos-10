import random

# Función principal
if __name__ == "__main__":
    # Generar un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    
    intentos = []  # Lista para guardar los intentos del usuario

    ejecutando = True
    while ejecutando == True:
        try:
            # Pedir al usuario que ingrese un número
            intento = int(input("Ingrese un número: "))

            if intento < numero_secreto:
                intentos.append(intento)  # Guardar el intento
                print("El número secreto es mayor\n")
            elif intento > numero_secreto:
                intentos.append(intento)  # Guardar el intento
                print("El número secreto es menor\n")
            elif intento == numero_secreto:
                intentos.append(intento)  # Guardar el intento
                print("Número correcto")
                ejecutando = False  # Salir del ciclo si adivina correctamente

        except ValueError:
            print("Por favor, ingrese un número válido.\n")

    # Mostrar los intentos ordenados
    intentos_ordenados = sorted(intentos)
    print("Tus intentos fueron: ", intentos_ordenados)
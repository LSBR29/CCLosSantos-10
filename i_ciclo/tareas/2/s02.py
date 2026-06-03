import random

numero_secreto = random.randint(1, 100)     # Genera un número entero aleatorio entre 1 y 100
intentos = []   # Lista donde se almacenarán todos los intentos válidos del usuario

ejecutando = True   # Variable de control para mantener el juego en ejecución
while ejecutando == True:
    try:
        intento = int(input("Ingrese un número: "))     # Solicita al usuario un número entero
    except ValueError:      # Maneja el error si el usuario ingresa un valor no numérico
        print("Por favor, ingrese un número válido.\n")
        continue

    # Verifica si el número ingresado es menor al número secreto
    if intento < numero_secreto:
        intentos.append(intento)    # Guarda el intento en la lista
        print("El número secreto es mayor")

    # Verifica si el número ingresado es mayor al número secreto
    elif intento > numero_secreto:
        intentos.append(intento)    # Guarda el intento en la lista
        print("El número secreto es menor")

    # Se ejecuta cuando el usuario adivina el número secreto
    elif intento == numero_secreto:
        intentos.append(intento)    # Guarda el intento en la lista
        print("Número correcto")
        ejecutando = False      # Finaliza el ciclo del juego

# Muestra todos los intentos realizados
print(f"Tus intentos fueron: {intentos}")
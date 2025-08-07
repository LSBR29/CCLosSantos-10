from random import randint

# Obtener un número aleatorio
numero_aleatorio = randint(1, 50)

# Definir variable de intentos
intentos = 5

# Repetir mientras los intentos sean mayor que 0
while intentos > 0:
    # Ingreso del número
    guess = int(input("Ingrese el número: "))
    
    # Verificar si es mayor, menor o igual que el número aleatorio generado
    if guess < numero_aleatorio:
        print("El número es mayor.")
    elif guess > numero_aleatorio:
        print("El número es menor.")
    else:
        print("Adivinó el número.")
        break # Salir del loop si se adivinó el número

    intentos -= 1 # Disminuir intentos

if intentos == 0:
    print(f"El número era: {numero_aleatorio}")


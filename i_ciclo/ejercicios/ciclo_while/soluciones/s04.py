# Definición de los datos a validar
usuario = "admin"
contra = "1234"

# Definición de la cantidad de intentos
intentos = 3

# Repetir hasta que no tenga intentos
while intentos != 0:
    # Pedir un usuario y contraseña
    usuario_ingresado = input("Ingrese el usuario: ")
    contra_ingresada = input("Ingrese la contraseña: ")

    # Revisar si los datos ingresados son los esperados
    if usuario_ingresado == usuario and contra_ingresada == contra:
        # Imprime que se inició correctamente
        print("Inicio de sesión correcto")
        # Se detiene el ciclo anticipadamente ya que aún pueden quedar intentos pero los datos ya son correctos
        break
    else:
        # Imprime que los datos son incorrectos
        print("El usuario o la contraseña son incorrectos")
        # Resta un intento
        intentos -= 1
else:
    print("Demasiados intentos fallidos.")
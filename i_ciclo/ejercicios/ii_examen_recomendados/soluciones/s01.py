# Función para pedir la contraseña a un usuario específico
def pedir_password(usuario):
    # Retorna la contraseña ingresada.
    contra = input(f"Ingrese la contraseña para '{usuario}': ")
    return contra

# Función para verificar si la contraseña ingresada es correcta
def verificar_password(password_usuario, password_correcto):
    # Retorna True si coinciden, False en caso contrario.
    return password_usuario == password_correcto

# Función para calcular el porcentaje de accesos correctos
def calcular_porcentaje(correctos, total):
    # Calcula el porcentaje de accesos correctos
    if total == 0:
        porcentaje = 0
    else:
        porcentaje = (correctos / total) * 100

    return porcentaje

# Bloque principal del programa
if __name__ == "__main__":
    # Diccionario con los usuarios y sus contraseñas
    usuarios = {
        "ana": "python123",
        "carlos": "hola456",
        "maria": "clave789",
        "luis": "abc123"
    }

    # Inicializar contadores
    accesos_correctos = 0
    accesos_incorrectos = 0

    # Recorrer todos los usuarios del diccionario
    for usuario, pass_correcto in usuarios.items():
        # Solicitar la contraseña al usuario
        pass_ingresada = pedir_password(usuario)

        # Verificar si la contraseña es correcta
        if verificar_password(pass_ingresada, pass_correcto):
            print(f"Acceso exitoso para '{usuario}'.")
            accesos_correctos += 1
        else:
            print(f"Acceso fallido para '{usuario}'. Contraseña incorrecta.")
            accesos_incorrectos += 1

    # Mostrar resumen de resultados
    total_intentos = accesos_correctos + accesos_incorrectos
    print("\nRESUMEN")
    print(f"Accesos correctos: {accesos_correctos}")
    print(f"Accesos incorrectos: {accesos_incorrectos}")

    # Calcular y mostrar el porcentaje
    porcentaje = calcular_porcentaje(accesos_correctos, total_intentos)
    print(f"Porcentaje de accesos correctos: {porcentaje}%")
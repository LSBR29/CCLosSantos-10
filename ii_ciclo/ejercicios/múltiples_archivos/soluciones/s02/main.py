import passwords

if __name__ == "__main__":
    try:
        longitud = int(input("Ingresa la longitud de la contraseña: "))

        if longitud < 4:
            print("Error: La longitud mínima es 4 caracteres.")
            raise ValueError

        password = passwords.generar_password(longitud)
        print(f"Contraseña generada: {password}")

    except:
        print("Por favor, ingresa un número entero válido.")
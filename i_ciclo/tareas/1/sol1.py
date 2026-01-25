#Definir una variable de control, si ocurre un error su valor se cambia a False
registrado = True

#Solicitar y validar el nombre completo
nombre = input("Ingrese su nombre completo: ")
nombre_sin_espacios = nombre.replace(" ", "")
if nombre_sin_espacios.isalpha() == False:
    print("Error: El nombre solo debe contener letras y espacios")
    registrado = False

#Solicitar y validar la edad
edad = input("Ingrese su edad: ")
if edad.isdigit() == False:
    print("Error: La edad debe ser un número entero positivo")
    registrado = False

"""Otra manera
try:
    edad = int(input("Ingrese su edad: "))
    if edad < 0:
        print("Error: La edad debe ser un número entero positivo")
        registrado = False
except:
    print("Error: La edad debe ser un número entero positivo")
    registrado = False
"""

#Solicitar y validar el correo electrónico
correo = input("Ingrese su correo electrónico: ")
if "@" not in correo:
    print("Error: El correo debe contener '@'")
    registrado = False

#Solicitar y validar el número de teléfono
telefono = input("Ingrese su número de teléfono: ")
if telefono.isdigit() == False or len(telefono) < 8:
    print("Error: El número de teléfono debe contener al menos 8 dígitos")
    registrado = False

#Solicitar y validar el país de residencia
pais = input("Ingrese su país de residencia: ")
if pais == "":
    print("Error: El país de residencia no puede estar vacío")
    registrado = False

#Si la variable de control es True se imprime el resumen, si no, se imprime error
if registrado:
    print("\nRegistro exitoso. Información ingresada:")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Correo: {correo}")
    print(f"Teléfono: {telefono}")
    print(f"País: {pais}")
else:
    print("No se pudo realizar el registro del usuario")
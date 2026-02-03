# Solicitar la cantidad de personas
cantidad = int(input("Cantidad de personas: "))

# Solicitar los nombres de las personas (claves del diccionario)
diccionario = dict()

for i in range(1, cantidad + 1):
    # Ingreso del nombre
    nombre = input(f"Ingrese el nombre de la persona {i}: ")

    # Ingresar nombre al diccionario como clave y un set vacío como valor
    diccionario.update({ nombre : set() })

# Solicitar los libros que ha leído cada persona
for persona, libros in diccionario.items():

    print(f"\n--- Libros para {persona} ---")

    # Pedir libros hasta que se ingrese solo ENTER
    libro = input("Ingrese un libro o presione enter para continuar: ")
    while libro != "":
        libros.add(libro)
        
        libro = input("Ingrese un libro o presione enter para continuar: ")

# Imprimir los libros que ha leído cada persona
for persona, libros in diccionario.items():
    exclusivos = libros

    # Restar al set de libros de una persona los otros sets, para encontrar los exclusivos
    for persona2, libros2 in diccionario.items():
        if persona2 == persona:
            continue

        exclusivos = exclusivos.difference(libros2)

    # Imprimir libros de una persona
    print(f"\n--- Libros para {persona} ---")
    print(libros)

    # Imprimir exclusivos de una persona si hay
    print(f"\n--- Exclusivos para {persona} ---")
    if exclusivos:
        print(exclusivos)
    else:
        print(f"No tiene exclusivos")

# Obtener un set con todos los libros, esto evita los repetidos
leidos = set()
for libros in diccionario.values():
    leidos.update(libros)

print(f"\n--- Libros leídos ---")
print(leidos)
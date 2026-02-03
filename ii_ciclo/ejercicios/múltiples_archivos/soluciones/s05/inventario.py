import os

def cargar_inventario(ruta):
    inventario = dict()

    if not os.path.exists(ruta):
        print("El archivo no existe")
        return {}

    with open(ruta, 'r') as f:
        contenido = f.readlines()

        for linea in contenido:
            linea = linea.strip()

            if not linea:
                continue

            producto, precio = linea.split(",")
            try:
                precio = float(precio)
                inventario.update({producto:precio})

            except:
                continue

    return inventario

def calcular_total(carrito, inventario):
    total = 0
    for producto in carrito:
        agregar = inventario[producto]
        total += agregar

    return total
import os

def leer_ventas(ruta):
    productos = dict()

    if not os.path.exists(ruta):
        print("El archivo no existe")
        return productos

    with open(ruta, 'r') as f:
        for linea in f.readlines():
            linea = linea.strip()
            if not linea:
                continue

            producto, cantidad, precio = linea.split(",")
            try:
                cantidad = int(cantidad)
                precio = float(precio)

                total_producto = cantidad*precio
                productos.update({producto:total_producto})
            except:
                continue

    return productos

def calcular_total(productos):
    total = 0

    for total_producto in productos.values():
        total += total_producto
    
    return total

if __name__ == "__main__":
    archivo_entrada = "Ejemplos/ventas.txt"
    archivo_salida = "Ejemplos/resumen.txt"

    productos = leer_ventas(archivo_entrada)

    if not productos:
        print("No se encontraron productos válidos")
    else:
        total = calcular_total(productos)

        print("Listado de productos:")
        
        with open(archivo_salida, "w") as f:
            for producto, total_producto in productos.items():
                print(f"{producto}: ₡{total_producto:.2f}")
                f.write(f"{producto}: {total_producto:.2f}\n")

            print(f"\nTotal: ₡{total}")
            f.write(f"\nTotal: {total}\n")
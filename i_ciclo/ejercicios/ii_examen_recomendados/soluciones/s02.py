# Función para pedir la cantidad que desea comprar de un producto
def pedir_cantidad(producto):
    # Retorna la cantidad ingresada (como entero).
    cantidad = int(input(f"¿Cuántas unidades de {producto} desea comprar? "))
    return cantidad

# Función para verificar si hay suficiente inventario
def hay_inventario(disponible, cantidad):
    # Retorna True si hay suficiente (disponible >= cantidad), False en caso contrario.
    return disponible >= cantidad

# Función para actualizar el inventario restando la cantidad comprada
def actualizar_inventario(inventario, producto, cantidad):
    # No retorna nada, modifica el diccionario directamente.
    inventario[producto] -= cantidad

# Bloque principal del programa
if __name__ == "__main__":
    # Diccionario con productos y cantidades disponibles
    inventario = {
        "Teclado": 5,
        "Mouse": 8,
        "Monitor": 3,
        "Audifonos": 6
    }

    # Inicializar contador de productos vendidos
    total_vendidos = 0

    # Mostrar inventario inicial
    print("Inventario inicial")
    for prod, cant in inventario.items():
        print(f"{prod}: {cant} unidades")

    # Recorrer todos los productos del inventario
    for producto, stock in inventario.items():
        # Mostrar información del producto actual
        print(f"\nProducto: {producto} (Disponible: {stock})")

        # Pedir cantidad que desea comprar
        cantidad_deseada = pedir_cantidad(producto)

        # Verificar si hay suficiente inventario
        if hay_inventario(stock, cantidad_deseada):
            # Actualizar el inventario
            actualizar_inventario(inventario, producto, cantidad_deseada)
            total_vendidos += cantidad_deseada
            print(f"Compra exitosa. Se vendieron {cantidad_deseada} unidades de '{producto}'.")
        else:
            print(f"Inventario insuficiente. Solo hay {stock} unidades disponibles.")

    # Mostrar inventario final y resumen
    print("\nInventario final")
    for prod, cant in inventario.items():
        print(f"{prod}: {cant} unidades")

    print(f"\nTotal de productos vendidos: {total_vendidos} unidades")
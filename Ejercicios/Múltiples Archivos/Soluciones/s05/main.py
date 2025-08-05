import inventario

if __name__ == "__main__":
    ruta = "inventario.txt"
    inv = inventario.cargar_inventario(ruta)

    if not inv:
        print("Inventario vacío.")
        exit()

    print("- Inventario disponible -")
    for nombre, precio in inv.items():
        print(f"- {nombre}: ₡{precio}")

    carrito = []

    while True:
        print("---------------------------")
        entrada = input("Nombre del producto: ")

        if entrada.lower() == "pagar":
            total = inventario.calcular_total(carrito, inv)
            print(f"Total a pagar: ₡{total}")
            break

        if entrada in inv.keys():
            carrito.append(entrada)
            print(f"Agregado: {entrada} (₡{inv[entrada]})")
        else:
            print(f"El producto '{entrada}' no existe en el inventario.")
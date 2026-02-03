# Crear el diccionario del inventario, que será un diccionario anidado
inventario = dict()

# Solicitar la cantidad de productos
cantidad_productos = int(input("Cantidad de productos: "))

# Registrar cada producto en el inventario
for i in range(1, cantidad_productos + 1):
    nombre_producto = input(f"\nIngrese el nombre del producto {i}: ")
    
    # Crear un diccionario vacío para los almacenes de este producto
    almacenes = dict()

    print("\n--- Almacenes para el producto ---")
    # Pedir almacenes y stock para el producto hasta que se presione ENTER
    nombre_almacen = input("Ingrese el nombre del almacén o presione enter para continuar: ")
    while nombre_almacen != "":
        try:
            stock = int(input(f"Cantidad en {nombre_almacen}: "))
        except:
            stock = 0

        # Agregar almacén y stock al diccionario
        almacenes.update({ nombre_almacen : stock })

        nombre_almacen = input("Ingrese el nombre del siguiente almacén o presione enter para continuar: ")

    # Agregar almacenes de un producto al inventario
    inventario.update({ nombre_producto : almacenes })

# Consultar el stock total por producto
print("\n--- Stock total por producto ---")
for producto, almacenes in inventario.items():
    stock_total = sum(almacenes.values())
    print(f"{producto}: {stock_total} unidades")

# Consultar los almacenes donde un producto está agotado
print("\n--- Almacenes donde hay productos agotados ---")
for producto, almacenes in inventario.items():
    agotados = []

    for nombre, cantidad in almacenes.items():
        if cantidad == 0:
            agotados.append(nombre)
    
    print(f"\n{producto}:")
    if agotados:
        print(f"Agotado en: {agotados}")
    else:
        print("Disponible en todos los almacenes")

# Mostrar los productos agotados en todos los almacenes
print("\n--- Productos agotados en todos los almacenes ---")
agotados_total = []

for producto, almacenes in inventario.items():
    # Si todos los valores de stock son cero
    if max(almacenes.values()) == 0:
        agotados_total.append(producto)

if agotados_total:
    print(agotados_total)
else:
    print("Ningún producto está completamente agotado.")
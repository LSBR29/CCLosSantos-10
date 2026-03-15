# Solicitud de datos tipo string
nombre_cliente = input("Ingrese el nombre del cliente: ")
nombre_producto = input("Ingrese el nombre del producto: ")

try:
    # Solicitud y conversión de datos numéricos
    precio_unitario = float(input("Ingrese el precio unitario: "))
    cantidad = int(input("Ingrese la cantidad: "))
    porcentaje_iva = int(input("Ingrese el porcentaje de IVA: "))
    porcentaje_descuento = int(input("Ingrese el porcentaje de descuento: "))
except:
    print("Error: Debe ingresar valores numéricos válidos para precio, cantidad, IVA y descuento.")
    exit()

# Cálculos
subtotal = precio_unitario * cantidad
iva = subtotal * (porcentaje_iva / 100)
descuento = subtotal * (porcentaje_descuento / 100)
total = subtotal + iva - descuento

# Impresión de resultados
print("FACTURA")
print(f"Cliente: {nombre_cliente.upper()}")
print(f"Producto: {nombre_producto.lower()}")
print(f"Subtotal: {subtotal}")
print(f"IVA: {iva}")
print(f"Descuento: {descuento}")
print(f"Total a pagar: {total}")
# Producto 1
print("Producto 1")
nombre1 = input("Nombre: ")
try:
    precio1 = float(input("Precio: "))
except ValueError:
    print("Error: precio no válido, se asigna 0.0.")
    precio1 = 0.0

# Producto 2
print("\nProducto 2")
nombre2 = input("Nombre: ")
try:
    precio2 = float(input("Precio: "))
except ValueError:
    print("Error: precio no válido, se asigna 0.0.")
    precio2 = 0.0

# Producto 3
print("\nProducto 3")
nombre3 = input("Nombre: ")
try:
    precio3 = float(input("Precio: "))
except ValueError:
    print("Error: precio no válido, se asigna 0.0.")
    precio3 = 0.0

# Listas vacías para almacenar nombres y precios
nombres = []
precios = []

# Agregar a las listas
nombres.append(nombre1)
precios.append(precio1)

nombres.append(nombre2)
precios.append(precio2)

nombres.append(nombre3)
precios.append(precio3)

# Resultados
print("\nResultados")
print("Nombres:", nombres)
print("Precios:", precios)

# Precio total usando sum()
total = sum(precios)
print(f"Precio total: {total}")

# Producto más caro usando max() e index()
precio_max = max(precios)
posicion = precios.index(precio_max)   # Índice del precio más alto
producto_caro = nombres[posicion]
print(f"Producto más caro: {producto_caro}")

""" Otras maneras
# Ir sumando cada precio para obtener el total
total = 0
total += precios[0]
total += precios[1]
total += precios[2]

# Comparar cada precio para encontrar la posición del más caro
precioMáximo = 0
posicion = 0
if precios[0] > precioMáximo:       
    precioMáximo = precios[0]       
    posicion = 0

if precios[1] > precioMáximo:
    precioMáximo = precios[1]
    posicion = 1

if precios[2] > precioMáximo:
    precioMáximo = precios[2]
    posicion = 2

# Cuando tengo la posición del más caro, puedo tener su nombre    
producto_caro = nombres[posicion]
"""
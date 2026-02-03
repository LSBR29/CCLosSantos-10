class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

productos = [
    Producto('Monitor', 150000),
    Producto('Teclado', 90000),
    Producto('Mouse', 50000),
    Producto('Laptop', 800000)
]

# Aplicar descuento
con_descuento = map(lambda p: Producto(p.nombre, p.precio * 0.9), productos)

# Filtrar por precios
caros = filter(lambda p: p.precio > 100000, con_descuento)

# Ordenar de mayor a menor
ordenados = sorted(caros, key=lambda p: p.precio, reverse=True)

# Mostrar resultados
print([f"{p.nombre}: {p.precio:.2f}" for p in ordenados])
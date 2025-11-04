estudiantes = [
    {'nombre': 'Ana', 'nota': 85},
    {'nombre': 'Maria', 'nota': 92},
    {'nombre': 'Luis', 'nota': 78},
    {'nombre': 'Pedro', 'nota': 90}
]

# Filtrar por notas
mayor_80 = filter(lambda est: est['nota'] >= 80, estudiantes)

# Ordenar de mayor a menor
ordenados = sorted(mayor_80, key=lambda est: est['nota'], reverse=True)

# Mostrar resultados
print([est['nombre'].upper() for est in ordenados])
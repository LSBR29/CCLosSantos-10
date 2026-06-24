# Función para calcular el promedio de una lista de notas
def calcular_promedio(notas):
    # Recibe una lista de notas (números) y retorna su promedio.
    if len(notas) == 0:
        promedio = 0
    else:
        promedio = sum(notas) / len(notas)

    return promedio

# Función para determinar si un promedio aprueba (nota >= 70)
def aprobo(promedio):
    # Retorna True si el promedio es mayor o igual a 70, False en caso contrario.
    return promedio >= 70

# Bloque principal del programa
if __name__ == "__main__":
    # Diccionario con estudiantes y sus listas de notas
    estudiantes = {
        "Ana": [90, 85, 88],
        "Carlos": [70, 65, 60],
        "Maria": [100, 95, 98],
        "Luis": [80, 75, 82]
    }

    # Inicializar contadores
    aprobados = 0
    reprobados = 0

    # Recorrer todos los estudiantes
    for estudiante, notas in estudiantes.items():
        # Calcular el promedio del estudiante
        promedio = calcular_promedio(notas)

        # Mostrar el resultado
        if aprobo(promedio):
            print(f"{estudiante} aprueba con un promedio de {promedio:.2f}")
            aprobados += 1
        else:
            print(f"{estudiante} reprueba con un promedio de {promedio:.2f}")
            reprobados += 1

    # Mostrar resumen final
    print("\nResumen")
    print(f"Estudiantes aprobados: {aprobados}")
    print(f"Estudiantes reprobados: {reprobados}")
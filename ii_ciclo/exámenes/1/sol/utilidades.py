def contar_ausencias(nombres, estados):
    ausencias_por_estudiante = {}

    for i in range(len(nombres)):
        nombre = nombres[i]

        # Se crea la clave en la primera aparición
        if nombre not in ausencias_por_estudiante:
            ausencias_por_estudiante[nombre] = 0

        if estados[i] == "ausente":
            ausencias_por_estudiante[nombre] += 1

    return ausencias_por_estudiante
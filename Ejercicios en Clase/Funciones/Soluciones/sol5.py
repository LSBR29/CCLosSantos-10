def estudiantes_frecuentes(lista):
    # Diccionario para contar asistencias por estudiante
    contador_asistencias = {}

    # Número total de días registrados
    total_dias = len(lista)

    # Recorremos cada día y su lista de estudiantes
    for dia, estudiantes in lista.items():
        for estudiante in estudiantes:
            if estudiante in contador_asistencias:
                contador_asistencias[estudiante] += 1
            else:
                contador_asistencias[estudiante] = 1

    # Seleccionamos estudiantes que asistieron todos los días
    resultado = []
    for estudiante, dias in contador_asistencias.items():
        if dias == total_dias:
            resultado.append(estudiante)

    # Devolvemos como tupla ordenada
    return tuple(resultado)


# Función principal
if __name__ == "__main__":
    lista = {
        "Lunes": ["Ana", "Luis", "Carlos"],
        "Martes": ["Ana", "Carlos"],
        "Miércoles": ["Ana", "Carlos", "Luis"]
    }

    print("Estudiantes que asistieron todos los días:", estudiantes_frecuentes(lista))
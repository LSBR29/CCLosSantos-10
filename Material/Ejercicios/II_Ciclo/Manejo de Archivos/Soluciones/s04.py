import os

def leer_estudiantes(ruta):
    estudiantes = []

    if not os.path.exists(ruta):
        print("El archivo no existe")
        return estudiantes

    with open(ruta, 'r') as f:
        for linea in f.readlines():
            linea = linea.strip()
            if not linea:
                continue

            nombre, nota = linea.split(",")
            try:
                nota = float(nota)
                estudiantes.append((nombre, nota))

            except:
                continue

    return estudiantes

if __name__ == "__main__":
    archivo_entrada = "Ejemplos/estudiantes.csv"
    archivo_salida = "Ejemplos/estudiantes_ordenado.txt"

    estudiantes = leer_estudiantes(archivo_entrada)

    if not estudiantes:
        print("No se encontraron estudiantes válidos")
        
    else:
        # Ordenar por nota descendente (mayor a menor)
        estudiantes.sort(key=lambda x: x[1], reverse=True)

        print("\nListado de estudiantes ordenados por nota:")
        
        with open(archivo_salida, "w") as f:
            for i in range(len(estudiantes)):
                print(f"{i + 1}. {estudiantes[i][0]} - {estudiantes[i][1]}")
                f.write(f"{i + 1}. {estudiantes[i][0]} - {estudiantes[i][1]}\n")
from datetime import date

def leer_diario(ruta_archivo):
    # Lee y devuelve todas las líneas del diario
    try:
        with open(ruta_archivo, "r") as archivo:
            return archivo.readlines()

    except:
        print("Error al leer el archivo")
        return []

def agregar_entrada(ruta_archivo, texto):
    # Obtiene la fecha actual automáticamente
    fecha = date.today()

    try:
        # 'a' permite agregar la nueva entrada sin borrar las anteriores
        with open(ruta_archivo, "a") as archivo:
            archivo.write(f"{fecha} | {texto}\n")
            return True
    except:
        return False

def buscar_por_palabra(lista_lineas, palabra):
    resultados = []

    # Recorre todas las líneas y busca la palabra dentro del texto
    for linea in lista_lineas:
        partes = linea.split("|", 1)

        if len(partes) == 2:
            texto = partes[1].strip()

            # La búsqueda no distingue entre mayúsculas y minúsculas
            if palabra.lower() in texto.lower():
                resultados.append(linea)

    return resultados


def eliminar_por_fecha(ruta_archivo, lista_lineas, fecha):
    nuevas_lineas = []
    eliminadas = False

    # Separa la fecha del texto para comparar únicamente la fecha
    for linea in lista_lineas:
        partes = linea.split("|", 1)

        if len(partes) == 2:
            fecha_linea = partes[0].strip()

            if fecha_linea == fecha:
                eliminadas = True
            else:
                nuevas_lineas.append(linea)

    # Si no hubo coincidencias, el archivo no se modifica
    if not eliminadas:
        return False

    try:
        # 'w' reemplaza el contenido anterior con las líneas restantes
        with open(ruta_archivo, "w") as archivo:
            archivo.writelines(nuevas_lineas)
            return True
    except:
        return False
def analizar_archivo(ruta):
    try:
        with open(ruta, 'r') as archivo:
            total = 0
            vacias = 0
            comentadas = 0

            for linea in archivo.readlines():
                total += 1
                linea_limpia = linea.strip()

                if linea_limpia == "":
                    vacias += 1
                elif linea_limpia.startswith("#"):
                    comentadas += 1

        return total, vacias, comentadas
    except:
        print(f"Error: El archivo '{ruta}' no existe.")
        return None, None, None

if __name__ == "__main__":
    ruta = "Ejemplos/codigo.py"

    total, vacias, comentadas = analizar_archivo(ruta)

    if total == None:
        exit()

    print(f"Líneas totales: {total}")
    print(f"Líneas vacías: {vacias}")
    print(f"Líneas comentadas: {comentadas}")
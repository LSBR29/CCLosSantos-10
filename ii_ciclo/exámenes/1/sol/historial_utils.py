def leer_historial(ruta):
    with open(ruta, "r") as archivo:
        try:
            return archivo.readlines()
        except:
            return []

def agregar_historial(ruta, entrada):
    with open(ruta, "a") as archivo:
        archivo.write(f"{entrada}\n")

def limpiar_historial(ruta): #PARTE EXTRA
    with open(ruta, "w") as archivo:
        archivo.write("")
from pathlib import Path

def leer(ruta):
    with open(ruta, 'r') as f:
        datos_productos = f.readlines()
        return datos_productos

def agregar(ruta, producto):
    with open(ruta, 'a') as f:
        f.write(producto)
        f.write("\n")

if __name__ == "__main__":
    ruta = "Ejemplos/compras.txt"

    if Path(ruta).exists():
        datos_productos= leer(ruta)

        cantidad = len(datos_productos)
        for i in range(cantidad):
            print(f"{i + 1}. {datos_productos[i].strip()}")
    else:
        print("El archivo no existe")
        print("Creando archivo...")

        f = open(ruta, 'n')
        f.close()

    agregando = True
    while agregando:
        nuevo = input("Ingrese el nombre del nuevo producto: ")

        if nuevo:
            agregar(ruta, nuevo)
        else:
            agregando = False
import diario_utils

def mostrar_menu():
    print("\n--- Diario Personal ---")
    print("1. Agregar nueva entrada")
    print("2. Buscar entradas por palabra")
    print("3. Eliminar entradas por fecha")
    print("4. Salir")

if __name__ == "__main__":
    ruta = "diario.txt"

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            texto = input("Ingrese el texto de la entrada: ")

            if diario_utils.agregar_entrada(ruta, texto):
                print("Entrada agregada correctamente")

        elif opcion == "2":
            palabra = input("Ingrese una palabra o frase: ")
            lineas = diario_utils.leer_diario(ruta)
            resultados = diario_utils.buscar_por_palabra(lineas, palabra)

            if resultados:
                print("\n--- Entradas encontradas ---")

                for linea in resultados:
                    print(linea)
            else:
                print("No se encontraron entradas")

        elif opcion == "3":
            fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
            lineas = diario_utils.leer_diario(ruta)

            if diario_utils.eliminar_por_fecha(ruta, lineas, fecha):
                print("Entradas eliminadas correctamente")
            else:
                print("No existen entradas para esa fecha")

        elif opcion == "4":
            print("Saliendo del programa")
            break

        else:
            print("Opción inválida")
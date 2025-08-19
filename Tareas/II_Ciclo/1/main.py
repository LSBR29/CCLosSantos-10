import log_utils

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Agregar evento nuevo")
    print("2. Ver todos los eventos")
    print("3. Filtrar eventos por tipo")
    print("4. Eliminar eventos por tipo")
    print("5. Salir")

def seleccion_tipo():
    print("\nTipos de Evento")
    print("1. INFO")
    print("2. ERROR")
    print("3. WARNING")
    
    tipo = input("Seleccione un tipo: ")
    if tipo == '1':
        tipo = "INFO"
    elif tipo == '2':
        tipo = "ERROR"
    elif tipo == '3':
        tipo = "WARNING"
    else:
        return

    return tipo


if __name__ == '__main__':
    ruta = 'logs.txt'

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            tipo = seleccion_tipo()

            if tipo:
                mensaje = input("Ingrese el mensaje del evento: ")
                log_utils.agregar_log(ruta, tipo, mensaje)
                print("Evento agregado correctamente")
            else:
                print("Tipo de evento inválido")

        elif opcion == '2':
            logs = log_utils.leer_logs(ruta)

            if logs:
                print("\n--- Todos los eventos ---")
                for linea in logs:
                    print(linea)
            else:
                print("No hay eventos registrados")

        elif opcion == '3':
            tipo = seleccion_tipo()
            
            if tipo:
                logs = log_utils.leer_logs(ruta)
                filtrados = log_utils.filtrar_logs(logs, tipo)

                if filtrados:
                    print(f"\n--- Eventos de tipo {tipo} ---")
                    for linea in filtrados:
                        print(linea)
                else:
                    print(f"No hay eventos del tipo {tipo}")
            else:
                print("Tipo de evento inválido")

        elif opcion == '4':
            tipo = seleccion_tipo()

            if tipo:
                log_utils.eliminar_logs_por_tipo(ruta, tipo)
                print(f"Eventos de tipo {tipo} eliminados")
            else:
                print("Tipo inválido")

        elif opcion == '5':
            print("Saliendo del programa")
            break

        else:
            print("Opción inválida")
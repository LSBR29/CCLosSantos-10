import qqsm

def menu(juego: qqsm.Juego):
    """Función que controla la ejecución de cada ronda del juego."""
    # Selecciona una pregunta según el nivel actual
    pregunta = juego.seleccionar_pregunta(juego.nivel_actual)

    # Muestra la pregunta y los comodines disponibles
    pregunta.mostrar_pregunta()
    juego.mostrar_comodines()

    while True:
        # Entrada del jugador: puede ser una respuesta, comodín o retiro
        accion = input("Seleccione una opción o escriba 'retiro': ").strip().upper()

        # Si no es una respuesta de A–D
        if accion not in ["A", "B", "C", "D"]:
            # Verifica si quiere usar el comodín 50:50
            if accion == "50:50":
                juego.usar_comodin(accion, pregunta)
                continue
            # O el comodín cambio de pregunta
            elif accion == "CAMBIO":
                nueva_pregunta = juego.usar_comodin(accion, pregunta)
                if nueva_pregunta:
                    # Actualiza la pregunta y la vuelve a mostrar
                    pregunta = nueva_pregunta
                    pregunta.mostrar_pregunta()
                    juego.mostrar_comodines()
                continue
            # O retirarse del juego
            elif accion == "RETIRO":
                print(f"Se lleva ₡{juego.calcular_premio(True)}")
                juego.jugando = False
                break
            # Si la acción no es válida
            else:
                print("Opción inválida.")
                continue

        # Si la entrada es una respuesta válida
        else:
            # Verifica la respuesta
            if pregunta.verificar_respuesta(accion):
                print("Correcto\n")
                # Si llega al nivel 15 gana el máximo premio
                if juego.nivel_actual == 15:
                    print(f"Has ganado ₡{juego.calcular_premio(True)}")
                    juego.jugando = False
                else:
                    # Avanza al siguiente nivel
                    juego.nivel_actual += 1
                break
            else:
                # Si la respuesta es incorrecta, calcula el premio de pérdida
                premio = juego.calcular_premio(False)
                print(f"Respuesta incorrecta. Te llevas ₡{premio}")
                juego.jugando = False
                break

if __name__ == "__main__":
    print("BIENVENIDO A ¿QUIÉN QUIERE SER MILLONARIO?")

    # Crea la instancia del juego
    juego = qqsm.Juego()
    ruta = input("Ingrese la ruta del archivo de preguntas: ")

    # Carga las preguntas desde el archivo especificado
    try:
        juego.cargar_preguntas(ruta)
    except:
        print("Error: Fallo al leer el archivo")
        juego.jugando = False

    # Bucle principal de juego, avanza hasta el nivel 15 o hasta que termine
    while juego.jugando:
        menu(juego)

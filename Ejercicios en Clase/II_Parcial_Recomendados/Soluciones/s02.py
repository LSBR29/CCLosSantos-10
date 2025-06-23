# Función principal
if __name__ == "__main__":
    # Lista de candidatos válidos
    candidatos = ["Ana", "Carlos", "Luis"]
    
    # Diccionario para guardar los votos
    votos = dict()

    for candidato in candidatos:
        votos.update({candidato:0})

    ejecutando = True
    while ejecutando == True:
        # Mostrar el menú principal
        print("1. Votar")
        print("2. Ver Resultados")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Mostrar los candidatos y pedir el voto
            print("\n-- Votación --")
            print(f"Candidatos: {candidatos}")
            voto = input("Escoja un candidato: ")

            if voto in candidatos:
                votos[voto] += 1
            else:
                print("El candidato no es válido\n")

        elif opcion == "2":
            # Mostrar los resultados actuales
            print("\n-- Resultados --")
            for candidato, cantidad in votos.items():
                print(f"{candidato}: {cantidad}")
            print()

        elif opcion == "3":
            # Salir del programa
            ejecutando = False
        else:
            print("Opción no válida, intente de nuevo.\n")
import utils

if __name__ == "__main__":
    criaturas = [
        utils.Criatura("Goblins", 75, "agresiva"),
        utils.Criatura("Golem", 80, "perezosa"),
        utils.Criatura("PEKKA", 90, "caotica"),
        utils.Criatura("Minion", 85, "caotica"),
        utils.Criatura("Witch", 85, "perezosa")
    ]

    # Imprimir todas
    print("\nCRIATURAS REGISTRADAS")
    for c in criaturas:
        print(f"{c.nombre} | Base: {c.v_base} | Pers.: {c.personalidad}")

    # Obtener las velocidades reales
    velocidades = list(utils.map_velocidades(criaturas))

    # Imprimir las velocidades reales
    print("\nVELOCIDADES REALES")
    for criatura, vel in zip(criaturas, velocidades):
        print(f"{criatura.nombre}: {vel:.2f}")

    # Calcular e imprimir el promedio
    promedio = sum(velocidades) / len(velocidades)
    print(f"\nPromedio de velocidades: {promedio:.2f}")

    # Ver e imprimir las superiores al promedio
    superiores = list(utils.filtrar_superiores(promedio, criaturas))
    print("\nCRIATURAS SUPERIORES AL PROMEDIO")
    for c in superiores:
        print(f"{c.nombre} (Velocidad actual: {c.velocidad_real():.2f})")

    # Ver el ganador
    ganador = utils.determinar_ganador(criaturas)
    print("\nGANADOR")
    print(f"{ganador.nombre} con velocidad {ganador.velocidad_real():.2f}")

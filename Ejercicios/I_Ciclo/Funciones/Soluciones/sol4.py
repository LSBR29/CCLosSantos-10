def analizar_palabras(*listas):
    # Convertimos cada lista en un conjunto para eliminar duplicados
    sets = [set(lista) for lista in listas]

    # Intersección: palabras en común en todos los conjuntos
    en_todas = sets[0]
    for s in sets[1:]:
        en_todas = en_todas.union(s)

    # Unión: palabras presentes en al menos uno
    en_alguna = sets[0]
    for s in sets[1:]:
        en_alguna = en_alguna.union(s)

    # Diferencia: palabras que solo tiene la primera persona
    solo_primera = sets[0]
    for s in sets[1:]:
        solo_primera = solo_primera.difference(s)

    # Mostramos resultados
    print("Palabras mencionadas por al menos una persona:", en_alguna)
    print("Palabras que les gustan a todos:", en_todas)
    print("Palabras solo de la primera persona:", solo_primera)

# Función principal
if __name__ == "__main__":
    persona1 = ["sol", "luna", "mar", "sol"]
    persona2 = ["luna", "estrella", "sol", "río"]
    persona3 = ["nube", "luna", "sol", "río"]

    analizar_palabras(persona1, persona2, persona3)
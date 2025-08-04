import notas

if __name__ == "__main__":
    lista_notas = []

    print("Ingresa las notas entre 0 y 100. Escribe 'fin' para terminar.")

    while True:
        entrada = input("Nota: ")

        if entrada.lower() == "fin":
            break

        try:
            entrada = float(entrada)
            if 0 <= entrada <= 100:
                notas.agregar_nota(lista_notas, entrada)
            else:
                print("La nota debe estar entre 0 y 100.")
        except:
            print("Entrada no válida.")

    if not lista_notas:
        print("No se ingresaron notas válidas.")
        exit()

    promedio = notas.calcular_promedio(lista_notas)
    mayor, menor = notas.obtener_mayor_menor(lista_notas)

    print(f"\nPromedio de notas: {promedio:.2f}")
    print(f"Nota más alta: {mayor}")
    print(f"Nota más baja: {menor}")
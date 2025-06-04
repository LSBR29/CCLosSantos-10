# Función para calcular el área de un rectángulo
def area_rectangulo(base, altura):
    area = base * altura
    return area

# Función para calcular el área de un triángulo
def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

# Función para calcular el área de un círculo
def area_circulo(radio):
    area = 3.1416 * radio ** 2
    return area

# Función principal
if __name__ == "__main__":
    ejecutando = True

    # Ciclo para ejecutar hasta que no se ingrese una figura
    while ejecutando == True:
        figura = input("Ingrese una figura (rectangulo, triangulo, circulo): ").lower()

        if figura == "rectangulo":
            medidas = input("Ingrese sus medidas (base altura): ").split()
            base = float(medidas[0])
            altura = float(medidas[1])
            area = area_rectangulo(base, altura)
            print(f"Área = {area}")

        elif figura == "triangulo":
            medidas = input("Ingrese sus medidas (base altura): ").split()
            base = float(medidas[0])
            altura = float(medidas[1])
            area = area_triangulo(base, altura)
            print(f"Área = {area}")

        elif figura == "circulo":
            radio = float(input("Ingrese el radio: "))
            area = area_circulo(radio)
            print(f"Área = {area}")

        else:
            print("La figura no existe")
            print("Saliendo...")
            ejecutando = False
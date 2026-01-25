class Restaurante:
    def __init__(self, nombre, tipo_comida):
        self.nombre = nombre
        self.tipo_comida = tipo_comida

    def mostrar_info(self):
        print(f"El restaurante {self.nombre} vende comida {self.tipo_comida}")

if __name__ ==  "__main__":
    r1 = Restaurante("Restaurante 1", "Italiana")
    r2 = Restaurante("Restaurante 2", "Mexicana")

    r1.mostrar_info()
    r2.mostrar_info()
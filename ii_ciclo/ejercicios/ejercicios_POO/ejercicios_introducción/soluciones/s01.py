class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self, comida):
        print(f"{self.nombre} está comiendo {comida}")

if __name__ == "__main__":
    nombre = input("Ingrese un nombre: ")
    m1 = Mascota(nombre)
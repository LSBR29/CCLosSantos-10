# Problema 1.
class Tanque:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.__nivel = 0

    def llenar(self, litros):
        if self.__nivel + litros > self.capacidad:
            self.__nivel = self.capacidad
        else:
            self.__nivel += litros  # Error 1, se asignaba litros en lugar de sumarlos al nivel actual

    def get_nivel(self):
        return self.__nivel

    def porcentaje(self):
        return self.__nivel / self.capacidad * 100  # Error 2, para porcentaje se debe multiplicar por 100

if __name__ == "__main__":
    t = Tanque(200)
    t.llenar(100)
    t.llenar(50)
    print(t.get_nivel())  # Error 3, __nivel es privado y desde afuera solo se puede leer con el método nivel()
    print(f"{t.porcentaje()}%")
    t.llenar(100)
    print(t.get_nivel())


# Problema 2.
class Vehiculo:
    def __init__(self, placa, kilometraje):
        self.placa = placa
        self.kilometraje = kilometraje

    def recorrer(self, km):
        self.kilometraje += km

    def __str__(self):
        return f"{self.placa} | {self.kilometraje} km"

class Camion(Vehiculo):
    def __init__(self, placa, kilometraje, carga_max):
        super().__init__(placa, kilometraje)  # Error 1, faltaba llamar al __init__ del padre para guardar placa y kilometraje
        self.carga_max = carga_max
        self.viajes = 0

    def recorrer(self, km):
        super().recorrer(km)  # Error 2, super necesita paréntesis para poder usar los métodos del padre
        self.viajes += 1

    def __str__(self):
        return super().__str__() + f" | Carga máxima {self.carga_max} kg | Viajes {self.viajes}"

if __name__ == "__main__":
    camion = Camion("CRC-123", 5000, 8000)  # Error 3, faltaba el argumento carga_max que pide el __init__
    print(camion)
    camion.recorrer(70)
    camion.recorrer(50)
    print(camion)
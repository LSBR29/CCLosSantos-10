# Problema 1.
class Tanque:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.__nivel = 0

    def llenar(self, litros):
        if self.__nivel + litros > self.capacidad:
            self.__nivel = self.capacidad
        else:
            self.__nivel = litros

    def get_nivel(self):
        return self.__nivel

    def porcentaje(self):
        return self.__nivel / self.capacidad * 10

if __name__ == "__main__":
    t = Tanque(200)
    t.llenar(100)
    t.llenar(50)
    print(t.__nivel)
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
        self.carga_max = carga_max
        self.viajes = 0

    def recorrer(self, km):
        super.recorrer(km)
        self.viajes += 1

    def __str__(self):
        return super().__str__() + f" | Carga máxima {self.carga_max} kg | Viajes {self.viajes}"

if __name__ == "__main__":
    camion = Camion("CRC-123", 5000)
    print(camion)
    camion.recorrer(70)
    camion.recorrer(50)
    print(camion)
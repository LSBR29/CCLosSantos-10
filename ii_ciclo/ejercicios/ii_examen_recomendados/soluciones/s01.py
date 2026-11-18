class Planta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.altura = 10
        self.dias_sin_agua = 0

    def regar(self):
        self.dias_sin_agua = 0
        self.altura += 2

    def pasar_dia(self):
        self.dias_sin_agua += 1

    def necesita_agua(self):
        return self.dias_sin_agua >= 3

    def necesita_poda(self):
        return self.altura > 20

    def mostrar_info(self):
        return f"{self.nombre} | Altura {self.altura} cm | Días sin agua {self.dias_sin_agua}"

if __name__ == "__main__":
    albahaca = Planta("Albahaca")
    menta = Planta("Menta")

    for _ in range(6):
        albahaca.regar()
    for _ in range(3):
        menta.pasar_dia()

    print(albahaca.mostrar_info())
    print(menta.mostrar_info())
    print(albahaca.necesita_poda())
    print(menta.necesita_poda())
    print(albahaca.necesita_agua())
    print(menta.necesita_agua())

    menta.regar()
    print(menta.mostrar_info())
    print(menta.necesita_agua())
class Envio:
    def __init__(self, destino, peso):
        self.destino = destino
        self.peso = peso

    def calcular_costo(self):
        return self.peso * 500

    def __str__(self):
        return f"Envío a {self.destino} | {self.peso} kg | Costo ₡{self.calcular_costo()}"

class EnvioExpress(Envio):
    def calcular_costo(self):
        return super().calcular_costo() + 2000

class EnvioInternacional(Envio):
    def __init__(self, destino, peso, pais):
        super().__init__(destino, peso)
        self.pais = pais

    def calcular_costo(self):
        return super().calcular_costo() * 2

    def __str__(self):
        return super().__str__() + f" | País {self.pais}"

if __name__ == "__main__":
    envios = [
        Envio("Cartago", 2),
        EnvioExpress("Heredia", 3),
        EnvioInternacional("Madrid", 4, "España"),
    ]

    total = 0
    for envio in envios:
        print(envio)
        total += envio.calcular_costo()

    print(f"Total ₡{total}")

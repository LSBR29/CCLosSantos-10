class Suscripcion():
    def __init__(self, nombre:str, premium:bool=False):
        self.nombre = nombre
        self.premium = premium

        self.__duracion = 0

    @property
    def duracion(self):
        return self.__duracion
        
    @duracion.setter
    def duracion(self, valor:int):
        if valor >= 0:
            self.__duracion = valor
        else:
            raise ValueError
        
    def calcular_total(self):
        total = self.duracion * 1000

        if self.premium:
            total += total * 0.1
        
        return total
    
    def __str__(self):
        return f"Suscripción: {self.nombre} - Duración: {self.duracion} meses - Total: {self.calcular_total()} (Premium: {self.premium})"
    
class GestorSuscripciones():
    def __init__(self):
        self.suscripciones = []

    def agregar_suscripcion(self, suscrip:Suscripcion):
        self.suscripciones.append(suscrip)

    def mostrar_todas(self):
        for s in self.suscripciones:
            print(s)

    def filtrar_premium(self):
        filtradas = filter(lambda s: s.premium, self.suscripciones)

        return list(filtradas)

if __name__ == "__main__":
    s1 = Suscripcion("Básica", False)
    s1.duracion = 3

    s2 = Suscripcion("Premium Plus", True)
    s2.duracion = 6
    
    s3 = Suscripcion("Premium Music", True)
    s3.duracion = 12

    gestor = GestorSuscripciones() 
    gestor.agregar_suscripcion(s1)
    gestor.agregar_suscripcion(s2)
    gestor.agregar_suscripcion(s3)

    gestor.mostrar_todas()

    print("\nSuscripciones Premium registradas:")
    for s in gestor.filtrar_premium():
        print(s.nombre)
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        return f"Nombre: {self.nombre}"

class Arquero(Personaje):
    def __init__(self, nombre, flechas = 10):
        # El nombre lo inicializa la clase padre
        super().__init__(nombre)
        self.flechas = flechas

    def mostrar_info(self):
        # Se extiende lo que ya devuelve Personaje
        return super().mostrar_info() + f", Flechas: {self.flechas}"


class ArmaduraMixin:
    def reducir_dano(self, dano, armadura):
        # Si el golpe no supera la armadura, no se recibe daño
        if dano > armadura:
            return dano - armadura
        return 0

class Guerrero(Personaje, ArmaduraMixin):
    def __init__(self, nombre, vida_maxima = 100, armadura = 5):
        # El nombre lo inicializa la clase padre
        super().__init__(nombre)
        self.vida_maxima = vida_maxima
        self.armadura = armadura

        # La vida empieza igual a la vida máxima
        self.__vida = vida_maxima

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, valor):
        # Solo se acepta una vida posible: ni negativa ni mayor que la máxima
        if valor >= 0 and valor <= self.vida_maxima:
            self.__vida = valor

    def mostrar_info(self):
        return super().mostrar_info() + f", Vida: {self.__vida}/{self.vida_maxima}, Armadura: {self.armadura}"

if __name__ == "__main__":
    # Arquero
    a1 = Arquero("Alex", 8)
    print(f"Datos del arquero: {a1.mostrar_info()}\n")

    # Guerrero: getter y setter de la vida
    g1 = Guerrero("Steve", 100, 8)
    print(f"Vida del guerrero {g1.nombre}: {g1.vida}")
    g1.vida = 60
    print(f"Vida del guerrero {g1.nombre} modificada a: {g1.vida}\n")

    # Mixin: daño de un golpe con armadura
    print(f"Daño del golpe con armadura de {g1.armadura}: {g1.reducir_dano(30, g1.armadura)}")
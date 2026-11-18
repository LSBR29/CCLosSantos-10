class Robot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__bateria = 100

    @property
    def bateria(self):
        return self.__bateria

    def mover(self):
        if self.__bateria < 10:
            return f"{self.nombre} no tiene batería"
        self.__bateria -= 10
        return f"{self.nombre} se movió"

class VoladorMixin:
    def volar(self):
        return f"{self.nombre} está volando"

class NadadorMixin:
    def nadar(self):
        return f"{self.nombre} está nadando"

class RobotVolador(Robot, VoladorMixin):
    pass

class RobotAnfibio(Robot, VoladorMixin, NadadorMixin):
    pass

if __name__ == "__main__":
    halcon = RobotVolador("Halcon")
    nautilus = RobotAnfibio("Nautilus")

    print(halcon.volar())

    print(nautilus.volar())
    print(nautilus.nadar())
    print(nautilus.mover())
    print(nautilus.bateria)

    for _ in range(9):
        nautilus.mover()
    print(nautilus.bateria)
    print(nautilus.mover())

    try:
        nautilus.bateria = 50
    except AttributeError:
        print("La batería es de solo lectura")
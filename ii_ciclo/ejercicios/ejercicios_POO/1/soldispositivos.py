# Clase Dispositivo
class Dispositivo:
    def __init__(self, n: str):
        self.nombre = n          # Atributo público
        self.encendido = False        # Inicialmente apagado

    def encender(self):
        self.encendido = True

    def apagar(self):
        self.encendido = False

    def mostrar_info(self):
        return f"Dispositivo: {self.nombre} | Encendido: {self.encendido}"


# Clase hija LuzInteligente
class LuzInteligente(Dispositivo):
    def __init__(self, n: str, valor: int=0):
        super().__init__(n)      # Inicializa atributos de Dispositivo

        if 0 <= valor <= 100:
            self.__brillo = valor             # Atributo privado (0 a 100)
        else:
            self.__brillo = 0

    def get_brillo(self):
        return self.__brillo

    def set_brillo(self, valor: int):
        if 0 <= valor <= 100:
            self.__brillo = valor

    def mostrar_info(self):
        return f"{super().mostrar_info()} | Brillo: {self.__brillo}%"


# Clase hija CafeteraInteligente
class CafeteraInteligente(Dispositivo):
    def preparar_cafe(self):
        if not self.encendido:
            return "No se puede preparar café: la cafetera está apagada."
        return "Café preparado correctamente."

    def mostrar_info(self):
        return f"{super().mostrar_info()} | Tipo: Cafetera Inteligente"


# Clase Mixin para registro de eventos
class RegistroMixin:
    def registrar_evento(self, mensaje):
        self.registros.append(mensaje)

    def mostrar_registros(self):
        return self.registros


# Integración del Mixin
class LuzRegistrable(LuzInteligente, RegistroMixin):
    def __init__(self, n: str):
        super().__init__(n)
        self.registros = []

    def encender(self):
        super().encender()
        super().registrar_evento(f"Encendida la luz: {self.nombre}")

    def apagar(self):
        super().apagar()
        self.registrar_evento(f"Apagada la luz: {self.nombre}")

    def set_brillo(self, valor: int):
        if 0 <= valor <= 100:
            super().registrar_evento(f"Brillo ajustado a {valor}%")
            super().set_brillo(valor)

if __name__ == "__main__":
    luz = LuzRegistrable("Dormitorio")
    cafetera = CafeteraInteligente("Cafetera Principal")

    luz.encender()
    luz.set_brillo(80)
    luz.apagar()

    cafetera.encender()
    print(cafetera.preparar_cafe())

    print("\n--- ESTADO DE DISPOSITIVOS ---")
    print(luz.mostrar_info())
    print(cafetera.mostrar_info())

    print("\n--- REGISTRO DE EVENTOS ---")
    print("\n".join(luz.mostrar_registros()))

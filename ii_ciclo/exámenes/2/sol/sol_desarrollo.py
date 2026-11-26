class Sensor:
    def __init__(self, codigo, ubicacion):
        self.codigo = codigo
        self.ubicacion = ubicacion
        self.__lecturas = []  # Atributo privado: almacena las lecturas del sensor

    @property
    def cantidad(self):
        return len(self.__lecturas)     # Devuelve la cantidad de lecturas registradas

    def es_valido(self, valor):
        return True                     # Las clases hijas definen sus propias validaciones

    def registrar(self, valor):
        if not self.es_valido(valor):   # Comprueba si el valor es válido
            return False

        self.__lecturas.append(valor)
        return True

    def ultimo(self):
        if len(self.__lecturas) == 0:   # Comprueba si existen lecturas registradas
            return None

        return self.__lecturas[-1]      # Devuelve la última lectura

    def en_alerta(self):
        return False                    # Las clases hijas implementan sus propias condiciones de alerta

    def __str__(self):
        return f"{self.codigo} ({self.ubicacion}) | {self.cantidad} lecturas"

class SensorTemperatura(Sensor):
    def __init__(self, codigo, ubicacion, limite_alerta):
        super().__init__(codigo, ubicacion)          # Ejecuta el constructor de la clase padre
        self.limite_alerta = limite_alerta

    def es_valido(self, valor):
        return -40 <= valor <= 125      # Acepta temperaturas entre -40 y 125 °C

    def en_alerta(self):
        return self.ultimo() is not None and self.ultimo() > self.limite_alerta

    def __str__(self):
        return super().__str__() + f" | Límite {self.limite_alerta} °C"

class SensorHumedad(Sensor):
    def es_valido(self, valor):
        return 0 <= valor <= 100    # Acepta valores de humedad entre 0 y 100 %

    def en_alerta(self):
        return self.ultimo() is not None and (self.ultimo() < 30 or self.ultimo() > 70)

class Estacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.sensores = []          # Lista que almacena los sensores de la estación

    def agregar_sensor(self, sensor):
        self.sensores.append(sensor)

    def registrar_lectura(self, codigo, valor):
        for sensor in self.sensores:
            if sensor.codigo == codigo:         # Busca el sensor que coincide con el código
                return sensor.registrar(valor)

        return False         # Devuelve False si no encuentra el sensor

    def alertas(self):
        resultado = []
        for sensor in self.sensores:
            if sensor.en_alerta():              # Utiliza el método correspondiente a cada tipo de sensor.
                resultado.append(sensor)

        return resultado

    def total_lecturas(self):
        total = 0
        for sensor in self.sensores:
            total += sensor.cantidad            # Suma las lecturas de todos los sensores.

        return total

# Extra: permite agregar la funcionalidad de exportar datos a CSV.
class ExportableMixin:
    def a_csv(self):
        return f"{self.codigo},{self.ubicacion},{self.cantidad}"

# Hereda de SensorHumedad y agrega la funcionalidad de ExportableMixin.
class SensorHumedadExportable(SensorHumedad, ExportableMixin):
    pass  # No necesita métodos adicionales.

if __name__ == "__main__":
    estacion = Estacion("Laboratorio de Los Santos")
    estacion.agregar_sensor(SensorTemperatura("T1", "Servidores", 35))
    estacion.agregar_sensor(SensorTemperatura("T2", "Oficina", 28))
    estacion.agregar_sensor(SensorHumedad("H1", "Servidores"))

    lecturas = [("T1", 31.5), ("T2", 24.0), ("H1", 45), ("T1", 36.2),
                ("H1", 120), ("T3", 20), ("T2", 25.5), ("H1", 28), ("T2", 26.0)]

    rechazadas = 0
    for codigo, valor in lecturas:
        if not estacion.registrar_lectura(codigo, valor):
            rechazadas += 1

    for sensor in estacion.sensores:
        print(sensor)
    print("Lecturas rechazadas:", rechazadas)

    print("Sensores en alerta:")
    for sensor in estacion.alertas():
        print(sensor.codigo)

    print("Total de lecturas:", estacion.total_lecturas())

    # Extra (quite el comentario si lo implementó)
    h2 = SensorHumedadExportable("H2", "Bodega")
    h2.registrar(50)
    h2.registrar(60)
    print(h2.a_csv())
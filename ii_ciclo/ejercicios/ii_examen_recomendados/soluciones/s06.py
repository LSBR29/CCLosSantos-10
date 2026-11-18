class Especie:      # Especie Común
    # Atributos: Código, Nombre, Avistamientos
    def __init__(self, cod, nom):   # Constructor
        self.codigo = cod
        self.nombre = nom
        self.__avistamientos = 0

    @property                 # Getter para avistamientos
    def avistamientos(self):
        return self.__avistamientos
    
    # Métodos: registar(cantidad), puntos_por_especie(), puntaje(), __lt__(), __str__()
    def registrar(self, cantidad):
        if cantidad > 0:
            self.__avistamientos += cantidad
            return True
        else:
            return False

    def puntos_por_especie(self):
        return 1

    def puntaje_total(self):
        puntaje = self.avistamientos * self.puntos_por_especie()
        return puntaje

    def __lt__(self, other):      # less than : menor que (<)
        return self.puntaje_total() < other.puntaje_total()

    def __str__(self):
        return f"{self.nombre} ({self.codigo}) | Avistamientos: {self.avistamientos} | Puntaje: {self.puntaje_total()}"

class Reserva:
    # Atributos: nombre, meta, especies
    def __init__(self, nom, met):
        self.nombre = nom
        self.meta = met
        self.especies = dict()         # {CODIGO: OBJETO}

    def agregar_especie(self, especie):
        self.especies[especie.codigo] = especie

    def registrar_avistamiento(self, codigo, cantidad):
        if codigo in self.especies:
            self.especies[codigo].registrar(cantidad)
            return True
        else:
            return False

    def puntaje_total(self):
        total = 0
        for especie in self.especies.values():
            total += especie.puntaje_total()

        return total

    def sin_avistamientos(self):
        no_vistos = []

        for especie in self.especies.values():
            if especie.avistamientos == 0:
                no_vistos.append(especie.nombre)

        return no_vistos

    def meta_alcanzada(self):
        return self.puntaje_total() >= self.meta

    def especie_destacada(self):
        destacada = None
        for especie in self.especies.values():
            if destacada is None or destacada < especie:        # Si la nueva revisada es mayor, se cambia como destacada
                destacada = especie

        return destacada

class EspecieRara(Especie):
    def puntos_por_especie(self):
        return 5

    def __str__(self):
        return super().__str__() + "| Rara"

class EspecieEndemica(Especie):
    def __init__(self, cod, nom, reg):
        super().__init__(cod, nom)
        self.region = reg

    def puntos_por_especie(self):
        return 10

    def __str__(self):
        return super().__str__() + f"| Región: {self.region}"

if __name__ == "__main__":
    reserva = Reserva("Reserva Los Santos", 40)
    reserva.agregar_especie(Especie("PIN", "Pinaroloxias inornata"))
    reserva.agregar_especie(EspecieRara("CEB", "Cebus imitator"))
    reserva.agregar_especie(EspecieRara("TAP", "Tapirus bairdii"))
    reserva.agregar_especie(EspecieEndemica("IST", "Isthmohyla nacientes", "Los Santos"))

    registros = [("PIN", 3), ("CEB", 2), ("IST", 1), ("PIN", 2), ("XYZ", 4), ("CEB", 0), ("IST", 2)]

    rechazados = 0
    for codigo, cantidad in registros:
        if not reserva.registrar_avistamiento(codigo, cantidad):
            rechazados += 1

    for codigo, especie in reserva.especies.items():
        print(f"{codigo}: {especie}")

    print(f"Registros rechazados: {rechazados}")
    print(f"Puntaje total: {reserva.puntaje_total()}")
    print(f"Sin avistamientos: {reserva.sin_avistamientos()}")
    print(f"Meta alcanzada: {reserva.meta_alcanzada()}")
    print(f"Especie destacada: {reserva.especie_destacada().nombre}")

    try:
        reserva.especies["PIN"].avistamientos = 100
    except AttributeError:
        print("Avistamientos solo se puede leer")
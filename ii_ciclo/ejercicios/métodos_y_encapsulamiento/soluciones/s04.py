class Producto:
    def __init__(self, nombre, precio):
        if precio < 0:
            print("Error")
            self.__precio = 0
        else:
            self.__precio = precio
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            print("Error")
        else:
            self.__precio = nuevo_precio

    def aplicar_descuento(self, porcentaje):
        if porcentaje < 0 or porcentaje > 100:
            print("Error")
        else:
            self.__precio -= self.__precio * (porcentaje / 100)

    def __eq__(self, other):
        if not isinstance(other, Producto):
            return False
        return self.__precio == other.__precio

    def __lt__(self, other):
        if not isinstance(other, Producto):
            return False
        return self.__precio < other.__precio

if __name__ == "__main__":
    p1 = Producto("Café", 3500)
    p2 = Producto("Galletas", 2000)

    print(p1 < p2)               # False

    p1.aplicar_descuento(10)
    print(p1.precio)             # 3500

    print(p1 == Producto("Otro", 3500))  # True
    p1.precio = -5               # Error
class Juego:
    def __init__(self, nombre_juego):
        self.titulo = nombre_juego
        self.minutos_jugados = 0

    def iniciar(self):
        print(f"El juego {self.titulo} está iniciando")

    def jugar(self, minutos):
        self.minutos_jugados += minutos
        print(f"Usted ha jugado {self.titulo} por {self.minutos_jugados}")

if __name__ == "__main__":
    juego = input("Ingrese un juego: ")
    j1 = Juego(juego)

    j1.iniciar()
    j1.jugar(50)
    j1.jugar(80)
    j1.jugar(70)
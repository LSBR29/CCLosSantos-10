class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"

if __name__ == "__main__":
    l1 = Libro("La Biblioteca de la Medianoche", "Matt Haig")
    print(l1.info())
class Publicacion:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

    def mostrar_info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"
    
class Revista(Publicacion):
    def __init__(self, titulo: str, autor: str, numero_edicion: int=1):
        super().__init__(titulo, autor)
        self.numero_edicion = numero_edicion

    def mostrar_info(self):
        return super().mostrar_info() + f", Edición: {self.numero_edicion}"

class ConDescuentoMixin:
    def aplicar_descuento(self, precio: float, porcentaje: float):
        precio_final = precio - precio*porcentaje/100
        return precio_final
    
class Libro(Publicacion, ConDescuentoMixin):
    def __init__(self, titulo: str, autor: str, precio: float=0, paginas: int=1):
        super().__init__(titulo, autor)
        self.precio = precio
        
        if paginas > 0:
            self.__paginas = paginas
        else:
            self.__paginas = 1

    @property
    def paginas(self):
        return self.__paginas
    
    @paginas.setter
    def paginas(self, valor):
        if valor > 0:
            self.__paginas = valor

    def mostrar_info(self):
        return super().mostrar_info() + f", Páginas: {self.__paginas}, Precio {self.precio}"

if __name__ == "__main__":
    r1 = Revista("Nature", "Norman Lockyer", "2025")
    print(f"Datos de la revista: {r1.mostrar_info()}\n")

    l1 = Libro("Dune", "Frank Herbert", 8900, 779)
    print(f"Páginas del libro {l1.titulo}: {l1.paginas}")
    l1.paginas = 10000
    print(f"Páginas del libro {l1.titulo} modificadadas a: {l1.paginas}\n")

    print(f"Precio del libro {l1.titulo} sin descuento: {l1.precio}")
    print(f"Precio del libro {l1.titulo} con descuento de 25%: {l1.aplicar_descuento(l1.precio, 25)}")
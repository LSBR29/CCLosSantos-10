class Dispositivo():
    def __init__(self, nombre:str, horas_dia:int):
        self.nombre = nombre
        self.horas_dia = horas_dia
        self.__consumo_watts = 0
        
    @property
    def consumo(self):
        return self.__consumo_watts
        
    @consumo.setter
    def consumo(self, valor:float):
        if valor >= 0:
            self.__consumo_watts = valor
        else:
            raise ValueError
    
    def calcular_consumo_mensual(self):
        return self.consumo * self.horas_dia * 30

class DispositivoInteligente(Dispositivo):
    def __init__(self, nombre:str, consumo:float, horas_dia:int, modo:bool=False):
        super().__init__(nombre, horas_dia)

        self.modo_ahorro = modo
        try:
            self.consumo = consumo
        except:
            raise ValueError
    
    def calcular_consumo_mensual(self):
        consumo = super().calcular_consumo_mensual()

        if self.modo_ahorro:
            return  consumo*0.8
        else:
            return consumo
    
    def __str__(self):
        return f"Dispositivo: {self.nombre} - Consumo mensual: {self.calcular_consumo_mensual()} (Modo Ahorro: {self.modo_ahorro})"
    
class Gestor():
    def __init__(self):
        self.dispositivos = []

    def agregar_dispositivo(self, dispositivo:Dispositivo):
        self.dispositivos.append(dispositivo)

    def mostrar_todos(self):
        for disp in self.dispositivos:
            print(disp)
            
    def mayor_consumo(self):
        ordenados = sorted(self.dispositivos, key=lambda disp: disp.calcular_consumo_mensual(), reverse=True)
        return ordenados[0]
    
    def menor_consumo(self):
        ordenados = sorted(self.dispositivos, key=lambda disp: disp.calcular_consumo_mensual())
        return ordenados[0]

if __name__ == "__main__":
    gestor = Gestor()

    try:
        bombillo = DispositivoInteligente(nombre="Bombillo LED", consumo=25, horas_dia=6, modo=True)
        enchufe = DispositivoInteligente(nombre="Enchufe WiFi", consumo=20, horas_dia=12)
    except:
        print("Hubo un error al crear los objetos")
        exit()

    gestor.agregar_dispositivo(bombillo)
    gestor.agregar_dispositivo(enchufe)

    gestor.mostrar_todos()
    print(f"El {gestor.mayor_consumo().nombre} es el que consume más energía")

    #Puntos Extra
    print(f"El {gestor.menor_consumo().nombre} es el que consume menos energía")
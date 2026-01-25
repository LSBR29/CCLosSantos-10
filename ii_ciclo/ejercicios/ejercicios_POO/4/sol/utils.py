import random

class Criatura:
    def __init__(self, nombre:str, velocidad:int, personalidad:str):
        self.nombre = nombre
        self.v_base = velocidad
        self.__personalidad = personalidad

        self.v_real = 0

    @property
    def personalidad(self):
        return self.__personalidad
    
    @personalidad.setter
    def personalidad(self, valor):
        if valor in ("agresiva", "perezosa", "caotica"):
            self.__personalidad = valor
        else:
            return ValueError("ERROR: PERSONALIDAD DESCONOCIDA")

    def velocidad_real(self):
        if self.personalidad == "agresiva":
            self.v_real = self.v_base + 0.3*self.v_base

        elif self.personalidad == "perezosa":
            self.v_real = self.v_base - 0.4*self.v_base

        elif self.personalidad == "caotica":
            self.v_real = self.v_base + random.uniform(-0.5, 0.5)*self.v_base
        
        return self.v_real

def map_velocidades(criaturas:list):
    return map(lambda criatura: criatura.velocidad_real(), criaturas)

def filtrar_superiores(promedio:float, criaturas:list):
    return filter(lambda criatura: criatura.v_real >= promedio, criaturas)

def determinar_ganador(criaturas:list):
    return max(criaturas, key=lambda criatura: criatura.v_real)
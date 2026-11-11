class Termostato:
    def __init__(self, temp = 25):
        if temp > 150 or temp <-50:
            print("Error: Temperatura fuera del rango")
            self.__temperatura_c = 25
        else:
            self.__temperatura_c = temp

    @property
    def temperatura(self):
        return self.__temperatura_c

    @temperatura.setter
    def temperatura(self, nueva_temp):
        if nueva_temp > 150 or nueva_temp <-50:
            print("Error: Temperatura fuera del rango")
        else:
            self.__temperatura_c = nueva_temp

    def a_fahrenheit(self):
        return self.__temperatura_c * 9/5 + 32

if __name__ == "__main__":
    t = Termostato(25.0)

    print(t.temperatura)        # 25.0

    print(t.a_fahrenheit())     # 77.0

    t.temperatura = -2000         # Error
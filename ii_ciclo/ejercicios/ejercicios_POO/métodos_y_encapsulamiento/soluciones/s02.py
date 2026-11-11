class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        if saldo_inicial < 0:
            print("Error")
            self.__saldo = 0  # Un valor por defecto si se ingresa un saldo negativo al crear el objeto
        else:
            self.__saldo = saldo_inicial

    def depositar(self, monto):
        if monto <= 0:
            print("Error")
        else:
            self.__saldo += monto

    def retirar(self, monto):
        if monto <= 0 or monto > self.__saldo:
            print("Error")
        else:
            self.__saldo -= monto

    def consultar_saldo(self):
        return self.__saldo

if __name__ == "__main__":
    c = CuentaBancaria(100)

    c.depositar(50)
    print(c.consultar_saldo())  # 150

    c.retirar(30)
    print(c.consultar_saldo())  # 120

    c.retirar(200)              # Error
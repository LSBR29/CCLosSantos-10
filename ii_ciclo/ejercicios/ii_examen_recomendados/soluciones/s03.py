class Usuario:
    def __init__(self, nombre, clave, correo):
        self.nombre = nombre
        self.__clave = clave
        self.correo = correo
        self.__intentos_fallidos = 0

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, nuevo_correo):
        if "@" not in nuevo_correo:
            raise ValueError("Correo inválido")
        self.__correo = nuevo_correo

    @property
    def bloqueada(self):
        return self.__intentos_fallidos >= 3

    def iniciar_sesion(self, clave):
        if self.bloqueada:
            return False
        if clave == self.__clave:
            self.__intentos_fallidos = 0
            return True
        self.__intentos_fallidos += 1
        return False

if __name__ == "__main__":
    usuario = Usuario("ana", "python2026", "ana@correo.com")

    print(usuario.iniciar_sesion("1234"))
    print(usuario.iniciar_sesion("python2026"))

    for _ in range(3):
        usuario.iniciar_sesion("0000")
    print(usuario.bloqueada)
    print(usuario.iniciar_sesion("python2026"))

    try:
        usuario.correo = "sin-arroba"
    except ValueError as error:
        print(error)

    try:
        usuario.bloqueada = False
    except AttributeError:
        print("bloqueada es de solo lectura")

    try:
        print(usuario.__clave)
    except AttributeError:
        print("La clave es privada")
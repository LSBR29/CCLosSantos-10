import math

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def valor(self):
        return self.numerador / self.denominador

    def simplificar(self):
        divisor = math.gcd(self.numerador, self.denominador)
        self.numerador //= divisor
        self.denominador //= divisor

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __eq__(self, other):
        return self.valor() == other.valor()

    def __lt__(self, other):
        return self.valor() < other.valor()

if __name__ == "__main__":
    a = Fraccion(1, 2)
    b = Fraccion(2, 4)
    c = Fraccion(3, 4)

    print(a, b, c)
    print(a == b)
    print(a < c)
    print(c < a)
    print(c.valor())

    b.simplificar()
    print(b)
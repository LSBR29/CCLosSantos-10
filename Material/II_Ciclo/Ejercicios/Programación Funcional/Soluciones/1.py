n = 15

# Todo hecho en una línea
impares_cuadrado = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, range(1, n+1))))

# Imprimir resultado
print(f"n = {n}")
print(impares_cuadrado)
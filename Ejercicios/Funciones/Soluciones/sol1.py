def suma_divisores(num):
    suma = 0

    for i in range(1, num):  # Recorre desde 1 hasta num-1
        if num % i == 0:     # Si i es divisor de num se suma
            suma += i
            
    return suma

# Función principal
if __name__ == "__main__":
    # Pedir dos números al usuario
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    # Calcular la suma de los divisores de cada número
    suma1 = suma_divisores(num1)
    suma2 = suma_divisores(num2)

    print(f"\nLos divisires del {num1} dan: {suma1}")
    print(f"Los divisires del {num2} dan: {suma2}")

    # Verificar si son amigos
    if suma1 == num2 and suma2 == num1:
        print(f"\n{num1} y {num2} son números amigos")
    else:
        print(f"\n{num1} y {num2} NO son números amigos")
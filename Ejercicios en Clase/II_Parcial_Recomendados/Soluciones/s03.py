# Función que retorna el doble de un número
def doble(n):
    return n * 2

# Función que retorna el triple de un número
def triple(n):
    return n * 3

# Llamar a la función principal
if __name__ == "__main__":
    try:
        # Pedir al usuario un número
        numero = int(input("Ingrese un número: "))
        
        # Calcular e imprimir el doble y el triple usando las funciones
        print("Doble:", doble(numero))
        print("Triple:", triple(numero))
    
    except ValueError:
        print("Por favor, ingrese un número válido.")
from random import randint

def leer_archivo(ruta):
    lista_strings = list()

    try:
        with open(ruta, 'r') as f:
            lista_strings = f.readlines()

            if lista_strings == []:
                raise FileNotFoundError

    except FileNotFoundError:
        with open(ruta, 'w') as f:
            # Generar 10 números aleatorios y escribirlos en el archivo
            for _ in range(10):
                numero_aleatorio = randint(1, 100)
                lista_strings.append(str(numero_aleatorio) + "\n")

            f.writelines(lista_strings)

    return lista_strings

def calcular_suma(lista_numeros):
    resultado = 0

    for num in lista_numeros:
        resultado += num

    return resultado

if __name__ == "__main__":
    ruta = "Ejemplos/numeros.txt"

    lista_strings = leer_archivo(ruta)
    lista_numeros = []

    for string in lista_strings:
        try:
            num = int(string)
            lista_numeros.append(num)
        except:
            continue

    suma_total = calcular_suma(lista_numeros)
    cantidad_numeros = len(lista_numeros)

    print(f"Suma total: {suma_total}")
    print(f"Promedio: {suma_total/cantidad_numeros}")
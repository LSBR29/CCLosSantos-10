cantidad = int(input("¿Cuántas palabras desea ingresar?: "))    # Solicita al usuario la cantidad de palabras
palabras = []   # Lista donde se almacenarán todas las palabras
totalCaracteres = 0     # Variable para contar la cantidad total de caracteres

# Ciclo for para solicitar las palabras
for n in range(cantidad):
    entrada = input("Ingrese una palabra: ")    # Solicita una palabra al usuario

    palabras.append(entrada)    # Agrega la palabra a la lista
    totalCaracteres += len(entrada)     # Suma la cantidad de caracteres de la palabra ingresada

masCorta = palabras[0]  # Se asume inicialmente que la primera palabra es la más corta
totalVocales = 0    # Contador para las palabras que empiezan con vocal

# Recorre todas las palabras almacenadas
for palabra in palabras:
    # Verifica si la palabra actual es más corta que la guardada
    if len(palabra) < len(masCorta):
        masCorta = palabra
    # Verifica si la primera letra es una vocal
    if palabra[0] in "aeiouAEIOU":
        totalVocales += 1

# Imprimir resultados
print()
print(f"Palabras ingresadas: {palabras}")
print(f"Cantidad total de caracteres: {totalCaracteres}")
print(f"Palabra más corta: {masCorta}")
print(f"Palabras que empiezan con vocal: {totalVocales}")
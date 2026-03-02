#Función para calcular promedio de un diccionario, recibe el diccionario y la cantidad de elementos que tiene
def promedio(notas, cantidad):
    prom = 0

    #Se recorren solo los valores del diccionario y se suman a una variable donde se guardará el promedio
    for nota in notas.values():
        prom += nota

    #Se divide la suma anterior entre la cantidad total
    prom /= cantidad

    #Se retorna el promedio
    return prom

#Función principal
if __name__ == "__main__":
    #Se pide la cantidad de estudiantes
    cantidad = int(input("Ingrese la cantidad de estudiantes: "))

    #Se crea una variable diccionario que tendrá la forma "Nombre":calificación
    calificaciones = {}

    #Se piden los datos usando un ciclo for con una cantidad de iteraciones definidas con range()
    for est in range(1, cantidad + 1):
        nombre = input(f"Nombre del estudiante {est}: ")
        nota = int(input(f"Calificación de {nombre}: "))

        #Se añaden los datos al diccionario respectivo
        calificaciones.update({nombre:nota})

    #Se imprime lo solicitado
    print(f"\nDiccionario de calificaciones: {calificaciones}")
    print(f"Promedio general: {promedio(calificaciones, cantidad)}")
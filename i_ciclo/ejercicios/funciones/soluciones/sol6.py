#Función recursiva
def cortes_necesarios(n):
    if n == 1:          #Caso base: Si solo se necesita un pedazo, se necesita la tabla entera (0 cortes)
        return 0
    else:
        return 1 + cortes_necesarios(n - 1)     #Caso recursivo: Se hace 1 corte (aumente el número de pedazos), y luego se resuelve para lo que falta.

#Función principal
if __name__ == "__main__":
    pedazos = int(input("¿Cuántos pedazos de madera quieres? "))
    print("Cortes necesarios:", cortes_necesarios(pedazos))
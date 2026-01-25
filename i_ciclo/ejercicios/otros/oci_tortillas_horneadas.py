#Ingresar los números
numeros = input("Ingrese dos números: ")

#Separar los números
num1, num2 = numeros.split()

#Convertirlos a enteros
num1 = int(num1)
num2 = int(num2)

#Calcular el tamaño de la tortilla
a = num1 + 5
b = num2 + 3

#Calcular los centímetros cuadrados de la tortilla
area = a * b

#Obtener la relación entre centímetros y gramos (1g por 1cm^2)
gramos = 1 * area

#Imprimir el resultado
print(gramos)
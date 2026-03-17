#Ingresar los números
numeros = input("Ingrese dos números: ")

#Separar los números
num1, num2 = numeros.split()

#Convertirlos a enteros
num1 = int(num1)
num2 = int(num2)

#Si la resta es mayor que 0, imprimo la resta
if num1 - num2 > 0:
    print(num1 - num2)
    
#Si la resta es menor que 0, me quedan 0
elif num1 - num2 < 0:
    print(0)
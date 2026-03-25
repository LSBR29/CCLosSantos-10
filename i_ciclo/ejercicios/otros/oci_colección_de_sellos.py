#Ingresar los números y convertir a entero
num1 = int(input())
num2 = int(input())

#Si la resta es mayor que 0, imprimo la resta
if num1 - num2 > 0:
    print(num1 - num2)
    
#Si la resta es menor que 0, me quedan 0
elif num1 - num2 < 0:
    print(0)


"""Otra manera
#Si el primero es mayor al segundo se puede hacer la resta
if num1 > num2:
    print(num1 - num2)

#Si no el resultado daría negativo y por tanto se entregaron todos
else:
    print(0)

"""
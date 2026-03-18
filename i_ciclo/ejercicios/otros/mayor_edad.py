#Pedimos una edad
edad = int(input("Ingrese una edad: "))

#Verificamos si es mayor o menor de edad
if edad >= 18:
    print("Es mayor de edad")
elif edad > 0 and edad < 18:
    print("Es menor de edad")
else: # En caso de que la edad no esté entre 0 y 18 o sea mayor a 18
    print("Número inválido")
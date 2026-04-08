# Listas para nombres y notas
nombres = []
notas = []

# Estudiante 1
print("Estudiante 1")
nombre1 = input("Nombre: ")
nombres.append(nombre1)
try:
    nota1 = int(input("Nota: "))
except ValueError:
    print("Error: nota no válida, se asigna 0.")
    nota1 = 0
notas.append(nota1)

# Estudiante 2
print("\nEstudiante 2")
nombre2 = input("Nombre: ")
nombres.append(nombre2)
try:
    nota2 = int(input("Nota: "))
except ValueError:
    print("Error: nota no válida, se asigna 0.")
    nota2 = 0
notas.append(nota2)

# Estudiante 3
print("\nEstudiante 3")
nombre3 = input("Nombre: ")
nombres.append(nombre3)
try:
    nota3 = int(input("Nota: "))
except ValueError:
    print("Error: nota no válida, se asigna 0.")
    nota3 = 0
notas.append(nota3)

# Nota más baja con min()
nota_minima = min(notas)

# Promedio con sum()¡
promedio = sum(notas) / len(notas)

# Aprobados (nota >= 60)
# Lista para almacenar los nombres de los estudiantes que aprobaron
aprobados = []

# Verificar estudiante 1 (índice 0)
if notas[0] >= 60:
    aprobados.append(nombres[0])

# Verificar estudiante 2 (índice 1)
if notas[1] >= 60:
    aprobados.append(nombres[1])

# Verificar estudiante 3 (índice 2)
if notas[2] >= 60:
    aprobados.append(nombres[2])

# Resultados
print("\nResultados")
print("Nombres:", nombres)
print("Notas:", notas)
print(f"Nota más baja: {nota_minima}")
print(f"Promedio: {promedio}")

if aprobados:
    print("Aprobados:", aprobados)
else:
    print("Ninguno aprobó")
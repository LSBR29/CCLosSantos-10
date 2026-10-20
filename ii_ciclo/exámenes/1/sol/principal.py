# Parte 1 - Verdadero o Falso
# 1. F
# 2. V
# 3. V
# 4. F
# 5. V
# 6. V
# 7. V
# 8. V
# 9. F
# 10. V
# 11. V
# 12. F
# 13. V
# 14. F
# 15. V
# 16. F
# 17. V
# 18. V
# 19. F
# 20. F

import utilidades

# Punto 1: leer todas las líneas del archivo
with open("asistencia.txt", "r") as archivo:
    lineas = archivo.readlines()

# Punto 2: separar nombre y estado
nombres = []
estados = []
for linea in lineas:
    partes = linea.strip().split(",")  # strip() quita el \n del final
    nombres.append(partes[0])
    estados.append(partes[1])

# Punto 3: total de ausencias del curso
total_ausencias = 0
for estado in estados:
    if estado == "ausente":
        total_ausencias += 1

# Puntos 4, 8 y 9: ausencias por estudiante (función en utilidades.py)
ausencias_por_estudiante = utilidades.contar_ausencias(nombres, estados)

# Punto 5: estudiante con más ausencias (también hay otras maneras de hacerlo)
mas_ausente = ""
max_ausencias = -1
for nombre, cantidad in ausencias_por_estudiante.items():
    if cantidad > max_ausencias:
        mas_ausente = nombre
        max_ausencias = cantidad

# Punto 6: crear resumen.txt (modo 'w')
with open("resumen.txt", "w") as resumen:
    resumen.write(f"Total de ausencias: {total_ausencias}\n")

    for nombre, cantidad in ausencias_por_estudiante.items():
        resumen.write(f"{nombre}: {cantidad}\n")

# Punto 7: agregar la línea final (modo 'a', no borra lo anterior)
with open("resumen.txt", "a") as resumen:
    resumen.write(f"Estudiante con más ausencias: {mas_ausente} ({max_ausencias})\n")

# Punto 10: mostrar el resumen en pantalla
print(f"Total de ausencias: {total_ausencias}")

for nombre, cantidad in ausencias_por_estudiante.items():
    print(f"{nombre}: {cantidad}")

print(f"Estudiante con más ausencias: {mas_ausente} ({max_ausencias})")
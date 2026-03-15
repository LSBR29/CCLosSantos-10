# Solicitud de datos
nombre_completo = input("Ingrese su nombre completo: ")
año_ingreso = input("Ingrese el año de ingreso: ")
identificacion = input("Ingrese su número de identificación: ")

# Modificaciones al nombre
nombre_mayus = nombre_completo.upper()
nombre_invertido = nombre_completo[::-1]

# Inicial
inicial = nombre_completo[0]

# Últimos 3 dígitos
ultimos_tres = identificacion[-3:]

# Código estudiantil
codigo = f"{inicial}_{ultimos_tres}_{año_ingreso}"

# Correo institucional
correo = codigo + "@ccls.ac.cr"

# Resultados
print("RESULTADO")
print(f"Nombre en mayúsculas: {nombre_mayus}")
print(f"Nombre invertido: {nombre_invertido}")
print(f"Inicial: {inicial}")
print(f"Últimos 3 dígitos: {ultimos_tres}")
print(f"Código estudiantil: {codigo}")
print(f"Correo institucional: {correo}")
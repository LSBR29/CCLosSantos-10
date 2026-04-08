# Mensaje 1
msg1 = input("Mensaje 1: ")

# Mensaje 2
msg2 = input("Mensaje 2: ")

# Mensaje 3
msg3 = input("Mensaje 3: ")

# Lista para almacenar los mensajes
mensajes = [msg1, msg2, msg3]

# Resultados
print("\nResultados")
print("Originales:", mensajes)

# Convertir cada mensaje a mayúsculas
mayusculas = [mensajes[0].upper(), mensajes[1].upper(), mensajes[2].upper()]
print("Mayúsculas:", mayusculas)

# Longitud de cada mensaje
longitudes = [len(mensajes[0]), len(mensajes[1]), len(mensajes[2])]
print("Longitudes:", longitudes)
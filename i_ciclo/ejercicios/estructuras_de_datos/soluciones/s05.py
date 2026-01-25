# Lista inicial con la información
actividad_usuarios = [
  ("Ana", "wikipedia.org", "2024-05-01"),
  ("Ana", "openai.com", "2024-05-02"),
  ("Luis", "google.com", "2024-05-01"),
  ("Luis", "wikipedia.org", "2024-05-03")
]

# Declarar diccionario
diccionario = dict()

# Recorrer lista de `actividad_usuarios` y agregar contenidos al diccionario
# Índice 0: el nombre del usuario
# Índice 1: la página visitada
for usuario, pagina, fecha in actividad_usuarios:
    # Verificar si no existe una clave con el usuario
    if usuario not in diccionario.keys():
        diccionario.update({ usuario : set() })

    # Agregar página al set en la clave `usuario` del diccionario
    diccionario[usuario].add(pagina)

# Imprimir los sitios por usuario
for usuario, conjunto in diccionario.items():
    print(f"\nUsuario: {usuario}")
    print(conjunto)

# Realizar intersección entre los sets de todos los usuarios
sitios_comunes = set.intersection(*diccionario.values())

print("\n--- Sitios comunes ---")
print(sitios_comunes)
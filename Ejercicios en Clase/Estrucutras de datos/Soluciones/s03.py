# Crear un diccionario donde la clave será el departamento
base_datos = dict()

# Solicitar la cantidad de departamentos
cantidad_departamentos = int(input("Cantidad de departamentos: "))

# Ingresar cada departamento con una lista vacía de empleados
for i in range(1, cantidad_departamentos + 1):
    nombre_departamento = input(f"Ingrese el nombre del departamento {i}: ")
    base_datos.update({ nombre_departamento : [] })

# Agregar empleados a cada departamento
for departamento, empleados in base_datos.items():

    print(f"\n--- Empleados para {departamento} ---")

    # Pedir empleados hasta que se presione ENTER sin texto
    nombre_empleado = input("Ingrese el nombre del empleado o presione enter para continuar: ")
    while nombre_empleado != "":
        edad_empleado = int(input("Edad del empleado: "))
        salario_empleado = float(input("Salario del empleado: "))

        # Agregar empleado al departamento como una tupla
        empleados.append((nombre_empleado, edad_empleado, salario_empleado))

        nombre_empleado = input("\nIngrese el nombre del siguiente empleado o presione enter para continuar: ")

# Imprimir empleados por departamento
for departamento, empleados in base_datos.items():
    if empleados:
        print(f"\n--- Empleados en {departamento} ---")
        print(empleados)

        # Calcular el promedio salarial por departamento
        print(f"\n--- Promedio salarial en {departamento} ---")

        suma_salarios = 0
        for empleado in empleados:
            suma_salarios += empleado[2]
            
        promedio = suma_salarios / len(empleados)
        print(f"Promedio: {promedio:.2f}")
    else:
        print(f"No hay empleados en {departamento}.")

# Buscar al empleado con el salario más alto
empleado_top = None
salario_maximo = 0
departamento_top = ""

for departamento, empleados in base_datos.items():
    for empleado in empleados:
        if empleado[2] > salario_maximo:
            salario_maximo = empleado[2]
            empleado_top = empleado
            departamento_top = departamento

print(f"\n--- Empleado con el salario más alto ---")
if empleado_top:
    print(f"{empleado_top[0]} ({empleado_top[1]} años) con salario {empleado_top[2]:.2f} en {departamento_top}")
else:
    print("No hay empleados registrados.")
# Solicitar el número de la tabla
num = int(input("Ingrese un número (1-9): "))

# Solicitar el número límite
limite = int(input("Ingrese hasta qué número desea ver la tabla de multiplicar: "))

idx = 1 # Inicio de la tabla de multiplicar

while idx <= limite:
    print(f"{num} x {idx} = {num * idx}")

    idx += 1 # Incrementar variable para asegurarse que el loop termine
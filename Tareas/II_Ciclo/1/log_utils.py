def agregar_log(ruta_archivo, tipo, mensaje):
    with open(ruta_archivo, 'a') as f:
        f.write(f'[{tipo}] {mensaje}\n')

def leer_logs(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as f:
            return f.readlines()
    except:
        return []

def filtrar_logs(lista_logs, tipo):
    filtrados = []

    for linea in lista_logs:
        if linea.startswith(f'[{tipo}]'):
            filtrados.append(linea)

    return filtrados

def eliminar_logs_por_tipo(ruta_archivo, tipo):
    lista_logs = leer_logs(ruta_archivo)
    logs_filtrados = filtrar_logs(lista_logs, tipo)

    for linea in logs_filtrados:
        lista_logs.remove(linea)
        
    with open(ruta_archivo, 'w') as f:
        f.writelines(lista_logs)
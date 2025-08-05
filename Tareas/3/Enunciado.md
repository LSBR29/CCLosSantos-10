# Tarea 3
## Descripción
Desarrolle un programa en Python que permita gestionar un archivo llamado `logs.txt`.
Cada línea del archivo representa un evento del sistema con la siguiente estructura:
```
[tipo] mensaje
```

donde `tipo` puede ser:
- `INFO` – mensajes informativos
- `ERROR` – errores del sistema
- `WARNING` – advertencias

### Ejemplo de contenido
```
[INFO] Inicio del sistema
[ERROR] No se pudo conectar a la base de datos
[WARNING] Memoria al 90%
```

---

## Funcionalidades del programa
El programa debe permitir al usuario:

1. **Agregar evento nuevo**
   - Mostrar un **submenú** para seleccionar el tipo de evento: `INFO`, `ERROR`, `WARNING`.
   - Solicitar el mensaje del evento.
   - Guardar la entrada en `logs.txt` con formato `[TIPO] mensaje`.
2. **Ver todos los eventos registrados**
   - Leer el archivo y mostrar todas las líneas.
3. **Filtrar eventos por tipo**
   - Mostrar solo los eventos que coincidan con el tipo seleccionado.
4. **Eliminar eventos por tipo**
   - Eliminar todas las entradas de un tipo específico.
     *Pista: Con la lista de todas las líneas, filtrar/eliminar las que no coincidan y sobrescribir el archivo usando el modo `'w'`.*
5. **Salir**
---

## Archivos requeridos

### `main.py`
- Muestra el menú principal y el submenú de tipos.
- Llama a las funciones definidas en `log_utils.py`.

### `fuciones_logs.py`
Debe contener las siguientes funciones:
```python
def agregar_log(ruta_archivo, tipo, mensaje):
    # Escribe una nueva línea en `logs.txt` en formato [TIPO] mensaje

def leer_logs(ruta_archivo):
    # Devuelve una lista de todas las entradas

def filtrar_logs(lista_logs, tipo):
    # Devuelve solo las entradas del tipo indicado

def eliminar_logs_por_tipo(ruta_archivo, lista_logs, tipo):
    # Reescribe `logs.txt` sin las líneas del tipo indicado
```

---

## Criterios de Evaluación
- **Escritura y lectura correcta del archivo**: 25%
- **Uso de múltiples archivos (`main.py`, `log_utils.py`)**: 10%
- **Uso de `try-except` para errores de archivo**: 10%
- **Permite seleccionar tipo de evento cuando se necesita**: 10%
- **Filtro de eventos por tipo**: 10%
- **Eliminación por tipo (reescritura de archivo)**: 15%
- **Manejo de errores en las entradas**: 10%
- **Menú claro y legible**: 5%
- **Comentarios claros**: 5%
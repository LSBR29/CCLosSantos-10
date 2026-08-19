# Tarea 1

## Descripción

Desarrolle un programa en Python que permita gestionar un diario personal almacenado en un archivo llamado `diario.txt`.

Cada línea del archivo representa una entrada del diario con la siguiente estructura:

```text
YYYY-MM-DD | texto de la entrada
```

* La **fecha** se genera automáticamente al agregar una entrada.
* El **texto** puede contener espacios y cualquier carácter.

### Ejemplo de contenido

```text
2025-01-05 | Empecé el año ordenando mi cuarto y encontré cosas que creía perdidas.
2025-01-08 | Hoy me regalaron una planta pequeña, espero que no se me muera rápido.
2025-01-12 | Hoy no hice nada interesante, solo me quedé en casa viendo series.
```

---

## Funcionalidades del programa

El programa debe permitir al usuario:

### 1. Agregar nueva entrada

* El programa obtiene la fecha actual automáticamente utilizando `date.today()`.
   - *Recomendación: Investigue el uso de `from datetime import date`.*
* Solicita únicamente el texto de la entrada.
* Guarda la línea en `diario.txt` con el formato:

```text
YYYY-MM-DD | texto
```

### 2. Buscar entradas por palabra clave

* Solicita una palabra o frase al usuario.
* Muestra todas las entradas cuyo texto contenga esa palabra o frase.
* La búsqueda debe ignorar mayúsculas y minúsculas.
* Si no hay coincidencias, muestra un mensaje indicándolo.

### 3. Eliminar entradas por fecha

* Solicita una fecha en formato `YYYY-MM-DD`.
* Elimina **todas** las entradas que correspondan exactamente con esa fecha.
* Si no existe ninguna entrada con esa fecha, muestra un mensaje de aviso y no modifica el archivo.
   - *Recomendación: Con la lista de todas las líneas, elimina las que comiencen por la fecha indicada y sobrescribe el archivo usando el modo `'w'`.*

### 4. Salir

Finaliza la ejecución del programa.

---

## Archivos requeridos

El programa debe estar dividido en dos archivos:

```text
main.py
diario_utils.py
```

### `main.py`

Debe:

* Mostrar el menú principal.
* Solicitar los datos al usuario.
* Utilizar las funciones de `diario_utils.py`.
* Manejar las opciones del menú.

### `diario_utils.py`

Debe contener las siguientes funciones:

```python
from datetime import date

def leer_diario(ruta_archivo):
    # Devuelve una lista con todas las líneas del archivo

def agregar_entrada(ruta_archivo, texto):
    # Obtiene la fecha actual con date.today()
    # Agrega una nueva entrada al archivo
    # Devuelve True si añadió correctamente y False si hubo un error

def buscar_por_palabra(lista_lineas, palabra):
    # Devuelve las líneas que contienen la palabra o frase

def eliminar_por_fecha(ruta_archivo, lista_lineas, fecha):
    # Elimina las entradas correspondientes a la fecha indicada
    # Devuelve True si eliminó correctamente y False si hubo un error
```

La función `leer_diario()` debe utilizarse para obtener las líneas del archivo antes de realizar las operaciones de búsqueda y eliminación.

---

## Criterios de Evaluación

* **Lectura y escritura correcta del archivo:** 25%
* **Uso de múltiples archivos (`main.py`, `diario_utils.py`):** 10%
* **Uso de `try-except` para errores de archivo:** 10%
* **Generación automática de la fecha con `date.today()`:** 15%
* **Búsqueda por palabra clave:** 15%
* **Eliminación por fecha exacta, incluyendo el caso sin coincidencias:** 15%
* **Validación de las entradas del usuario (menú):** 5%
* **Menú claro y legible:** 5%
* **Comentarios claros:** 5%
# Ejercicios `Manejo de archivos`
### 1. Suma y promedio
Crear un programa que lea un archivo de texto llamado `numeros.txt` que contiene un número por línea.
El programa debe:

- Leer los números.
- Imprimir la suma total y el promedio.
- Detectar y manejar errores:
  - Si el archivo no existe, mostrar un mensaje.
  - Si hay contenido no numérico, ignorar esas líneas y continuar.
  - Si el archivo está vacío o no existe, generarlo con 10 números aleatorios entre 1 y 100.
- Incluir una función que calcule la suma de los números.

---

### 2. Lista de compras  
Crear un programa que lea un archivo de texto llamado `compras.txt`, donde cada línea representa un producto.  
El programa debe:

- Leer todos los productos y mostrarlos enumerados.
- Permitir al usuario agregar un nuevo producto ingresado por teclado.
- Guardar el nuevo producto al final del archivo.
- Detectar y manejar errores:
  - Si el archivo no existe, crearlo vacío.

---

### 3. Contador de líneas de código
Crear un programa que lea un archivo `.py` llamado `codigo.py` y cuente:

- Cuántas líneas totales tiene.
- Cuántas líneas están comentadas (inician con `#`).
- Cuántas líneas están vacías.
- Detectar y manejar errores:
  - Si el archivo no existe, mostrar un mensaje.

---

### 4. Conversión CSV a lista ordenada  
Crear un programa que lea un archivo CSV llamado `estudiantes.csv` con el formato:  
`nombre,nota` (una por línea).  
El programa debe:

- Leer los datos y ordenarlos de mayor a menor según la nota.
- Mostrar el listado ordenado con posición, nombre y nota.
- Guardar el resultado en un nuevo archivo llamado `estudiantes_ordenado.txt`.
- Detectar y manejar errores:
  - Si el archivo no existe, mostrar un mensaje de error.

---

### 5. Estadísticas de ventas  
Crear un programa que lea un archivo `ventas.txt` con registros de ventas por línea en el formato:  
`producto,cantidad,precio_unitario`.  
El programa debe:

- Calcular y mostrar la venta total de cada producto.
- Mostrar total general.
- Generar un nuevo archivo llamado `resumen.txt` con los resultados.
- Detectar y manejar errores:
  - Validar que los datos numéricos sean correctos.
  - Si el archivo no existe, mostrar un mensaje de error.
# Ejercicios `Múltiples Archivos`
### 1. Conversión de medidas (simple)
Crear un módulo llamado `medidas.py` que tenga funciones para convertir metros a centímetros y kilómetros.
El programa principal debe:

- Pedir al usuario una distancia en metros.  
- Usar el módulo para convertirla a centímetros y kilómetros.  
- Mostrar los resultados.  

**Requisitos:**
- Si el usuario ingresa un valor no numérico, mostrar un mensaje de error.  
- El módulo debe contener al menos dos funciones: `metros_a_centimetros()` y `metros_a_kilometros()`.  

---

### 2. Generador de contraseñas (simple)
Crear un módulo llamado `passwords.py` que contenga una función para generar contraseñas aleatorias.
El programa principal debe:

- Pedir al usuario la longitud de la contraseña.  
- Usar el módulo para generar una contraseña con letras, números y caracteres especiales.  
- Mostrar la contraseña generada.  

**Requisitos:**
- Si el usuario ingresa un valor menor a 4, mostrar un mensaje de error.  
- La función del módulo debe llamarse `generar_password(longitud)`.  

---

### 3. Gestión de notas
Crear un módulo llamado `notas.py` que contenga funciones para:  
1. Agregar una nota a una lista.  
2. Calcular el promedio de las notas.  
3. Mostrar la nota más alta y la más baja.

El programa principal debe:
- Pedir al usuario ingresar varias notas (entre 0 y 100) hasta que escriba "fin".  
- Usar el módulo para calcular y mostrar:  
  - Promedio de las notas.  
  - Nota más alta y más baja.  

**Requisitos:**
- Manejar entradas no numéricas ignorándolas con un mensaje.  
- Si no se ingresan notas, mostrar un mensaje y salir.  

---

### 4. Librería de utilidades de cadenas

Crear un módulo llamado `utilidades_texto.py` con funciones para:  
1. Contar cuántas vocales tiene un texto.  
2. Invertir el texto.  
El programa principal debe:
- Pedir al usuario un texto.  
- Mostrar el número de vocales.  
- Mostrar el texto invertido.  

**Requisitos:**
- El módulo debe contener al menos dos funciones bien definidas.  

---

### 5. Tienda en línea con inventario desde archivo
Crear un módulo llamado `inventario.py` que contenga funciones para:  
1. Cargar los productos disponibles desde un archivo `inventario.txt` (almacenados en formato `producto,precio`).  
2. Calcular el total de la compra.

El programa principal debe:
- Cargar el inventario desde el archivo al iniciar.  
- Mostrar el inventario inicial.
- Permitir al usuario agregar productos al carrito escribiendo su nombre.  
- Cuando el usuario escriba "pagar", mostrar el total y salir.  

**Requisitos:**
- Si el usuario ingresa un producto que no existe, mostrar un mensaje.
- Si el archivo `inventario.txt` no existe, mostrar un mensaje de error.
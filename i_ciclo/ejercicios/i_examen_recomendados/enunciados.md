# Ejercicios Recomendados

### 1. Registro de Productos y Precios

Solicita al usuario ingresar el nombre y el precio de **3 productos**.  
Luego muestra:

- Lista de nombres y lista de precios
- Precio total de la compra
- Nombre del producto más caro

**Requisitos:**
- Usar `try-except` al ingresar el precio. Si ocurre un error (`ValueError`), asignar `precio = 0.0`.

**Ejemplo esperado de ejecución:**
```
Producto 1
Nombre: Café
Precio: 2500

Producto 2
Nombre: Pan
Precio: mil
Error: precio no válido, se asigna 0.0.

Producto 3
Nombre: Leche
Precio: 1200

Resultados
Nombres: ['Café', 'Pan', 'Leche']
Precios: [2500.0, 0.0, 1200.0]
Precio total: 3700.0
Producto más caro: Café
```

---

### 2. Transformación de Mensajes

Solicita al usuario ingresar 3 mensajes de texto.  
Luego:

- Muestra la lista original
- Muestra cada mensaje convertido a mayúsculas
- Muestra la cantidad de caracteres de cada mensaje

**Ejemplo esperado de ejecución:**
```
Mensaje 1: Hola mundo
Mensaje 2: Python es funcional
Mensaje 3: Probando

Resultados
Originales: ['Hola mundo', 'Python es funcional', 'Probando']
Mayúsculas: ['HOLA MUNDO', 'PYTHON ES FUNCIONAL', 'PROBANDO']
Longitudes: [10, 19, 8]
```

---

### 3. Notas de Estudiantes con Filtro

Solicita al usuario ingresar el nombre y la nota (entera) de **3 estudiantes**.  
Luego:

- Muestra las listas de nombres y notas
- Muestra la nota más baja
- Muestra el promedio de notas
- Muestra los nombres de los estudiantes que aprobaron (nota >= 70)

**Requisitos:**
- Usar `try-except` al ingresar la nota. Si hay error, asignar `nota = 0`.
- Si ningún estudiante aprueba, mostrar "Ninguno aprobó".

**Ejemplo esperado de ejecución:**
```
Estudiante 1
Nombre: Ana
Nota: 85

Estudiante 2
Nombre: Carlos
Nota: cuarenta
Error: nota no válida, se asigna 0.

Estudiante 3
Nombre: María
Nota: 58

Resultados
Nombres: ['Ana', 'Carlos', 'María']
Notas: [85, 0, 58]
Nota más baja: 0
Promedio: 47.67
Aprobados: ['Ana']
```

 <!-- INCUYEN OTROS TEMAS
### Ejercicio 1: Evaluación de Rendimiento Académico

Solicita al usuario ingresar los nombres y notas de varios estudiantes.
Luego muestra:

- Lista de estudiantes con su nota
- Promedio general del grupo
- Cuántos estudiantes aprobaron (nota >= 70)
- Cuál fue el mejor y el peor estudiante

**Requisitos:**

- Usar dos listas: una para nombres y otra para notas
- Usar funciones como `sum()`, `max()`, `min()`

**Ejemplo esperado de ejecución:**
```
¿Cuántos estudiantes desea registrar?: 3
Nombre del estudiante 1: Ana
Nota del estudiante 1: 80
Nombre del estudiante 2: Luis
Nota del estudiante 2: 65
Nombre del estudiante 3: Marta
Nota del estudiante 3: 92

Notas ingresadas:
Ana : 80
Luis : 65
Marta : 92
Promedio: 79.0
Aprobados: 2
Mejor estudiante: Marta (92)
Peor estudiante: Luis (65)
```

---

### Ejercicio 2: Clasificador de Palabras

Solicita al usuario una lista de palabras (separadas por coma).
Luego:

- Crea una lista con palabras que empiezan con vocal
- Otra con palabras que empiezan con consonante
- Muestra la cantidad de palabras en cada categoría y sus listas respectivas

**Ejemplo esperado de ejecución:**
```
Ingrese una lista de palabras separadas por coma: árbol, sol, elefante, casa, iglú, nube

Palabras que empiezan con vocal: ['árbol', 'elefante', 'iglú']
Cantidad con vocal: 3
Palabras que empiezan con consonante: ['sol', 'casa', 'nube']
Cantidad con consonante: 3
```

---

### Ejercicio 3: Análisis de Precios
Pide al usuario que ingrese una lista de precios de productos. Luego:

- Calcula el total de la compra
- Muestra cuántos productos son mayores a 1000 colones
- Muestra el precio más caro y más barato
- Aplica un 10% de descuento si el total supera los 5000 colones

**Requisitos:**

- Validar que los precios sean positivos, si alguno no lo es lo ignora
- Usar listas y funciones como `sum()`, `max()`, `min()`

**Ejemplo esperado de ejecución:**
```
Ingrese los precios de los productos separados por coma: 1200, 300, 5200, 1500

Total antes de descuento: 8200
Productos mayores a 1000 colones: 3
Precio más caro: 5200
Precio más barato: 300
Total con descuento:
-->
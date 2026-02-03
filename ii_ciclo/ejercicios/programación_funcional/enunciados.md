# Ejercicios `Programación Funcional`

### 1. Filtrado y transformación de datos

Crear una lista con los números del 1 a `n`.
El programa debe:

* Usar `filter()` para quedarse solo con los números impares.
* Usar `map()` para elevarlos al cuadrado.
* Mostrar el resultado.

**Ejemplo esperado:**
```
n = 15
[1, 9, 25, 49, 81, 121, 169, 225]
```

---

### 2. Ordenamiento y comprensión de listas

Dada una lista de diccionarios que representan estudiantes:

```python
estudiantes = [
    {'nombre': 'Ana', 'nota': 85},
    {'nombre': 'Maria', 'nota': 92},
    {'nombre': 'Luis', 'nota': 78},
    {'nombre': 'Pedro', 'nota': 90}
]
```

El programa debe:

* Usar `filter()` para obtener solo los que tienen nota ≥ 80.
* Usar `sorted()` para ordenarlos por nota descendente.
* Usar una **comprensión de listas** para crear una lista solo con los nombres en mayúsculas.

**Salida esperada:**
```
['MARIA', 'PEDRO', 'ANA']
```

---

### 3. POO + programación funcional

Crea una clase `Producto` con los atributos `nombre` y `precio`.

El programa debe:

1. Crear una lista de varios objetos `Producto`.
```python
productos = [
    Producto('Monitor', 150000),
    Producto('Teclado', 90000),
    Producto('Mouse', 50000),
    Producto('Laptop', 800000)
]
```

2. Usar `map()` para aplicar un **descuento del 10%** a todos los precios.
3. Usar `filter()` para quedarse solo con los productos cuyo precio final sea **mayor a 100 000**.
4. Usar `sorted()` para ordenarlos de mayor a menor precio.
5. Mostrar los nombres y precios finales usando una comprensión de listas.

**Salida esperada:**
```
['Laptop: 720000.00', 'Monitor: 135000.00']
```
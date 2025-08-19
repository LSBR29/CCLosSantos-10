# Ejercicios `Complejidad Algorítmica`
### 1.
Se tienen las siguientes funciones que realizan cálculos distintos.

Determine la complejidad temporal de ambos algoritmos.
```python
def f1(lista):
    total = 0
    for i in range(len(lista)):
        for j in range(len(lista) // 3):
            total += lista[i] * lista[j]
    return total
```


```python
def f2(lista):
    total = 0
    for i in range(len(lista)):
        for j in range(len(lista) // 3):
            for k in range(len(lista) // 2):
                total += lista[i] * lista[j] * lista[k]
    return total
```

**Respuesta:**
* `f1` → O(n²)
* `f2` → O(n³)

**Explicación:**

En `f1`, el bucle externo recorre `n` veces y el interno recorre `n/3 ≈ n` veces, por lo que en total se hacen `n × n = n²` operaciones.

En `f2`, hay tres bucles anidados: `n × (n/3) × (n/2) ≈ n³`. Por lo tanto, las complejidades son O(n²) y O(n³).

---

### 2.
Un número perfecto es aquel cuya suma de sus factores propios es igual al número. Ejemplo: 6 (1 + 2 + 3 = 6) y 28 (1 + 2 + 4 + 7 + 14 = 28).

Determine la complejidad temporal del siguiente algortimo:
```python
def esPerfecto(n):
    s = 1
    i = 2
    while i * i < n:
        if n % i == 0:
            s += i + n // i
        i += 1
        i += 1
        if i * i == n:
            s += i
            s += i
    return s == n
```

**Respuesta:** O(√n)

**Explicación:**

Este código solo recorre divisores hasta la raíz cuadrada de `n`. Cada vez que encuentra un divisor, añade también el cociente `n//i`. De esta forma evita recorrer hasta `n/2` o `n`, lo que sería mucho más costoso.

---

### 3.
Determine la complejidad temporal y espacial del siguiente algortimo:
Determine la complejidad temporal y espacial del siguiente algortimo:
```python
def suma_elementos(lista):
    total = 0
    for x in lista:
        total += x
    return total
```

**Respuesta:** Temporal O(n), Espacial O(1)

**Explicación:**

El bucle recorre toda la lista, por lo que tarda O(n).
En cuanto a espacio, solo usa la variable `total` sin estructuras adicionales, así que es O(1). El espacio ocupado por la lista no cuenta, pues es entrada (parámetro de la función) y no ocupa memoria extra generada por el algoritmo.

---

### 4.
Determine la complejidad temporal y espacial del siguiente algortimo:
### 4.
Determine la complejidad temporal y espacial del siguiente algortimo:
```python
def suma_matrices(A, B):
    filas = len(A)
    columnas = len(A[0])
    C = [[0] * columnas for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            C[i][j] = A[i][j] + B[i][j]
    return C
```
**Respuesta:** Temporal O(n²), Espacial O(n²)

**Explicación:**

La matriz tiene tamaño `n × n`. Los dos bucles recorren todos sus elementos → O(n²).
Además, se crea una nueva matriz `C` del mismo tamaño que A y B, ocupando O(n²) memoria adicional.

---

### 5.
Determine la complejidad temporal y espacial del siguiente algortimo:
### 5.
Determine la complejidad temporal y espacial del siguiente algortimo:
```python
def buscar_en_matriz(matriz, objetivo):
    for fila in matriz:
        if objetivo in fila:
            return True
    return False
```
Se puede suponer que la matriz es de tamaño `n × n`.

**Respuesta:** Temporal O(n²), Espacial O(1)

**Explicación:**

El peor caso es cuando el `objetivo` no está en la matriz, por lo que se revisan todas las filas. La operación `if objetivo in fila` cuesta O(n), y hay `n` filas → O(n²).
En cuanto a memoria, no se crean estructuras adicionales; se usan los parámetros pasados a la función → O(1).

---

### 6.
Determine la complejidad espacial del siguiente algortimo:
```python
def suma_lista(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total
```

**Respuesta:** O(1)

**Explicación:**

El algoritmo solo usa una variable `total` (constante en memoria), sin importar el tamaño de la lista. La lista ya está dada como entrada, por lo tanto no cuenta como espacio adicional.

---

### 7.
Determine la complejidad espacial del siguiente algortimo:
```python
def cuadrados(n):
    resultado = []
    for i in range(n):
        resultado.append(i*i)
    return resultado
```

**Respuesta:** O(n)

**Explicación:**

La lista `resultado` crece proporcionalmente a `n`, almacenando `n` valores.

---

### 8.
Determine la complejidad espacial del siguiente algortimo:
```python
def duplicados(lista):
    conjunto = set()
    for elemento in lista:
        if elemento in conjunto:
            return True
        conjunto.add(elemento)
    return False
```

**Respuesta:** O(n)

**Explicación:**

El conjunto `conjunto` puede llegar a almacenar todos los elementos de la lista en el peor caso (cuando no hay duplicados). Por eso, la memoria usada es proporcional al tamaño de la lista.

---

### 9.
Determine la complejidad espacial del siguiente algortimo:
```python
def constante(n):
    return n*n + 100
```

**Respuesta:** O(1)

**Explicación:**

Sin importar el valor de `n`, no se crean nuevas variables que ocupen un espacio. La complejidad espacial es constante.
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
    if n < 2:
        return False
    s = 1
    i = 2

    while i * i <= n:
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i

        i += 1

    return s == n
```

**Respuesta:** O(√n)

**Explicación:**

Este código solo recorre divisores hasta la raíz cuadrada de `n`. Cada vez que encuentra un divisor, añade también el cociente `n//i`. De esta forma evita recorrer hasta `n/2` o `n`, lo que sería mucho más costoso.

---

### 3.
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
Determine la complejidad temporal del siguiente algortimo:
```python
def buscar_en_matriz(matriz, objetivo):
    for fila in matriz:
        if objetivo in fila:
            return True
    return False
```
Se puede suponer que la matriz es de tamaño `n × n`.

**Respuesta:** Temporal O(n²)

**Explicación:**

El peor caso es cuando el `objetivo` no está en la matriz, por lo que se revisan todas las filas. La operación `if objetivo in fila` cuesta O(n), y hay `n` filas → O(n²).

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

---

### 10.
Un algoritmo recibe un número entero `n` y devuelve `True` si es par y `False` si es impar. Para ello, simplemente calcula el residuo de la división entre 2 y compara con 0.

**Respuesta:** O(1)

**Explicación:**
El tiempo de ejecución es constante, independientemente del valor de `n`. No hay bucles ni llamadas recursivas; solo se ejecuta un número fijo de instrucciones.

---

### 11.
Un algoritmo recibe una lista de números y calcula el promedio de todos sus elementos. Para ello, recorre la lista una sola vez sumando cada elemento y, al final, divide la suma total entre la cantidad de elementos.

¿Complejidad Temporal?

Recibe lista -> O(n)
Recorre la lista -> O(n)
Suma cada elemento -> O(1)
Divide la suma entre cantidad -> O(1)
                O(n + n + 1 + 1) = O(2n + 2) = O(2n) = O(n)








**Respuesta:** O(n)

**Explicación:**
El algoritmo debe visitar cada elemento de la lista exactamente una vez para realizar la suma. Si la lista tiene `n` elementos, el número de operaciones crece linealmente con `n`.

---

### 12.
Un algoritmo recibe dos listas de números de igual longitud `n` y devuelve una nueva lista donde cada posición `i` contiene la suma de los elementos de ambas listas en esa posición. Para ello, recorre ambas listas simultáneamente con un solo bucle que va desde `0` hasta `n-1`.

**Respuesta:** O(n)

**Explicación:**
Aunque hay dos listas de entrada, el bucle se ejecuta `n` veces (una por cada índice). En cada iteración se realizan operaciones de tiempo constante, por lo que la complejidad temporal es lineal respecto al tamaño de las listas.

---

### 15.
Un algoritmo recibe una lista ordenada de números y un valor objetivo. Para encontrar la posición del objetivo, utiliza la técnica de búsqueda binaria: compara el objetivo con el elemento central de la lista; si son iguales, termina; si el objetivo es menor, repite el proceso en la mitad izquierda; si es mayor, en la mitad derecha. En cada paso, el tamaño del problema se reduce a la mitad.

**Respuesta:** O(log n)

**Explicación:**
Cada iteración divide el tamaño de la lista a la mitad. El número de iteraciones necesarias para reducir la lista a un solo elemento es `log₂(n)`. Por lo tanto, la complejidad temporal es logarítmica respecto a `n`.

---

### 16.
Determine la complejidad temporal del siguiente algoritmo:
```python
def acceso(lista):
    if len(lista) > 0:
        return lista[0] + lista[-1]
    return 0
```

**Respuesta:** O(1)

**Explicación:**
El algoritmo siempre accede únicamente a la primera y última posición de la lista, sin importar cuántos elementos tenga. No hay bucles ni recursión; las operaciones son de tiempo constante.

---

### 17.
Determine la complejidad temporal del siguiente algoritmo:
```python
def maximo_lista(lista):
    max_val = lista[0]
    for num in lista:
        if num > max_val:
            max_val = num
    return max_val
```

**Respuesta:** O(n)

**Explicación:**
El bucle `for` recorre cada uno de los `n` elementos de la lista exactamente una vez, realizando una comparación por cada elemento. Por lo tanto, el tiempo de ejecución crece de forma lineal con el tamaño de la entrada.

---

### 18.
Determine la complejidad temporal del siguiente algoritmo:
```python
def contar_pares_con_suma(lista, objetivo):
    contador = 0
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == objetivo:
                contador += 1
    return contador
```

**Respuesta:** O(n²)

**Explicación:**
El algoritmo utiliza dos bucles anidados. El bucle externo recorre `n` elementos y el interno, en promedio, recorre `n/2` elementos. Al estar anidados, el número total de iteraciones es proporcional a `n × n = n²`.

---

### 19.
Determine la complejidad temporal del siguiente algoritmo:
```python
def existe_triplete_suma_cero(lista):
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if lista[i] + lista[j] + lista[k] == 0:
                    return True
    return False
```

**Respuesta:** O(n³)

**Explicación:**
Hay tres bucles anidados, cada uno dependiente del tamaño `n` de la lista. El número de combinaciones de tripletes que se evalúan es del orden de `n × n × n = n³`, por lo que la complejidad temporal es cúbica.

---

### 20.
Determine la complejidad temporal del siguiente algoritmo:
```python
def fibonacc(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

**Respuesta:** O(2ⁿ)

**Explicación:**
Cada llamada a la función genera dos llamadas recursivas adicionales, formando un árbol binario de altura `n`. El número total de llamadas crece exponencialmente, aproximadamente `2ⁿ`. Por esta razón, el algoritmo es extremadamente ineficiente para valores grandes de `n`.

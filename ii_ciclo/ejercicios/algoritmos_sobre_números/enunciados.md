# Ejercicios `Algoritmos sobre Números`

---

### 1.
Liam busca el máximo de la lista `[(1,1), (1,2), (2,2), (1,3), (0,4), (3,3)]`, compuesta por pares ordenados. Se dice que un par `P` es mayor que otro par `Q` si:
* la suma de los elementos de `P` es mayor que la de `Q`, **o**
* las sumas son iguales, pero el primer elemento de `P` es mayor que el de `Q`.

Liam empieza definiendo que el máximo es el par `(-1, -1)` y revisa la lista posición por posición, de izquierda a derecha, contando cuántas veces encuentra un nuevo máximo. ¿Cuántas veces encontró un nuevo máximo?

* A. 1
* B. 2
* C. 3
* D. 4
* E. 5

**Respuesta:** D. 4

**Explicación:**

Esta pregunta es una versión del algoritmo de la teoría para encontrar el máximo: se recorre el arreglo una vez, comparando cada elemento contra el mejor visto hasta el momento, y actualizando cuando se encuentra algo mejor.

Siguiendo la comparación:

| Par revisado | suma | ¿Nuevo máximo? | Máximo actual |
|---|---|---|---|
| (1,1) | 2 | sí (2 > -2) | (1,1) |
| (1,2) | 3 | sí (3 > 2) | (1,2) |
| (2,2) | 4 | sí (4 > 3) | (2,2) |
| (1,3) | 4 | no (suma igual, 1 < 2) | (2,2) |
| (0,4) | 4 | no (suma igual, 0 < 2) | (2,2) |
| (3,3) | 6 | sí (6 > 4) | (3,3) |

Hubo **4** actualizaciones.

---

### 2.
Se tiene la siguiente lista de números `a = [-31, 65, -33, -15]`. Sea `b` la lista que se obtiene al calcular la suma de prefijos de `a`. Sea `c` la lista que se obtiene al calcular la suma de prefijos de `b`. ¿Cuál es el elemento máximo de la lista `c`?

* A. -10
* B. 3
* C. 4
* D. 34
* E. 65

**Respuesta:** C. 4

**Explicación:**

Primero se calcula `b`, la suma de prefijos de `a`:

```python
a = [-31, 65, -33, -15]
b = [a[0]]
for i in range(1, len(a)):
    b.append(b[-1] + a[i])
# b = [-31, 34, 1, -14]
```

Luego se calcula `c`, la suma de prefijos de `b`:

```python
c = [b[0]]
for i in range(1, len(b)):
    c.append(c[-1] + b[i])
# c = [-31, 3, 4, -10]
```

El máximo de `c` es **4**. 

---

### 3.
Sea `P` el arreglo de sumas de prefijo de cierto arreglo `A`, donde `P[i] = A[0] + A[1] + ... + A[i]`:

```
P = [3, 4, 8, 9, 14, 23, 25, 31]
```

Usando únicamente `P`, ¿cuál es la suma de los elementos de `A` en el rango `[3, 6]` (inclusive en ambos extremos)?

* A. 15
* B. 21
* C. 22
* D. 16
* E. 17

**Respuesta:** E. 17

**Explicación:**

La suma de un subarreglo entre los índices `i` y `j` se calcula como `P[j] - P[i-1]`. Aquí `i=3` y `j=6`, así que:

$$P[6] - P[2] = 25 - 8 = 17$$

Se puede confirmar reconstruyendo `A` a partir de `P` y sumando directamente las posiciones 3 a 6:

```python
P = [3, 4, 8, 9, 14, 23, 25, 31]
A = [P[0]] + [P[i]-P[i-1] for i in range(1, len(P))]
# A = [3, 1, 4, 1, 5, 9, 2, 6]
print(sum(A[3:7]))  # 17
```

---

### 4.
En una búsqueda binaria estándar, sobre un arreglo ordenado, ¿cuál elemento es el primero que debe ser comparado?

* A. El promedio de todos los elementos
* B. Un elemento aleatorio
* C. El primer elemento
* D. El elemento del medio
* E. El último elemento

**Respuesta:** D. El elemento del medio

**Explicación:**

La búsqueda binaria revisa primero el valor de la mitad del arreglo (`medio = (izquierda + derecha) // 2`), y según si ese valor es mayor, menor o igual al buscado, descarta una de las dos mitades y repite el proceso sobre la mitad restante.

---

### 5.
Se calcula el MCD de 60 y 96 dividiendo repetidamente ambos números entre sus factores primos comunes (2, 2 y 3), hasta que ya no comparten factores, y se multiplican los factores usados para obtener el resultado: 2×2×3 = 12. ¿Cuál es un algoritmo **alternativo** para obtener el mismo resultado?

* A. Algoritmo de factorización prima
* C. Algoritmo de Euclides
* D. Algoritmo de la división y residuo
* E. Criba de Eratóstenes

**Respuesta:** C. Algoritmo de Euclides

**Explicación:**

El método (dividir ambos números por sus factores primos comunes sucesivamente) es en sí una forma de "factorización prima", así que esa opción sería redundante con el propio método mostrado, no una alternativa distinta. Una forma genuinamente distinta de llegar al mismo resultado es el **algoritmo de Euclides**, que no requiere factorizar nada.

---

### 6.
¿Cuál de los siguientes códigos calcula el máximo común divisor de dos números de forma **más eficiente**?

* A.
```python
def gcd(a, b):
    result = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            result = i
    return result
```
* B.
```python
def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
```
* D.
```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
```
* E.
```python
def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1
```

**Respuesta:** D 

**Explicación:**

Las opciones A y E son de fuerza bruta: prueban divisores uno por uno. La opción B es el algoritmo de Euclides por **restas sucesivas**, correcto pero potencialmente muy lento cuando un número es mucho más grande que el otro (por ejemplo, `mcd(1000000, 3)` tardaría cerca de 333,333 restas). La opción D es el **algoritmo de Euclides con residuo** (`mcd(a,b) = mcd(b, a mod b)`), el mismo de la teoría, que reduce los números mucho más rápido (complejidad O(log(min(a,b)))).

---

### 7.
Sean `a`, `e`, `n`, `p` cuatro números enteros, tal que `n = aᵉ mod p`. Al utilizar exponenciación binaria para calcular `n`, ¿cuál es la complejidad temporal?

* A. O(log(a))
* B. O(log(n·p))
* C. O(log(p))
* D. O(log(e))
* E. O(log(n))

**Respuesta:** D. O(log(e))

**Explicación:**

Como se explica en la teoría, la exponenciación binaria divide el problema a la mitad en función del **exponente** (`b` en la notación de la teoría, `e` en esta pregunta): en cada paso se calcula `a^(e/2)` y se combina el resultado, reduciendo el exponente a la mitad cada vez. El número de veces que se puede dividir `e` entre 2 es `O(log(e))`. La base `a`, el módulo `p` y el resultado `n` no influyen en cuántos pasos toma el algoritmo.

---

### 8.
¿Cuál de los siguientes algoritmos es más eficiente para calcular `aᵇ` (donde `a` y `b` son enteros y `b` es positivo) en términos de complejidad temporal?

* A. Multiplicar `a` por sí mismo `b` veces.
* B. Usar un bucle que multiplique `a` por sí mismo `b/2` veces y luego multiplique el resultado por sí mismo.
* C. Usar una búsqueda binaria para encontrar el valor de `ab`.
* D. Aplicar la exponenciación binaria, que reduce el problema en cada paso dividiendo el exponente a la mitad y usando las propiedades de los números pares e impares.
* E. Usar una tabla de búsqueda con los valores de `ab` precomputados para todos los valores posibles de `a` y `b`.

**Respuesta:** D

---

### 9.
La exponenciación binaria (exponenciación rápida) permite calcular `aᵉ` mucho más rápido que multiplicar `a` por sí mismo `e` veces. ¿En qué idea se basa principalmente?

* A. En factorizar el exponente en sus números primos.
* B. En guardar en memoria los resultados intermedios para no recalcularlos.
* C. En usar una igualdad algebraica para reemplazar la potencia por una sola multiplicación.
* D. En dividir la base entre dos en cada paso del cálculo.
* E. En elevar la base al cuadrado sucesivamente y combinar las potencias.

**Respuesta:** E

**Explicación:**

La idea central de la exponenciación binaria, según la teoría,.

--- 

### 10.
¿Cuántos números primos hay entre 1 y 20 (ambos inclusive)?

* A. 9
* B. 8
* C. 7
* D. 6
* E. 10

**Respuesta:** B. 8

**Explicación:**

Los números primos entre 1 y 20 son: 2, 3, 5, 7, 11, 13, 17 y 19, en total **8** primos.

```python
def es_primo(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

primos = [i for i in range(1,21) if es_primo(i)]
print(primos, len(primos))  # [2,3,5,7,11,13,17,19] 8
```

---

### 11.
¿Cuál de las siguientes afirmaciones es correcta sobre el test de primalidad que verifica divisores hasta √n?

* A. Requiere conocer los factores primos de `n` de antemano.
* B. Es más rápido para detectar primos que compuestos.
* C. Tiene moderada complejidad computacional debido a que requiere O(√n) operaciones.
* D. Solo funciona cuando `n` es un cuadrado perfecto.
* E. Es probabilístico y requiere muchas ejecuciones.

**Respuesta:** C

**Explicación:**

La teoría indica que "no es necesario probar todos los divisores hasta `n`, basta con revisar hasta √n", lo que da una complejidad O(√n).

---

### 12.
Un número perfecto es aquel cuya suma de sus factores propios (menores que el número) es igual al número — por ejemplo, 6 (1+2+3=6) o 28 (1+2+4+7+14=28). ¿Cuál de los siguientes códigos determina, en el **menor número de pasos**, si un número es perfecto?

* A.
```python
def esPerfecto(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n
```
* B.
```python
def esPerfecto(n):
    s = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            s += i
    return s == n
```
* E.
```python
def esPerfecto(n):
    s = 1
    i = 2
    while i * i < n:
        if n % i == 0:
            s += i + n // i
        i += 1
    if i * i == n:
        s += i
    return s == n
```

**Respuesta:** E

**Explicación:**

Las opciones A y B son correctas (dan el resultado correcto en números perfectos y no perfectos), pero recorren todos los divisores desde 1 hasta `n` o `n/2`, es decir, complejidad **O(n)**. La opción E aplica la misma idea del test de primalidad O(√n) de la teoría: en vez de revisar todos los divisores, solo revisa hasta `√n`, y por cada divisor `i` encontrado suma también su pareja `n/i` (porque los divisores vienen en pares: si `i` divide a `n`, también lo hace `n/i`), tratando aparte el caso de la raíz cuadrada exacta.

---

### 13.
¿Cuál es el principal factor que limita la eficiencia de la Criba de Eratóstenes al encontrar todos los primos desde 1 hasta un número muy grande?

* A. Consume O(n·log(n)) en espacio
* B. Es O(n²) en su ejecución
* C. Consume O(n) en espacio
* D. La cantidad de primos por debajo de n es muy baja
* E. Requiere muchos ciclos anidados (con for o while)

**Respuesta:** C. Consume O(n) en espacio

**Explicación:**

Como se describe en la teoría, la criba construye una lista `es_primo` de tamaño `n+1` para marcar cada número — esto requiere **memoria proporcional a n**, es decir, O(n) en espacio.

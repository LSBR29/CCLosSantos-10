# Ejercicios `Complejidad Algorítmica`
### 1. 
Se tienen las siguientes funciones que realizan cálculos distintos:
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

La complejidad temporal de las funciones `f1` y `f2` son, respectivamente:

**A. *O*($n^2$) y *O*($n^3$)**

B. *O*($n^3$) y *O*($n^{2/3}$)

C. *O*($n^3$) y *O*($n^{3/2}$)  

D. *O*($n^2$) y *O*($n^6$)  

E. *O*($n^6$) y *O*($n^2$)

---

### 2.
Un número perfecto es aquel cuya suma de sus factores propios es igual al
número. Por ejemplo, el número 6 es perfecto, pues sus factores propios
(menores que el número) son: 1, 2, 3 y 1 + 2 + 3 = 6. Otro número perfecto es
28, donde sus factores propios son 1, 2, 4, 7, 14 y 1 + 2 + 4 + 7 + 14 = 28.

¿Cuál de los siguientes códigos determina, en el menor número de pasos, si
un número es perfecto?

A. 
```python
def esPerfecto(n):
    s = 0
    for i in range(1, n):
        if s % i == 0:
            s += i
        return s == n
```

**B.**
```python
def esPerfecto(n):
    s = 1
    i = 2
    while i * i < n:
        if n % i == 0:
            s += i + n // i
            i+=1
        if i * i == n:
            s+=i
    return s == n
```

C. 
```python
def esPerfecto(n):
    s = 0
    for i in range(1, n // 2 + 1):
        if s % i == 0:
            s += i
    return s < n
```

### 3.
Analiza el siguiente código y determina la complejidad temporal y espacial en el peor caso, respectivamente:

```python
def suma_elementos(lista):
    total = 0
    for x in lista:
        total += x
    return total
```
A. O($n$) y O($1$)

B. O($n^2$) y O($1$)

**C. O($n$) y O($n$)**

D. O($1$) y O($1$)

E. O($n^2$) y O($n$)

### 4. 
Analiza el siguiente código y determina la complejidad temporal y espacial en el peor caso:

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
**A. O($n^2$) y O($n^2$)**

B. O($n^2$) y O($1$)

C. O($n$) y O($n^2$)

D. O($n^3$) y O($n^2$)

E. O($n^3$) y O($n^3$)

### 5. 
Analiza el siguiente código y determina la complejidad temporal y espacial en el peor caso:

```python
def buscar_en_matriz(matriz, objetivo):
    for fila in matriz:
        if objetivo in fila:
            return True
    return False
```
Supón que la matriz es de tamaño $n \times n$.

A. O($n$) y O($1$)

**B. O($n^2$) y O($1$)**

C. O($n \log n$) y O($1$)

D. O($n^2$) y O($n$)

E. O($n \log n$) y O($n$)
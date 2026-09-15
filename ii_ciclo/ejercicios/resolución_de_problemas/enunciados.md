# Ejercicios `Resolución de Problemas`

---

### 1.
Se tiene el siguiente código:
```python
x = 900
while x > 0:
    x //= 2
    if x % 2 == 0:
        print("Hola")
```
¿Cuántas veces se imprime la palabra "Hola"?

* A. 10
* B. 9
* C. 6
* D. 5
* E. 0

**Respuesta:** C. 6 

**Explicación:**

Siguiendo el ciclo paso a paso, dividiendo `x` entre 2 en cada vuelta y revisando la paridad del resultado:

| x antes | x//=2 → x | ¿par? | ¿imprime? |
|---|---|---|---|
| 900 | 450 | sí | Hola (1) |
| 450 | 225 | no | — |
| 225 | 112 | sí | Hola (2) |
| 112 | 56 | sí | Hola (3) |
| 56 | 28 | sí | Hola (4) |
| 28 | 14 | sí | Hola (5) |
| 14 | 7 | no | — |
| 7 | 3 | no | — |
| 3 | 1 | no | — |
| 1 | 0 | sí | Hola (6) |

Con `x = 0` el ciclo se detiene (`0 > 0` es falso). En total se imprime "Hola" 6 veces. Uso de ciclos: revisar cada paso para tomar una decisión (aquí, si imprimir o no).

---

### 2.
Se tiene el siguiente código:
```python
x = 10
while x > 0:
    x -= 3
print(x)
```
¿Qué valor imprime el programa al finalizar?

* A. -2
* B. 1
* C. 0
* D. -3
* E. -1

**Respuesta:** A. -2 

**Explicación:**

Siguiendo  `x`: 10 → 7 → 4 → 1 → -2. En cada paso se revisa la condición `x > 0` antes de restar: con `x = 1` la condición es verdadera (1 > 0), así que se ejecuta una vuelta más, dando `x = -2`. Con `x = -2` la condición ya es falsa y el ciclo termina. El valor final impreso es -2.

---

### 3.
¿Cuántas veces se ejecuta la instrucción de impresión en el siguiente fragmento?
```python
for i in range(1, 5):
    for j in range(i):
        print(i, j)
```

* A. 10
* B. 12
* C. 8
* D. 20
* E. 16

**Respuesta:** A. 10 

**Explicación:**

El ciclo externo recorre `i = 1, 2, 3, 4`. Para cada `i`, el ciclo interno se ejecuta exactamente `i` veces (ya que `range(i)` genera `i` valores). Por lo tanto, el total de impresiones es:

$$1 + 2 + 3 + 4 = 10$$

---

### 4.
Juan tiene un arreglo ordenado con gran cantidad de elementos y utiliza búsqueda binaria para revisar si el número 555 está presente. Durante la primera iteración, el espacio de búsqueda fue el completo. En la segunda iteración, se tuvo un espacio de búsqueda reducido, y así sucesivamente. Su búsqueda duró 10 iteraciones para encontrar el número buscado. ¿Qué fracción del espacio completo representó el espacio de búsqueda durante la séptima iteración?

* A. 1/7
* B. 1/128
* C. 1/14
* D. 1/64
* E. No se puede determinar

**Respuesta:** D. 1/64

**Explicación:**

En cada iteración de una búsqueda binaria, el espacio de búsqueda se reduce a la mitad del anterior:

| Iteración | Fracción del espacio |
|---|---|
| 1 | 1/2^0 = 1 |
| 2 | 1/2^1 = 1/2 |
| 3 | 1/2^2 = 1/4|
| ... | ... |
| 7 | 1/2^6 = 1/64 |

---

### 5.
¿Cuál es el concepto asociado a esta definición: "Consiste en probar todas las combinaciones posibles para encontrar la solución al problema. Es simple pero generalmente ineficiente, y solo es factible para problemas de pequeño tamaño."?

* A. Programación Dinámica
* B. Búsqueda exhaustiva
* C. Backtracking
* D. Búsqueda binaria
* E. Algoritmo Voraz

**Respuesta:** B. Búsqueda exhaustiva

---

### 6.
La mamá de Conner tiene una política particular para darle dinero: de todos los billetes disponibles en su cartera (siempre desordenados), Conner puede tomar una cantidad entera de billetes hasta alcanzar un límite `K`. Su estrategia es tomar siempre el billete de mayor denominación disponible entre los que quedan. El algoritmo de Conner se puede clasificar como:

* A. Programación Dinámica
* B. Divide y Vencerás
* C. Backtracking
* D. Estrategia de búsqueda binaria
* E. Algoritmo Voraz

**Respuesta:** E. Algoritmo Voraz

---

### 7.
Ana y Luis tienen un conjunto de tareas, cada una con una duración y una ganancia, y quieren maximizar la ganancia total dentro de un tiempo límite `T`, ejecutando una tarea a la vez. Proponen la siguiente estrategia: en cada paso, escoger la tarea disponible con mayor ganancia por unidad de tiempo, sin reconsiderar las decisiones ya tomadas. ¿A qué tipo de algoritmo corresponde esta estrategia?

* A. Algoritmo Voraz
* B. Programación Dinámica
* C. Búsqueda Exhaustiva
* D. Backtracking
* E. Divide y Vencerás

**Respuesta:** A. Algoritmo Voraz

---

### 8.
Juan es una persona que se resiste a usar la computadora, así que cada vez que no sabe el significado de una palabra utiliza el diccionario. Su técnica de búsqueda consiste en abrir el diccionario por la mitad y revisar si la palabra buscada está en esa página; si no, determina en qué mitad del espacio restante debería estar la palabra y mueve la búsqueda hacia el centro de esa mitad, repitiendo hasta encontrarla. La técnica que usa Juan se describe mejor como:

* A. Programación Dinámica
* B. Búsqueda exhaustiva
* C. Estrategia basada en ciclos o loops
* D. Backtracking
* E. Divide y Vencerás

**Respuesta:** E. Divide y Vencerás

---

### 9.
Sara ha estado estudiando ajedrez y se encontró con la pregunta de cuáles son todas las maneras posibles de colocar el máximo número de reinas en un tablero de 7×7, tal que ninguna pieza esté en la misma fila, columna o diagonal. Decide crear un programa que pruebe inicialmente todas las formas de colocar las piezas, **descartando** las soluciones parciales que no cumplan el criterio esperado tan pronto se detectan. La estrategia que mejor se ajusta a esta descripción es:

* A. Divide y vencerás
* B. Programación dinámica
* C. Algoritmos voraces
* D. Programación de grafos
* E. Vuelta atrás (Backtracking)

**Respuesta:** E. Vuelta atrás (Backtracking)

---

### 10.
Una posible definición de backtracking (vuelta atrás) es:

* A. Técnica que divide un problema en subproblemas más pequeños, resuelve cada uno por separado y luego combina las soluciones.
* B. Técnica de optimización inspirada en la selección natural, que usa mutación, cruce y selección para generar soluciones nuevas.
* C. Algoritmos que toman decisiones paso a paso eligiendo siempre la opción que parece mejor en ese momento.
* D. Técnica para resolver problemas de decisión incremental, donde se construyen soluciones parcialmente y se abandonan tan pronto se determina que la solución parcial no puede completarse de forma válida. Se usa comúnmente en problemas de búsqueda y optimización.
* E. Técnica que emplea modelos probabilísticos para predecir la mejor solución, ajustando iterativamente probabilidades según la retroalimentación de soluciones anteriores.

**Respuesta:** D

---

### 11.
¿Cuál de los siguientes pares (técnica, característica) es **incorrecto**?

* A. Programación Dinámica — Almacena resultados de subproblemas para evitar recomputación; requiere subestructura óptima y subproblemas solapados.
* B. Divide y Vencerás — Divide el problema en subproblemas independientes, los resuelve recursivamente y combina los resultados.
* C. Backtracking — Recorre sistemáticamente el espacio de soluciones y, gracias a la poda de ramas, garantiza un tiempo de ejecución polinomial en el peor caso.
* D. Búsqueda Exhaustiva — Evalúa todas las posibilidades; garantiza encontrar la solución óptima si existe, pero puede ser muy lenta.
* E. Algoritmo Voraz — En cada paso toma la decisión localmente óptima; no siempre garantiza la solución globalmente óptima.

**Respuesta:** C

---

### 12.
Sean `f(0) = 1` y `f(1) = 3`. Sabiendo que `f(n) = 2 · (f(n-1) + f(n-2))` para todo `n` mayor a 1, ¿cuánto es `f(10)`?

* A. 9136
* B. 1224
* C. 24960
* D. 68192
* E. Es imposible determinarlo, faltan datos

**Respuesta:** C. 24960 

**Explicación:**

Al igual que el ejemplo de Fibonacci de la teoría, la forma más segura de resolver esto es construir un arreglo `dp` que vaya guardando cada valor calculado, para no tener que recalcular subproblemas:

```python
f = [1, 3]
for n in range(2, 11):
    f.append(2 * (f[n-1] + f[n-2]))
print(f[10]) # 24960
```

---

### 13.
Sea `f(0) = 1` y `f(1) = 2`. Sabiendo que `f(n) = f(n-1) + 2 · f(n-2)` para todo `n` mayor a 1, ¿cuánto es `f(10)`?

* A. 2¹⁰
* B. 3¹⁰
* C. 4⁶
* D. 10³
* E. Es imposible determinarlo, faltan datos

**Respuesta:** A. 2¹⁰ (= 1024) 

**Explicación:**

Aplicando el mismo enfoque de memoización que en el ejemplo de Fibonacci:

```python
f = [1, 2]
for n in range(2, 11):
    f.append(f[n-1] + 2*f[n-2])
print(f[10])  # 1024
```

---

### 14.
Se define la siguiente función recursiva: `g(0) = 2`, `g(1) = 5`, `g(n) = 3 · g(n-1) - g(n-2)` para todo `n ≥ 2`. ¿Cuánto vale `g(6)`?

* A. 610
* B. 1215
* C. 233
* D. 13
* E. 2018

**Respuesta:** A. 610 

**Explicación:**

Se calcula guardando cada resultado intermedio (memoización), en lugar de recalcular la recursión desde cero cada vez:

```python
g = [2, 5]
for n in range(2, 7):
    g.append(3*g[n-1] - g[n-2])
print(g[6])  # 610
```

---

### 15.
Se tiene el siguiente código:
```python
def conteo(x, y):
    if x == 0 or y == 0:
        return x + y
    if conocido[(x, y)]:
        return respuesta[(x, y)]
    r = conteo(x - 1, y) + conteo(x, y - 1)
    respuesta[(x, y)] = r
    conocido[(x, y)] = True
    return r
```
El código anterior emplea una técnica conocida como:

* A. Memoización
* B. Iteración
* C. Compilación
* D. Voracidad
* E. Ramificación y poda

**Respuesta:** A. Memoización

**Explicación:**

El código revisa, antes de recalcular, si el resultado para el par `(x, y)` ya fue calculado (`if conocido[(x,y)]`); si es así, lo devuelve directamente en vez de repetir la recursión, y si no, lo calcula, lo guarda en `respuesta[(x,y)]` y marca `conocido[(x,y)] = True`. Esto es exactamente memoización: **guardar las soluciones de subproblemas ya resueltos para no repetir cálculos**.

---

### 16.
Es una técnica de diseño de algoritmos que se basa en resolver problemas dividiéndolos en subproblemas más pequeños, resolviendo cada subproblema **una sola vez** y almacenando su resultado (memoización). Se usa cuando un problema tiene subproblemas superpuestos y subestructura óptima. Esto corresponde con la definición de:

* A. Búsqueda binaria
* B. Backtracking
* C. Divide y Vencerás
* D. Programación dinámica
* E. Algoritmo Voraz

**Respuesta:** D. Programación dinámica

**Explicación:**

La frase "subproblemas superpuestos" es la diferencia frente a "divide y vencerás": en divide y vencerás los subproblemas suelen ser independientes entre sí (como en la búsqueda binaria, donde cada mitad no depende de la otra), mientras que en programación dinámica los mismos subproblemas reaparecen una y otra vez (como `fibonacci(n-2)`, que se necesita tanto para calcular `fibonacci(n-1)` como `fibonacci(n)`), y por eso conviene guardarlos (memoizarlos) en lugar de recalcularlos.

---

### 17.
La programación dinámica mejora la eficiencia de ciertos algoritmos recursivos principalmente porque:

* A. Almacena (memoiza) los resultados de los subproblemas ya resueltos para no volver a calcularlos.
* B. En cada paso elige la opción que parece mejor en ese momento.
* C. Divide el problema en mitades independientes que se resuelven por separado.
* D. Prueba todas las combinaciones posibles y elige la mejor.
* E. Reescribe el algoritmo para eliminar por completo la recursión, lo que reduce el número de operaciones.

**Respuesta:** A

---

### 18.
Se tienen las siguientes funciones:
```python
def f2(a, b):
    return 7 * a + 5 * b

def f1(a, b):
    return f2(a, b) * f2(b, a)

def f3(a, b):
    return f1(a + 2, b + 2) * 2 + 4 * a + b
```
Si se evalúa `f3(11, 17)`, se obtiene el resultado equivalente a:

* A. ((7·11 + 5·17) · (7·17 + 5·11)) · 2 + 4·11 + 17
* B. ((7·13 + 5·19) · (7·13 + 5·19)) · 2 + 4·11 + 17
* C. ((7·13 + 5·19) · (7·19 + 5·13)) · 2 + 4·11 + 17
* D. ((7·19 + 5·13) · (7·19 + 5·13)) · 2 + 4·11 + 17
* E. ((7·11 + 5·17) · (7·17 + 5·11)) · 2 + 4·17 + 11

**Respuesta:** C 
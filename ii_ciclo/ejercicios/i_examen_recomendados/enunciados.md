# Ejercicios Recomendados

### 1.
¿Qué contendrá el archivo `notas.txt` después de ejecutar el siguiente código?
```python
archivo = open("notas.txt", "w")
archivo.write("Primera línea\n")
archivo.close()

archivo = open("notas.txt", "w")
archivo.write("Segunda línea\n")
archivo.close()
```

**Respuesta:** Solo `"Segunda línea"`.

**Explicación:**

Cada vez que se abre un archivo en modo `'w'`, su contenido se borra por completo.

---

### 2.
¿Qué contendrá el archivo `notas2.txt` después de ejecutar el siguiente código?
```python
archivo = open("notas2.txt", "w")
archivo.write("Línea A\n")
archivo.close()

archivo = open("notas2.txt", "a")
archivo.write("Línea B\n")
archivo.close()
```

**Respuesta:** `"Línea A"` seguida de `"Línea B"`.

**Explicación:**

El modo `'a'` (append) no borra el contenido existente; agrega lo nuevo al final del archivo.

---

### 3.
Un archivo `datos3.txt` contiene:
```
uno
dos
tres
```
¿Qué devuelve cada una de estas tres formas de leerlo (por separado, cada una en un archivo recién abierto)?
```python
f.read()
f.readline()
f.readlines()
```

**Respuesta:**
- `read()` : `'uno\ndos\ntres\n'` (todo el contenido como un único string)
- `readline()` : `'uno\n'` (solo la primera línea)
- `readlines()` : `['uno\n', 'dos\n', 'tres\n']` (una lista con cada línea como elemento)

**Explicación:**

`read()` no distingue líneas, trae todo el texto de una vez. `readline()` avanza solo una línea por llamada. `readlines()` sí separa por líneas, pero devuelve una lista de strings (cada uno conserva el `\n` al final).

---

### 4.
Explique por qué se recomienda usar `with open(...) as archivo:` en lugar de `archivo = open(...)` seguido de `archivo.close()`.

**Respuesta:** Porque `with` garantiza el cierre del archivo aunque ocurra un error dentro del bloque.

**Explicación:**

Si se usa `open()` sin `with` y ocurre una excepción antes de llegar a la línea `archivo.close()`, el archivo queda abierto (sin cerrarse), lo cual puede causar pérdida de datos no guardados o bloqueos del archivo. Con `with`, Python cierra el archivo automáticamente al salir del bloque, sin importar si terminó normalmente o por un error.

---

### 5.
¿Qué contendrá el archivo `animales.txt` después de ejecutar este código?
```python
lineas = ["gato\n", "perro\n", "loro\n"]
with open("animales.txt", "w") as f:
    f.writelines(lineas)
```

**Respuesta:**
```
gato
perro
loro
```

**Explicación:**

`writelines()` escribe cada elemento de la lista tal cual, uno tras otro, sin agregar saltos de línea automáticamente.

---

### 6.
Si el archivo `existe.txt` ya existe, ¿qué ocurre al ejecutar lo siguiente?
```python
archivo = open("existe.txt", "x")
```

**Respuesta:** Se produce un error (`FileExistsError`); el archivo no se abre.

**Explicación:**

El modo `'x'` (creación exclusiva) sirve para crear un archivo nuevo.

---

### 7.
¿Qué contendrá el archivo `combo.txt` después de ejecutar este código?
```python
with open("combo.txt", "w") as f:
    f.write("Total: 0\n")

with open("combo.txt", "a") as f:
    f.write("Detalle: nada\n")
```

**Respuesta:**
```
Total: 0
Detalle: nada
```

**Explicación:**

El primer bloque crea el archivo (o lo sobrescribe si ya existía) con la primera línea. El segundo bloque, al usar `'a'`, agrega la segunda línea sin borrar la primera.

---

### 8.
¿Qué ocurre al ejecutar el siguiente código?
```python
with open("resultado.txt", "w") as archivo:
    total = 42
    archivo.write(total)
```

**Respuesta:** Se produce un error: `TypeError: write() argument must be str, not int`.

**Explicación:**

`write()` solo acepta strings. Como `total` es un entero, hay que convertirlo antes: `archivo.write(str(total))`.

---

### 9.
El archivo `numeros.txt` no existe todavía en la carpeta. ¿Qué ocurre al ejecutar lo siguiente?
```python
with open("numeros.txt", "r") as archivo:
    contenido = archivo.read()
```

**Respuesta:** Se produce un error: `FileNotFoundError`.

**Explicación:**

El modo `'r'` (lectura) solo funciona si el archivo ya existe; a diferencia de `'w'` o `'a'`, no lo crea.

---

### 10.
El archivo `datos.txt` contiene:
```
uno
dos
tres
```
¿Qué imprime el siguiente código?
```python
with open("datos.txt") as archivo:
    for linea in archivo:
        print(linea, end="")
```

**Respuesta:**
```
uno
dos
tres
```

**Explicación:**

Un archivo abierto se puede recorrer directamente con un `for`, línea por línea, sin necesidad de llamar `readlines()` primero; Python entrega cada línea (incluyendo su `\n`) en cada vuelta del ciclo. Por eso el `print` usa `end=""`: si no, cada línea tendría un salto de línea extra, ya que la línea misma ya trae el suyo.

---

### 11.
El archivo `asistencia.txt` contiene:
```
Ana,presente
Luis,ausente
Ana,ausente
```
Un estudiante escribe este código para contar las ausencias:
```python
total_ausencias = 0
with open("asistencia.txt") as archivo:
    for linea in archivo:
        partes = linea.split(",")

        nombre = partes[0]
        estado = partes[1]

        if estado == "ausente":
            total_ausencias += 1

print(total_ausencias)
```
El código no marca ningún error, pero imprime `0` en lugar de `2`. ¿Cuál es el problema, y cómo se corrige?

**Respuesta:** El problema es que no se usó `.strip()`; corrigiendo la línea `partes = linea.strip().split(",")` el resultado es `2`.

**Explicación:**

Cada línea leída del archivo conserva el salto de línea `\n` al final. Por eso `estado` queda como `'presente\n'` o `'ausente\n'`, y la comparación `estado == "ausente"` nunca es verdadera: ningún estado coincide exactamente, así que `total_ausencias` queda en `0`. Se soluciona quitando los espacios y saltos de línea con `.strip()` antes de separar por comas.

---

### 12.
El archivo `registro.txt` ya existe y contiene `"dato inicial\n"`. ¿Qué ocurre al ejecutar lo siguiente?
```python
archivo = open("registro.txt")
archivo.write("nueva línea\n")
```

**Respuesta:** Se produce un error: `UnsupportedOperation: not writable`.

**Explicación:**

Cuando `open()` se llama sin indicar un modo, Python usa por defecto `'r'` (solo lectura). Con `'r'` sí se puede leer el archivo normalmente, pero intentar escribir en él lanza este error, porque el archivo nunca se abrió con permiso de escritura.

---

### 13.
De los siguientes dos `import`, indique cuál necesita instalarse primero con `pip install` y cuál no.
```python
import pandas
import utilidades
```
(`utilidades.py` es un archivo propio guardado en la misma carpeta que el programa).

**Respuesta:** `pandas` necesita `pip install pandas`; `utilidades` no necesita `pip` porque es un archivo propio.

**Explicación:**

`pandas` es una librería externa que no viene incluida con Python, por lo que debe instalarse antes de poder importarla. `utilidades.py`, al estar en la misma carpeta que el programa principal, puede importarse directamente sin instalar nada: Python lo encuentra como un módulo local.

---

### 14.
Se tienen dos archivos en la misma carpeta:

`utilidades.py`
```python
def saludar(nombre):
    return f"Hola, {nombre}"
```

`principal.py`
```python
import utilidades

print(utilidades.saludar("Ana"))
```

¿Qué imprime `principal.py` al ejecutarse?

**Respuesta:** `Hola, Ana`

**Explicación:**

Al hacer `import utilidades`, `principal.py` obtiene acceso a todo lo definido en `utilidades.py`, pero debe llamarlo anteponiendo el nombre del módulo (`utilidades.saludar(...)`). Como ambos archivos están en la misma carpeta, Python encuentra el módulo sin problema.

---

### 15.
¿Cuál es la diferencia entre estas dos formas de importar la misma función, y cómo cambia la forma de llamarla?
```python
# Opción A
import utilidades
utilidades.saludar("Ana")

# Opción B
from utilidades import saludar
saludar("Ana")
```

**Respuesta:** Ambas hacen lo mismo, pero con `import utilidades` hay que anteponer el nombre del módulo al llamar la función; con `from utilidades import saludar` se importa la función directamente y se llama por su nombre solo.

**Explicación:**

`import utilidades` trae el módulo completo bajo su propio "espacio de nombres", por lo que cada función debe escribirse como `utilidades.funcion()`. `from utilidades import saludar` trae únicamente esa función, permitiendo usarla directamente como `saludar()`.

---

### 16.
Un estudiante tiene esta estructura de carpetas:
```
proyecto/
├── principal.py
└── modulos/
    └── utilidades.py
```
Y en `principal.py` escribe:
```python
import utilidades
```
Al ejecutar `principal.py`, obtiene `ModuleNotFoundError: No module named 'utilidades'`. ¿Cuál es el error?

**Respuesta:** `utilidades.py` no está en la misma carpeta que `principal.py`; está dentro de la subcarpeta `modulos/`, y Python no lo encuentra con un `import`.

**Explicación:**

Un `import` simple busca el módulo en la misma carpeta que el archivo que se ejecuta (además de en las rutas conocidas de Python). Como `utilidades.py` está en una subcarpeta distinta, no se localiza automáticamente. Para resolverlo se debería mover `utilidades.py` a la carpeta `proyecto/`.

---

### 17.
¿Qué estrategia de resolución de problemas utiliza el siguiente código?
```python
def suma_par_objetivo(lista, objetivo):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == objetivo:
                return (lista[i], lista[j])
    return None
```

**Respuesta:** Fuerza bruta (búsqueda exhaustiva).

**Explicación:**

El código prueba todas las parejas posibles de elementos de la lista, una por una, sin ningún criterio que descarte, hasta encontrar una que cumpla la condición.

---

### 18.
¿Qué estrategia de resolución de problemas utiliza el siguiente código para dar vuelto?
```python
def dar_vuelto(monedas, objetivo):
    monedas = sorted(monedas, reverse=True)
    usadas = []
    restante = objetivo
    for m in monedas:
        while restante >= m:
            usadas.append(m)
            restante -= m
    return usadas
```

**Respuesta:** Algoritmo voraz (greedy).

**Explicación:**

En cada paso, el algoritmo toma la moneda más grande posible en ese momento, sin reconsiderar la elección después.

---

### 19.
¿Qué estrategia de resolución de problemas utiliza el siguiente código?
```python
def busqueda_binaria(lista, objetivo, ini, fin):
    if ini > fin:
        return -1
    medio = (ini + fin) // 2
    if lista[medio] == objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, objetivo, medio + 1, fin)
    else:
        return busqueda_binaria(lista, objetivo, ini, medio - 1)
```

**Respuesta:** Divide y vencerás.

**Explicación:**

El problema (buscar en toda la lista) se divide en un subproblema más pequeño (buscar solo en la mitad izquierda o la mitad derecha), descartando la otra mitad por completo en cada llamada.

---

### 20.
¿Qué estrategia de resolución de problemas utiliza el siguiente código?
```python
def permutaciones(actual, restantes, resultado):
    if not restantes:
        resultado.append(actual[:])
        return
    for i in range(len(restantes)):
        actual.append(restantes[i])
        permutaciones(actual, restantes[:i] + restantes[i+1:], resultado)
        actual.pop()
```
Al llamarlo con `restantes = [1, 2, 3]`, ¿cuántas permutaciones genera?

**Respuesta:** Backtracking. Genera 6 permutaciones: `[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]`.

**Explicación:**

El algoritmo construye una solución paso a paso (`actual.append(...)`), y luego deshace ese paso (`actual.pop()`) para probar otra alternativa en el mismo punto. Ese "avanzar y luego retroceder para explorar otra opción" es exactamente el patrón de backtracking.

---

### 21.
¿Qué estrategia de resolución de problemas utiliza el siguiente código, y en qué se diferencia de la versión recursiva de Fibonacci?
```python
memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]
```

**Respuesta:** Programación dinámica (memoización).

**Explicación:**

El diccionario `memo` guarda los resultados ya calculados para no volver a calcularlos. Al ejecutar `fib(20)`: la versión recursiva simple hace 21 891 llamadas, mientras que la versión con memoización hace solo 39 llamadas, porque cada subproblema se resuelve una única vez y luego se reutiliza.

---

### 22.
¿Qué estrategia de resolución de problemas utiliza el siguiente código, y cuántos subconjuntos genera para `restantes = [1, 2, 3]`?
```python
def subconjuntos(actual, restantes, resultado):
    if not restantes:
        resultado.append(actual[:])
        return
    subconjuntos(actual, restantes[1:], resultado)
    actual.append(restantes[0])
    subconjuntos(actual, restantes[1:], resultado)
    actual.pop()
```

**Respuesta:** Backtracking. Genera 8 subconjuntos: `[], [3], [2], [2,3], [1], [1,3], [1,2], [1,2,3]`.

**Explicación:**

En cada elemento, el código explora dos caminos: no incluirlo y sí incluirlo (agregándolo con `append` y luego deshaciendo con `pop` para probar la otra rama). Esa exploración de ambas alternativas en cada paso es backtracking.

---

### 23.
¿Qué estrategia de resolución de problemas utiliza el siguiente código?
```python
def contar_positivos(lista):
    contador = 0
    for x in lista:
        if x > 0:
            contador += 1
    return contador
```

**Respuesta:** Ciclos.

**Explicación:**

Recorre una sola vez todos los elementos de una estructura de datos con un ciclo, sin ramificarse en múltiples caminos, sin dividir el problema y sin necesidad de reconsiderar decisiones.

---

### 24.
¿Qué imprime el siguiente código?
```python
total = 0
for numero in [3, 7, 2, 9, 4]:
    if numero % 2 == 0:
        total += numero
print(total)
```

**Respuesta:** `6`

**Explicación:**

El ciclo recorre la lista y solo suma los números pares. De `[3, 7, 2, 9, 4]`, los pares son `2` y `4`, cuya suma es `2 + 4 = 6`.

---

### 25.
¿Qué estrategia de resolución de problemas utiliza el siguiente código para encontrar el valor máximo de una lista?
```python
def maximo_dv(lista, ini, fin):
    if ini == fin:
        return lista[ini]
    medio = (ini + fin) // 2
    izq = maximo_dv(lista, ini, medio)
    der = maximo_dv(lista, medio + 1, fin)
    return izq if izq > der else der
```

**Respuesta:** Divide y vencerás.

**Explicación:**

El problema se divide en dos subproblemas más pequeños (el máximo de la mitad izquierda y el máximo de la mitad derecha), y luego se combinan comparando ambos resultados. Es el mismo patrón que la búsqueda binaria, aplicado a un problema distinto.

---

### 26.
Determine la complejidad temporal del siguiente algoritmo:
```python
def sumar_pares(lista):
    total = 0
    n = len(lista)
    for i in range(0, n, 2):
        total += lista[i]
    return total
```

**Respuesta:** O(n)

**Explicación:**

Aunque el ciclo avanza de dos en dos (`range(0, n, 2)`), la cantidad de iteraciones sigue siendo proporcional a `n` (aproximadamente `n/2`). Como las constantes se descartan en notación Big-O, `n/2` sigue siendo O(n).

---

### 27.
Determine la complejidad temporal del siguiente algoritmo:
```python
def contar_triangular(n):
    contador = 0
    for i in range(n):
        for j in range(i, n):
            contador += 1
    return contador
```

**Respuesta:** O(n²)

**Explicación:**

El ciclo interno no siempre recorre `n` elementos completos. El total de operaciones es `n(n+1)/2`. Como `n(n+1)/2` es un polinomio de segundo grado en `n`, su complejidad es O(n²).

---

### 28.
Determine la complejidad temporal del siguiente algoritmo:
```python
def busqueda_binaria_rec(lista, objetivo, ini, fin):
    if ini > fin:
        return -1
    medio = (ini + fin) // 2
    if lista[medio] == objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria_rec(lista, objetivo, medio + 1, fin)
    else:
        return busqueda_binaria_rec(lista, objetivo, ini, medio - 1)
```

**Respuesta:** O(log n)

**Explicación:**

Cada llamada recursiva descarta la mitad de la lista restante.

---

### 29.
Determine la complejidad espacial del siguiente algoritmo, donde `n` es el tamaño de cada lado de la matriz:
```python
def crear_matriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(0)
        matriz.append(fila)
    return matriz
```

**Respuesta:** O(n²)

**Explicación:**

El algoritmo crea una matriz de `n` filas, y cada fila tiene `n` elementos, para un total de `n × n = n²` valores almacenados en memoria.

---

### 30.
Determine la complejidad temporal del siguiente algoritmo:
```python
def resumen(lista):
    total = 0
    for x in lista:
        total += x

    maximo = lista[0]
    for x in lista:
        if x > maximo:
            maximo = x

    return total, maximo
```

**Respuesta:** O(n)

**Explicación:**

Aunque hay dos ciclos, no están anidados, van uno después del otro, cada uno recorriendo la lista completa una vez. El total de operaciones es `n + n = 2n`. Como la constante `2` se descarta en notación Big-O, la complejidad sigue siendo O(n).

---

### 31.
Determine la complejidad espacial del siguiente algoritmo:
```python
def contar_frecuencias(lista):
    frecuencias = {}
    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    return frecuencias
```

**Respuesta:** O(n)

**Explicación:**

En el peor caso (cuando todos los elementos de la lista son distintos), el diccionario `frecuencias` termina almacenando una entrada por cada elemento de la lista de entrada. Por lo tanto, el espacio adicional usado crece proporcionalmente al tamaño `n` de la lista.

---

### 32.
Determine la complejidad temporal del siguiente algoritmo:
```python
def contar_reducciones(n):
    pasos = 0
    while n > 1:
        n = n // 2
        pasos += 1
    return pasos
```

**Respuesta:** O(log n)

**Explicación:**

En cada iteración del `while`, el valor de `n` se divide entre 2. Se necesitan `log(n)` divisiones para reducir `n` hasta 1.
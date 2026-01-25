# Ejercicios `Complejidad Algorítmica`
### 1.
En el contexto de sumas de prefijos, si tenemos el arreglo de prefijos [1, 9, 25, 27, 32, 36]. Sin cononecer el arreglo ¿cuál es la suma del desde el elemento en el índice 2 al elemento en el índice 4?

**Respuesta:** 31

**Explicación:** La suma del subarreglo desde el índice i hasta j se calcula como prefijos[j] - prefijos[i-1]. 

Para i=2 y j=4: prefijos[4] - prefijos[1] = 32 - 9 = 23.

También podemos encontrar el arreglo original y hacer la suma: [1, 8, 16, 2, 5, 4]

16 + 2 + 5 = 23

---

### 2.
¿Cuál es el máximo común divisor (MCD) de 29 y 12 usando el algoritmo de Euclides?

**Respuesta:** 1

**Explicación:** Realizando el procedimiento completo:

(29, 12)
29 % 12 = 5

(12, 5)
12 % 5 = 2

(5, 2)
5 % 2 = 1

(2, 1)
2 % 1 = 0

(1, 0)
MCD = 1

---

### 3.
¿Cuál es la salida de este código?¿Porque es incorrecta?

```python
arreglo = [5, 3, 8, 2]

minimo = 0
for num in arreglo:
    if num < minimo:
        minimo = num
```

**Respuesta:** 0, no es el mínimo del arreglo

**Explicación:** El código inicializa `minimo` en 0. Como todos los números son mayores que 0, nunca se actualiza. Debería inicializarse con el primer elemento del arreglo.

---

### 4. 
¿Cuál es el principal factor que limita la eficiencia de la Criba de Eratóstenes en encontrar todos los primos desde 1 hasta un número muy grande?

• A. Consume *O(n log n)* en espacio

• B. Es *O(n^2)* en su ejecución

• C. Consume *O(n)* en espacio

• D. La cantidad de primos por debajo de es muy baja

• E. Requiere muchos ciclos anidados (con for o while)

**Respuesta:** C

**Explicación:** Desde el inicio creamos una lista con n elementos lo cual requiere n espacios.

---

### 5. 
Sean *a*, *e*, *n*, *p* cuatro números enteros, tal que *n = a^e mod p*. Al utilizar
exponenciación binaria para calcular, ¿cuál es la complejidad temporal?

• A. *O(log a)*

• B. *O(log np)*

• C. *O(log p)*

• D. *O(log e)*

• E. *O(log n)*

**Respuesta:** D

**Explicación:** La complejidad para calcular *a^b* con exponenciación binaria es *O(log b)*
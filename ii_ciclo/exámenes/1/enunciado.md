# Examen I
## Indicaciones generales
- La duración del examen es de 2h 30min.
- Subir al Google Classroom las soluciones en el espacio denominado *I Examen*.
    - En caso de tener problemas puede enviar la solución al correo [santiagobrenesruiz@gmail.com](mailto:santiagobrenesruiz@gmail.com)
- Debe entregar los archivos: `principal.py`, `utilidades.py`, `por_corregir.py`.
- En Classroom se encuentran disponibles: `asistencia.txt` (para probar la Parte 3) y `por_corregir.py` (archivo con el código de la Parte 2).
- El examen es de carácter individual.
- Es permitido utilizar una hoja de notas o apuntes.

---

## Parte 1. Verdadero o Falso (20 pts, 1 pt c/u)

Al inicio del archivo `principal.py`, escriba como comentario su respuesta (V o F) para cada una de las siguientes 20 afirmaciones.

1. El modo `'a'` sobrescribe todo el contenido del archivo cada vez que se abre.
2. El método `readlines()` devuelve una lista donde cada elemento es una línea del archivo.
3. Usar `with open(...) as archivo:` garantiza que el archivo se cierre automáticamente al salir del bloque.
4. El modo `'x'` abre el archivo para escritura y no genera ningún error si el archivo ya existe.
5. El método `read()` devuelve todo el contenido del archivo como un único string.
6. Para usar funciones de un archivo `utilidades.py` desde otro archivo, se debe escribir `import utilidades`.
7. Un módulo como `pandas` debe instalarse antes de poder importarlo.
8. Si dos archivos `.py` están guardados en la misma carpeta, uno puede importar funciones del otro sin necesidad de instalar nada.
9. Un algoritmo voraz reconsidera sus decisiones anteriores si más adelante encuentra una mejor opción.
10. La búsqueda binaria es un ejemplo de la estrategia "divide y vencerás".
11. La fuerza bruta (búsqueda exhaustiva) garantiza encontrar la solución correcta, pero puede ser muy lenta.
12. El backtracking nunca "retrocede", o sea, una vez que toma una decisión, la mantiene hasta el final aunque ya sepa que no puede funcionar.
13. La programación dinámica evita volver a calcular subproblemas que ya se resolvieron antes.
14. Un algoritmo voraz siempre garantiza encontrar la solución óptima.
15. Recorrer todos los elementos de una lista con un ciclo `for` es un ejemplo de la estrategia "uso de ciclos".
16. La complejidad temporal se mide en segundos que tarda el programa en ejecutarse.
17. Un algoritmo que solo usa unas pocas variables sueltas tiene complejidad espacial O(1).
18. Un ciclo simple que recorre una vez una lista de `n` elementos tiene complejidad temporal O(n).
19. Dos ciclos anidados, donde cada uno recorre todos los elementos de una lista de tamaño `n`, dan una complejidad temporal O(n).
20. Crear una lista nueva que guarda una copia de cada elemento de una lista de entrada de tamaño `n` tiene complejidad espacial O(1).

---

## Parte 2. Corrección de código y complejidades (40 pts, 10 pts c/u)

Se le entrega en Classroom el archivo `por_corregir.py`, con el código de los 4 ejercicios ya escrito. Debe completar ese mismo archivo:

- En los ejercicios de corrección (1 y 2): corrija el código directamente donde está el error, y agregue un comentario breve (1-2 líneas) explicando cuál era el problema.
- En los ejercicios de complejidad (3 y 4): no modifique el código; agregue como comentario, justo debajo de la función, la complejidad solicitada y una breve justificación.

### 1. Manejo de archivos

El siguiente código intenta leer y mostrar el contenido de un archivo que ya existe:

```python
archivo = open("datos.txt", "w")
contenido = archivo.read()
print(contenido)
```

### 2. Uso de ciclos

El siguiente código debería sumar todos los elementos de una lista, pero el resultado que produce es incorrecto:

```python
def sumar_lista(lista):
    total = 0
    for i in range(2, len(lista)):
        total += lista[i]
    return total
```

### 3. Calcule la complejidad temporal

Determine la complejidad temporal del siguiente algoritmo:

```python
def contar_repetidos(lista):
    contador = 0
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i != j and lista[i] == lista[j]:
                contador += 1
    return contador
```

### 4. Calcule la complejidad espacial

Determine la complejidad espacial del siguiente algoritmo:

```python
def lista_de_cuadrados(lista):
    resultado = []
    for x in lista:
        resultado.append(x ** 2)
    return resultado
```

---

## Parte 3. Desarrollo (40 pts)

Un profesor lleva el registro de asistencia de su curso en un archivo de texto y necesita un programa que le genere un resumen: cuántas ausencias hay en total, cuántas tiene cada estudiante, y quién es el estudiante con más ausencias.

### Archivo de entrada: `asistencia.txt`

Cada línea tiene el nombre de un estudiante y su estado en una clase, separados por una coma. Un mismo estudiante puede aparecer varias veces (una vez por cada clase registrada).

```
Ana,presente
Luis,ausente
Ana,ausente
Carla,presente
Luis,ausente
```

### Requerimientos

El programa debe dividirse en dos archivos: `principal.py` (programa principal) y `utilidades.py` (funciones auxiliares).

1. En `principal.py`, abrir `asistencia.txt` con `with open` en modo lectura y leer todas las líneas con `readlines()`.
2. Procesar cada línea (separándola por la coma) para obtener el nombre y el estado. Guardar los resultados en dos listas: `nombres` y `estados`.
3. Con un ciclo, calcular el total de ausencias de todo el curso y guardarlo en una variable `total_ausencias`.
4. Con un ciclo, calcular cuántas ausencias tiene cada estudiante, guardando el resultado en un diccionario `ausencias_por_estudiante` (donde cada clave es el nombre y cada valor es su cantidad de ausencias).
5. Determinar cuál es el estudiante con la mayor cantidad de ausencias (guardar su nombre y su cantidad de ausencias).
6. Escribir un archivo nuevo `resumen.txt` (modo escritura) con el total de ausencias y el detalle de ausencias por estudiante, una línea por estudiante.
7. Agregar al final de `resumen.txt` una línea indicando el nombre del estudiante con más ausencias y su cantidad.
8. Mover la lógica del punto 4 a una función llamada `contar_ausencias(nombres, estados)` dentro de `utilidades.py`, que reciba las dos listas y devuelva el diccionario de ausencias por estudiante.
9. Importar `utilidades.py` desde `principal.py` y usar la función `contar_ausencias` en lugar del código del punto 4.
10. Mostrar en pantalla, de forma ordenada, el resumen completo: el total de ausencias, la cantidad de ausencias por estudiante, y quién tuvo más.

> Nota: No es necesario validar que el archivo `asistencia.txt` exista, ni que las líneas tengan el formato correcto; se asume que el archivo siempre viene bien formado.

### Criterios de Evaluación

- Lectura del archivo `asistencia.txt` con `with open` y `readlines()`: 4 pts
- Separación correcta de cada línea en nombre y estado: 4 pts
- Cálculo correcto del total de ausencias: 4 pts
- Cálculo correcto de las ausencias por estudiante: 4 pts
- Determinación correcta del estudiante con más ausencias: 4 pts
- Escritura correcta de `resumen.txt` (modo `'w'`): 4 pts
- Agregado correcto de la línea final a `resumen.txt` (modo `'a'`): 4 pts
- Función `contar_ausencias()` correctamente definida en `utilidades.py`: 4 pts
- Uso correcto de `import utilidades` desde `principal.py`: 4 pts
- Impresión ordenada y clara del resumen en pantalla: 4 pts

**Total: 40 pts**

### Ejemplo de ejecución

```
Total de ausencias: 3
Ana: 1
Luis: 2
Carla: 0
Estudiante con más ausencias: Luis (2)
```

> **Funciones Útiles**
> - **Diccionarios:** `diccionario[clave] = valor` (crear o actualizar un valor), `clave in diccionario` (verificar si una clave ya existe), `diccionario.items()` (recorrer pares clave-valor con un `for`).
>
> *No son funciones obligatorias, puede utilizar otras si lo considera necesario.*
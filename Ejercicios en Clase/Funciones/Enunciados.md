# Ejercicios `Funciones`
### 1. Números amigos
Dos números son amigos si la suma de sus divisores (excepto el número) es igual al otro número.
- Pida dos números al usuario.
- Cree una función para calcular la suma de los divisores de un número.
- Imprima si estos números son o no amigos.
**Ejemplo:**
```
Ingrese el primer número: 220
Ingrese el segundo número: 284

Los divisires de 220 dan: 284
Los divisores de 284 dan: 220

220 y 284 son números amigos
```

### 2. Palabra más frecuente por longitud
Dado un texto, crea una función que:
- Encuentre la palabra más repetida.
- Devuelva un diccionario con la palabra como clave y la frecuencia como valor.
**Ejemplo:**
```
Ingrese el texto: aaa bbb ccc aaa bbb bbb ccc aaa aaa aaa 

Palabra más repetida: 'aaa'
Frecuencia: {'aaa': 5, 'bbb': 3, 'ccc': 2}
```

### 3. Calculadora de áreas con diferentes figuras
Crear varias función que según el nombre de una figura geométrica (círculo, rectángulo, triángulo) y sus medidas, devuelvan el área correspondiente.
- Debe ejecutar el programa hasta que la figura no sea válida.
**Ejemplo:**
```
Ingrese una figura (rectangulo, triangulo, circulo): rectangulo
Ingrese sus medidas (base altura): 5 2
Area = 10

Ingrese una figura (rectangulo, triangulo, circulo): circulo
Ingrese el radio: 3
Area = 28.2744

Ingrese una figura (rectangulo, triangulo, circulo): 
La figura no existe
Saliendo...
```

### 4. Análisis de palabras favoritas
Un grupo de personas comparte sus palabras favoritas. Cada persona da una lista con varias palabras, pero algunas pueden repetirse.
- Crea una función que reciba una o más listas de palabras.
- Convierte cada lista en un set para eliminar palabras repetidas.
- Usando operaciones entre conjuntos para devuelva lo siguiente:
    - Las palabras que les gustan a todas las personas.
    - Las palabras que le gustan al menos a una persona.
    - Las palabras que solo le gustan a la primera persona.
```python
persona1 = ["sol", "luna", "mar", "sol"]  
persona2 = ["luna", "estrella", "sol", "río"]  
persona3 = ["nube", "luna", "sol", "río"]  
```
```
Palabras mencionadas por al menos una persona: {'sol', 'luna', 'mar', 'estrella', 'río', 'nube'}
Palabras que les gustan a todos: {'sol', 'luna'}  
Palabras solo de la primera persona: {'mar'}  
``

### 5. Registro de asistencia con diccionarios y sets
Dado un diccionario donde las claves son días y los valores son sets con nombres de estudiantes que asistieron ese día.
Crea una función que reciba este diccionario y devuelva una tupla con los estudiantes que asistieron todos los días.
**Ejemplo:**
```python
lista = {
  "Lunes": ["Ana", "Luis", "Carlos"],
  "Martes": ["Ana", "Carlos"],
  "Miércoles": ["Ana", "Carlos", "Luis"]
}
```
```
(Ana, Carlos)
```
# Tarea 2
## Descripción
Esta tarea consiste en **dos ejercicios independientes** que utilizan **funciones**, además de estructuras como **listas, diccionarios y sets**.
Recuerde incluir **comentarios descriptivos**, utilizar **nombres de variables claros** y estructurar el programa con **funciones**.

---

## Ejercicio 1: Contador de vocales únicas
Cree un programa que cuente las **vocales únicas** (sin repetir) encontradas en una palabra ingresada por el usuario.

1. Solicite al usuario una palabra.
2. Valide que la palabra solo contenga letras.
   - En caso contrario, imprima un mensaje de error y vuelva a pedir la palabra hasta que sea correcta
3. Convierta la palabra a minúsculas.
4. Encuentre y almacene las **vocales** sin repetir.
   - Recomendado usar un `set`
5. Imprima:
   - Cuántas vocales únicas se encontraron.
   - Qué vocales fueron.

### Requisitos adicionales
- Debe usar una función para pedir y **validar la palabra**, que retorne la palabra en minúsculas.

### Ejemplo de Ejecución
```
Ingrese una palabra: 12345
Error: Solo puede contener letras

Ingrese una palabra: Prueba
Número de vocales únicas: 3
Vocales encontradas: {'u', 'e', 'a'}
```

## Criterios de Evaluación
- **Validación de la entrada mediante una función**: 15%
- **Identificación de las vocales**: 15%
- **Uso de estructuras para eliminar elementos repetidos**: 10%
- **Presentación de resultados**: 10%

---

## Ejercicio 2: Diccionario de calificaciones
Cree un programa que construya un **diccionario de estudiantes** con sus respectivas calificaciones, y luego calcule el promedio general.

1. Solicite al usuario ingresar el número de estudiantes.
2. Para cada estudiante:
   - Solicite su nombre.
   - Solicite una calificación.
   - Guarde la información en un **diccionario** con la forma:  
     `{"Nombre": calificación}`.
3. Al final:
   - Muestre el diccionario completo.
   - Calcule e imprima el promedio general de las calificaciones.

### Requisitos adicionales
- Debe usar una función que reciba un diccionario y que retorne el **promedio**.

### Ejemplo de Ejecución
```
Ingrese la cantidad de estudiantes: 3

Nombre del estudiante 1: Ana
Calificación de Ana: 85
Nombre del estudiante 2: Carlos
Calificación de Luis: 90
Nombre del estudiante 3: Pedro
Calificación de Marta: 78

Diccionario de calificaciones: {'Ana': 85, 'Carlos': 90, 'Pedro': 78}
Promedio general: 84.33
```

## Criterios de Evaluación
- **Solicitud de información de los estudiantes**: 10%
- **Construcción correcta del diccionario**: 15%
- **Cálculo del promedio usando una función**: 15%
- **Presentación de resultados**: 10%

---

## **Entrega**
- El código de cada ejercicio debe estar en **archivos separados** (`ejercicio1.py` y `ejercicio2.py`).
- Subir los archivos `.py` en la sección correspondiente de **Google Classroom**.
# Tarea 2

## Descripción

Esta tarea consiste en **dos ejercicios independientes** en los cuales se utilizarán principalmente **listas y ciclos**.

Debe añadir comentarios descriptivos a su solución, así como asignar nombres de variables claros.

Cada ejercicio tiene un valor de **50%**.

---

## Ejercicio 1: Análisis de palabras (50%)

Se requiere implementar en Python un programa de análisis de palabras.

El programa debe:

* Solicitar al usuario la cantidad de palabras que desea ingresar.

* Utilizar algún ciclo para solicitar cada una de las palabras.

* Al finalizar el ingreso, el programa deberá mostrar:

  * La cantidad total de caracteres ingresados.
  * La palabra más corta.
  * Cuántas palabras empiezan con vocal.

* Todas las palabras ingresadas deben almacenarse en una lista y mostrarse al final del programa.

### **Ejemplo de Ejecución**

```text
¿Cuántas palabras desea ingresar?: 5
Ingrese una palabra: Casa
Ingrese una palabra: Elefante
Ingrese una palabra: Sol
Ingrese una palabra: Avion
Ingrese una palabra: Programacion

Palabras ingresadas: ['Casa', 'Elefante', 'Sol', 'Avion', 'Programacion']
Cantidad total de caracteres: 32
Palabra más corta: Sol
Palabras que empiezan con vocal: 2
```

---

## Ejercicio 2: Adivinar el número (50%)

Se requiere implementar en Python un juego de adivinanza de números.

El programa debe:

- Generar un número entero aleatorio entre 1 y 100 (ambos incluidos).

- Solicitar al usuario que ingrese un número repetidamente hasta que acierte el número secreto.

- Después de cada intento, el programa indicará si el número ingresado es mayor o menor que el número secreto.

- Al finalizar el juego (número adivinado), se mostrarán todos los intentos realizados por el usuario.

*Se debe gestionar posibles errores de entrada mediante el uso de try-except (por ejemplo, si el usuario ingresa texto en lugar de un número).*

**Recomendaciones:**
- Investigue sobre el uso del módulo `random` para generar números enteros aleatorios, debe documentar/comentar correctamente la información encontrada.
```python
import random
```

### **Ejemplo de Ejecución**

```
Ingrese un número: 50
El número secreto es menor
Ingrese un número: 25
El número secreto es menor
Ingrese un número: 12
El número secreto es menor
Ingrese un número: 6
El número secreto es menor
Ingrese un número: 3
El número secreto es menor
Ingrese un número: 1
Número correcto
Tus intentos fueron: [50, 25, 12, 6, 3, 1]
```

---

## Criterios de Evaluación

### Ejercicio 1 (50%)

* **Solicitud de cantidad de palabras (5%)**: Solicita la cantidad de palabras a ingresar.
* **Solicitud de las palabras (10%)**: Utiliza algún ciclo para solicitar las palabras.
* **Almacenamiento de palabras (5%)**: Guarda todas las palabras ingresadas en una lista.
* **Conteo de caractéres (5%)**: Calcula la cantidad total de caracteres.
* **Palabra más corta (10%)**: Identifica la palabra con menor cantidad de caracteres.
* **Conteo por vocales (5%)**: Calcula la cantidad de palabras que empiezan con vocal.
* **Presentación y formato (5%)**: Salida ordenada y clara.
* **Comentarios en el código (5%)**

---

### Ejercicio 2 (50%)

* **Generación del número aleatorio (5%)**: Uso correcto del módulo `random` para generar un entero entre 1 y 100.
* **Entrada de usuario y manejo de errores (10%)**: Permite ingresar solamente un número entero sin interrumpir el programa.
* **Manejo infinito del juego (10%)**: El jeugo se repite hasta que se acierta el número, y finaliza adecuadamente.
* **Instrucciones de juego para el usuario (5%)**: Comparación correcta entre el número ingresado y el número secreto.
* **Almacenamiento y presentación de intentos (10%)**: Registro e impresión de cada intento válido en una lista.
* **Presentación y formato (5%)**: Salida ordenada y clara.
* **Comentarios en el código (5%)**

---

## **Entrega**

* El código de cada ejercicio debe estar en **archivos separados** (`ejercicio1.py` y `ejercicio2.py`).
* Subir los archivos `.py` en la sección correspondiente de **Google Classroom**.
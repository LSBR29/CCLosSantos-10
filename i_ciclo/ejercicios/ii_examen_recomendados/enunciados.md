# Ejercicios Recomendados

### 1. Sistema de inicio de sesión

Escriba un programa que simule un sistema de inicio de sesión utilizando un diccionario de usuarios y contraseñas.

Puede usar:
```python
usuarios = {
    "ana": "python123",
    "carlos": "hola456",
    "maria": "clave789",
    "luis": "abc123"
}
```

El programa debe:

* Recorrer todos los usuarios del diccionario.
* Solicitar al usuario una contraseña para cada cuenta.
* Verificar si la contraseña es correcta.
* Mostrar un mensaje indicando si el acceso fue exitoso o falló.
* Llevar un conteo de:
  * accesos correctos,
  * accesos incorrectos.
* Calcular el porcentaje de accesos correctos al finalizar.

Debe implementar las siguientes funciones:
* `pedir_password(usuario)`
* `verificar_password(password_usuario, password_correcto)`
* `calcular_porcentaje(correctos, total)`

**Ejemplo de ejecución:**


---

### 2. Sistema de inventario y ventas

Escriba un programa que simule el inventario de una tienda.

Puede usar:
```python
inventario = {
    "Teclado": 5,
    "Mouse": 8,
    "Monitor": 3,
    "Audifonos": 6
}
```

El programa debe:

* Mostrar cada producto junto con la cantidad disponible.
* Solicitar al usuario cuántas unidades desea comprar.
* Verificar si existe suficiente inventario.
* Actualizar la cantidad restante del producto.
* Mostrar un mensaje indicando:
  * compra exitosa,
  * o inventario insuficiente.
* Llevar un conteo de:
  * productos vendidos
* Mostrar el inventario final al terminar.

Debe implementar las siguientes funciones:
* `pedir_cantidad(producto)`
* `hay_inventario(disponible, cantidad)`
* `actualizar_inventario(inventario, producto, cantidad)`

**Ejemplo de ejecución:**


---

### 3. Sistema de calificaciones de estudiantes

Escriba un programa que procese las calificaciones de varios estudiantes utilizando un diccionario.

Puede usar:
```python
estudiantes = {
    "Ana": [90, 85, 88],
    "Carlos": [70, 65, 60],
    "Maria": [100, 95, 98],
    "Luis": [80, 75, 82]
}
```

El programa debe:

* Recorrer todos los estudiantes.
* Calcular el promedio de notas de cada estudiante.
* Mostrar si el estudiante:
  * aprueba,
  * o reprueba.
* Llevar un conteo de:
  * estudiantes aprobados,
  * estudiantes reprobados.

Debe implementar las siguientes funciones:

* `calcular_promedio(notas)`
* `aprobo(promedio)`

**Ejemplo de ejecución:**


---

 <!-- OTROS RECOMENDADOS
### Ejercicio 1: Adivina el número
Crear programa genera un número aleatorio entre 1 y 100. El usuario debe adivinarlo. Luego de cada intento, indica si el número es mayor o menor. Guarda los intentos y al final muestra todos los intentos ordenados.

**Recomendaciones:**
- Utilizar el siguiente código para generar números aleatorios:
    ```python
    import random

    num = random.randint(1, 100)
    ```

- Usar un ciclo while para pedir los números.

**Ejemplo de ejecución:**
```
Ingrese un número: 50
El número secreto es mayor

Ingrese un número: 75
El número secreto es menor

Ingrese un número: 39
Número correcto

Tus intentos fueron: [39, 50, 75]
```

---
### Ejercicio 2: Sistema de votación 
Crea un programa que permita a un grupo de personas votar por uno de tres candidatos ya dados en formato de lista.
El programa debe:
- Mostrar un menú para votar o ver resultados.
- Guardar los votos en un diccionario.
- Validar que se vota por una opción existente.

**Recomendaciones:**
- Usar un ciclo while para mostrar el menú.

**Ejemplo de ejecución:**
```
1. Votar
2. Ver Resultados
3. Salir
Seleccione una opción: 1
-- Votación --
Candidatos: Ana, Carlos, Luis
Escoja un candidato: Ana

1. Votar
2. Ver Resultados
3. Salir
Seleccione una opción: 1
Candidatos: Ana, Carlos, Luis
-- Votación --
Escoja un candidato: María
El candidato no es válido

1. Votar
2. Ver Resultados
3. Salir
Seleccione una opción: 2
-- Resultados --
Ana: 1
Carlos: 0
Luis: 0

1. Votar
2. Ver Resultados
3. Salir
Seleccione una opción: 3
```

---
### Ejercicio 3: El doble y triple
Cree un programa que pida al usuario un número y luego use dos funciones:
- doble(n) : retorna el doble del número
- triple(n) : retorna el triple del número
El programa debe imprimir ambos resultados.

**Ejemplo de ejecución:**
```
Ingrese un número: 12
Doble: 24
Triple: 36
```
-->
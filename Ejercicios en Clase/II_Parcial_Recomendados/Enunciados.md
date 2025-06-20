# Ejercicios Recomendados
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
Seleccione una opción: 1
-- Votación --
Candidatos: Ana, Carlos, Luis
Escoja un candidato: Ana

1. Votar
2. Ver Resultados
Seleccione una opción: 1
Candidatos: Ana, Carlos, Luis
-- Votación --
Escoja un candidato: María
El candidato no es válido

1. Votar
2. Ver Resultados
Seleccione una opción: 2
-- Resultados --
Ana: 1
Carlos: 0
Luis: 0
```

---
### Ejercicio 3: El doble y triple
Crea un programa que pida al usuario un número y luego use dos funciones:
- doble(n) → retorna el doble del número
- triple(n) → retorna el triple del número
El programa debe imprimir ambos resultados.

**Ejemplo de ejecución:**
```
Ingrese un número: 12
Doble: 24
Triple: 36
```
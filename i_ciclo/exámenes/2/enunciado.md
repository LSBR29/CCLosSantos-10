# II Examen
## Indicaciones generales
- La duración del examen es de 2h.
- Subir al Google Classroom las soluciones en el espacio denominado *I Examen*.
    - En caso de tener problemas puede enviar la solución al correo [santiagobrenesruiz@gmail.com](mailto:santiagobrenesruiz@gmail.com)
- Debe entregar el archivo: `main.py`.
- El examen es de carácter individual.
- Es permitido utilizar una hoja de notas o apuntes.

---

## Juego de Preguntas y Respuestas
Se debe completar un programa que simule un juego de preguntas y respuestas.

El archivo `main.py` ya tiene código desarrollado el cual no es necesario modificar, puede encontrarlo en Classroom.

El programa utilizará un diccionario con preguntas y respuestas correctas ya definido dentro del archivo. El objetivo es recorrer todas las preguntas, solicitar una respuesta al usuario, verificar si es correcta y calcular el resultado final del juego.

### Diccionario de preguntas
El diccionario tendrá el siguiente formato:
```python
preguntas = {
    "¿Capital de Costa Rica?": "San José",
    "¿Cuál es el número primo más pequeño?": "2"
}
```
* La clave corresponde a la pregunta.
* El valor corresponde a la respuesta correcta.

### Funcionamiento
1. El programa debe recorrer todas las preguntas almacenadas en el diccionario.
2. Por cada pregunta:
   * Debe mostrar la pregunta al usuario.
   * Solicitar una respuesta.
   * Verificar si la respuesta es correcta.
   * Mostrar inmediatamente un mensaje indicando si acertó o falló.
3. El programa debe llevar un conteo de respuestas correctas.
4. Al finalizar:
   * Debe mostrar la cantidad total de aciertos.
   * Debe mostrar el porcentaje obtenido.


### Por implementar

* **`pedir_respuesta(pregunta)`**
  * Recibe una pregunta como parámetro.
  * Muestra la pregunta al usuario.
  * Solicita una respuesta.
  * Retorna la respuesta ingresada.

* **`es_correcta(respuesta_usuario, respuesta_correcta)`**
  * Recibe la respuesta del usuario y la respuesta correcta.
  * Compara ambas respuestas.
  * Retorna:
    * `True` si son iguales.
    * `False` en caso contrario.
  * La comparación debe realizarse sin distinguir mayúsculas y minúsculas.

* **`calcular_porcentaje(aciertos, total)`**
  * Recibe la cantidad de aciertos y el total de preguntas.
  * Calcula el porcentaje de respuestas correctas.
  * Retorna el resultado.

* **Bloque principal del programa**
  * Inicializa una variable para almacenar la cantidad de aciertos.
  * Recorre el diccionario utilizando `.items()`.
  * Por cada pregunta:
    * Llama a `pedir_respuesta`.
    * Verifica la respuesta utilizando `es_correcta`.
    * Actualiza el contador de aciertos cuando corresponda.
    * Muestra:
      * `"Correcto"` si acertó.
      * `"Incorrecto"` si falló.
  * Al finalizar:
    * Muestra la cantidad total de aciertos.
    * Muestra el porcentaje calculado utilizando `calcular_porcentaje`.

---

### Ejemplo de ejecución

```text
¿Capital de Costa Rica?
> san josé
Correcto

¿Cuál es el número primo más pequeño?
> 5
Incorrecto

Aciertos: 1
Porcentaje obtenido: 50.00%
```

---

### Recomendaciones
* Puede utilizar `.lower()` o `.upper()` para comparar respuestas sin importar mayúsculas o minúsculas.
* Recuerde que `.items()` permite recorrer simultáneamente la pregunta y la respuesta correcta.
* El porcentaje puede calcularse con la fórmula:

```python
(aciertos / total) * 100
```

---

## Criterios de evaluación

### Funciones
* `pedir_respuesta` implementada correctamente: 15 pts
* `es_correcta` implementada correctamente: 20 pts
* `calcular_porcentaje` implementada correctamente: 15 pts

### Programa
* Recorrido correcto del diccionario utilizando `.items()`: 15 pts
* Conteo correcto de aciertos: 10 pts
* Verificación correcta de respuestas: 10 pts
* Cálculo correcto del porcentaje final: 10 pts

### Código
* Código ordenado, nombres de variables claras y comentarios: 5 pts

**Total:** **100 pts**

---

## Puntos extra
Puede obtener **10 puntos extra** si agrega al menos 5 preguntas adicionales (de cualquier tema).
# Ejercicio POO
## Juego: *¿Quién quiere ser millonario?*

---

## Requerimientos

### 1. Clase `Pregunta`

Representa una pregunta con sus opciones y respuesta correcta.

**Atributos:**

* `dificultad` (int): número de nivel (1 a 15).
* `texto` (str): enunciado de la pregunta.
* `opciones` (list): contiene las cuatro opciones de respuesta.
* `__respuesta_correcta` (str): letra (A–D) de la respuesta correcta.

**Métodos:**

* `__init__(...)`: inicializa los atributos.
* `mostrar_pregunta(self)`: muestra el número de nivel, el texto y las opciones con sus letras.
* `verificar_respuesta(self, respuesta_usuario)`: devuelve `True` si la respuesta coincide con la correcta.

**Debe incluir un getter y setter para el atributo de __respuesta_correcta, que valide si se está ingresando A, B, C o D, en caso contrario resulta en ValueError**
---

### 2. Mixin `Comodin5050Mixin`

Implementa el comodín **50:50**, que elimina dos opciones incorrectas y muestra las dos restantes.

**Método:**

* `usar_5050(self, pregunta: Pregunta)`:

  * Mantiene la respuesta correcta.
  * Elige aleatoriamente una de las otras tres opciones.
  * Muestra las dos opciones restantes en formato:

    ```
    A) opción1
    C) opción2
    ```

---

### 3. Mixin `ComodinCambioMixin`

Permite cambiar la pregunta actual por otra del mismo nivel.

**Método:**

* `usar_cambio(self, nivel, preguntaActual)`: selecciona una nueva pregunta del mismo nivel y la devuelve, asegurando que no sea la misma.

---

### 4. Clase `Juego`

Controla el flujo principal del juego, los niveles, premios y comodines.

**Atributos sugeridos:**

* `preguntas`: lista de objetos `Pregunta`.
* `nivel_actual`: nivel actual del jugador (inicia en 1).
* `jugando`: indica si el juego sigue activo.
* `comodines_usados`: diccionario que registra si los comodines “50:50” y “cambio” ya se usaron.
* `premios`: diccionario con los valores por nivel.

**Métodos:**

* `__init__(self)`: inicializa atributos y estructura de premios.
* `cargar_preguntas(self, ruta)`: lee las preguntas desde un archivo CSV.
  Cada línea tiene el formato:

  ```
  dificultad,pregunta,opcionA,opcionB,opcionC,opcionD,respuesta_correcta
  ```
* `seleccionar_pregunta(self, nivel)`: elige aleatoriamente una pregunta del nivel indicado.
* `calcular_premio(self, correcto)`: devuelve el premio según el nivel y las zonas seguras (nivel 5 y 10).
* `mostrar_comodines(self)`: imprime los comodines disponibles.
* `usar_comodin(self, tipo, preguntaActual)`: ejecuta el comodín solicitado, verificando que no haya sido usado.

---

### 5. Sistema de premios
| Nivel |   Premio   |
| :---: | :--------: |
|   15  | 30 000 000 |
|   14  | 15 000 000 |
|   13  | 10 000 000 |
|   12  |  7 500 000 |
|   11  |  5 000 000 |
|   **10**  |  **3 000 000** * | 
|   9   |  2 000 000 |
|   8   |  1 500 000 |
|   7   |  1 000 000 |
|   6   |   650 000  |
|   **5**   |   **500 000**  * |
|   4   |   400 000  |
|   3   |   300 000  |
|   2   |   200 000  |
|   1   |   100 000  |

* Si el jugador pierde antes del nivel 5, gana ₡0.
* Si pierde entre el nivel 6 y 10, gana ₡500 000.
* Si pierde entre el 11 y el 15, gana ₡3 000 000.
* Si se retira, recibe el premio correspondiente al último nivel superado.

---

### 6. Archivo `menu.py`

Debe contener la función `menu(juego)` y el bloque principal `__main__`.

1. Carga las preguntas.
2. Muestra la pregunta del nivel actual.
3. Permite:
   * Responder (`A`, `B`, `C`, `D`),
   * Usar un comodín (`50:50` o `cambio`),
   * Retirarse del juego.
4. Verificar la respuesta y actualiza el nivel o finaliza el juego.
5. Muestra el premio correspondiente al final.

---

### 7. Estructura final

```
EjemploQQSM/
 ├── qqsm.py         # Contiene Pregunta, Mixins y Juego
 ├── menu.py         # Controla el flujo del juego
 └── preguntas.csv   # Banco de preguntas
```
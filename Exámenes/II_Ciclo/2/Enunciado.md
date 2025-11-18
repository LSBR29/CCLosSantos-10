# II Examen Parcial
## Indicaciones generales
* La duración del examen es de 2h.
* Subir al Google Classroom la solución en el espacio denominado *II Examen*.
  * En caso de tener problemas puede enviar la solución al correo: **[santiagobrenesruiz@gmail.com](mailto:santiagobrenesruiz@gmail.com)**
* Debe entregar el archivo: `main.py`
* El examen es de carácter **individual**.
* Es permitido utilizar una hoja de notas o apuntes.

---

## Sistema: *Gestor de Dispositivos Inteligentes*

Completar en Python el programa para que permita gestionar dispositivos eléctricos inteligentes, calcular su consumo mensual, y determinar cuál de ellos tiene el mayor consumo energético.

---

### Requerimientos

#### 1. Clase `Dispositivo`

Representa un aparato eléctrico común con consumo energético.

**Atributos:**

* `nombre` (str): nombre del dispositivo.
* `horas_dia` (int): horas de uso diario.
* `__consumo_watts` (float): potencia en watts (privado).

**Métodos:**

* `__init__(self, nombre, horas_dia)`: inicializa los atributos.
* `calcular_consumo_mensual(self)`: retorna el consumo en Wh por mes (`consumo_watts * horas_dia * 30`).
* Getter y Setter para el atributo privado (`consumo`) que valide que el valor sea positivo (Puede usar cualquier método).

---

#### 2. Clase `DispositivoInteligente()`

Hereda de la clase `Dispositivo` para incluir funciones adicionales.

**Atributos:**

* `modo_ahorro` (bool): indica si está activado el modo ahorro.

**Métodos:**

* `__init__(self, nombre, consumo, horas_dia, modo=False)`: inicializa los atributos.
  * Usando `super()` para el nombre y las horas.
  * Usando el setter para el consumo.
  * De manera normal, como un atributo para el modo.
* `calcular_consumo_mensual(self)`: amplía el método original y utilizando `super()` permite que:
  * Si `modo_ahorro` es `True`, el consumo mensual se retorna con 20% menos (`consumo*0.8`).
  * Si `modo_ahorro` es `False`, el consumo mensual se retorna igual.
* `__str__(self)`: retorna el nombre del dispositivo, su consumo mensual y el estado del modo ahorro.

---

#### 3. Clase `Gestor`

Controla los dispositivos.

**Atributos:**

* `dispositivos` (list): lista de objetos `DispositivoInteligente`.

**Métodos:**

* `__init__(self)`: inicializa la lista vacía.
* `agregar_dispositivo(self, dispositivo)`: añade un nuevo dispositivo.
* `mostrar_todos(self)`: muestra todos los dispositivos usando `print(objeto)`.
* `mayor_consumo(self)`: identifica y devuelve el objeto de **mayor consumo mensual**.
  * Recomendación: ordenar la lista de dispositivos según el consumo de cada dispositivo.
  * Puede utilizar la función `sorted(iterable, key=function, reverse=bool)`, donde `function` puede ser creada con `lambda` o `def`.
* **Extra:** `menor_consumo(self)`: identifica y devuelve el objeto de **menor consumo mensual**.

---

### Ejemplo de salida esperada
En el archivo `main.py` se encuentra el ejemplo a ejecutar, se espera que produzca la siguiente salida:
*No es necesario, pero si lo requiere puede modificar el ejemplo*
```
Dispositivo: Bombillo LED - Consumo mensual: 3600.0 Wh (Modo ahorro: True)
Dispositivo: Enchufe WiFi - Consumo mensual: 7200.0 Wh (Modo ahorro: False)

El Enchufe WiFi es el que consume más energía.
El Bombillo LED es el que consume menos energía.
```

---

## Criterios de Evaluación
- Definición correcta de las clases: 15pts
- Correcta inicialización de atributos : 20pts
- Uso adecuado de herencia y `super()` : 10pts
- Implementación correcta del getter : 10pts
- Validación de datos en el setter (valores positivos) : 10pts
- Implementación correcta del método `calcular_consumo_mensual()` : 15pts
- Implementación correcta del método `__str__()` : 5pts
- Implementación correcta del método `mostrar_todos()` : 5pts
- Implementación correcta del método `mayor_consumo()` : 10pts
- **Extra:** Comentarios claros en el código : 5 pts
- **Extra:** Método `menor_consumo()` funcional : 10pts

**Total:** **115 pts**
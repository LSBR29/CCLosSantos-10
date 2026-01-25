# Ejercicio POO
## Simulador de Dispositivos Inteligentes

---

## Requerimientos

### 1. Clase base `Dispositivo`

Representa cualquier aparato electrónico del hogar.

**Atributos:**

* `nombre` (string, publico): nombre del dispositivo.
* `encendido` (bool, público): indica si está encendido o apagado.

**Métodos:**

* `__init__(self, nombre)`: inicializa con el nombre y `encendido=False`.
* `encender(self)`: cambia el estado a `True`.
* `apagar(self)`: cambia el estado a `False`.
* `mostrar_info(self)`: devuelve un string con el formato:
  `"Dispositivo: <nombre> | Encendido: <True/False>"`.

---

### 2. Clase hija `LuzInteligente`

Hereda de `Dispositivo` y añade control de brillo.

**Atributos adicionales:**

* `__brillo` (int, privado): nivel de brillo entre 0 y 100.

**Métodos:**

* `get_brillo(self)`: devuelve el nivel actual de brillo.
* `set_brillo(self, valor)`: actualiza el brillo solo si `0 <= valor <= 100`.
* `mostrar_info(self)`: sobrescribe al padre para incluir el brillo.

---

### 3. Clase hija `CafeteraInteligente`

Hereda de `Dispositivo` y puede preparar café si está encendida.

**Métodos:**

* `preparar_cafe(self)`:

  * Si el dispositivo está apagado, devuelve `"No se puede preparar café: la cafetera está apagada."`
  * Si está encendido, devuelve `"Café preparado correctamente."`.
* `mostrar_info(self)`: sobrescribe al padre, agregando el texto `"Tipo: Cafetera Inteligente"`.

---

### 4. Clase `RegistroMixin`

Esta clase permite registrar eventos en una lista.

**Métodos:**

* `registrar_evento(self, mensaje)`: agrega un mensaje a una lista `registros`.
* `mostrar_registros(self)`: devuelve todos los mensajes almacenados.

---

### 5. Integración del Mixin

Cree una clase `LuzRegistrable` que **herede de `LuzInteligente` y `RegistroMixin`** y tenga como atributo una lista `registros`.
Debe registrar automáticamente cada cambio de brillo o encendido/apagado con el mensaje correspondiente:

Ejemplo de mensajes esperados:

```
"Encendida la luz del dormitorio"
"Brillo ajustado a 80%"
"Apagada la luz del dormitorio"
```

Para hacerlo, sobrescriba los métodos `encender()`, `apagar()` y `set_brillo()`
de modo que, además de ejecutar la acción original (con `super()`), llamen a `registrar_evento()` con el mensaje correcto.

---

## Resultado esperado (ejemplo)

```
Café preparado correctamente.

--- ESTADO DE DISPOSITIVOS ---
Dispositivo: Dormitorio | Encendido: False | Brillo: 80%
Dispositivo: Cafetera Principal | Encendido: True | Tipo: Cafetera Inteligente

--- REGISTRO DE EVENTOS ---
Encendida la luz: Dormitorio
Brillo ajustado a 80%
Apagada la luz Dormitorio
```
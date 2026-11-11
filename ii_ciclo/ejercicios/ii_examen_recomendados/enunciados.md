# Ejercicios Recomendados

### 1. Clase `Planta`

Crear una clase `Planta` que lleve el control de la altura de una planta en un jardín.

**Requisitos**

* Atributos `nombre` (str) y `altura` (int, en cm). La altura empieza en `10` y no se recibe como parámetro.
* `regar()` aumenta la altura en `2` cm.
* `necesita_poda()` devuelve `True` si la altura es mayor que `20`, si no devuelve `False`.
* `mostrar_info()` devuelve un `str` con el formato `<nombre> | Altura <altura> cm`.

**Ejemplo de ejecución**

```python
if __name__ == "__main__":
    albahaca = Planta("Albahaca")
    menta = Planta("Menta")

    for _ in range(6):
        albahaca.regar()
    menta.regar()
    menta.regar()

    print(albahaca.mostrar_info())
    print(menta.mostrar_info())
    print(albahaca.necesita_poda())
    print(menta.necesita_poda())
```

**Salida esperada**

```
Albahaca | Altura 22 cm
Menta | Altura 14 cm
True
False
```

---

### 2. Clase `Fraccion`

Crear una clase `Fraccion` que represente una fracción con numerador y denominador. Puede asumir que ambos son enteros positivos.

**Requisitos**

* Atributos `numerador` y `denominador`.
* `valor()` devuelve el resultado decimal de la división, sin modificar la fracción.
* `simplificar()` modifica la fracción dividiendo numerador y denominador entre su máximo común divisor (puede usar `math.gcd`).
* `__str__` devuelve el texto `numerador/denominador`, por ejemplo `3/4`.
* `__eq__` y `__lt__` comparan dos fracciones por su valor. Así, `1/2` y `2/4` deben ser iguales aunque no estén simplificadas.

**Ejemplo de ejecución**

```python
if __name__ == "__main__":
    a = Fraccion(1, 2)
    b = Fraccion(2, 4)
    c = Fraccion(3, 4)

    print(a, b, c)
    print(a == b)
    print(a < c)
    print(c < a)
    print(c.valor())

    b.simplificar()
    print(b)
```

**Salida esperada**

```
1/2 2/4 3/4
True
True
False
0.75
1/2
```

---

### 3. Clase `Usuario`

Crear una clase `Usuario` que proteja su clave y bloquee la cuenta después de varios intentos fallidos.

**Requisitos**

* Atributo público `nombre`, y atributos privados `__clave` y `__intentos_fallidos` (empieza en `0`).
* El constructor recibe `nombre`, `clave` y `correo`.
* Propiedad `correo` con `@property` y `@correo.setter`. El setter lanza `ValueError("Correo inválido")` si el texto no contiene `@`. El constructor debe asignar el correo usando esta propiedad.
* Propiedad `bloqueada` de solo lectura (solo `@property`, sin `setter`). Devuelve `True` si hay 3 intentos fallidos o más.
* `iniciar_sesion(clave)` si la cuenta está bloqueada devuelve `False`. Si la clave es correcta reinicia los intentos fallidos y devuelve `True`. Si es incorrecta suma un intento fallido y devuelve `False`.

**Ejemplo de ejecución**

```python
if __name__ == "__main__":
    usuario = Usuario("ana", "python2026", "ana@correo.com")

    print(usuario.iniciar_sesion("1234"))
    print(usuario.iniciar_sesion("python2026"))

    for _ in range(3):
        usuario.iniciar_sesion("0000")
    print(usuario.bloqueada)
    print(usuario.iniciar_sesion("python2026"))

    try:
        usuario.correo = "sin-arroba"
    except ValueError as error:
        print(error)

    try:
        usuario.bloqueada = False
    except AttributeError:
        print("bloqueada es de solo lectura")

    try:
        print(usuario.__clave)
    except AttributeError:
        print("La clave es privada")
```

**Salida esperada**

```
False
True
True
False
Correo inválido
bloqueada es de solo lectura
La clave es privada
```

---

### 4. Clases `Envio`, `EnvioExpress` y `EnvioInternacional`

Una empresa de mensajería necesita calcular el costo de sus envíos según el tipo.

**Requisitos**

* Clase base `Envio` con atributos `destino` (str) y `peso` (int, en kg).
* `calcular_costo()` devuelve `peso * 500`.
* `__str__` devuelve `Envío a <destino> | <peso> kg | Costo ₡<costo>`, usando `calcular_costo()`.
* Clase hija `EnvioExpress` sobreescribe `calcular_costo()` para agregar `2000` al costo normal (use `super()`).
* Clase hija `EnvioInternacional` agrega el atributo `pais` (use `super().__init__`) y sobreescribe `calcular_costo()` para duplicar el costo normal (use `super()`). Su `__str__` agrega ` | País <pais>` al final (use `super()`).

**Ejemplo de ejecución**

```python
if __name__ == "__main__":
    envios = [
        Envio("Cartago", 2),
        EnvioExpress("Heredia", 3),
        EnvioInternacional("Madrid", 4, "España"),
    ]

    total = 0
    for envio in envios:
        print(envio)
        total += envio.calcular_costo()

    print(f"Total ₡{total}")
```

**Salida esperada**

```
Envío a Cartago | 2 kg | Costo ₡1000
Envío a Heredia | 3 kg | Costo ₡3500
Envío a Madrid | 4 kg | Costo ₡4000 | País España
Total ₡8500
```

---

### 5. Robots con habilidades

Crear robots que puedan combinar habilidades usando mixins.

**Requisitos**

* Clase `Robot` con atributo público `nombre` y atributo privado `__bateria`, que empieza en `100`.
* Propiedad `bateria` de solo lectura.
* `mover()` gasta `10` de batería y devuelve `<nombre> se movió`. Si quedan menos de `10`, no gasta nada y devuelve `<nombre> no tiene batería`.
* `VoladorMixin` con el método `volar()`, que devuelve `<nombre> está volando`.
* `NadadorMixin` con el método `nadar()`, que devuelve `<nombre> está nadando`.
* `RobotVolador` hereda de `Robot` y `VoladorMixin`.
* `RobotAnfibio` hereda de `Robot`, `VoladorMixin` y `NadadorMixin`.

**Ejemplo de ejecución**

```python
if __name__ == "__main__":
    halcon = RobotVolador("Halcon")
    nautilus = RobotAnfibio("Nautilus")

    print(halcon.volar())
    print(hasattr(halcon, "nadar"))

    print(nautilus.volar())
    print(nautilus.nadar())
    print(nautilus.mover())
    print(nautilus.bateria)

    for _ in range(9):
        nautilus.mover()
    print(nautilus.bateria)
    print(nautilus.mover())

    for clase in RobotAnfibio.__mro__:
        print(clase.__name__)

    try:
        nautilus.bateria = 50
    except AttributeError:
        print("La batería es de solo lectura")
```

**Salida esperada**

```
Halcon está volando
False
Nautilus está volando
Nautilus está nadando
Nautilus se movió
90
0
Nautilus no tiene batería
RobotAnfibio
Robot
VoladorMixin
NadadorMixin
object
La batería es de solo lectura
```
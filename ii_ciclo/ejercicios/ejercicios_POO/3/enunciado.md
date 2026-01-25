# Ejercicio POO

## Sistema: *Gestor de Suscripciones Digitales*

---

## Requerimientos

### 1. Clase `Suscripcion`

Representa una suscripción digital a un servicio.

**Atributos:**

* `nombre` (str): nombre del plan o suscripción.
* `__duracion` (int): duración en meses (valor mayor que 0, privado).
* `premium` (bool): indica si la suscripción es premium (`True`) o básica (`False`).

**Métodos:**

* `__init__(self, nombre, premium=False)`: inicializa los atributos.
* Getters y Setters para el atributo privado `duracion`.

  * El setter debe generar un error si se asigna un valor no positivo.
* `calcular_total(self)`:

  * Si la suscripción **no es premium**, el costo es `1000` por cada mes.
  * Si la suscripción **es premium**, el costo es un `10%` más que lo calculado para no premium.
  * Retorna el total a pagar según la duración.
* `__str__(self)`:

  * Devuelve una descripción legible con el nombre, duración y costo total, indicando si es premium.

---

### 2. Clase `GestorSuscripciones`

Administra el conjunto de suscripciones registradas.

**Atributos:**

* `suscripciones` (list): lista de objetos `Suscripcion`.

**Métodos:**

* `__init__(self)`: inicializa la lista vacía.
* `agregar_suscripcion(self, suscripcion)`: agrega una nueva suscripción al registro.
* `mostrar_todas(self)`: muestra todas las suscripciones con `print(objeto)`.
* `filtrar_premium(self)`:

  * Muestra únicamente las suscripciones que sean **premium**.

---

### 3. Ejemplo de salida esperada

```
Suscripción: Básica - Duración: 3 meses - Total: 3000 (Premium: False)
Suscripción: Premium Plus - Duración: 6 meses - Total: 6600 (Premium: True)
Suscripción: Premium Music - Duración: 12 meses - Total: 13200 (Premium: True)

Suscripciones Premium registradas:
Premium Plus
Premium Music
```

Puede utilizar el siguiente código como ejemplo a ejecutar:
```python
if __name__ == "__main__":
    s1 = Suscripcion("Básica", False)
    s1.duracion = 3

    s2 = Suscripcion("Premium Plus", True)
    s2.duracion = 6
    
    s3 = Suscripcion("Premium Music", True)
    s3.duracion = 12

    gestor = GestorSuscripciones() 
    gestor.agregar_suscripcion(s1)
    gestor.agregar_suscripcion(s2)
    gestor.agregar_suscripcion(s3)

    gestor.mostrar_todas()

    print("\nSuscripciones Premium registradas:")
    for s in gestor.filtrar_premium():
        print(s.nombre)
```
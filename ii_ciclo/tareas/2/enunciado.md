# Tarea 2
## Descripción
Esta tarea consiste en desarrollar un programa en Python que modele **personajes de un juego** utilizando conceptos de la Programación Orientada a Objetos.
Recuerde incluir **comentarios y nombres descriptivos**.

---

## Requerimientos
### Clase `Personaje`
* **Atributos:**
  * `nombre` (string, público).
* **Métodos:**
  * `mostrar_info(self)`: retorna un string en el formato:
    `"Nombre: <nombre>"`.

---

### Clase `Arquero` (hereda de `Personaje`)
* **Atributos:**
  * `flechas` (int, público), con 10 como valor por defecto (si no se da el parámetro).
* **__init__:**
  * Recibe `nombre`, `flechas`.
  * Usa `super()` para inicializar `nombre`.
* **Métodos:**
  * `mostrar_info(self)`: extiende el método heredado y devuelve:
    `"Nombre: <nombre>, Flechas: <flechas>"`.

---

### Clase `Guerrero` (hereda de `Personaje` y de `ArmaduraMixin`)
* **Atributos:**
  * `vida_maxima` (int, público), con 100 como valor por defecto (si no se da el parámetro).
  * `__vida` (int, privado), que al crear el guerrero empieza igual a su `vida_maxima`.
  * `armadura` (int, público), con 5 como valor por defecto (si no se da el parámetro).
* **__init__:**
  * Debe recibir `nombre`, `vida_maxima`, `armadura`.
  * Usar `super()` para inicializar `nombre`.
* **Métodos:**
  * Getter: devuelve la vida.
  * Setter: solo actualiza la vida si el nuevo valor es una vida posible para el guerrero, es decir, que no sea negativa ni mayor que su `vida_maxima`. Si no lo es, la vida se queda como estaba.
  * `mostrar_info(self)`: extiende el método heredado y devuelve:
    `"Nombre: <nombre>, Vida: <vida>/<vida_maxima>, Armadura: <armadura>"`.

---

### Clase `ArmaduraMixin`
* **Método:**
  * `reducir_dano(self, dano, armadura)`: recibe el daño de un golpe y el valor de una armadura.
    Devuelve el daño que realmente se recibe, que es `dano - armadura`; si el golpe no supera la armadura, devuelve 0.

> Esta clase no tiene constructor ni atributos propios, solo implementa la funcionalidad.
---

### Integración del Mixin
La clase `Guerrero` debe heredar de la clase `ArmaduraMixin` para poder reducir el daño de los golpes que recibe.

---

### Requisitos de demostración
Para comprobar las funcionalidades debe incluir lo siguiente en su código:
* Crear un objeto arquero
* Mostrar la información del arquero
* Crear un objeto guerrero
* Mostrar la vida del guerrero, modificarla y mostrarla nuevamente (utilizando el getter y setter)
* Reducir el daño de un golpe con la armadura del guerrero y mostrar el resultado

---

## Ejemplo de ejecución (Su solución no puede usar exactamente los datos de este ejemplo)
```txt
Datos del arquero: Nombre: Alex, Flechas: 8

Vida del guerrero Steve: 100
Vida del guerrero Steve modificada a: 60

Daño del golpe con armadura de 8: 22
```

---

## Criterios de Evaluación
* **Definición correcta de clases y atributos**: 15%
* **Uso de atributos privados y getters/setters con validación**: 20%
* **Herencia y sobrescritura de métodos (`mostrar_info`)**: 20%
* **Uso correcto de `super()`**: 15%
* **Uso del Mixin funcional (`reducir_dano`)**: 15%
* **Demostración con ejemplos claros**: 10%
* **Comentarios y claridad del código**: 5%
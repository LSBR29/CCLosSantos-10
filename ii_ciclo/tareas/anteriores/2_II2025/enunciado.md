# Tarea 2
## Descripción
Esta tarea consiste en desarrollar un programa en Python que modele una **biblioteca** utilizando conceptos de la Programación Orientada a Objetos.
Recuerde incluir **comentarios y nombres descriptivos**.

---

## Requerimientos
### Clase `Publicacion`
* **Atributos:**
  * `titulo` (string, público).
  * `autor` (string, público).
* **Métodos:**
  * `mostrar_info(self)`: retorna un string en el formato:
    `"Título: <titulo>, Autor: <autor>"`.

---

### Clase `Revista` (hereda de `Publicacion`)
* **Atributos:**
  * `numero_edicion` (int, público), con 1 como valor por defecto (si no se da el parámetro).
* **__init__:**
  * Recibe `titulo`, `autor`, `numero_edicion`.
  * Usa `super()` para inicializar `titulo` y `autor`.
* **Métodos:**
  * `mostrar_info(self)`: extiende el método heredado y devuleve:
    `"Título: <titulo>, Autor: <autor>, Edición: <numero_edicion>"`.

---

### Clase `Libro` (hereda de `Publicacion`)
* **Atributos:**
  * `__paginas` (int, privado), con 1 como valor por defecto (si no se da el parámetro).
  * `precio` (float, público), con 0 como valor por defecto (si no se da el parámetro).
* **__init__:**
  * Debe recibir `titulo`, `autor`, `paginas`, `precio`.
  * Validar que `paginas > 0` (si no, asignar 1).
  * Usar `super()` para inicializar `titulo` y `autor`.
* **Métodos:**
  * Getter: devuelve el número de páginas.
  * Setter: solo actualiza el número de páginas si `valor > 0`.
  * `mostrar_info(self)`: extiende el método heredado y devuleve:
    `"Título: <titulo>, Autor: <autor>, Páginas: <paginas>, Precio: <precio>"`.

---

### Clase `ConDescuentoMixin`
* **Método:**
  * `aplicar_descuento(self, precio, porcentaje)`: recibe un precio y un porcentaje (0–100).
    Devuelve el precio final luego de aplicar el descuento.

> Esta clase no tiene constructor ni atributos propios, solo implementa la funcionalidad.
---

### Integración del Mixin
La clase `Libro` debe heredar de la clase `ConDescuentoMixin` para poder aplicar descuentos a sus precios.

---

### Requisitos de demostración
Para comprobar las funcionalidades debe incluir lo siguiente en su código:
* Crear un objeto revista
* Mostrar la información de la revista
* Crear un objeto libro
* Mostrar el número de páginas del libro, modificarlas y mostrarlas nuevamente (utilizando el getter y setter)
* Aplicar un descuento al libro y mostrar el precio final

---

## Ejemplo de ejecución
```txt
Datos de la revista: Título: Nature, Autor: Norman Lockyer, Edición: 2025

Páginas del libro Dune: 779
Páginas del libro Dune modificadadas a: 10000

Precio del libro Dune sin descuento: 8900
Precio del libro Dune con descuento de 25%: 6675.0
```

---

## Criterios de Evaluación
* **Definición correcta de clases y atributos**: 15%
* **Uso de atributos privados y getters/setters con validación**: 20%
* **Herencia y sobrescritura de métodos (`mostrar_info`)**: 20%
* **Uso correcto de `super()`**: 15%
* **Uso del Mixin funcional (`aplicar_descuento`)**: 15%
* **Demostración con ejemplos claros**: 10%
* **Comentarios y claridad del código**: 5%
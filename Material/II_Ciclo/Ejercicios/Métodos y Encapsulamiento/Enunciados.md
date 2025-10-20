# Ejercicios `Métodos y Encapsulamiento`

### 1. Clase `Libro`
Crea una clase `Libro` con los atributos públicos `titulo` y `autor`. 
Implementar un método `info()` que retorne la información del libro con el formato:
```
Título: <titulo>, Autor: <autor>
```

**Requisitos:**
* Al crear un objeto se deben dar el `titulo` y `autor`.
* `info()` debe devolver una `str` exactamente en el formato indicado.

---

### 2. Clase `CuentaBancaria`
Implementar una clase `CuentaBancaria` que gestione un saldo privado.
La clase debe permitir depositar, retirar y consultar el saldo de forma segura.

**Requisitos:**
* El atributo del saldo debe ser privado: `__saldo`.
* Al crear un objeto se debe dar un saldo inicial o tomar 0 por defecto.
* Método `depositar(monto)`:
  * Aumenta `__saldo` en `monto`.
  * Debe validar que `monto` sea un número positivo; si no, imprimir `Error`
* Método `retirar(monto)`:
  * Disminuye `__saldo` en `monto` si hay suficiente saldo y `monto` es positivo.
  * Si `monto` es mayor que el saldo o no es positivo, imprimir `Error`
* Método `consultar_saldo()` que retorne el saldo actual.

---

## 3. Clase `Termostato`
Diseñar una clase `Termostato` que contenga la temperatura interna en grados Celsius y permita leerla y ajustarla mediante propiedades. Además, que tenga un método para convertir a Fahrenheit.

**Requisitos:**
* La temperatura debe ser un atributo privado: `__temperatura_c`.
* Implementar la propiedad `temperatura` con `@property` y `@temperatura.setter`:
  * El `getter` devuelve la temperatura en °C.
  * El `setter` primero valida que la temperatura esté en el rango de `-50` a `150` °C y luego modifica el atributo; si no, imprimir `Error`.
* Método `a_fahrenheit()` que retorne el valor de la temperatura en °F (usando la fórmula `°F = °C * 9/5 + 32`).

---

## 4. Clase `Producto`
Crear una clase `Producto` con atributos privados para nombre y precio.
Debe exponer el precio con `@property` y permitir aplicar descuentos.
Además, se debe implemetar la comparación entre productos por precio.

**Requisitos:**
* Atributos privados: `__nombre`, `__precio`.
* Propiedad `nombre` de solo lectura (solo `@property`, sin `setter`).
* Propiedad `precio` con `@property` y `@precio.setter` que valide que el precio no sea negativo; si lo es, imprimir `Error`.
* Método `aplicar_descuento(porcentaje)` que reciba un número entre `0` y `100` y reduzca el precio en ese porcentaje.
* Implementar `__lt__` y `__eq__` para comparar productos por precio.
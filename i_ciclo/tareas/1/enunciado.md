# Tarea 1

## Descripción

Esta tarea consiste en **dos ejercicios independientes** en los que se utilizarán principalmente **variables, tipos de datos, entrada y salida, manejo de errores, expresiones y manejo de strings**.

Debe añadir comentarios descriptivos a su solución, así como asignar nombres de variables claros.

Cada ejercicio tiene un valor de **50%**.

---

## Ejercicio 1: Sistema de Facturación (50%)

Se requiere un programa en Python que simule el cálculo de una factura a partir de los datos ingresados por el usuario.

El programa debe solicitar:

1. **Nombre del cliente (string)**
2. **Nombre del producto (string)**
3. **Precio unitario (float)**
4. **Cantidad (int)**
5. **Porcentaje de IVA (int)**
6. **Porcentaje de descuento (int)**

El programa debe calcular:

* Subtotal (El precio unitario multiplicado por la cantidad)
* Monto del IVA (El subtotal multiplicado por el porcentaje de IVA)
* Monto del descuento (El subtotal multiplicado por el porcentaje de descuento)
* Total final a pagar (El subtotal más el IVA menos el descuento)

El programa debe mostrar:

* Nombre del cliente en mayúsculas
* Nombre del producto en minúsculas
* Subtotal
* IVA
* Descuento
* Total

Se debe utilizar `try/except` para manejar errores en la conversión de números, puede utilizar `exit()` para cerrar el programa si se dió algún error.

### **Ejemplo de Ejecución**

```
Ingrese el nombre del cliente: Santiago Brenes
Ingrese el nombre del producto: Cuaderno
Ingrese el precio unitario: 500
Ingrese la cantidad: 2
Ingrese el porcentaje de IVA: 13
Ingrese el porcentaje de descuento: 5

FACTURA
Cliente: SANTIAGO BRENES
Producto: cuaderno

Subtotal: 1000.0
IVA: 130.0
Descuento: 50.0
Total a pagar: 1080.0
```

---

## Ejercicio 2: Generador de Código (50%)

Se requiere un programa en Python que genere automáticamente un código a partir de los datos de un estudiante.

El programa debe solicitar:

1. **Nombre completo**
2. **Año de ingreso**
3. **Número de identificación**

El programa debe generar:

* Nombre en mayúsculas
* Nombre invertido
* La inicial
* Últimos 3 dígitos del número de identificación
* Código estudiantil con la inicial, los dígitos de identificación y el año de ingreso
* Un correo electrónico con el código estudiantil

No se permite el uso de condicionales.

### **Ejemplo de Ejecución**

```
Ingrese su nombre completo: Santiago Brenes
Ingrese el año de ingreso: 2026
Ingrese su número de identificación: 123456789

RESULTADO
Nombre en mayúsculas: SANTIAGO BRENES
Nombre invertido: senerB ogaitnaS
Inicial: S
Últimos 3 dígitos: 789
Código estudiantil: S_789_2026
Correo institucional: S_789_2026@ccls.cr
```

---

## Criterios de Evaluación

### Ejercicio 1 (50%)

* **Entrada y declaración de variables (10%)**: Uso correcto de tipos de datos.
* **Cálculos matemáticos (15%)**: Subtotal, IVA, descuento y total correctos.
* **Manejo de strings (10%)**: Uso correcto de métodos necesarios.
* **Manejo de errores (5%)**: Uso adecuado de `try/except`.
* **Presentación y formato (5%)**: Salida ordenada y clara.
* **Comentarios en el código (5%)**

---

### Ejercicio 2 (50%)

* **Entrada y declaración de variables (10%)**: Uso correcto de tipos de datos.
* **Generación de código y correo (15%)**: Construcción correcta utilizando strings.
* **Manejo de strings (10%)**: Uso correcto de métodos necesarios.
* **Presentación y formato (5%)**: Salida ordenada y clara.
* **Comentarios en el código (5%)**

---

## **Entrega**

* El código de cada ejercicio debe estar en **archivos separados** (`ejercicio1.py` y `ejercicio2.py`).
* Subir los archivos `.py` en la sección correspondiente de **Google Classroom**.

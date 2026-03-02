# Tarea 1
## Descripción
Esta tarea consiste en **dos ejercicios independientes** en los que se utilizará principalemente el **manejo de strings y la estructura de control `if-elif-else`**.
Debe añadir comentarios descriptivos a su solución, así como asignar nombres de variables claros.

---

## Ejercicio 1: Validación de datos
Se requiere un programa en Python que solicite información personal al usuario y valide que cada dato cumpla con ciertas condiciones antes de mostrar un resumen con la información ingresada.

1. **Nombre completo**: Debe contener únicamente letras y espacios.
    - _Sugerencia_: Verifique que el string al quitarle los espacios en blanco sea distinto de `""` posea únicamente letras. Esto se realiza porque `isalpha()` no reconoce a los espacios como letras.
2. **Edad**: Debe ser un número entero positivo.
3. **Correo electrónico**: Debe contener el carácter `@`.
4. **Número de teléfono**: Debe contener solo dígitos y 8 caracteres.  
5. **País de residencia**: No puede estar vacío.
    - _Sugerencia_: Verifique que el string al quitarle los espacios alrededor sea distinto de `""` (un string vacío).

Si un dato ingresado es inválido, se debe mostrar un mensaje de error explicando la razón.
Si todos los datos son válidos, el programa debe mostrar un resumen con la información ingresada.

### **Ejemplo de Ejecución**
```
Ingrese su nombre completo: Juan Pérez
Ingrese su edad: 25
Ingrese su correo electrónico: juanperez@gmail.com
Ingrese su número de teléfono: 87654321
Ingrese su país de residencia: Costa Rica

Registro exitoso. Información ingresada:
Nombre: Juan Pérez
Edad: 25
Correo: juanperez@gmail.com
Teléfono: 87654321
País: Costa Rica
```

Si el usuario ingresa datos inválidos, el programa debe mostrar un mensaje de error:
```
Ingrese su nombre completo: Juan123
Error: El nombre solo debe contener letras y espacios.

Ingrese su edad: -5
Error: La edad debe ser un número entero positivo.

Ingrese su correo electrónico: juanperezgmail.com
Error: El correo debe contener '@' y un dominio válido.

Ingrese su número de teléfono: 12345
Error: El número de teléfono debe contener al menos 8 dígitos.

No se pudo realizar el registro del usuario.
```

### Criterios de Evaluación
- **Validación de Nombre (10%)**: Debe contener únicamente letras y espacios.
- **Validación de Edad (5%)**: Debe ser un número entero positivo.
- **Validación de Correo Electrónico (10%)**: Debe contener el carácter `@`.
- **Validación de Número de Teléfono (10%)**: Debe contener solo dígitos y 8 caracteres.
- **Validación del País de Residencia (5%)**: No puede estar vacío.
- **Presentación del Resumen (10%)**: Si todos los datos son válidos, debe mostrarse un resumen con la información ingresada.

---

## Ejercicio 2: Conversor de monedas
Se requiere un programa en Python que imprima un menú de conversión de monedas con 4 opciones numeradas y solicite al usuario el número de opción que quiere para luego ejecutar la conversión.
En cada caso debe solicitar la cantidad de dinero a convertir.

1. **Colones a Dolares**
    - _Conversión_: Un dolar equivale a 490 colones.
2. **Colones a Euros**
    - _Conversión_: Un euro equivale a 550 colones.
3. **Dolares a Colones**
    - _Conversión_: Un dolar equivale a 490 colones.
4. **Euros a Colones**
    - _Conversión_: Un euro equivale a 550 colones.

Si se ingresa un número inválido debe imprimir un mensaje de error.
Recuerde que se pueden utilizar números con decimales.

### **Ejemplo de Ejecución**
```
Bienvenido al Conversor de Monedas
1. Colones a Dolares
2. Colones a Euros
3. Dolares a Colones
4. Euros a Colones

Seleccione una opción: 3
Ingrese la cantidad de dolares a convertir: 50

50 dolares equivalen a 24500 colones
```

En caso de indicar una opción inválida:
```
Bienvenido al Conversor de Monedas
1. Colones a Dolares
2. Colones a Euros
3. Dolares a Colones
4. Euros a Colones

Seleccione una opción: 6
Error esa opción no existe
```

Si la cantidad monetaria no es un número o es negativa:
```
Bienvenido al Conversor de Monedas
1. Colones a Dolares
2. Colones a Euros
3. Dolares a Colones
4. Euros a Colones

Seleccione una opción: 2
Ingrese la cantidad de colones a convertir: numeros
Error debe ingresar un número
```
### Criterios de Evaluación
- **Impresión del menú (10%)**: Imprime el menú con un orden claro.
- **Conversión de colones a dolares (5%)**: Conversión correcta.
- **Conversión de colones a euros (5%)**: Conversión correcta.
- **Conversión de dolares a colones (5%)**: Conversión correcta.
- **Conversión de euros a colones (5%)**: Conversión correcta.
- **Manejo de errores (20%)**: Solo se permiten las opciones impresas y cantidades positivas.

---

## **Entrega**
- El código de cada ejercicio debe estar en **archivos separados** (`ejercicio1.py` y `ejercicio2.py`).
- Subir los archivos `.py` en la sección correspondiente de **Google Classroom**.
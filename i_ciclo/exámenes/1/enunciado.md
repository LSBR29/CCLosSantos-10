# I Examen
## Indicaciones generales
- La duración del examen es de 2h.
- Subir al Google Classroom las soluciones en el espacio denominado *I Examen*.
    - En caso de tener problemas puede enviar la solución al correo santiagobrenesruiz@gmail.com
- Debe entregar el archivo: `ejercicio.py`.
- El examen es de carácter individual.
- Es permitido utilizar una hoja notas o apuntes.

---

## Registro de visitantes
Una empresa desea registrar la información de exactamente **3 visitantes**. Para cada visitante se debe solicitar su **nombre** (texto) y su **edad** (número entero).
El programa debe procesar los datos y mostrar varias listas con información.

---

### Funcionamiento

1. **Entrada de datos**
   - Solicitar al usuario el nombre y la edad de cada uno de los 3 visitantes.
   - Para la **edad**, usar un bloque `try-except` para capturar errores de tipo `ValueError` (por si el usuario ingresa texto). En caso de error, asignar automáticamente `edad = 0`.

2. **Almacenamiento**
   - Guardar todos los nombres en una lista llamada `nombres`.
   - Guardar todas las edades en una lista llamada `edades`.

3. **Procesamiento para cada visitante**
   Para cada uno de los 3 visitantes (utilizando su índice en las listas), obtener:
   - **Primera letra** del nombre.
   - **Paridad de la edad**:
     - Si la edad es 0 (por error de entrada): guardar `"error"`.
     - Si la edad es par: guardar el string `"par"`.
     - Si la edad es impar: guardar `"impar"`.

   *Recuerde que la paridad se puede obtener según el resultado del residuo con 2 (número \% 2)*
   
4. **Salida**
   Mostrar en pantalla de forma clara:
   - La lista `nombres`.
   - La lista `edades`.
   - La lista `primeras_letras`: lista con la primera letra de cada nombre.
   - La lista `paridades`: lista con los strings `"par"`, `"impar"` o `"error"`.
   - Extra: Mostrar la edad máxima

> **Nota:** No es necesario validar que la edad sea un número positivo ni que el nombre no esté vacío; se asume que el usuario puede ingresar cualquier texto.
---

### Criterios de Evaluación
- Lectura de los 3 nombres y 3 edades: 15 pts
- Manejo de errores con `try-except` para cada edad: 15 pts
- Almacenamiento correcto en listas `nombres` y `edades`: 10 pts
- Obtención de la primera letra de cada nombre: 15 pts
- Determinación de paridad de cada edad: 15 pts
- Construcción y presentación de las listas `primeras_letras`, `paridades`: 10 pts
- Impresión ordenada y clara de todas las listas: 5 pts
- Código ordenado, nombres de variables claras y comentarios: 5 pts
- **Extra:** Imprimir la edad máxima encontrada: 10 pts
- **Total** **100 pts**

---

### Ejemplo de ejecución

```
Visitante 1
Nombre: María
Edad: 12

Visitante 2
Nombre: Carlos
Edad: quince
Error: edad no válida, se asigna 0.

Visitante 3
Nombre: Cristina
Edad: 17

Resultados
Nombres: ['María', 'Carlos', 'Cristina']
Edades: [12, 0, 17]
Primeras letras: ['M', 'C', 'C']
Paridades: ['par', 'error', 'impar']
Edad Máxima: 17 (PUNTOS EXTRA)
```
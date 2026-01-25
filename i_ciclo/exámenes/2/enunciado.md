# II Examen Parcial
## Indicaciones generales
- La duración del examen es de 2h.
- Subir al Google Classroom las soluciones en el espacio denominado *II Examen Parcial*.
    - En caso de tener problemas puede enviar la solución al correo santiagobrenesruiz@gmail.com
- Entregue un documento ejecutable: `ejercicio.py`.
- El examen es de carácter individual.
- Es permitido utilizar una hoja notas o apuntes.

---

## Ejercicio: Calculadora inteligente  
Implemente en Python una calculadora de operaciones básicas (suma, resta, multiplicación, división) que permita al usuario realizar múltiples operaciones, además que permita repetir la última operación (ANS) y ver el historial de cálculos realizados.
El programa debe mostrar un menú hasta que el usuario decida salir.

---

### Requerimientos
1. El menú principal debe contar con las siguientes opciones:
   - 1 - Nueva operación
   - 2 - Ver historial
   - 3 - Salir
2. Para nuevas operaciones, solicitar al usuario dos números (pueden tener decimales) y la operación a realizar (`suma`, `resta`, `multiplicacion`, `division`).
    - Si se ingresa el valor `ANS` en lugar de un número, use el último resultado obtenido como número o `0` si no hay operaciones pasadas.
3. Realizar la operación elegida mediante una función específica: `suma(a, b)`, `resta(a, b)`, etc.
    - Mostrar un mensaje de error si se intenta dividir entre cero y volver al menú principal.
4. Guardar cada operación en un diccionario con el formato *operacion : resultado*, por ejemplo: `{"2 + 3" : 5}`.
5. Para ver el historial, imprima en líneas separadas el diccionario creado.

> [!RECOMENDACIONES]
> Note que el menú se muestra infinitamente hasta que se escoja la opción 3.
> Recuerde que `diccionario.items()`, `diccionario.values()`, `diccionario.keys()`, se puede convertir con `list()` para un mejor manejo.
> No es necesario validar las entradas (números y existencia de opciones), se otorgarán puntos extra si lo realiza.

---

### Criterios de Evaluación
- Formato correcto del menú principal : 5pts
- Repetición del menú hasta que el usuario decida: 10pts
- Solicitud correcta de los números (con decimales) : 10pts
- Solicitud correcta de la operación a realizar : 5pts
- Permite el uso de resultados anteriores con la palabra `ANS` : 10pts
- Almacenamiento de los resultados anteriores : 15pts
- Uso correcto de funciones para las operaciones : 20pts
- Manejo de error de división entre cero : 10pts
- Impresión clara del historial de resultados: 10pts
- Comentarios claros en el código : 5 pts
- **Extra:** Validación de errores en la entrada : 5 pts
- **Extra:** Opción para limpiar el historial : 5 pts

**Total** **110 pts**

---

### Ejemplo de ejecución
```
BIENVENIDO A LA CALCULADORA INTELIGENTE
1 - Nueva operación
2 - Ver historial
3 - Salir
Seleccione una opción > 1

Primer número: 10
Segundo número: 0
Operación a realizar: division
Error, no se puede dividir entre 0

1 - Nueva operación
2 - Ver historial
3 - Salir
Seleccione una opción > 1

Primer número: 5
Segundo número: 3
Operación a realizar: multiplicacion
El resultado es: 15.0

1 - Nueva operación
2 - Ver historial
3 - Salir
Seleccione una opción > 1

Primer número: ANS
Segundo número: 5
Operación a realizar: resta
El resultado es: 10.0

1 - Nueva operación
2 - Ver historial
3 - Salir
Seleccione una opción > 2
5.0 * 3.0 = 15.0
15.0 - 5.0 = 10.0

1 - Nueva operación
2 - Ver historial
3 - Salir
Seleccione una opción > 3
```
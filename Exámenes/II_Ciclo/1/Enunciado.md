# I Examen Parcial
## Indicaciones generales
- La duración del examen es de 1h 20min.
- Subir al Google Classroom las soluciones en el espacio denominado *I Examen Parcial*.
    - En caso de tener problemas puede enviar la solución al correo santiagobrenesruiz@gmail.com
- Debe entregar los archivos: `main.py`, `historial_utils.py`, `operaciones.py`
- El examen es de carácter individual.
- Es permitido utilizar una hoja notas o apuntes.

---

## Calculadora inteligente  
Completar en Python una calculadora que realice operaciones matemáticas, permita usar `ANS`, y almacene/lea el historial desde un archivo de texto. El programa debe dividirse en utilizando múltiples archivos/módulos. 

---

## Archivos Conocidos
Los siguientes archivos se brindan y pueden/deben ser utilizados para completar la solución:

### `operaciones.py` (No modificar)
```python
# operaciones.py
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b
```

### `historial_utils.py` (Se debe completar)
```python
# historial_utils.py
def leer_historial(ruta):
    """
    Debe abrir el archivo en la ruta pasada como parámetro 
    y devolver una lista donde cada elemento es una línea del archivo (una operación).
    Si el archivo no existe, devolver una lista vacía.
    """

def agregar_historial(ruta, entrada):
    """
    Debe abrir el archivo en la ruta pasada como primer parámetro 
    y agregar la entrada recibida como segundo parámetro seguido de
    un salto de línea ("\n")
    """

def limpiar_historial(ruta): #PARTE EXTRA
    """
    Debe abrir el archivo en la ruta pasada como parámetro 
    y borrar todo el contenido.
    """
```

### `main.py` (Se debe completar)
```python
if __name__ == "__main__":
    ruta = "historial.txt"
    ejecutando = True

    print("BIENVENIDO A LA CALCULADORA INTELIGENTE")
    while ejecutando:
        print("1 - Nueva operación")
        print("2 - Ver historial")
        print("3 - Limpiar historial (EXTRA)")
        print("4 - Salir")

        opcion = input("Seleccione una opción > ")

        if opcion == '1':
            a = input("\nPrimer número: ")
            b = input("Segundo número: ")
            
            operacion = input("Operación a realizar: ")

        elif opcion == '2':

        elif opcion == '3': #PARTE EXTRA

        elif opcion == '4':
            ejecutando = False
    
        else:
            print("Error: Opción inválida\n")
```

---
### Requerimientos
1. El menú principal debe contar con las siguientes opciones:
   - 1 - Nueva operación
   - 2 - Ver historial
   - 3 - Limpiar historial (EXTRA)
   - 4 - Salir
2. Para nuevas operaciones, se solicita al usuario dos números (pueden tener decimales) y la operación a realizar (`suma`, `resta`, `multiplicacion`, `division`).
    - Si se ingresa el valor `ANS` en lugar de un número, use el último resultado obtenido como número o `0` si no hay operaciones pasadas.
3. Realizar la operación elegida mediante una función específica del archivo `operaciones.py`.
4. Guardar cada operación en el documento `historial.txt` utilizando las funciones del archivo `historial_utils.py` con el formato *operacion = resultado*, por ejemplo: `2 + 3 = 5`.
5. Para ver el historial, utilice las funciones del archivo `historial_utils.py`, si está vacío imprima un mensaje de error.

> [!RECOMENDACIONES]
> No es necesario validar las entradas (números y existencia de opciones).

---

### Criterios de Evaluación
- Uso de módulos : 10pts
- Completa la función `leer_historial()`: 15pts
- Completa la función `agregar_historial()`: 15pts
- Solicitud correcta de los números (con decimales) : 5pts
- Permite el uso de resultados anteriores con la palabra `ANS` : 10pts
- Uso de las funciones de `operaciones.py` : 10pts
- Historial leído y escrito en `historial.txt` : 10pts
- Comentarios claros en el código : 5 pts
- **Extra:** Opción para limpiar el historial : 10 pts

**Total** **90 pts**

---

### Ejemplo de ejecución
```
BIENVENIDO A LA CALCULADORA INTELIGENTE
1 - Nueva operación
2 - Ver historial
3 - Limpiar historial (EXTRA)
4 - Salir
Seleccione una opción > 2
El historial está vacío

1 - Nueva operación
2 - Ver historial
3 - Limpiar historial (EXTRA)
4 - Salir
Seleccione una opción > 1

Primer número: 5
Segundo número: 3
Operación a realizar: multiplicacion
El resultado es: 15.0

1 - Nueva operación
2 - Ver historial
3 - Limpiar historial (EXTRA)
4 - Salir
Seleccione una opción > 1

Primer número: ANS
Segundo número: 5
Operación a realizar: resta
El resultado es: 10.0

1 - Nueva operación
2 - Ver historial
3 - Limpiar historial (EXTRA)
4 - Salir
Seleccione una opción > 2
5.0 * 3.0 = 15.0
15.0 - 5.0 = 10.0

1 - Nueva operación
2 - Ver historial
3 - Limpiar historial (EXTRA)
4 - Salir
Seleccione una opción > 4
```

`historial.txt`
```
5.0 * 3.0 = 15.0
15.0 - 5.0 = 10.0
```
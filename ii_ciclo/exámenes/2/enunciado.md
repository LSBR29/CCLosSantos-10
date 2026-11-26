# Examen II
## Indicaciones generales
- La duración del examen es de 2h 30min.
- Subir al Google Classroom las soluciones en el espacio denominado *Examen*.
    - En caso de tener problemas puede enviar la solución al correo [santiagobrenesruiz@gmail.com](mailto:santiagobrenesruiz@gmail.com)
- Debe entregar los archivos: `por_corregir.py` (Parte 1) y `main.py` (Parte 2).
- En Classroom se encuentran disponibles: `por_corregir.py` (Parte 1) y `main.py` (Parte 2).
- El examen es de carácter individual.
- Es permitido utilizar una hoja de notas o apuntes.

---

## Parte 1. Corrección de errores (30 pts)

Cada uno de los siguientes programas tiene 3 errores en líneas distintas. Corrija el código directamente en el archivo y agregue un comentario breve (1-2 líneas) explicando cuál era el problema.

Cada error vale 5 pts (4 pts por la corrección y 1 pt por el comentario).

### Problema 1.

El programa debe llenar un tanque de agua con capacidad de 200 litros y mostrar su nivel y su porcentaje de llenado.

```python
class Tanque:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.__nivel = 0

    def llenar(self, litros):
        if self.__nivel + litros > self.capacidad:
            self.__nivel = self.capacidad
        else:
            self.__nivel = litros

    def get_nivel(self):
        return self.__nivel

    def porcentaje(self):
        return self.__nivel / self.capacidad * 10

if __name__ == "__main__":
    t = Tanque(200)
    t.llenar(100)
    t.llenar(50)
    print(t.__nivel)
    print(f"{t.porcentaje()}%")
    t.llenar(100)
    print(t.nivel())
```

Una vez corregido el programa, la salida debe ser:

```
150
75.0%
200
```

### Problema 2.

El programa debe registrar los kilómetros recorridos por un camión y contar cuántos viajes ha hecho.

```python
class Vehiculo:
    def __init__(self, placa, kilometraje):
        self.placa = placa
        self.kilometraje = kilometraje

    def recorrer(self, km):
        self.kilometraje += km

    def __str__(self):
        return f"{self.placa} | {self.kilometraje} km"

class Camion(Vehiculo):
    def __init__(self, placa, kilometraje, carga_max):
        self.carga_max = carga_max
        self.viajes = 0

    def recorrer(self, km):
        super.recorrer(km)
        self.viajes += 1

    def __str__(self):
        return super().__str__() + f" | Carga máxima {self.carga_max} kg | Viajes {self.viajes}"

if __name__ == "__main__":
    camion = Camion("CRC-123", 5000)
    print(camion)
    camion.recorrer(70)
    camion.recorrer(50)
    print(camion)
```

Una vez corregido el programa, la salida debe ser:

```
CRC-123 | 5000 km | Carga máxima 8000 kg | Viajes 0
CRC-123 | 5120 km | Carga máxima 8000 kg | Viajes 2
```

---

## Parte 2. Desarrollo (70 pts)

### Sistema: *Estación de monitoreo de sensores*

Se debe completar un programa que registre las lecturas de varios sensores de un laboratorio, rechace las lecturas imposibles y detecte cuáles sensores están en alerta. El archivo `main.py` en Classroom tiene el ejemplo a ejecutar, el cual no es necesario modificar.

---

### Requerimientos

#### 1. Clase `Sensor`

Representa un sensor genérico que guarda sus lecturas.

**Atributos:**

* `codigo` (str): identificador del sensor.
* `ubicacion` (str): lugar donde está instalado.
* `__lecturas` (list): lecturas registradas (privado), empieza vacía.

**Métodos:**

* `__init__(self, codigo, ubicacion)`: inicializa los atributos.
* Getter para `cantidad` de solo lectura (sin `setter`): retorna cuántas lecturas hay registradas.
* `es_valido(self, valor)`: retorna `True`. Cada tipo de sensor lo redefine con su propia regla.
* `registrar(self, valor)`: si `es_valido(valor)` es `True`, guarda la lectura y retorna `True`. Si no, no guarda nada y retorna `False`.
* `ultimo(self)`: retorna la última lectura registrada, o `None` si no hay ninguna.
* `en_alerta(self)`: retorna `False`. Cada tipo de sensor lo redefine con su propia regla.
* `__str__(self)`: retorna `<codigo> (<ubicacion>) | <cantidad> lecturas`.

---

#### 2. Clase `SensorTemperatura`

Hereda de `Sensor` y agrega un límite de alerta en °C.

**Atributos:**

* `limite_alerta` (float): temperatura máxima permitida.

**Métodos:**

* `__init__(self, codigo, ubicacion, limite_alerta)`: inicializa los atributos, usando `super()` para el código y la ubicación.
* `es_valido(self, valor)`: retorna `True` solo si el valor está entre `-40` y `125` (ambos incluidos).
* `en_alerta(self)`: retorna `True` si hay lecturas y la última supera el límite de alerta.
* `__str__(self)`: amplía el método original usando `super()` para agregar ` | Límite <limite_alerta> °C` al final.

---

#### 3. Clase `SensorHumedad`

Hereda de `Sensor`. No necesita `__init__` ni `__str__` propios.

**Métodos:**

* `es_valido(self, valor)`: retorna `True` solo si el valor está entre `0` y `100` (ambos incluidos).
* `en_alerta(self)`: retorna `True` si hay lecturas y la última está por debajo de `30` o por encima de `70`.

---

#### 4. Clase `Estacion`

Controla los sensores de un laboratorio.

**Atributos:**

* `nombre` (str): nombre de la estación.
* `sensores` (list): lista de objetos `Sensor`.

**Métodos:**

* `__init__(self, nombre)`: inicializa el nombre y la lista vacía.
* `agregar_sensor(self, sensor)`: añade un sensor a la lista.
* `registrar_lectura(self, codigo, valor)`: busca el sensor con ese código y le registra la lectura. Retorna `True` si se guardó, y `False` si el sensor no existe o la lectura no es válida.
* `alertas(self)`: retorna una lista con los sensores que están en alerta.
* `total_lecturas(self)`: retorna la suma de las lecturas registradas por todos los sensores de la estación.

---

#### Extra

* `ExportableMixin` con el método `a_csv(self)`, que retorna el texto `<codigo>,<ubicacion>,<cantidad>`.
* Clase `SensorHumedadExportable` que hereda de `SensorHumedad` y `ExportableMixin`.

---

### Ejemplo de salida esperada
En el archivo `main.py` se encuentra el ejemplo a ejecutar, se espera que produzca la siguiente salida:
*No es necesario, pero si lo requiere puede modificar el ejemplo*
```
T1 (Servidores) | 2 lecturas | Límite 35 °C
T2 (Oficina) | 3 lecturas | Límite 28 °C
H1 (Servidores) | 2 lecturas
Lecturas rechazadas: 2
Sensores en alerta:
T1
H1
Total de lecturas: 7
```

> **Funciones Útiles**
> - **Listas:** `lista.append(valor)` (agregar un elemento), `len(lista)` (cantidad de elementos), `lista[-1]` (último elemento).
>
> *No son funciones obligatorias, puede utilizar otras si lo considera necesario.*

---

### Criterios de Evaluación

- Clase `Sensor` con `__init__` y atributos: 6 pts
- Propiedad `cantidad` de solo lectura: 5 pts
- Métodos `registrar()` y `ultimo()`: 10 pts
- Herencia y uso de `super().__init__` en `SensorTemperatura`: 8 pts
- Método `es_valido()` redefinido en ambas subclases: 8 pts
- Método `en_alerta()` redefinido en ambas subclases: 9 pts
- Método `__str__()` en `Sensor` y en `SensorTemperatura`: 6 pts
- Método `agregar_sensor()`: 3 pts
- Método `registrar_lectura()`: 6 pts
- Método `alertas()`: 4 pts
- Método `total_lecturas()`: 5 pts
- **Extra:** `ExportableMixin` y `SensorHumedadExportable` funcionales: 5 pts
- **Extra:** Comentarios claros en el código: 5 pts

**Total:** **70 pts** (+ 10 pts extra)
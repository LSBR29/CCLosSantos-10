# Ejercicio POO
## Carrera de Criaturas

---

## Requerimientos

### 1. Clase `Criatura`

Representa una criatura participante en una carrera, donde su desempeño depende tanto de su velocidad base como de su personalidad.

**Atributos:**

* `nombre` (str): nombre de la criatura.
* `v_base` (int): velocidad inicial mayor que 0.
* `personalidad` (str): una de `agresiva`, `perezosa` o `caotica`.
* `v_real` (int): no se recibe como parámetro, solo almacena la velocidad real.

**Métodos:**

* `__init__(...)`: inicializa los atributos.
* `velocidad_real(self)`: devuelve la velocidad efectiva según la personalidad:

  * **agresiva** → incrementa la velocidad base en un **30%**.
  * **perezosa** → reduce la velocidad base en un **40%**.
  * **caotica** → cada vez que se consulta, modifica la velocidad base con un valor aleatorio entre **-50%** y **+50%**.

---

**Funciones requeridas:**

1. `map_velocidades(criaturas)`
   *Utiliza `map` para obtener una lista con las velocidades reales de cada criatura.*

2. `filtrar_superiores(promedio, criaturas)`
   *Usa `filter` para devolver únicamente las criaturas cuya velocidad real sea mayor al promedio especificado.*

3. `determinar_ganador(criaturas)`
   *Utiliza `max` para determinar cuál criatura posee la mayor velocidad real y devolverla como ganadora.*

--- 
### 3. Ejemplo de salida esperada
Puede utilizar el siguiente código como ejemplo a ejecutar:

```python
if __name__ == "__main__":
    criaturas = [
        utils.Criatura("Goblins", 75, "agresiva"),
        utils.Criatura("Golem", 80, "perezosa"),
        utils.Criatura("PEKKA", 90, "caotica"),
        utils.Criatura("Minion", 85, "caotica"),
        utils.Criatura("Witch", 85, "perezosa")
    ]

    # Imprimir todas
    print("\nCRIATURAS REGISTRADAS")
    for c in criaturas:
        print(f"{c.nombre} | Base: {c.v_base} | Pers.: {c.personalidad}")

    # Obtener las velocidades reales
    velocidades = list(utils.map_velocidades(criaturas))

    # Imprimir las velocidades reales
    print("\nVELOCIDADES REALES")
    for criatura, vel in zip(criaturas, velocidades):
        print(f"{criatura.nombre}: {vel:.2f}")

    # Calcular e imprimir el promedio
    promedio = sum(velocidades) / len(velocidades)
    print(f"\nPromedio de velocidades: {promedio:.2f}")

    # Ver e imprimir las superiores al promedio
    superiores = list(utils.filtrar_superiores(promedio, criaturas))
    print("\nCRIATURAS SUPERIORES AL PROMEDIO")
    for c in superiores:
        print(f"{c.nombre} (Velocidad actual: {c.velocidad_real():.2f})")

    # Ver el ganador
    ganador = utils.determinar_ganador(criaturas)
    print("\nGANADOR")
    print(f"{ganador.nombre} con velocidad {ganador.velocidad_real():.2f}")
```
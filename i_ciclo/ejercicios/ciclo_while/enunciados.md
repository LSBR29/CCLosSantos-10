# Ejercicios ciclo `while`
#### Ejercicio 1: Contador con condiciones
Cree un programa que imprima los números del 1 al 20, pero:  
- Si el número es múltiplo de 3, que imprima `"Fizz"`.  
- Si es múltiplo de 5, que imprima `"Buzz"`.  
- Si es múltiplo de ambos, que imprima `"FizzBuzz"`.  

Use un bucle `while`.

**Ejemplo:**  
```plaintext
1
2
3 Fizz
4
5 Buzz
6 Fizz
...
```

#### Ejercicio 2: Validación de número primo
Solicite al usuario un número mayor que 1.  
Luego, mediante un bucle `while` que verifique sus divisores, imprima si el número es primo (por ejemplo: `"El número 5 es primo"`).

**Ejemplo:**  
```plaintext
Ingrese un número entero positivo: 5
El número 5 es primo
```

#### Ejercicio 3: Suma acumulativa con control de errores
Pida al usuario que ingrese números uno por uno. Sume los valores válidos (enteros positivos) hasta que el usuario escriba `"fin"`. Si ingresa algo incorrecto (como letras o números negativos), ignórelos y continúe.  
Al final, imprima la suma resultante.

**Ejemplo:**  
```plaintext
Ingrese un número entero positivo: 8
Ingrese un número entero positivo: 4
Ingrese un número entero positivo: fin
La suma resultante es: 12
```

#### Ejercicio 4: Sistema de login con bloqueo  
Simule un sistema de login donde el usuario tenga hasta 3 intentos para ingresar un usuario y contraseña válidos. Si falla, imprima un mensaje de bloqueo.  
El usuario válido es `admin` y la contraseña `1234`. Imprima mensajes apropiados según el caso.

**Ejemplo:**  
```plaintext
Usuario: admin
Contraseña: 1234
Inicio de sesión correcto
```

**Ejemplo con fallos:**  
```plaintext
Usuario: user
Contraseña: 123
El usuario o la contraseña son incorrectos
```

**Ejemplo con bloqueo:**  
```plaintext
Ingrese el usuario: user
Ingrese la contraseña: 1
El usuario o la contraseña son incorrectos
Ingrese el usuario: 1
Ingrese la contraseña: user
El usuario o la contraseña son incorrectos
Ingrese el usuario: ad
Ingrese la contraseña: 123
El usuario o la contraseña son incorrectos
Demasiados intentos fallidos.
```

#### Ejercicio 5: Adivinar número con intentos contados  
Genere un número aleatorio entre 1 y 50. El usuario tendrá hasta 5 intentos para adivinarlo.  
Después de cada intento, imprima si el número secreto es mayor o menor que el ingresado.  
Si no lo acierta, imprima el número correcto al final.

**Ejemplo (acierto):**  
```plaintext
Ingrese el número: 25
El número es menor.
Ingrese el número: 12
El número es mayor.
Ingrese el número: 19
Adivinó el número.
```

**Ejemplo (sin acierto):**  
```plaintext
Ingrese el número: 5
El número es mayor.
Ingrese el número: 50
El número es menor.
Ingrese el número: 40
El número es menor.
Ingrese el número: 20
El número es menor.
Ingrese el número: 10
El número es menor.
El número era: 7
```

#### Ejercicio 6: Frecuencia de letra en una palabra  
Solicite al usuario una palabra y una letra.  
Recorra la palabra con un bucle `while` y cuente cuántas veces aparece la letra (sin usar `.count()`).  
Al final, imprima el resultado, por ejemplo: `"La letra o aparece 2 veces en la palabra probando."`

**Ejemplo:**  
```plaintext
Ingrese una palabra: probando  
Ingrese una letra: o
La letra o aparece 2 veces en la palabra probando.
```

#### Ejercicio 7: Suma de dígitos
Solicite un número entero positivo y calcule la suma de sus dígitos uno a uno usando solo operaciones aritméticas.  
Luego imprima la suma.

**Ejemplo:**  
```plaintext
Ingrese un número entero positivo: 342
La suma de los dígitos es: 9
```

#### Ejercicio 8: Tabla personalizada de multiplicar  
Solicite al usuario un número entre 1 y 9, y el límite de la tabla (por ejemplo, hasta 15).  
Con un bucle `while`, imprima la tabla de multiplicar de ese número hasta el límite indicado.

**Ejemplo:**  
```plaintext
Ingrese un número (1-9): 7
Ingrese hasta qué número desea ver la tabla de multiplicar: 4
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
```

#### Ejercicio 9: Menú interactivo con opciones  
Cree un menú con las siguientes opciones:  
1. Ingresar nombre  
2. Mostrar saludo personalizado  
3. Salir  

Debe funcionar con un `while` hasta que el usuario elija salir. Si selecciona la opción 2 sin haber ingresado un nombre, imprima un mensaje de advertencia.  
Al seleccionar salir, imprima `"Saliendo del programa..."`

**Ejemplo:**  
```plaintext
1. Ingresar nombre
2. Mostrar saludo personalizado
3. Salir
Ingrese una opción de las mostradas en el menú: 1
Ingrese su nombre: Santiago

1. Ingresar nombre
2. Mostrar saludo personalizado
3. Salir
Ingrese una opción de las mostradas en el menú: 2
Hola Santiago

1. Ingresar nombre
2. Mostrar saludo personalizado
3. Salir
Ingrese una opción de las mostradas en el menú: 3
Saliendo del programa...
```
# Bucle `while` en Python

El bucle `while` es una estructura de control fundamental en la programación que te permite **ejecutar un bloque de código repetidamente** mientras una condición específica sea **verdadera** (True). 

## Sintaxis básica

La sintaxis del bucle `while` es bastante simple:

``` Python
while condicion:
    # Bloque de código que se ejecuta
    # mientras la condición sea verdadera
```

* **`while`**: La palabra clave que inicia el bucle.

* **`condicion`**: Una expresión que se evalúa como `True` o `False`. El bucle continúa ejecutándose mientras esta condición sea `True`.

* **Bloque de código**: El código indentado que se ejecutará en cada iteración.

Es crucial **asegurarse de que la condición eventualmente se vuelva `False`** para evitar un **bucle infinito**. Esto generalmente se logra modificando una variable dentro del bucle que está involucrada en la condición.

## Ejemplos de uso

### Ejemplo 1: Contador simple

Este es el uso más básico. Se usa un contador que incrementa en cada iteración hasta que la condición ya no es verdadera.

``` Python
contador = 0
while contador < 5:
    print(f"El contador es: {contador}")
    contador += 1
print("El bucle ha terminado.")
```

**Explicación:** El bucle se ejecuta mientras `contador` sea menor que 5. En cada iteración, se imprime el valor y se le suma 1 a `contador`. Cuando `contador` llega a 5, la condición `5 < 5` es `False` y el bucle finaliza.

***

### Ejemplo 2: Suma de números hasta un límite

Este ejemplo demuestra cómo el bucle `while` es útil cuando no se sabe de antemano cuántas veces se ejecutará el código.

``` Python
suma = 0
numero = 1
while suma <= 20:
    suma += numero
    print(f"Número actual: {numero}")
    print(f"La suma actual es: {suma}")
    numero += 1
print(f"La suma total (mayor a 20) es: {suma}")
```

**Explicación:** El bucle se repite mientras `suma` sea menor o igual a 20. En cada paso, se suma el valor de `numero` a `suma`, y `numero` se incrementa. El bucle se detiene cuando `suma` supera los 20.

***

### Ejemplo 3: Bucle con una bandera (flag)

Una "bandera" es una variable booleana que controla el flujo de un bucle. Se usa para detener el bucle cuando se cumple una condición interna.

``` Python
juego_activo = True
while juego_activo:
    comando = input("Ingresa 'salir' para terminar el juego: ")
    if comando.lower() == 'salir':
        juego_activo = False
        print("Saliendo del juego...")
    else:
        print("Continuando el juego...")
print("El juego ha finalizado.")
```

**Explicación:** El bucle continúa mientras `juego_activo` sea `True`. Cuando el usuario escribe "salir", la variable `juego_activo` se cambia a `False`, lo que hace que la condición del `while` se evalúe como `False` en la siguiente iteración, terminando el bucle.

***

### Ejemplo 4: Uso de `break` y `continue`

Las sentencias `break` y `continue` son útiles para controlar la ejecución de un bucle.

* **`break`**: Termina completamente la ejecución del bucle.

* **`continue`**: Salta la iteración actual y continúa con la siguiente.

``` Python
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue  # Salta esta iteración, no se imprimirá '3'
    if i == 7:
        break     # Detiene completamente el bucle
    print(f"El valor de i es: {i}")
print("Bucle terminado.")
```

**Explicación:** El bucle se ejecuta de 1 a 10. Cuando `i` es 3, `continue` hace que se omita la impresión y se pase a la siguiente iteración. Cuando `i` es 7, `break` detiene el bucle por completo.

***

### Ejemplo 5: Menú de opciones simple

Un uso común de `while` es para crear menús interactivos que se repiten hasta que el usuario decide salir.

``` Python
opcion = ""
while opcion != "4":
    print("\nMenú de Opciones:")
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Dar la hora")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("¡Hola! ¿Cómo estás?")
    elif opcion == "2":
        print("¡Hasta pronto!")
    elif opcion == "3":
        print("Son las 5 de la tarde.")
    elif opcion == "4":
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")
```

**Explicación:** El bucle se ejecuta mientras la `opcion` elegida no sea "4". Dentro del bucle, se muestra el menú y se procesa la opción del usuario. El bucle solo se detiene cuando el usuario elige la opción de salida.

# Ejercicios

* [Ejercicios simples](Ejercicios_simples.md)
* [Otros ejercicios](Otros_ejercicios.md)

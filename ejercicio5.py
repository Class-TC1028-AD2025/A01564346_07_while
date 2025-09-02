
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
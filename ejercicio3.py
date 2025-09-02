
juego_activo = True
while juego_activo:
    comando = input("Ingresa 'salir' para terminar el juego: ")
    if comando.lower() == 'salir':
        juego_activo = False
        print("Saliendo del juego...")
    else:
        print("Continuando el juego...")
print("El juego ha finalizado.")
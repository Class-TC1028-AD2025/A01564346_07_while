
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue  # Salta esta iteración, no se imprimirá '3'
    if i == 7:
        break     # Detiene completamente el bucle
    print(f"El valor de i es: {i}")
print("Bucle terminado.")
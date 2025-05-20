"""
Calcula el promedio de una lista de números
Ejercicio 7
"""

try:
    # Pedimos al usuario una lista de números separados por comas
    entrada = input("Introduce una lista de números separados por comas: ").strip()

    # Validamos si la entrada está vacía
    if not entrada:
        print("No se ingresaron números.")
        exit()

    # Convertimos la cadena en una lista de números
    numeros = [float(num) for num in entrada.split(",")]

    # Calculamos el promedio
    promedio = sum(numeros) / len(numeros)

    # Mostramos el resultado
    print("El promedio de la lista es:", promedio)

except ValueError:
    print("Error: Asegúrate de introducir solo números separados por comas.")

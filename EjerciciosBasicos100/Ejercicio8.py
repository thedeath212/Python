"""
Crear una tupla con diferentes elementos
Ejercicio 8
"""

# Solicitamos al usuario que ingrese números separados por comas
entrada = input("Introduce una tupla de números separados por comas: ")

# Validamos si la entrada está vacía
if not entrada.strip():
    print("No se ingresaron números.")
    exit()

# Convertimos la cadena en una tupla de números
try:
    tupla = tuple(map(int, entrada.split(",")))
except ValueError:
    print("Error: asegúrate de ingresar solo números separados por comas.")
    exit()

# Mostramos la tupla
print("La tupla es:", tupla)
# Mostramos el tipo de la tupla
print("El tipo de la tupla es:", type(tupla))
# Mostramos la longitud de la tupla
print("La longitud de la tupla es:", len(tupla))
# Mostramos el primer elemento de la tupla
print("El primer elemento de la tupla es:", tupla[0])
# Mostramos el último elemento de la tupla
print("El último elemento de la tupla es:", tupla[-1])
# Mostramos un rango de elementos de la tupla
print("Los elementos de la tupla desde el índice 1 hasta el 3 son:", tupla[1:4])
# Mostramos un rango de elementos de la tupla
print("Los elementos de la tupla desde el índice 2 hasta el final son:", tupla[2:])

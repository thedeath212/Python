"""
Convierte un numero decimal a binario, octal y hexadecimal.
Ejercicio 12

"""

# Definimos el número decimal
numero_decimal = int(input("Introduce un número decimal: "))
# Convertimos el número decimal a binario
numero_binario = bin(numero_decimal)
# Convertimos el número decimal a octal
numero_octal = oct(numero_decimal)
# Convertimos el número decimal a hexadecimal
numero_hexadecimal = hex(numero_decimal)
# Mostramos los resultados
print("El número decimal", numero_decimal, "en binario es:", numero_binario)
print("El número decimal", numero_decimal, "en octal es:", numero_octal)
print("El número decimal", numero_decimal, "en hexadecimal es:", numero_hexadecimal)

    
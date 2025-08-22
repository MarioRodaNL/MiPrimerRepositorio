# Pedir el nombre al usuario
nombre = input("Por favor, introduce tu nombre: ")

nombre_mayus = nombre.upper()       # Convertir el nombre a mayúsculas
num_letras = len(nombre.replace(" ", ""))       # Contar el número de letras (sin contar espacios)

print(f"{nombre_mayus} tiene {num_letras} letras")

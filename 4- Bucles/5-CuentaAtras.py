numero = int(input("Ingrese un número entero positivo: "))
resultado = ""   # cadena donde acumulamos los impares

for i in range(1, numero + 1):
    if numero != 0:
        resultado = str(i) + ", " + resultado

resultado = resultado.rstrip(", ")      # Quitar la última coma y espacio extra

print(resultado)
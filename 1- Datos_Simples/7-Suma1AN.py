# Pedir al usuario un número entero positivo
n = int(input("Por favor, introduce un número entero positivo: "))

if n > 0:
    suma = 0
    i = 1
    while i <= n:
        suma += i
        i + 1

    print(f"La suma de los {n} primero enteros positivos es: {suma}")
else:
    print("El número debe ser positivo.")

#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
#Si el divisor es cero el programa debe mostrar un error

n1 = int(input("Ingrese su primer número: "))
n2 = int(input("Ingrese su segundo número: "))

if n2 == 0:
    print("ERROR - El divisor no debe ser 0")
else:
    division = n1 / n2
    print(division)
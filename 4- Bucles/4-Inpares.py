#Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas

numero = int(input("Ingrese un número entero positivo: "))
aux = 0
str = ""
i = 1

while aux != numero:
    if i % 2 != 0:
        str += str(i) + ", "

    aux += 1
    i += 1

print(str)

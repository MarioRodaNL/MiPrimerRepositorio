#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido

user_name = input("Por favor, ingrese su nombre: ")
n = int(input("Ingrese un número entero: "))

while n != 0:
    print(user_name)
    n -= 1
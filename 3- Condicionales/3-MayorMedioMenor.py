n1 = int(input("Ingrese su primer número: "))
n2 = int(input("Ingrese su segundo número: "))
n3 = int(input("Ingrese su tercer número: "))

mayor = n1

if n2 > mayor:
    medio = mayor
    mayor = n2
else:
    medio = n2

if n3 > mayor:
    menor = medio
    medio = mayor
    mayor = n3
elif n3 > medio:
    menor = medio
    medio = n3
else:
    menor = n3

print(f"El mayor es {mayor}, el del medio es {medio} y el menor es {menor}.")
n1 = int(input("Ingrese su primer número: "))
n2 = int(input("Ingrese su segundo número: "))

if n1 > n2:
    mayor = n1
    menor = n1
else:
    mayor = n2
    menor = n1

print(f"El mayor es {mayor} y el menor es {menor}")
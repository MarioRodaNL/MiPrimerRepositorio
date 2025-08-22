#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla el pago que le corresponde

horas_trabajadas = int(input("Por favor, ingrese la cantidad de horas trabajadas: "))
coste_por_hora = int(input("Por favor, ingrese el coste por hora: "))
pago = horas_trabajadas * coste_por_hora

print(f"El pago que corresponde es: {pago}")
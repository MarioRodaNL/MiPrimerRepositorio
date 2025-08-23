#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión

cant_invertir = float(input("Ingrese la cantidad a invertir: "))
int_anual = float(input("Ingrese el interés anual (en %): "))
años = int(input("Ingrese la cantidad de años: "))

capital = cant_invertir

for i in range(1, años + 1):
    capital = capital * (1 + int_anual / 100)   # aplicar interés compuesto
    print(f"En el año {i} el capital acumulado es: {capital:.2f}")

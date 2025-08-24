import math

def areaCirculo(radio):
    area = math.pi * (radio ** 2)
    return area

def volumenCilindro(radio, altura):
    volumen = areaCirculo(radio) * altura
    return volumen

print(f"El área de un círculo con radio 2 es: {areaCirculo(2):.2f}")
print(f"El volumen de un cilindro de area {areaCirculo(2):.2f} y altura es 5 es: {volumenCilindro(2,5):.2f}")
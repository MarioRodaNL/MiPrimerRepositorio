import math

class Circulo:
    def __init__(self, radio):
        self._radio = radio   # Usamos _radio como atributo interno

    # === Radio ===
    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor):
        if valor <= 0:
            raise ValueError("El radio debe ser positivo")
        self._radio = valor

    # === Diámetro ===
    @property
    def diametro(self):
        return self._radio * 2

    @diametro.setter
    def diametro(self, valor):
        if valor <= 0:
            raise ValueError("El diámetro debe ser positivo")
        self._radio = valor / 2

    # === Perímetro (longitud de circunferencia) ===
    @property
    def perimetro(self):
        return 2 * math.pi * self._radio

    @perimetro.setter
    def perimetro(self, valor):
        if valor <= 0:
            raise ValueError("El perímetro debe ser positivo")
        self._radio = valor / (2 * math.pi)

    # === Área ===
    @property
    def area(self):
        return math.pi * (self._radio ** 2)

    @area.setter
    def area(self, valor):
        if valor <= 0:
            raise ValueError("El área debe ser positiva")
        self._radio = math.sqrt(valor / math.pi)

    def __repr__(self):
        return f"Circulo(radio={self._radio:.2f})"

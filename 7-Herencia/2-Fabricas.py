class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_info(self):
        return f"Llantas: {self.llantas}, Color: {self.color}, Precio: ${self.precio}"


class Moto(Fabrica):
    def __init__(self, color, precio):
        super().__init__(2, color, precio)  # una moto siempre tiene 2 llantas

    def mostrar_info(self):
        return f"Moto -> {super().mostrar_info()}"


class Auto(Fabrica):
    def __init__(self, color, precio):
        super().__init__(4, color, precio)  # un auto siempre tiene 4 llantas

    def mostrar_info(self):
        return f"Auto -> {super().mostrar_info()}"


# Ejemplo de uso:
moto1 = Moto("Rojo", 1500)
auto1 = Auto("Negro", 8000)

print(moto1.mostrar_info())  # Moto -> Llantas: 2, Color: Rojo, Precio: $1500
print(auto1.mostrar_info())  # Auto -> Llantas: 4, Color: Negro, Precio: $8000

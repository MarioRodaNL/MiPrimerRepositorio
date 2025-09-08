class Marino:
    def hablar(self):
        print("Hola, soy un animal marino!")


class Pulpo(Marino):
    def hablar(self):
        print("Hola, soy un Pulpo!")


class Foca(Marino):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)


# Ejemplo de uso:
marino = Marino()
pulpo = Pulpo()
foca = Foca("Hola, soy una Foca!")

marino.hablar()  # Hola, soy un animal marino!
pulpo.hablar()   # Hola, soy un Pulpo!
foca.hablar()    # Hola, soy una Foca!

class Vehiculo:
    def __init__(self, chofer, km_recorridos=0):
        self.chofer = chofer
        self.km_recorridos = km_recorridos

    def asignar_chofer(self, nuevo_chofer):
        """Método genérico (sobrescrito en subclases)."""
        self.chofer = nuevo_chofer

    def recorrer(self, km):
        self.km_recorridos += km


class Moto(Vehiculo):
    def __init__(self, chofer, km_recorridos=0):
        super().__init__(chofer, km_recorridos)
        self.acompañante = None

    def asignar_chofer(self, nuevo_chofer):
        if self.acompañante is not None:
            print("❌ No se puede cambiar de chofer mientras haya un acompañante.")
        else:
            self.chofer = nuevo_chofer

    def agregar_acompañante(self, persona):
        if self.acompañante is None:
            self.acompañante = persona
        else:
            print("❌ La moto ya tiene un acompañante.")

    def quitar_acompañante(self):
        self.acompañante = None


class Colectivo(Vehiculo):
    def __init__(self, chofer, km_recorridos=0):
        super().__init__(chofer, km_recorridos)
        self.pasajeros = []

    def asignar_chofer(self, nuevo_chofer):
        if len(self.pasajeros) > 0:
            print("❌ No se puede cambiar de chofer mientras haya pasajeros.")
        else:
            self.chofer = nuevo_chofer

    def agregar_pasajero(self, persona):
        self.pasajeros.append(persona)

    def quitar_pasajeros(self):
        self.pasajeros = []

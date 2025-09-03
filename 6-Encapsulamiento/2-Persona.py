class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumpleaños(self):
        self.edad +=1

    def dar_edad(self):
        print(self.edad)

pepito = Persona("Pepito", 11)
pepito.dar_edad()
pepito.cumpleaños()
pepito.cumpleaños()
pepito.dar_edad()


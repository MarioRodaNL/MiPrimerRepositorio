class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"


class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, carrera):
        super().__init__(nombre, apellido)  # inicializa la parte de Persona
        self.edad = edad
        self.carrera = carrera

    def mostrar_carrera(self):
        return f"{self.nombre_completo()} estudia {self.carrera}"


# Ejemplo de uso:
persona1 = Persona("Juan", "Pérez")
print(persona1.nombre_completo())   # Juan Pérez

estudiante1 = Estudiante("Ana", "Gómez", 20, "Ingeniería en Sistemas")
print(estudiante1.nombre_completo())  # Ana Gómez
print(estudiante1.mostrar_carrera())  # Ana Gómez estudia Ingeniería en Sistemas

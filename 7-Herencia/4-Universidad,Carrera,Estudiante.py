class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre

class Carrera:
    def __init__(self, especialidad):
        self.especialidad = especialidad

class Estudiante:   
    def __init__(self, universidad, carrera, nombre, edad):
        self.universidad = universidad
        self.carrera = carrera
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Universidad: {self.universidad.nombre}")
        print(f"Carrera: {self.carrera.especialidad}")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

# Crear objetos
uni = Universidad("UNO")
carrera = Carrera("Lic. Informática")

# Crear estudiante con esos objetos
Carlito = Estudiante(uni, carrera, "Carlito", 20)

# Mostrar info
Carlito.mostrar_info()



        
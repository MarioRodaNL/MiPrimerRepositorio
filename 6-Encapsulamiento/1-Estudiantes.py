class Estudiante:
    def __init__(self, nombre, nota):   #Constructor
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def resultado(self):
        if self.nota >= 6:  # puedes cambiar el 6 por el mínimo que quieras
            print(f"{self.nombre} ha aprobado con {self.nota}.")
        else:
            print(f"{self.nombre} NO ha aprobado. Su nota es {self.nota}.")


# Ejemplo de uso
est1 = Estudiante("Juan", 8)
est2 = Estudiante("María", 4)

est1.imprimir()
est1.resultado()

print("-" * 30)

est2.imprimir()
est2.resultado()

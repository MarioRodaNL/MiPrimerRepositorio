class Nota:
    def __init__(self, nota):
        self.nota = nota

    def obtenerValor(self):
        return self.nota
    
    def aprobado(self):
        aprobado = False
        if self.nota >= 4:
            aprobado = True

        return aprobado         #ChatGPT recomienda reducir codigo unicamente con esta linea return self.nota >= 4
    
    def desaprobado(self):
        desaprobado = False
        if self.nota < 4:
            desaprobado = True

        return desaprobado      #ChatGPT recomienda reducir codigo unicamente con esta linea return self.nota < 4
    
    def recuperar(self, nuevoValor):
        if nuevoValor > self.nota:
            self.nota = nuevoValor

        print(self.nota)

n = Nota(4)
n.recuperar(7)
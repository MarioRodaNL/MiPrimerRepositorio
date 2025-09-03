class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def estaSobreElEjeX(self):      #devuelve valor booleano
        return self.x == 0
    
    def estaSobreElEjeY(self):
        return self.y == 0
    
    def esElOrigenDeCoordenadas(self):  #devuelve valor booleano
        return self.x == 0 and self.y == 0
    

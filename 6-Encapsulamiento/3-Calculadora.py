class Calculadora:
    def __init__ (self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def suma(self):           #Aca habia cometido el error de escribir suma(n1, n2) en vez de suma(self)
        suma = self.n1 + self.n2
        print(self)

    def resta(self):
        resta = self.n1 - self.n2
        print(resta)
    
    def division(self):
        if self.n2 != 0:
            div = self.n1 / self.n2
            print(div)
        else:
            print("No se puede dividir por cero")

    def multi(self):
        multi = self.n1 * self.n2
        print(multi)

n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))

cal = Calculadora(n1, n2)
cal.suma()
cal.resta()
cal.division()
cal.multi()
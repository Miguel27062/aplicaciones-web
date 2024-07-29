class Rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho
    def calcular_area(self):
        return self.longitud * self.ancho
rectangulo = Rectangulo(5, 3)
area = rectangulo.calcular_area()
print("El área del rectángulo es:", area)

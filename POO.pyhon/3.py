import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):

        return math.pi * self.radio**2
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
circulo = Circulo(5)
area = circulo.calcular_area()
perimetro = circulo.calcular_perimetro()
print("El área del círculo es:", area)
print("El perímetro del círculo es:", perimetro)
